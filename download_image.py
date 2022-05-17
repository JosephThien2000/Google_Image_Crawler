from asyncio import protocols
import os
import requests
from PIL import Image, ImageTk
from pathlib import *

# Change directory function
def change_dir_Resize(path, subdir_name):
    """
        Tạo thư mục mới và thay đổi thư mục path hiện tại thành thư mục mới
    """

    # change directory to current path
    os.chdir(path)

    # create new directory
    new_dir = path + '/images'
    p = Path(new_dir)
    if not p.exists():
        p.mkdir()
    os.chdir(new_dir)

    new_dir = new_dir + f"/{subdir_name}_resized"
    p = Path(new_dir)
    if not p.exists():
        p.mkdir()
    os.chdir(new_dir)

# Change directory function
def change_dir_Original(path, subdir_name):
    """
        Tạo thư mục mới và thay đổi thư mục path hiện tại thành thư mục mới
    """

    # change directory to current path
    os.chdir(path)

    # create new directory
    new_dir = path + '/images'
    p = Path(new_dir)
    if not p.exists():
        p.mkdir()
    os.chdir(new_dir)

    new_dir = new_dir + f"/{subdir_name}_original"
    p = Path(new_dir)
    if not p.exists():
        p.mkdir()
    os.chdir(new_dir)

# download_image_resize function
def download_image_resize(url, name):
    """
        Dowload ảnh về thư mục đã được tạo
    """

    # # creat a new directory, change, and save image
    # change_dir(path)
    
    # download image
    open_img = Image.open(url)
    photo = open_img.resize((224, 224))
    return photo.save(name)

# download_image_originally function
def download_image_originally(url, name):
    """
        Dowload ảnh về thư mục đã được tạo
    """

    # # creat a new directory, change, and save image
    # change_dir(path)
    
    # download image
    photo = Image.open(url)
    return photo.save(name)