__author__ = 'Mayur Mehta'
#handles the input and output of images
#images are converted to grayscale 0 to 255 value set
#jpg are converted to png
import Image


class ImgIO:
    value_list = []
    height = 0
    width = 0

    def __init__(self):
        value_list = []
        height = 0
        width = 0

    def read_image(self, image_name):  # image name --- xxx.ext
        im = Image.open(image_name).convert('LA')  # Can be many different formats.
        pix = im.load()
        self.width = im.size[0]
        self.height = im.size[1]
        for i in range(0, im.size[0]):
            for j in range(0, im.size[1]):
                self.value_list.append(pix[i, j][0])

    def write_image(self, image_name):
        im = Image.new('LA', (self.width, self.height))
        pix = im.load()
        for i in range(0, self.width):
            for j in range(0, self.height):
                pix[i, j] = (self.value_list[i * self.height + j], 255)
        im.save(image_name)


def main():  # test case
    print('start!!!!!')
    testobj = ImgIO()
    testobj.read_image("test.jpg")
    testobj.write_image("new.png")


if __name__ == '__main__':
    main()
