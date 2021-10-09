#!/usr/bin/env python3

# this script read a text file with x rows times y columns, and output a file with y rows and x column.
# for examples：
# input：                     output：
#   1 2 3                     1 a 一
#   a b c                     2 b 二
#   一 二 三                  3 c 三

import sys
import os

# founction


def row2column():
    row_length = []
    rows = {}
    with open( input_file , 'r') as fip:
        data = fip.readlines()
        for i in range(len(data)):
            data[i] = data[i].replace('\n','')
        # print(len(data))
        print(data)

        # i=0
        # for i in range(len(data)):
        #     datasplit.append() = data[i].split(' ')
        #     # print(data[i].split())
        #     break
        # print(datasplit)

        # for ele in datasplit[::-1]:
        #     # print(ele)
        #     if len(ele) == 0:
        #         data.remove(ele)
        # print(datasplit)

        print(len(data))
        for i in range(len(data)):
            # for j in range(len(data[i])):
            row_length.append( len(data[i].split()) )
            rows['row_' + str(i)] = data[i].split()
            # print(data[i].split())

        print(row_length)
        print(rows)

        # print(data)
        # print(max(row_length))

        # i = 0
        # j = 0

        # for key,value in rows.items():
        #     # print(value)
        #     for ele in value[::-1]:
        #         # print(ele)
        #         if len(ele) == 0:
        #             value.remove(ele)
        #     # print(value)

        i = 0
        j = 0
        with open( output_file ,'a') as fop:
            for j in range(max(row_length)):
                for i in range(len(row_length)):
                    # print(rows['row_' + str(i)][j])
                    # break
                    fop.write(rows['row_' + str(i)][j] + ' ')
                fop.write('\n')


# main program
# Read command line arguments
if len(sys.argv) == 1:
    print('Correct usage: row2column.py input_file_name output_file_name')
    sys.exit()
else:
    input_file   = sys.argv[1]
    output_file  = sys.argv[2]

# check if the file exists
if not os.path.isfile(input_file):
    print("Cannot find input file in your system")
    sys.exit()

if not os.path.exists(output_file):
    print("Cannot find output file in your system")
    os.system('touch ' + output_file)

row2column()
