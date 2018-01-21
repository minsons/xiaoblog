# coding:utf-8
"""

 万象图优的 照片处理技术
 处理各个照片的技术

"""
import requests
import time
import datetime
# 设置用户属性, 包括secret_id, secret_key, region
# appid已在配置中移除,请在参数Bucket中带上appid。Bucket由bucketname-appid组成
secret_id = 'AKIDwv20mYOrsjNp9Ha6udGmaEgw0sYdmuuj'     # 替换为用户的secret_id
secret_key = '1ueHj298zHUVQEvRozzobRBk7HF0e7PU'     # 替换为用户的secret_key
region = 'gz'    # 替换为用户的region
token = ''                 # 使用临时秘钥需要传入Token，默认为空,可不填

##a=[appid]&b=[bucket]&k=[SecretID]&e=[expiredTime]&t=[currentTime]&r=[rand]&u=[userid]&f=[fileid]
token ='a=1253323447&b=myimg1&k=AKIDwv20mYOrsjNp9Ha6udGmaEgw0sYdmuuj&e=0&t='+str(int(time.time()))+"&r=2637374747&f=2"
host = 'https://myimg1-1253323447.cos.ap-guangzhou.myqcloud.com/1002.png'
host2="https://myimg1-1253323447.picgz.myqcloud.com/l002.png"
headers = {'x-cos-acl': 'public-read',"Authorization":token}
# 文件流 简单上传
filename='C:/Users/ThinkPad/Pictures/flask/1002.png'
files = {'file': open(filename, 'rb')}
r= requests.post(host,headers,files=files)
# r = requests.get('https://github.com/timeline.json')
# print(r)
print(r.__dict__)