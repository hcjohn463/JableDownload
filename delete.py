import os

def deleteMp4(folderPath):
    originFile = folderPath.split(os.path.sep)[-1] + '.mp4'
    # 找出所有不是originFile的mp4文件(保留封面图片)
    files = [file for file in os.listdir(folderPath) if file.endswith('.mp4') and file != originFile]
    for file in files:
        os.remove(os.path.join(folderPath, file))


def deleteM3u8(folderPath):
    files = os.listdir(folderPath)
    for file in files:
        if file.endswith('.m3u8'):
            os.remove(os.path.join(folderPath, file))
