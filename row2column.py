#!/usr/bin/env python3

# this script read a text file with x rows times y columns, and output a file with y rows and x column.
# The length of all rows need to be equal, same for column.
# for examples：
# input：                     output：
#   1 2 3                     1 a 一
#   a b c                     2 b 二
#   一 二 三                  3 c 三

import sys
import os


def row2column(input_file, output_file):
    column_number = 0
    # ie. row_length
    data_dict = {}

    with open(input_file, 'r') as fip:
        data = fip.readlines()
        # print(type(data))
        # print(data)
        # print(data[0])
        row_number = len(data)

        for i in range(len(data)):
            data_dict['row_' + str(i)] = data[i].split()

            if column_number != len(data_dict['row_' + str(i)]):
                column_number = len(data_dict['row_' + str(i)])
                # print('column_number first set')
            else:
                print('check of column_number pass')
        # print(data_dict)

        with open(output_file, 'w') as fop:
            for i in range(column_number):
                for j in range(row_number):
                    fop.write(data_dict['row_' + str(j)][i].ljust(8))
                fop.write('\n')

        # print(len(data))
        # print(row_number)
        # print(column_number)


# main program
# Read command line arguments
# main()
def main():
    if len(sys.argv) == 1:
        print('Correct usage: row2column.py input_file_name output_file_name')
        sys.exit()
    else:
        Ginput_file = sys.argv[1]
        Goutput_file = sys.argv[2]

    # check if the file exists
    if not os.path.isfile(Ginput_file):
        print("Cannot find input file in your system")
        sys.exit()

    file_path = os.path.split(Ginput_file)
    print(file_path)

    if not os.path.exists(file_path[0] + '/' + Goutput_file):
        print("Cannot find output file in your system, now create it")
        cmd = 'touch ' + file_path[0] + '/' + Goutput_file
        print(cmd)
        os.system(cmd)

    row2column(Ginput_file, file_path[0] + '/' + Goutput_file)


if __name__ == "__main__":
    main()
