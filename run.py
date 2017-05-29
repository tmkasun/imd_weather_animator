import os
import requests
import shutil
import glob
import itertools

import pylab as pl
from bs4 import BeautifulSoup
from Sattellite import Satellite

frame_rate = .05
selected_satellite = Satellite(Satellite.KALPANA1)
selected_satellite.set_image_type(selected_satellite.image_types.INFRARED)
base_url = selected_satellite.get_URL()
sorted_url = base_url + "?C=M;O=D"
data_dir_name = "images/{satellite_name}/{selected_type}/".format(selected_type=selected_satellite.get_image_type(),
                                                                  satellite_name=selected_satellite.name)

if not os.path.exists(data_dir_name):
    os.makedirs(data_dir_name)


def get_images():
    res = requests.get(sorted_url)
    page = BeautifulSoup(res.text, "lxml")
    skip_count = 3
    count = 0
    max_imgs = 15
    for t in page.find_all('tr'):
        count += 1
        if (max_imgs + skip_count) <= count:
            print("All files download successfully ...")
            break
        if count <= skip_count:
            print("Skipping unrelated TRs ...")
            continue
        img_name = t.find_all('a')[0].get('href')
        img_save_path = data_dir_name + img_name
        if os.path.exists(img_save_path):
            print("Skipping download since file({}) is already exist ...".format(img_save_path))
            continue
        print("Downloading file {} ...".format(img_name))
        data = requests.get(base_url + img_name, stream=True)
        if not data.status_code == 200:
            print("Error downloading file!!!")
            break
        with open(img_save_path, 'wb') as img_file:
            print("Writing file {} to disk ...".format(img_save_path))
            data.raw.decode_content = True
            shutil.copyfileobj(data.raw, img_file)


def animate():
    files = sorted(glob.glob(data_dir_name + "*.jpg"))
    img = None
    for image in itertools.cycle(files):
        im = pl.imread(image)
        if img is None:
            img = pl.imshow(im)
        else:
            img.set_data(im)
        pl.pause(frame_rate)
        pl.draw()


def main():
    get_images()
    animate()


if __name__ == '__main__':
    main()
