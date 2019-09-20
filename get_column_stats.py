import sys
import math
import argparse


'''Mean and Standard Deviation Functions

    * getmean - returns the mean of a list of numbers.
    * getstdev - returns the standard deviation of a list of numbers.'''
def getmean(V):
    '''Finds the mean of a list of numbers.
    Parameters:
        V: List of numbers.
    Returns:
        The mean of all numbers in the list.
    '''
    if V == []:
        return None

    return sum(V) / len(V)


def getstdev(V):
    '''Finds the standard deviation of a list of numbers.
    Parameters:
        V: List of numbers.
    Returns:
        The standard deviation of all numbers in the list.
    '''
    if V == []:
        return None

    return math.sqrt(sum([(getmean(V)-x)**2 for x in V]) / len(V))


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

    mean = getmean(V)

    stdev = getstdev(V)

    print('mean:', mean)
    print('stdev:', stdev)


if __name__ == '__main__':
    main()
