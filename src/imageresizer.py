#!/usr/bin/env python3
"""Put this in the folder location that you want to resize all of the photos.

This resizes all photos in the current working directory to a specified target width.

"""

import os
import sys
import PIL
from PIL import Image
from pathlib import Path

target_width = 1000  # in pixels

# gather image paths in current directory
current_dir = Path(".")
image_paths = [x for x in current_dir.glob("**/*.jpg")]      #all jpgs recursively

# make directory to save the smaller versions
small_photo_dir = Path("./smallphotos/")
if not small_photo_dir.exists():
    small_photo_dir.mkdir(mode = 0o777)

# resize a photo, JPG, 8 bits per pixel, 3MB limit, 375000 pixels max
def resize_save(photo_width):
    for image_path in image_paths:
        photo = Image.open(image_path)
        photo_width = photo.width
        photo_height = photo.height 

        if photo.width > 600:
            # maintain aspect ratio
            downsize = target_width / photo_width
            rounded_downsize = round(downsize, 4)
            new_height = round(photo_height * rounded_downsize)

            # assemble new photo path 
            image_parts = image_path.absolute().parts
            image_parts = list(image_parts)
            image_parts[7] = "smallphotos"
            new_absolute_path = image_parts[0] + "/".join(image_parts[1:-1]) + "/" + image_path.stem + "_small.jpg"
            print(new_absolute_path)

            # resize
            small_photo = photo.resize((target_width, new_height))

            # store it in the small photo directory
            small_photo.save(new_absolute_path, format="JPEG")
resize_save(target_width)
print("success")

