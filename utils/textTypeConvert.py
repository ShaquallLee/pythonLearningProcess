import base64
import hashlib


def get_md5(text):
    '''
    将text编码为md5形式
    :param text:
    :return:
    '''
    md5 = hashlib.md5()
    md5.update(text)
    return md5.hexdigest()


def get_sha1(text):
    '''
    SHA1编码
    :param text:
    :return:
    '''
    sha1 = hashlib.sha1()
    sha1.update(text)
    return sha1.hexdigest()


def get_base64(text, code):
    '''
    将text编码为base64型
    :param text:
    :return:
    '''
    bs = bytes(text, encoding=code)
    return base64.b64encode(bs)


def get_text_from_base64(text, code):
    '''
    将base64编码的text解码为正常值
    :param text:
    :return:
    '''
    bs = str(text, encoding=code)
    return base64.b64decode(bs)
