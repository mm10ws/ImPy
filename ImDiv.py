__author__ = 'Mayur M'
import ImgIO


def div(image1, image2):  # divide two images
    if image1.width == image2.width and image1.height == image2.height:
        return_red = []
        return_green = []
        return_blue = []
        for i in range(0, len(image1.red)):
            if image2.red[i] != 0:
                tmp_r = image1.red[i] / image2.red[i]
            else:
                tmp_r = 255  # zero divide trap
            if image2.green[i] != 0:
                tmp_g = image1.green[i] / image2.green[i]
            else:
                tmp_g = 255  # zero divide trap
            if image2.blue[i] != 0:
                tmp_b = image1.blue[i] / image2.blue[i]
            else:
                tmp_b = 255  # zero divide trap
            return_red.append(tmp_r)
            return_green.append(tmp_g)
            return_blue.append(tmp_b)

        return return_red, return_green, return_blue
    else:
        print "Error: image dimensions do not match!"


def main():  # test case
    print('start!!!!!')
    ima = ImgIO.ImgIO()
    imb = ImgIO.ImgIO()
    ima.read_image("y.jpg")
    imb.read_image("test1.png")
    div_r, div_g, div_b = div(ima, imb)
    imc = ImgIO.ImgIO()
    imc.read_list(div_r, div_g, div_b, "final4.png", ima.width, ima.height)
    imc.write_image("final4.png")


if __name__ == '__main__':
    main()