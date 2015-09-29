#!/usr/bin/env python
# -*- coding:utf-8 -*

"""Copy pictures into a directory according to the name of a picture.

The program is to copy the pictures into a directory according to
the file name of the pictures. For example, the file name is such as
UnitID_BabyID_SerialID.jpg. The file will be copied to the directory
.\UnitID\BabyID\. If the directory does not exist, we will create the
directory.
The source root directory and destination root directory will be assigned
or inputted from the command prompt.
"""

__author__ = "Zhiwei Yan"
__copyright__ = "Copyright 2015, The CopyPic Project"
__credits__ = ["Zhiwei Yan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Zhiwei YAN"
__email__ = "jerod.yan@gmail.com"
__status__ = "Production"

import os
import glob
import time


FILE_NAME_SPLIT_BLOCK_NUM = 2
FILE_NAME_SPLIT_SEPARATOR = '_'
PATH_SEPARATOR  = "/"
WILD_FILE_PATTERN = "*.bmp"
SLEEP_TIME_DURATION = 5
LINE_SEPARATOR_CHAR = '*'
LINE_SEPARATOR_CHAR_NUM = 60


def list_file(d):
    return glob.glob(d)

# Create main application
if __name__ == '__main__':

    # input the source root directory and the destination root directory
    src_root_dir = raw_input("The source root directory (/home/from/): ")
    des_root_dir = raw_input("The destination root directory (/home/to/): ")

    print 'From ' + src_root_dir + ' To ' + des_root_dir

    while True:
        print LINE_SEPARATOR_CHAR * LINE_SEPARATOR_CHAR_NUM
        print time.ctime()

        # get file name list in the source root dir
        file_list = list_file(src_root_dir + WILD_FILE_PATTERN)

        if not file_list:
            time.sleep(SLEEP_TIME_DURATION)
            continue

        # copy the file if the file name is correct, such as AB001_BABY002_0004.bmp
        for file_fullname in file_list:
            file_basename = os.path.basename(file_fullname)
            path_list = file_basename.split(FILE_NAME_SPLIT_SEPARATOR, FILE_NAME_SPLIT_BLOCK_NUM)

            if len(path_list) > FILE_NAME_SPLIT_BLOCK_NUM:

                des_path = des_root_dir + path_list[0] + PATH_SEPARATOR + path_list[1]

                # make the destination dir
                if not os.path.exists(des_path):
                    try:
                        os.makedirs(des_path)
                    except StandardError:
                        print 'make dir error!' + des_path

                # move the file to destination dir
                des_full_name = des_path + PATH_SEPARATOR + file_basename
                try:
                    os.rename(file_fullname, des_full_name )
                except StandardError:
                    print 'move file error!'

                print file_fullname, " --> ", des_full_name

            else:
                continue




#
