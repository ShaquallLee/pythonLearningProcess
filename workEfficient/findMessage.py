import os
import re
from utils import listDir, getFileText


def findMessageFromFileList(file_dir, text):
    '''
    从一个文件目录的所有文件中找到所有包含text的文件
    :param file_dir: 文件夹地址
    :param text: 内容/正则表达式
    :return res_l: 符合条件的文件列表
    '''
    if not isinstance(text, str):
        raise TypeError(text, ' is not string.')
    file_list = []
    res_l = []
    listDir(file_dir, file_list)
    for file_path in file_list:
        file_text = getFileText(file_path)
        if re.search(text, file_text) != None:
            res_l.append(file_path)
    return res_l


if __name__ == '__main__':
    file_dir = '../待分析文本/'
    text = '永嘉路'
    # removeFileByFileTypeFromFolder(file_dir, 'struc')
    res_l = findMessageFromFileList(file_dir, text)
    print(res_l)
