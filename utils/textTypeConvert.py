import base64


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
