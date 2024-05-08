import requests
info_url = 'https://kyfw.12306.cn/otn/leftTicket/queryG?leftTicketDTO.train_date=2024-05-08&leftTicketDTO.from_station=GZQ&leftTicketDTO.to_station=BJP&purpose_codes=ADULT'
# 伪装
headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'cookie' : '_uab_collina=171514181880168973328087; JSESSIONID=6DFA0EAC4879FA1DDC0EA9A8161C2033; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; BIGipServerpassport=937951498.50215.0000; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=552075530.50210.0000; _jc_save_fromDate=2024-05-08; _jc_save_toDate=2024-05-08; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u5E7F%u5DDE%2CGZQ; _jc_save_toStation=%u5317%u4EAC%2CBJP'
    }
resp = requests.get(info_url,headers=headers)

resp.encoding = 'utf-8'
resp_data = resp.json().get('data').get('result')
print(resp_data)
for r in resp_data:
   data = [a for a in r.split('|')]
   print(data)
