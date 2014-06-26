__author__ = 'Mayur M'
# handles the input and output of images

import Image  # using PIL


class ImgIO:
    width = 0
    height = 0
    image_name = "none"
    red = []  # stores image values for red
    green = []  # stores image values for blue
    blue = []  # stores image values for green

    def __init__(self):
        self.red = []
        self.green = []
        self.blue = []
        self.height = 0
        self.width = 0
        self.image_name = "none.png"

    def read_image(self, image_name):  # image name --- xxx.ext
        im = Image.open(image_name)  # Can be many different formats.
        pix = im.load()
        self.width = im.size[0]
        self.height = im.size[1]
        self.image_name = image_name
        tmplist0 = []
        tmplist1 = []
        tmplist2 = []
        for i in range(0, im.size[0]):
            for j in range(0, im.size[1]):
                tmplist0.append(pix[i, j][0])
                tmplist1.append(pix[i, j][1])
                tmplist2.append(pix[i, j][2])
        self.red = tmplist0
        self.green = tmplist1
        self.blue = tmplist2

    def write_image(self, name):
        im = Image.new("RGB", (self.width, self.height))
        pix = im.load()
        for i in range(0, self.width):
            for j in range(0, self.height):
                pix[i, j] = (
                    self.red[i * self.height + j], self.green[i * self.height + j], self.blue[i * self.height + j])
        im.save(name)

    def read_list(self, red, green, blue, name, width, height):
        if len(red) == width * height:
            self.red = red
            self.green = green
            self.blue = blue
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
    testobj.read_image("test1.png")
    testobj.write_image("new1.png")


if __name__ == '__main__':
    main()
