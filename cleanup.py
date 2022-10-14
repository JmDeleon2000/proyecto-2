import os
from PIL import Image
import zipfile
import re
import numpy as np


if not os.path.isdir('jpgs'):
    os.mkdir('jpgs')

dims = (1000, 1000)

zip = zipfile.ZipFile('data/mayo-clinic-strip-ai.zip')

#Te prometo que no es una zipbomb
Image.MAX_IMAGE_PIXELS = None




regex= r'train/(\w*)[.tif$|.tiff$]'
for i in zip.namelist():
    if not re.match(regex, i):
        continue

    filename = re.findall(regex, i)[0]
    newfilename = f'jpgs/{filename}.jpg'
    if os.path.isfile(newfilename):
        continue
    print(f'Working on {i} ...')

    with zip.open(i) as file:
        img = Image.open(file)
        img = img.convert(mode='L')
        img = np.array(img)
        img[img > 240] = 0
        img = Image.fromarray(img)
        img = img.crop((0, 0, img.size[0], img.size[1]/2))
        img = img.resize(dims, Image.Resampling.BICUBIC, box = img.getbbox(), reducing_gap=1.5)
        img.save(newfilename, quality=90, optimize=True)

