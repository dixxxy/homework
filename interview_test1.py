def print_directory_contents(sPath):
    """
    这个函数 接受文件夹的名称作为输入参数
    返回该文件夹中文件的路径
    以及其包含在文件夹中文件的路径
    :param sPath:
    :return:
    """
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)