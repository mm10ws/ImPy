__author__ = 'Mayur Mehta'
import ImgIO


def add(image1, image2):  # add two images together
    if image1.width == image2.width and image1.height == image2.height:
        return_list = []
        return_list = [sum(x) for x in zip(image1.value_list, image2.value_list)]
        for i in range(0, len(return_list)):
            if 0 <= return_list[i] <= 255:
                pass
            else:
                return_list[i] = 255
        return return_list
    else:
        print "Error: image dimensions do not match!"
        #return 0


def main():  # test case
    print('start!!!!!')
    ima = ImgIO.ImgIO()
    imb = ImgIO.ImgIO()
    ima.read_image("test.jpg")
    imb.read_image("new.png")
    add_list = add(ima, imb)
    imc = ImgIO.ImgIO()
    imc.read_list(add_list, "final.png", ima.width, ima.height)
    imc.write_image()


if __name__ == '__main__':
    main()