__author__ = 'Mayur M'
import math

import ImgIO


def tan(image1):  # computes tan of image values
    return_red = []
    return_green = []
    return_blue = []
    for i in range(0, len(image1.red)):
        tmp_r = int(math.tan(image1.red[i]) * 255)
        tmp_g = int(math.tan(image1.green[i]) * 255)
        tmp_b = int(math.tan(image1.blue[i]) * 255)
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
    tan_r, tan_g, tan_b = tan(ima)
    imc = ImgIO.ImgIO()
    imc.read_list(tan_r, tan_g, tan_b, "final9.png", ima.width, ima.height)
    imc.write_image("final9.png")


if __name__ == '__main__':
    main()