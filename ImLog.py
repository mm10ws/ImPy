__author__ = 'Mayur Mehta'
import math

import ImgIO


def log(image1, base):  # computes log with given base
    return_list = []
    for i in range(0, len(image1.value_list)):
        tmp = int(math.log(image1.value_list[i], base))
        if 0 <= tmp <= 255:
            return_list.append(tmp)
        else:
            return_list.append(tmp % 255)  # loop values around if saturation
    return return_list


def main():  # test case
    print('start!!!!!')
    ima = ImgIO.ImgIO()
    ima.read_image("test.png")
    log_list = log(ima, 2)
    imc = ImgIO.ImgIO()
    imc.read_list(log_list, "final10.png", ima.width, ima.height)
    imc.write_image("final10.png")


if __name__ == '__main__':
    main()