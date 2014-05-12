__author__ = 'Mayur Mehta'
import math

import ImgIO


def e(image1, number):  # number to the power of image where number is a float
    return_list = []
    for i in range(0, len(image1.value_list)):
        tmp = int(math.floor(number ** image1.value_list[i]))
        if 0 <= tmp <= 255:
            return_list.append(tmp)
        else:
            return_list.append(tmp % 255)  # loop values around if saturation
    return return_list


def main():  # test case
    print('start!!!!!')
    ima = ImgIO.ImgIO()
    ima.read_image("test.png")
    e_list = e(ima, 2)
    imc = ImgIO.ImgIO()
    imc.read_list(e_list, "final6.png", ima.width, ima.height)
    imc.write_image("final6.png")


if __name__ == '__main__':
    main()