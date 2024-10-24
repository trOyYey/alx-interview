#!/usr/bin/python3
"""
0-stats.py module
"""
import sys


def print_data(data):
    ''' prints function for the data '''
    data_o = "File size: {}\n".format(data['size'])
    for key in data['codes']:
        if data['codes'][key] != 0:
            data_o += '{}: {}\n'.format(key, data['codes'][key])
    sys.stdout.write(data_o)
    sys.stdout.flush()


def reformat_data(data, line):
    ''' check if the input is valid and extracts data from it '''
    line = line.rsplit()
    try:
        status = line[-2]
        if status in data['codes']:
            data['codes'][status] += 1
        data['size'] += int(line[-1])
    except (IndexError, ValueError):
        pass


def main(data):
    ''' main entry point '''
    i = 0
    for line in sys.stdin:
        reformat_data(data, line)
        i += 1
        if i % 10 == 0:
            print_data(data)
    print_data(data)


if __name__ == '__main__':
    data = {
        'size': 0, 'codes': {
            '200': 0, '301': 0,
            '400': 0, '401': 0, '403': 0,
            '404': 0, '405': 0, '500': 0
        }
    }

    try:
        main(data)
    except KeyboardInterrupt:
        print_data(data)
        raise

