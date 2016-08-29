from x256 import x256
import os
import time
from optparse import OptionParser
from PIL import Image, ImageSequence
from imterminal import ImTerminal



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
    index = 0

    for frame in ImageSequence.Iterator(image):

        if index == 0:
            imt = ImTerminal(opt.width, opt.height)
            if opt.height:
                f.write(str(opt.height) + "\n")
            else:
                f.write(str(frame.size[1]) + "\n")

        tmp = imt.convert(frame.convert('RGB'))
        f.write(tmp)
#        print len(tmp)/int(opt.width)/int(opt.height)
        f.write(str(frame.info['duration']) + "\n")
        index = index + 1
    f.close()
