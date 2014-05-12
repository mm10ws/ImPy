__author__ = 'Mayur Mehta'
#handles the input and output of images
#images are converted to grayscale 0 to 255 value set
#jpg are converted to png
import Image  # using PIL


class ImgIO:
    width = 0
    height = 0
    image_name = "none"
    value_list = []  # stores image values

    def __init__(self):
        self.value_list = []
        self.height = 0
        self.width = 0
        self.image_name = "none.png"

    def read_image(self, image_name):  # image name --- xxx.ext
        im = Image.open(image_name).convert('LA')  # Can be many different formats.
        pix = im.load()
        self.width = im.size[0]
        self.height = im.size[1]
        self.image_name = image_name
        tmplist = []
        for i in range(0, im.size[0]):
            for j in range(0, im.size[1]):
                tmplist.append(pix[i, j][0])
        self.value_list = tmplist

    def write_image(self, name):
        im = Image.new('LA', (self.width, self.height))
        pix = im.load()
        for i in range(0, self.width):
            for j in range(0, self.height):
                pix[i, j] = (self.value_list[i * self.height + j], 255)
        im.save(name)

    def read_list(self, input_list, name, width, height):
        if len(input_list) == width * height:
            self.value_list = input_list
            self.width = width
            self.height = height
            self.image_name = name
        else:
            print "Incorrect dimensions for specified image list: "
            print width
            print height



def main():  # test case
    print('start!!!!!')
    testobj = ImgIO()
    testobj.read_image("new.jpg")
    testobj.write_image("new1.png")


if __name__ == '__main__':
    main()
