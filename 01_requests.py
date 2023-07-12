"""
向京东官网发请求,获取响应内容
"""
import requests

resp = requests.get(url='https://www.jd.com/')
# 1.text属性: 获取响应内容-字符串
html = resp.text
print(html)




















