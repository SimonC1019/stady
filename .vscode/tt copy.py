from os import *
from os.path import *

# 指定要列出所有檔案的目錄
path = "\user /"

# 取得所有檔案與子目錄名稱
files = listdir(path)

# 以迴圈處理
for f in files:
  # 產生檔案的絕對路徑
  fullpath = join(path, f)
  # 判斷 fullpath 是檔案還是資料夾
  if isfile(fullpath):
    print("檔案：", f)
  elif isdir(fullpath):
    print("資料夾：", f)

"""
f=open('2100.txt','r')
for line in f:
    print(line,end="")
f.close()
"""