import os
path = r"D:\rvl-cdip\images"
for dirpath, dirnames, files in os.walk(path):
    for file in files:
        if file.endswith(".tif"):
            old = os.path.join(dirpath, file)
            new = os.path.splitext(os.path.join(dirpath, file))[0]+'.jpg'
            os.rename(old, new)