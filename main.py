from utils import *

s = '1234567'
print(s, '转化为', get_md5(s))
print(s, '转化为', get_sha1(s))
result = {
    "result": b"DQoxLiDlh7rnp5/"}
# print('字符串：', s)
# ss = get_base64(s, 'utf-8')
# print('base64编码：', ss)
sss = get_text_from_base64(result['result'], 'utf-8')
print('转化回来的正常字符串形式：', str(sss, encoding='utf-8'))
