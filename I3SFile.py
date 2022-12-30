import os

class Archive():
    def __init__(self):
        pass

    def hex2DIR(self, root, hex_str, file_depth=8, mkdir=False):
        '''
        root : the top folder
        hex_str : hex(decimal number)
        file_depth : the deepth of file, default is 8
        mkdir : Ture if you want to create folder automactically, default if false
        '''
        if(file_depth%2 == 1):
            raise IOError("file_depth must be even")
        __hex_str = hex_str[2:].zfill(file_depth)
        folder_list = []
        for i in range(int(file_depth/2)):
            folder_list.append(__hex_str[i*2:i*2+2])
        path = root  + '\\' +'\\'.join(folder_list[:-1])
        filename = folder_list[-1]
        if mkdir and not os.path.isdir(path):
            os.makedirs(path)
        return(path + '\\' + filename)

    def dir2DEC(self, file_path, file_depth=8):
        '''
        use to scan folder and return decimal
        file_path : file_path
        file_depth : the deepth of file, default is 8
        '''
        if(file_depth%2 == 1):
            raise IOError("file_depth must be even")
        fd_list = file_path.split('\\')[int(file_depth * -1 / 2):]
        result = ''.join(fd_list)
        return(eval('0x' + str(result[:file_depth])))
