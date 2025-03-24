import os

class Archive():
    def __init__(self, fileDepth=8):
        if(self.fileDepth%2 == 1):
            raise IOError("fileDepth must be even")
        self.intFileID = 0
        self.hexFullFileName = ""
        self.fileDepth = fileDepth

    def getHexDIR(self, FileID, fileDepth=8):
        __hex_str = str(hex(FileID))[2:].zfill(self.fileDepth)
        for i in range(int(self.fileDepth/2)):
            self.hexFullFileName += __hex_str[i*2:i*2+2] + "\\"
        self.hexFullFileName = self.hexFullFileName[:-1]
        return self.hexFullFileName

    def getFileID(self, hexFileName):
        fdList = hexFileName.split('\\')[int(self.fileDepth * -1 / 2):]
        result = ''.join(fdList)
        self.intFileID = eval('0x' + str(result[:self.fileDepth]))
        return self.intFileID