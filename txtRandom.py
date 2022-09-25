import os
import random


def main():
    path = 'data/labels'
    files = os.listdir(path)
    num = len(files)
    list = range(num)
    tr = int(num * 0.8)
    train = random.sample(list, tr)
    trainval = open('data/train.txt', 'w')
    test = open('data/val.txt', 'w')

    root = 'data/images/'
    for i in list:
        name = root + files[i][:-4] + '.jpg\n'
        if i in train:
            trainval.write(name)
        else:
            test.write(name)

    trainval.close()
    test.close()


# 将data/labels下的txt分成训练txt和val.txt
if __name__ == '__main__':
    main()
