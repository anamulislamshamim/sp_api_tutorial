import csv 
import json 
import time 

import pandas as pd 
import requests 
import seaborn as sns 

from keys import CLIENT_CONFIG 
from sp_api.api import Reports, Sales
from sp_api.base import Marketplaces, ReportType, ProcessingStatus, Granularity


# todo something


if __name__ == "__main__":
    report_type = ReportType.GET_FBA_MYI_ALL_INVENTORY_DATA
    res = Reports(credentials=CLIENT_CONFIG, marketplace=Marketplaces.US)
    data = res.create_report(report_type=report_type) 
    report = data.payload
    report_id = report['reportId']
    
    res = Reports(credentials=CLIENT_CONFIG, marketplace=Marketplaces.US)
    data = res.get_report(report_id)
    
    report_data = ''
    
    while data.payload.get('processingStatus') not in [ProcessingStatus.DONE, ProcessingStatus.FATAL, ProcessingStatus.CANCELLED]:
        print(data.payload)
        print("Sleeping...")
        time.sleep(2)
        data = res.get_report(report_id)
        
    if data.payload.get('processingStatus') in [ProcessingStatus.FATAL, ProcessingStatus.CANCELLED]:
        print("Report Failed!")
        report_data = data.payload
    else:
        print("success!")
        print(data.payload)
        report_data = res.get_report_document(data.payload['reportDocumentId'])
        print("Document:")
        print(report_data.payload)
    
    report_url = report_data.payload.get('url')
    print(report_url)
    
    res = requests.get(report_url)
    decoded_content = res.content.decode('cp1252')
    reader = csv.DictReader(decoded_content.splitlines(), delimeter='\t')
    
    data_list = []
    for row in reader:
        # parsing each row and store into the data_list 
        data = {
            'sku': row['sku'],
            # pass 
        }
        
        data_list.append(data)
    
    # save the data into the data.json file 
    with open('./responses/data.json', 'w') as out:
        json.dump(data_list, out)
    
    f = open('./responses/data.json')
    data = json.load(f)
    f.close()
    asins = [x['asin'] for x in data][:5]
    
    marketplaces = dict(US=Marketplaces.US, CA=Marketplaces.CA)
    data = []
    for asin in asins:
        for country, marketplace_id in marketplaces.items():
            sales = Sales(credentials=CLIENT_CONFIG, marketplaces=marketplace_id)
            res = sales.get_order_metrics(interval=('2021-09-01T00:00:00-07:00', '2022-09-28T00:00:00-07:00'),
                                          granularity=Granularity.Total, asin=asin)
            metrics = res.payload[0]
            data.append({'unit_count': metrics['unitCount'], 'order_item_count': metrics['orderItemCount'], 
                         'order_count': metrics['orderCount'], 'country': country, 'asin': asin})
    
    # showing the data using pandas and seaborn
    df = pd.DataFrame(data)
    print(df)
    
    sns.set_theme(style='whitegrid')
    g = sns.catplot(
        data = df, 
        kind = 'bar',
        x='asin',
        y = 'unit_count',
        hue="country",
        errorbar="sd",
        palette="dark", 
        alpha=.6,
        height=6
    )
    
    g.despine(left=True)
    g.set_axis_labels("", 'Unit Count')
    g.legend.set_title("Seller Inventory Report")