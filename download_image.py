from asyncio import protocols
import os
import requests
from PIL import Image, ImageTk

# Change directory function
def change_dir(path):
    """
        Tạo thư mục mới và thay đổi thư mục path hiện tại thành thư mục mới
    """

    # change directory to current path
    os.chdir(path)

    # create new directory
    new_dir = path + "/" + 'image'

    # check if directory exists
    try:
        os.mkdir(new_dir)
    except:
        for retry in range(100):
            try:
                os.rename(new_dir,new_dir)
                break
            except:
                print("rename failed, retrying...")

    return os.chdir(new_dir)

# Download_image function
def download_image(url, name):
    """
        Dowload ảnh về thư mục đã được tạo
    """

    # # creat a new directory, change, and save image
    # change_dir(path)
    
    # download image
    open_img = Image.open(url)
    photo = open_img.resize((224, 224))
    return photo.save(name)