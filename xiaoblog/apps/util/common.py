import logging

ALLOWED_file_EXTENSIONS = set(['md', 'MD', 'word', 'txt', 'py', 'java', 'c', 'c++', 'xlsx'])
ALLOWED_photo_EXTENSIONS = set(['png', 'jpg', 'xls', 'JPG', 'PNG', 'gif', 'GIF'])

#日志打印模板
def getLogger():
    logger = logging.getLogger("Debuger")
    logger.setLevel(logging.DEBUG)
    dh=logging.FileHandler("F:/pypro")
    ## '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    dh.setFormatter(formatter)

    logger.addHandler(dh)
    return  logger

import hashlib
# md5 32位加密
def md5(strs):
    m2=hashlib.md5()
    m2.update(strs.encode('utf8'))
    return m2.hexdigest()

def verifyMd5(strs,hash_strs):
    if md5(strs)==hash_strs:
        return True
    else:
        return False

 # 生成随机数量
from random import Random
def random_str(randomlength=5):
    _str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        _str += chars[random.randint(0, length)]
    return _str

def allowed_photo(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_photo_EXTENSIONS

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_file_EXTENSIONS

# 截取字符串
def getstrsplit(beginint,strs):
    lens=len(strs)
    return strs[beginint:lens]

def trueReturn(data, msg='success'):
    return {
        "status": True,
        "data": data,
        "msg": msg
    }


def falseReturn(data, msg='fail'):
    return {
        "status": False,
        "data": data,
        "msg": msg
    }

# stl = 'Ifyouusenode.js, you should require the module first:'
# print(getstrsplit(4,stl))
