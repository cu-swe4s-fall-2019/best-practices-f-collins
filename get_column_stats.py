import sys
import math
import argparse


def main():
    parser = argparse.ArgumentParser(
            description='Program to get stats of a column of data.',
            prog='calculate')

    parser.add_argument('--file_name',
                        type=str,
                        help='The name of the file to get stats from.',
                        required=True)

    parser.add_argument('--col_num',
                        type=int,
                        help='The number of column to be analyzed.',
                        required=True)

    args = parser.parse_args()

    file_name = args.file_name
    col_num = args.col_num

    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('File does not exist or read access is not given.')
        quit(1)

    V = []

    try:
        for l in f:
            A = [int(x) for x in l.split()]
            V.append(A[col_num])
    except IndexError:
        print('Column does not exist in data file.')
        print('Ensure that every line has ' + str(args.col_num) + ' values.')
        print('Reminder that columns are zero-indexed.')
        quit(1)
    except ValueError:
        # could be improved by giving the user the offending character and the
        # line it was found on.
        print('Non number found in data.')
        quit(1)

    mean = sum(V)/len(V)

    stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))

    print('mean:', mean)
    print('stdev:', stdev)


if __name__ == '__main__':
    main()
