#  怎么发送请求
# pip install requests
# pip install lxml 删除<body/> 这些代码，只提取文字
""" ''' 三个点也行
这是多行注释
"""
# 单行注释
import requests
from lxml import etree 
# 发送给谁
url = 'https://www.bg3.co/novel/pagea/woyouqigejinenglan-zhuandetuoluo_1.html'
counter = 1
while True:
    # 伪装自己
    counter+=1
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    # 发送请求
    resp  = requests.get(url,headers=headers) # 不要header 也是可以的，header带的内容实在是太多了
    # 设置编码
    resp.encoding = 'utf-8'

    # 提取文字
    e = etree.HTML(resp.text)
    info = '\n'.join(e.xpath('//div[@class="content"]/p/text()') )# 提取文本信息
    title = e.xpath('//h1/text()')[0] # 提取H1标题
    # print(info)
    # print(title) 
    # 响应信息
    # print(resp.text)

    url = f'https://www.bg3.co/novel/pagea/woyouqigejinenglan-zhuandetuoluo_{counter}.html'
    print(title) 
    # 保存
    with open ('我有七个技栏.txt','w',encoding='utf-8') as f: #如果没有这个文件会自动在目录创建一个，以写的方式打开
        # 用 f 为代号来操控文件 \n 是换行
        f.write(title+'\n\n'+info+'\n\n')
    if url == 'https://www.bg3.co/novel/pagea/woyouqigejinenglan-zhuandetuoluo_11.html':
        break   
    '''
    退出循环 break;
    '''