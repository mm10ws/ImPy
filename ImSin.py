__author__ = 'Mayur Mehta'
import math

import ImgIO


def sin(image1):  # computes sin of image values
    return_list = []
    for i in range(0, len(image1.value_list)):
        tmp = int(math.sin(image1.value_list[i]) * 255)
        if 0 <= tmp <= 255:
            return_list.append(tmp)
        else:
            return_list.append(tmp % 255)  # loop values around if saturation
    return return_list


def main():  # test case
    print('start!!!!!')
    ima = ImgIO.ImgIO()
    ima.read_image("test.png")
    sin_list = sin(ima)
    imc = ImgIO.ImgIO()
    imc.read_list(sin_list, "final7.png", ima.width, ima.height)
    imc.write_image("final7.png")


if __name__ == '__main__':
    main()