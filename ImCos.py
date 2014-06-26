__author__ = 'Mayur M'
import math

import ImgIO


def cos(image1):  # computes cos of image values
    return_red = []
    return_green = []
    return_blue = []
    for i in range(0, len(image1.red)):
        tmp_r = int(math.cos(image1.red[i]) * 255)
        tmp_g = int(math.cos(image1.green[i]) * 255)
        tmp_b = int(math.cos(image1.blue[i]) * 255)
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
    cos_r, cos_g, cos_b = cos(ima)
    imc = ImgIO.ImgIO()
    imc.read_list(cos_r, cos_g, cos_b, "final8.png", ima.width, ima.height)
    imc.write_image("final8.png")


if __name__ == '__main__':
    main()