__author__ = 'Mayur M'
import math

import ImgIO


def pwr(image1, number):  # image to the power of number where number is a float
    return_red = []
    return_green = []
    return_blue = []
    for i in range(0, len(image1.red)):
        tmp_r = int(math.floor(image1.red[i] ** number))
        tmp_g = int(math.floor(image1.green[i] ** number))
        tmp_b = int(math.floor(image1.blue[i] ** number))
        if 0 <= tmp_r <= 255:
            return_red.append(tmp_r)
        else:
            return_red.append(tmp_r % 255)  # loop values around if saturation
        if 0 <= tmp_g <= 255:
            return_green.append(tmp_g)
        else:
            return_green.append(tmp_g % 255)  # loop values around if saturation
        if 0 <= tmp_b <= 255:
            return_blue.append(tmp_b)
        else:
            return_blue.append(tmp_b % 255)  # loop values around if saturation
    return return_red, return_green, return_blue


def main():  # test case
    print('start!!!!!')
    ima = ImgIO.ImgIO()
    ima.read_image("y.jpg")
    pwr_r, pwr_g, pwr_b = pwr(ima, 2)
    imc = ImgIO.ImgIO()
    imc.read_list(pwr_r, pwr_g, pwr_b, "final5.png", ima.width, ima.height)
    imc.write_image("final5.png")


if __name__ == '__main__':
    main()