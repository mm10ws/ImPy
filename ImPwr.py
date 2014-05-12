__author__ = 'Mayur Mehta'
import math

import ImgIO


def pwr(image1, number):  # image to the power of number where number is a float
    return_list = []
    for i in range(0, len(image1.value_list)):
        tmp = int(math.floor(image1.value_list[i] ** number))
        if 0 <= tmp <= 255:
            return_list.append(tmp)
        else:
            return_list.append(tmp % 255)  # loop values around if saturation
    return return_list


def main():  # test case
    print('start!!!!!')
    ima = ImgIO.ImgIO()
    ima.read_image("test.png")
    pwr_list = pwr(ima, 10)
    imc = ImgIO.ImgIO()
    imc.read_list(pwr_list, "final5.png", ima.width, ima.height)
    imc.write_image("final5.png")


if __name__ == '__main__':
    main()