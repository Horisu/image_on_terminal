from x256 import x256
import cv2
import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i","--image", dest="image",
                  help="original image", metavar="IMAGE")
parser.add_option("-f","--file", dest="file",
                  help="write to FILE", metavar="FILE")
parser.add_option("--width", dest="width",
                  help="output width", metavar="WIDTH")
parser.add_option("--height", dest="height",
                  help="output height", metavar="HEIGHT")


(opt, args) = parser.parse_args()

if not opt.image:
    print "please specify image file"
    exit()
if not opt.file:
    print "please specify output file"
    exit()

if os.path.exists(opt.file):
    print "{} already exists".format(opt.file)
    os.remove(opt.file)
    print "{} is removed".format(opt.file)

image = cv2.imread(opt.image);

if image is None:
    print "not found such image file"
    exit()

h, w = image.shape[:2]

print "height = {}".format(h)
print "width  = {}".format(w)

b = 0
g = 1
r = 2

f = open(opt.file, "w")

for i in range(h):
    tmp = ""
    for j in range(w):
        tmp = tmp + '\\e[48;5;' + str( x256.from_rgb(image[i,j,r],image[i,j,g],image[i,j,b]) ) + "m  "

    tmp = tmp + '\\e[0m'
    tmp = tmp + "\n"
    f.write(tmp)

f.close()
