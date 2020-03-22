import cv2 
import numpy as np 
import os
from tqdm import tqdm
from random import shuffle

test_path = '/home/abhinavjava/Projects/img_classification/bird_species/dataset/test/'
train_path = '/home/abhinavjava/Projects/img_classification/bird_species/dataset/train/'
valid_path = '/home/abhinavjava/Projects/img_classification/bird_species/dataset/valid/'
BIRD_150 = '/home/abhinavjava/Projects/img_classification/bird_species/dataset/BIRDS-150.txt'
IMG_SIZE = 224


def get_label(name, file_path=BIRD_150):
    x = -1
    with open(file_path, 'r') as f:
        content = f.read()
        l = content.split(',')
        # print(l)
        # print("first element", l[0])
        x = l.index(name)


    return x



def gen_train_data(train_path):
    X_train = []
    Y_train = []
    training_data = []

    for species in tqdm(os.listdir(train_path)):
        #print(species)
        for ind, p in enumerate(os.listdir(os.path.join(train_path, species))):
            pic_path = str(os.path.join(train_path, species) + '/'+str(p))
            #print(pic_path)
            label = get_label(str(species))

            #print(label)
            try:
                assert(label>=0)
                image = cv2.imread(pic_path)
                image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
                training_data.append([image, label])
                
            except:
                pass
            


    shuffle(training_data)

    for features, labels in training_data:
        X_train.append(features)
        Y_train.append(labels)

    # Y_train = np_utils.to_categorical(Y_train, 150)

    X_train = np.array(X_train).reshape(-1, IMG_SIZE, IMG_SIZE, 3)
    np.save('X_valid.npy', X_train)
    np.save('Y_valid.npy', Y_train)

    return (X_train, Y_train)

        
gen_train_data(valid_path)

