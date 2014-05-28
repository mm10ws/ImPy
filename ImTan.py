__author__ = 'Mayur Mehta'
import math

import ImgIO


def tan(image1):  # computes tan of image values
    return_list = []
    for i in range(0, len(image1.value_list)):
        tmp = int(math.tan(image1.value_list[i]))
        if 0 <= tmp <= 255:
            return_list.append(tmp)
        else:
            return_list.append(tmp % 255)  # loop values around if saturation
    return return_list


def main():  # test case
    print('start!!!!!')
    ima = ImgIO.ImgIO()
    ima.read_image("test.png")
    tan_list = tan(ima)
    imc = ImgIO.ImgIO()
    imc.read_list(tan_list, "final9.png", ima.width, ima.height)
    imc.write_image("final9.png")


if __name__ == '__main__':
    main()