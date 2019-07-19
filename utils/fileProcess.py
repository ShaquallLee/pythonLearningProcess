import os


def listDir(path, list_name):  # 传入存储的list
    '''
    读取目录下所有文件
    :param path:
    :param list_name:
    :return:
    '''
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listDir(file_path, list_name)
        else:
            list_name.append(file_path)


def getFileText(filename):
    '''
    读取text
    :param filename:
    :return:
    '''
    text = ''
    try:
        with open(filename, 'r', encoding='gbk') as f:
            text_l = f.readlines()
    except:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                text_l = f.readlines()
        except:
            print('read {} error'.format(filename))
            return ''
    for item in text_l:
        text += item.replace('\n', '')
    return text


def removeFileFromList(file_list):
    '''
    删除文件夹中符合规则的文件
    :param file_list:文件列表
    :return:
    '''
    for file_path in file_list:
        if (os.path.exists(file_path)):
            os.remove(file_path)
        else:
            print(file_path, 'not exit')
    return True


def removeFileByFileTypeFromFilelist(file_list, file_type):
    '''
    删除列表中指定类型的文件
    :param file_list:
    :param file_type:
    :return:
    '''
    for file_path in file_list:
        if file_path.split('.')[-1] == file_type:
            if os.path.exists(file_path):
                print('移除目录下文件：%s' % file_path)
                os.remove(file_path)
            else:
                print(file_path, 'not exit')


def removeFileByFileTypeFromFolder(folder_path, file_type):
    '''
    删除文件夹下指定类型的文件
    :param folder_path:文件夹地址
    :param file_type:文件类型
    :return:
    '''
    file_list = []
    listDir(folder_path, file_list)
    for file_path in file_list:
        if file_path.split('.')[-1] == file_type:
            if os.path.exists(file_path):
                print('移除目录下文件：%s' % file_path)
                os.remove(file_path)
            else:
                print(file_path, 'not exit')
