__author__ = 'Mayur Mehta'
import math

import ImgIO


def log(image1, base):  # computes log with given base
    return_red = []
    return_green = []
    return_blue = []
    for i in range(0, len(image1.red)):
        if image1.red[i] != 0:
            tmp_r = int(math.log(image1.red[i], base))
            if 0 <= tmp_r <= 255:
                return_red.append(tmp_r)
            else:
                return_red.append(tmp_r % 255)  # loop values around if saturation
        else:
            return_red.append(255)  # zero divide trap
        if image1.green[i] != 0:
            tmp_g = int(math.log(image1.green[i], base))
            if 0 <= tmp_g <= 255:
                return_green.append(tmp_g)
            else:
                return_green.append(tmp_g % 255)  # loop values around if saturation
        else:
            return_green.append(255)  # zero divide trap
        if image1.blue[i] != 0:
            tmp_b = int(math.log(image1.blue[i], base))
            if 0 <= tmp_b <= 255:
                return_blue.append(tmp_b)
            else:
                return_blue.append(tmp_b % 255)  # loop values around if saturation
        else:
            return_blue.append(255)  # zero divide trap

    return return_red, return_green, return_blue


def main():  # test case
    print('start!!!!!')
    ima = ImgIO.ImgIO()
    ima.read_image("y.jpg")
    log_r, log_g, log_b = log(ima, 2)
    imc = ImgIO.ImgIO()
    imc.read_list(log_r, log_g, log_b, "final10.png", ima.width, ima.height)
    imc.write_image("final10.png")


if __name__ == '__main__':
    main()