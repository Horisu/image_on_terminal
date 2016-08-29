from x256 import x256
import os
import time
from optparse import OptionParser
from PIL import Image

class ImTerminal:

    def __init__(self, width=None, height=None):
        self.w = width
        self.h = height

    def convert(self, image):
        if self.w or self.h:
            if self.w:
                w = int(self.w)
            else:
                w = image.size[0]
            if self.h:
                h = int(self.h)
            else:
                h = image.size[1]
            im = image.resize((w,h))

        else:
            (w, h) = image.size
            im = image
        tmp = ""
        index = 0
        for i in range(h):
            for j in range(w):
                px = im.getpixel((j,i))
                tmp = tmp + '\\e[48;5;' + str( x256.from_rgb(px[0],px[1],px[2]) ) + "m" + "  "
                index += 1
            tmp = tmp + '\\e[0m'
            tmp = tmp + "\n"

        return tmp



if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-i","--image", dest="image", help="original image", metavar="IMAGE")
    parser.add_option("-o","--output", dest="output", help="write to OUTPUT", metavar="OUTPUT")
    parser.add_option("--width", dest="width", help="output width", metavar="WIDTH")
    parser.add_option("--height", dest="height", help="output height", metavar="HEIGHT")

    (opt, args) = parser.parse_args()

    if not opt.image:
        print "please specify image file"
        exit()
    if not opt.output:
        print "please specify output file"
        exit()

    if os.path.exists(opt.output):
        print "{} already exists".format(opt.output)
        os.remove(opt.output)
        print "{} is removed".format(opt.output)

    image = Image.open(opt.image);

    f = open(opt.output, "w")

    imt = ImTerminal(opt.width, opt.height)
    abc = imt.convert(image)
    f.write(abc)
    f.close()
