import jwt
import datetime
import hashlib

SECRECT_KEY = 'secret'

def md5Encoding(youstr):
    m=hashlib.md5()
    m.update(youstr)
    encodingstr=m.hexdigest()
    print(encodingstr)


# 生成jwt 信息
def  jwtEncoding(some,aud='webkit'):
    datetimeInt = datetime.datetime.utcnow() + datetime.timedelta(seconds=180)
    print(datetimeInt)
    option = {
        'exp':datetimeInt,
        'aud': aud,
        'some': some
    }
    encoded2 = jwt.encode(option, SECRECT_KEY, algorithm='HS256')
    return encoded2


# userInfo = {
#             "id":12,
#             "username":"2234",
#             "email":"23423dsd"
#         }
#
# listr = jwtEncoding(userInfo)
# print(listr.decode())


# 解析jwt 信息
def  jwtDecoding(token,aud='webkit'):
    decoded = None
    try:
        decoded = jwt.decode(token, SECRECT_KEY, audience=aud, algorithms=['HS256'])
    except jwt.ExpiredSignatureError :
        print("erroing.................")
        decoded = {"error_msg":"is timeout !!","some":None}
    except Exception:
        decoded ={"error_msg":"noknow exception!!","some":None}
        print("erroing2.................")
    return decoded

# md5Encoding('xiaomdingdkdkkd'.encode(encoding='utf-8'))



# decond ='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MTM0MTY4MzcsImF1ZCI6IndlYmtpdCIsInNvbWUiOnsiaWQiOjEyLCJ1c2VybmFtZSI6IjIyMzQiLCJlbWFpbCI6IjIzNDIzZHNkIn19.Mr4-2NLwS0qv4NbXOPJkE8T15MFnxn-tlRyIk7igyXk'
# jsonst = jwtDecoding(decond)
# print(jsonst)
# ou=jsonst['some']
# print(ou)
# print(ou['id'])

"""

option ={
    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=180),
    'aud': 'ouyangouyang',
    'some':{
        "username":"xiaoming",
        "role":"admin"
    }
}


encoded = jwt.encode(option, 'secret', algorithm='HS256')
print(encoded)
encoded2=jwt.encode(option, 'secret',algorithm='HS256', headers={'kid': '230498151c214b788dd97f22b85410a5'})
print(encoded2)

token ='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MTM0MTE4MDksImF1ZCI6Im91eWFuZ291eWFuZyIsInNvbWUiOnsidXNlcm5hbWUiOiJ4aWFvbWluZyIsInJvbGUiOiJhZG1pbiJ9fQ.hggReinf7BzpRM3XmuvNX6VAFpkT0EhiSRgudYw9bKo'
decoded = jwt.decode(token, 'secret', audience='ouyangouyang', algorithms=['HS256'])
print(decoded)
print(decoded['aud'])

"""



"""

encoded = jwt.encode({'some': 'payload'}, 'secret', leeway=datetime.timedelta(seconds=10), algorithm='HS256')
print(encoded)
encoded2=jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256', headers={'kid': '230498151c214b788dd97f22b85410a5'})
print(encoded2)

"""
