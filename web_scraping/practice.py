from furl import furl 


link = "https://www.amazon.com/s?k=school+supplies&_encoding=UTF8&content-id=amzn1.sym.7acbca95-6949-4783-9691-9ac9df8021d9&pd_rd_r=6744c621-fa0f-4977-999a-c2c997eaac82&pd_rd_w=4gb61&pd_rd_wg=27Fct&pf_rd_p=7acbca95-6949-4783-9691-9ac9df8021d9&pf_rd_r=ENCEEYPJJPMEAVK7ZQEC&ref=pd_gw_unk"


f = furl(link)

print(f.args)