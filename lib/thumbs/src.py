# coding: utf-8

""" function to generate thumbnails
    Examples:
    resize_and_crop(path_to_file, '200x0') -> Resize
    resize_and_crop(path_to_file, '0x200') -> Resize
    resize_and_crop(path_to_file, '200x150') -> Resize & Crop
"""

import os
import math
from PIL import Image

from init import app

def scale(max_x, max_y, size):

    # set values
    x, y = size
    new_x = max_x
    new_y = (float(max_x) / x) * y

    # check aspect ratio
    if (new_y < max_y):
        new_y = max_y
        new_x = (float(max_y) / y) * x

    return (math.ceil(new_x), math.ceil(new_y))

def resize_and_crop(path, size='100x100'):

    THUMB_DIR = 'thumbs'
    QUALITY = 92

    # check if there is filename
    if not path:
        return None

    # compute new filename
    x, y = [int(x) for x in size.split('x')]
    filename = os.path.basename(path)
    dirname = os.path.dirname(path)
    root, ext = os.path.splitext(filename)
    new_filename = "%s_%dx%d%s" % (root, x, y, ext)
    new_relative_path = os.path.join(THUMB_DIR, new_filename)
    new_path = os.path.join(dirname, new_relative_path)

    # process image if it doesn't exists
    if not os.path.exists(new_path):

        # open image
        try:
            image = Image.open(path)
        except IOError:
            return None

        # set options
        options = image.info
        options['quality'] = QUALITY

        # resize image
        image_x, image_y = scale(x, y, image.size)
        image.thumbnail((image_x, image_y), Image.ANTIALIAS)

        # crop image height
        if image_y > y & y is not 0:
            center_y = (image_y - y) / 2
            left, top = 0, 0 + int(center_y)
            box = (left, top, left + x, top + y)
            image = image.crop(box)

        # crop image width
        if image_x > x & x is not 0:
            center_x = (image_x - x) / 2
            left, top = 0 + int(center_x), 0
            box = (left, top, left + x, top + y)
            image = image.crop(box)

        # save image
        new_dirname = os.path.join(dirname, THUMB_DIR)
        if not os.path.exists(new_dirname):
            os.makedirs(new_dirname)
        try:
            image.save(new_path, **options)
        except IOError:
            return None

    return new_relative_path

def get_thumb(filename, size, directory):
    
    # check if file exists
    path = os.path.join(app.project_dir, app.config['MEDIA_ROOT'], directory, filename)
    if not os.path.exists(path):
        filename = 'default.png'
        directory = 'default'
        path = os.path.join(app.project_dir, app.config['MEDIA_ROOT'], directory, filename)

    # resize and crop
    new_relative_path = resize_and_crop(path, size)
    if new_relative_path is not None:
        url = app.config['MEDIA_URL'] + directory + '/' + new_relative_path
    else:
        url = ''
    return url

