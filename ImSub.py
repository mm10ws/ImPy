__author__ = 'Mayur M'
import ImgIO


def sub(image1, image2):  # subtract two images
    if image1.width == image2.width and image1.height == image2.height:
        return_red = []
        return_green = []
        return_blue = []
        for i in range(0, len(image1.red)):
            tmp_r = image1.red[i] - image2.red[i]  # subtract the RGB values
            tmp_g = image1.green[i] - image2.green[i]
            tmp_b = image1.blue[i] - image2.blue[i]
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
    else:
        print "Error: image dimensions do not match!"


def main():  # test case
    print('start!!!!!')
    ima = ImgIO.ImgIO()
    imb = ImgIO.ImgIO()
    ima.read_image("y.jpg")
    imb.read_image("test1.png")
    sub_r, sub_g, sub_b = sub(ima, imb)
    imc = ImgIO.ImgIO()
    imc.read_list(sub_r, sub_g, sub_b, "final2.png", ima.width, ima.height)
    imc.write_image("final2.png")


if __name__ == '__main__':
    main()