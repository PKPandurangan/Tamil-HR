import json
import os,sys
# import Image
import numpy
from scipy.misc import imread
from PIL import Image
import csv
import json


finallist = []


def get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.
    newlist = []

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
            if filepath.endswith('.JPEG'):
                try:
                    im = Image.open(filepath)
                    # finalImage = imread(filepath)
                    # for pixel in iter(im.getdata()):
                    #     print(pixel)
                    greyscale_map = list(im.getdata())
                    # greyscale_map = numpy.array(greyscale_map)
                    # imgdata = im.flatten()

                    fname = os.path.splitext(filename)[0]
                    filetype = fname.split('-', 1)

                    newlist = (greyscale_map, str(filetype[1]))
                    # newlist.append(greyscale_map)
                    # newlist[1].append(str(filetype[1]))

                    # aarray = numpy.empty((3,), dtype=object)
                    # aarray = numpy.array(im.getdata(), str(filetype[1]))

                    # eacharray = numpy.array(greyscale_map, filetype[1], dtype=object)
                    finallist.append(newlist)
                    # print(imgdata)
                except IOError:
                    print
                    "cannot create thumbnail for '%s'" % filepath

    return file_paths  # Self-explanatory.


dir_path = os.path.dirname(os.path.realpath(__file__))
newtestdatapath = dir_path + "/new_train_data"

# Run the above function and store its results in a variable.
full_file_paths = get_filepaths(newtestdatapath)

with open('data.json', 'w') as outfile:
    json.dump(finallist, outfile)

#
# thefile = open('test.txt', 'w')
# for item in finallist:
#   thefile.write("%s\n" % item)

# with open('list.txt', 'w') as fp:
#     fp.write('\n'.join('%s %s' % x for x in finallist))

# with open('finallist.csv','w') as out:
#     csv_out = csv.writer(out)
#     # csv_out.writerow(['name', 'num'])
#     for row in finallist:
#         csv_out.writerows(row)

# narray = numpy.array(finallist)
# print(narray)