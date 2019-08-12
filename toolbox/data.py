from functools import partial

import numpy as np
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from pathlib import Path
from toolbox.image import bicubic_rescale
from toolbox.image import modcrop
from toolbox.paths import data_dir


def load_set(name, lr_sub_size=11, lr_sub_stride=5, scale=3):
    hr_sub_size = lr_sub_size * scale
    hr_sub_stride = lr_sub_stride * scale
    lr_gen_sub = partial(generate_sub_images, size=lr_sub_size,
                         stride=lr_sub_stride)
    hr_gen_sub = partial(generate_sub_images, size=hr_sub_size,
                         stride=hr_sub_stride)

    lr_sub_arrays = []
    hr_sub_arrays = []
    for path in (data_dir / name).glob('*'):
        lr_image, hr_image = load_image_pair(str(path), scale=scale)
        lr_sub_arrays += [img_to_array(img) for img in lr_gen_sub(lr_image)]
        hr_sub_arrays += [img_to_array(img) for img in hr_gen_sub(hr_image)]
    x = np.stack(lr_sub_arrays)
    y = np.stack(hr_sub_arrays)
    return x, y

def load_set_same_size(train_set, lr_sub_size=33, lr_sub_stride=15, scale=2):
    input_dir = data_dir / Path(train_set['input_set'])
    label_dir = data_dir / Path(train_set['label_set'])
    sub_size=lr_sub_size
    sub_stride=lr_sub_stride

    gen_sub = partial(generate_sub_images, size=sub_size,
                         stride=sub_stride)

    lr_sub_arrays = []
    hr_sub_arrays = []

    for i in range(1,400):
        inputFileName = "img{}_00_recon.bmp".format(str(i))
        modelHorFileName = "img{}_03.bmp".format(str(i))
        inputImage = load_img(input_dir / inputFileName)
        labelImage = load_img(label_dir / modelHorFileName)

        lr_sub_arrays += [img_to_array(img) for img in gen_sub(inputImage)]
        hr_sub_arrays += [img_to_array(img) for img in gen_sub(labelImage)]

    x = np.stack(lr_sub_arrays)
    y = np.stack(hr_sub_arrays)

    return x, y

def load_image_pair(path, scale=3):
    image = load_img(path)
    image = image.convert('YCbCr')
    hr_image = modcrop(image, scale)
    lr_image = bicubic_rescale(hr_image, 1 / scale)
    return lr_image, hr_image


def generate_sub_images(image, size, stride):
    for i in range(0, image.size[0] - size + 1, stride):
        for j in range(0, image.size[1] - size + 1, stride):
            yield image.crop([i, j, i + size, j + size])
