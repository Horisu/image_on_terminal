from x256 import x256
import cv2
import os
from optparse import OptionParser


class ImTerminal:

    def __init__(self, width=None, height=None):
        self.w = width
        self.h = height

    def convert(self, image):
        h, w = image.shape[:2]

        print "height = {}".format(h)
        print "width  = {}".format(w)

        b = 0
        g = 1
        r = 2

        tmp = ""
        for i in range(h):
            for j in range(w):
                tmp = tmp + '\\e[48;5;' + str( x256.from_rgb(image[i,j,r],image[i,j,g],image[i,j,b]) ) + "m" + "  "

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
                    
    image = cv2.imread(opt.image);

    f = open(opt.output, "w")

    imt = ImTerminal(opt.width, opt.height)
    abc = imt.convert(image)
    f.write(abc)
    f.close()
