__author__ = 'Mayur Mehta'
#handles the input and output of images
#images are converted to grayscale 0 to 255 value set
#jpg are converted to png
import Image


class ImgIO:
    value_list = []
    height = 0
    width = 0
    image_name = "none.png"

    def __init__(self):
        value_list = []
        height = 0
        width = 0
        image_name = "none.png"

    def read_image(self, image_name):  # image name --- xxx.ext
        im = Image.open(image_name).convert('LA')  # Can be many different formats.
        pix = im.load()
        self.width = im.size[0]
        self.height = im.size[1]
        self.image_name = image_name
        for i in range(0, im.size[0]):
            for j in range(0, im.size[1]):
                self.value_list.append(pix[i, j][0])

    def write_image(self):
        im = Image.new('LA', (self.width, self.height))
        pix = im.load()
        for i in range(0, self.width):
            for j in range(0, self.height):
                pix[i, j] = (self.value_list[i * self.height + j], 255)
        im.save(self.image_name)

    def read_list(self, input_list, name, width, height):
        if len(input_list) == 2 * width * height:
            self.value_list = input_list
            self.width = width
            self.height = height
            self.image_name = name
        else:
            print "Incorrect dimensions for specified image list"


def main():  # test case
    print('start!!!!!')
    testobj = ImgIO()
    testobj.read_image("test.jpg")
    testobj.write_image("new.png")


if __name__ == '__main__':
    main()
