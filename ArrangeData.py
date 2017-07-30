import os
import PIL
from PIL import Image
import PIL.ImageOps
from scipy.misc import imread


dir_path = os.path.dirname(os.path.realpath(__file__))
size = 100, 100

# Add Test Data folder
testdatapath = dir_path + "/old_test_data"
newtestdatapath = dir_path + "/new_test_data"

def get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

            #New File path to save data
            finalfilepath = os.path.join(newtestdatapath, filename)
            outfile = os.path.splitext(finalfilepath)[0] + ".png"

            #remove the file if it exists already
            if os.path.exists(outfile):
                os.remove(outfile)

            if filepath != outfile:
                try:
                    im = Image.open(filepath)
                    im.thumbnail(size, Image.ANTIALIAS)
                    offset_x = (size[0] - im.size[0]) / 2
                    offset_y = (size[1] - im.size[1]) / 2
                    offset_tuple = (round(offset_x), round(offset_y))  # pack x and y into a tuple

                    newimg = Image.new('RGBA', size, (255, 255, 255, 255))  # with alpha
                    newimg.paste(im, offset_tuple)

                    #Convert to grayscale image
                    newimg = newimg.convert('L')
                    # newimg.save(outfile)

                    # convertimage = Image.open(outfile)
                    inverted_image = PIL.ImageOps.invert(newimg)
                    # imagem = cv2.bitwise_not(convertimage)
                    # bw = gray.point(lambda x: 0 if x < 128 else 255, '1')
                    inverted_image.save(outfile, "png")
                    finalImage = imread(outfile)
                    imgdata = finalImage.flatten()
                    # finallist.append(imgdata)

                except IOError:
                    print
                    "cannot create thumbnail for '%s'" % filepath

    return file_paths  # Self-explanatory.


# Run the above function and store its results in a variable.
full_file_paths = get_filepaths(testdatapath)

