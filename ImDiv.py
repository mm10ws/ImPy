__author__ = 'Mayur Mehta'
import ImgIO


def div(image1, image2):  # divide two images
    if image1.width == image2.width and image1.height == image2.height:
        return_list = []
        for i in range(0, len(image1.value_list)):
            if image2.value_list[i] != 0:
                tmp = image1.value_list[i] / image2.value_list[i]
            else:
                tmp = 255  # zero divide trap
            return_list.append(tmp)
        return return_list
    else:
        print "Error: image dimensions do not match!"


def main():  # test case
    print('start!!!!!')
    ima = ImgIO.ImgIO()
    imb = ImgIO.ImgIO()
    ima.read_image("test.png")
    imb.read_image("new.png")
    div_list = div(ima, imb)
    imc = ImgIO.ImgIO()
    imc.read_list(div_list, "final4.png", ima.width, ima.height)
    imc.write_image("final4.png")


if __name__ == '__main__':
    main()