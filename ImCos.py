__author__ = 'Mayur Mehta'
import math

import ImgIO


def cos(image1):  # computes cos of image values
    return_list = []
    for i in range(0, len(image1.value_list)):
        tmp = int(math.cos(image1.value_list[i]) * 255)
        if 0 <= tmp <= 255:
            return_list.append(tmp)
        else:
            return_list.append(tmp % 255)  # loop values around if saturation
    return return_list


def main():  # test case
    print('start!!!!!')
    ima = ImgIO.ImgIO()
    ima.read_image("test.png")
    cos_list = cos(ima)
    imc = ImgIO.ImgIO()
    imc.read_list(cos_list, "final8.png", ima.width, ima.height)
    imc.write_image("final8.png")


if __name__ == '__main__':
    main()