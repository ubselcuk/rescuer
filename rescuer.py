from fpdf import FPDF
from PIL import Image
import argparse
import os


def fuck(test, i):
    if test.size[0] > test.size[1]:
        pdf.add_page("L")
        pdf.image(imagelist[i], 0, 0, 297, 210)
    elif test.size[1] > test.size[0]:
        pdf.add_page("P")
        pdf.image(imagelist[i], 0, 0, 210, 297)
    else:
        print("ERROROROROR")


def burn():


    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in [f for f in filenames if f.endswith(".png")]:
            full_path = os.path.join(dirpath, filename)

            
            im1 = Image.open(full_path)
            rgb_im1 = im1.convert('RGB')
            newpath = full_path[:full_path.find('.')]
            rgb_im1.save(newpath + '.jpg')

            oldpng = full_path[:full_path.find('.')]
            os.rename(full_path, oldpng + " saved.png")



    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in [f for f in filenames if f.endswith(".jpg")]:
            full_path = os.path.join(dirpath, filename)
            imagelist.append(full_path)

    imagelist.sort()
    for i in range(0, len(imagelist)):
        im1 = Image.open(imagelist[i])
        width = im1.size[0]
        height = im1.size[1]

        if horv == "v":
            if width > height:
                im2 = im1.transpose(Image.ROTATE_270)
                os.remove(imagelist[i])
                im2.save(imagelist[i])
                test = im2
            else:
                test = im1

            fuck(test, i)

        if horv == "h":
            if height > width:
                im2 = im1.transpose(Image.ROTATE_90)
                os.remove(imagelist[i])
                im2.save(imagelist[i])
                test = im2
            else:
                test = im1

            fuck(test, i)

        if horv == "d":
            fuck(im1, i)

    pdf.output("output/" + name + ".pdf", "F")
    print("All Ok!")


pdf = FPDF()
imagelist = []

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-i', '--input', metavar='')
parser.add_argument('-o', '--output', metavar='')
parser.add_argument('-r', '--rotate', metavar='')
parser.add_argument('-h', '--horizontal', action='store_true')
parser.add_argument('-v', '--vertical', action='store_true')
parser.add_argument('-d', '--default', action='store_true')


args = parser.parse_args()

error = 0
direction = 1

try:

    if args.rotate:
        test = "input/" + args.rotate + ".jpg"
        im1 = Image.open(test)
        im2 = im1.transpose(Image.ROTATE_90)
        os.remove(test)
        im2.save(test)
        print("\nOk!\n")
        exit()

    if args.input:
        folder = args.input
    else:
        print("Input folder selected by default")
        folder = "input"

    if args.output:
        name = args.output
    else:
        print("Enter the name of the pdf file")
        error += 1

    if args.horizontal:
        horv = "h"
        direction = 0

    if args.vertical:
        horv = "v"
        direction = 0

    if args.default:
        horv = "d"
        direction = 0

    if direction > 0:
        print("Enter the direction of the files")
        exit()


    if error == 0 and direction == 0:
        burn()
    else:
        pass


except:
    print('Task failed succesfuly.')
    pass
