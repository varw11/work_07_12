"""
向测试网站发请求,来验证User-Agent是什么
"""
import requests

url = 'http://httpbin.org/get'
headers = {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}

resp = requests.get(url=url, headers=headers)
# 1.text:响应内容-字符串
html = resp.text
# 2.content:响应内容-bytes,爬取图片、音频、文件、视频... ...
html = resp.content
# 3.status_code: HTTP响应码
code = resp.status_code
# 4.url: 返回实际数据的url地址
url = resp.url





















