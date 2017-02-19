#-*- coding: utf-8 -*-

import sys
import os

def write_stdout(s):
    sys.stdout.write(s)
    sys.stdout.flush()
    
def main():
    while 1:
        # transition from ACKNOWLEDGED to READY
        write_stdout('READY\n')

        # read header line and print it to stderr
        line = sys.stdin.readline()

        with open('event.log', 'a') as f:
            f.write(line)

        headers = dict([ x.split(':') for x in line.split() ])
        data = sys.stdin.read(int(headers['len']))

        with open('event.log', 'a') as f:
            f.write(data)
            f.write('\n\n')

        write_stdout('RESULT 2\nOK')
        
if __name__ == '__main__':
    main()