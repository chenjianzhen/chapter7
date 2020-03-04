import os

def run(**args):
    """
    列举当前目录下的所有文件
    @return:将文件的列表作为字符串返回
    """
    print('[*] In dirlister module.')
    files = os.listdir('.')

    return str(files)
