__author__ = 'Mayur Mehta'
import ImgIO


def mult(image1, image2):  # multiply two images
    if image1.width == image2.width and image1.height == image2.height:
        return_list = []
        for i in range(0, len(image1.value_list)):
            tmp = image1.value_list[i] * image2.value_list[i]
            if 0 <= tmp <= 255:
                return_list.append(tmp)
            else:
                return_list.append(tmp % 255)  # loop values around if saturation
        return return_list
    else:
        print "Error: image dimensions do not match!"


def main():  # test case
    print('start!!!!!')
    ima = ImgIO.ImgIO()
    imb = ImgIO.ImgIO()
    ima.read_image("test.png")
    imb.read_image("new.png")
    mult_list = mult(ima, imb)
    imc = ImgIO.ImgIO()
    imc.read_list(mult_list, "final3.png", ima.width, ima.height)
    imc.write_image("final3.png")


if __name__ == '__main__':
    main()