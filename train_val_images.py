import os
from shutil import copy
from tqdm import tqdm

# Разделим изображения на тренировочную и валидационную выборку

FOLDER = 'labels'


def train_val_split(MODE: str, size: int, folder: str):
    labels = sorted(os.listdir(folder))

    if MODE == 'train':
        train_images_path = 'train/images'
        train_labels_path = 'train/labels'

        if not os.path.isdir(train_images_path):
            os.makedirs(train_images_path)
            os.makedirs(train_labels_path)

        for label in tqdm(labels[:size]):
            img = label[:-4] + '.jpg'
            copy(os.path.join('images', img), os.path.join(train_images_path, img))
            copy(os.path.join('labels', label), os.path.join(train_labels_path, label))

    if MODE == 'val':
        val_images_path = 'val/images'
        val_labels_path = 'val/labels'

        if not os.path.isdir(val_images_path):
            os.makedirs(val_images_path)
            os.makedirs(val_labels_path)

        for label in tqdm(labels[-size:]):
            img = label[:-4] + '.jpg'
            copy(os.path.join('images', img), os.path.join(val_images_path, img))
            copy(os.path.join('labels', label), os.path.join(val_labels_path, label))

    return


train_val_split(MODE='train', size=20, folder=FOLDER)
train_val_split(MODE='val', size=8, folder=FOLDER)
