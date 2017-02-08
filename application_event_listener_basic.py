#!/usr/bin/env python
# -*- coding: utf-8 -*-


# import os
# import sys
# import time

# from supervisor import childutils
# from raven import Client


# sentry = Client('http://bd566ca2cf9f4160bf6ec4dc5ea579fd:ef8f7bd22bba4bcaac466584cc3c1841@h16.mzhen.cn:9090/7')


# class MessageListener(object):
    
#     def __init__(self):
#         self.stdin = sys.stdin
#         self.stdout = sys.stdout
#         self.stderr = sys.stderr

    
#     def write_stdout(self, s):
#         self.stdout.write(s)
#         self.stdout.flush()

    
#     def runresolver(self):

#         while True:
#             # headers, payload = childutils.listener.wait(self.stdin, self.stdout)
#             # print headers, payload

#             # childutils.listener.ok(self.stdout)

#             self.write_stdout('READY\n')

#             line = sys.stdin.readline()
            
#             print line
#             self.write_stdout('OK\n')

            

# def main():
#     message_listener = MessageListener()
#     message_listener.runresolver()


# if __name__ == '__main__':
#     main()



#!/usr/bin/env python
import sys
import os
def write_stdout(s):
    sys.stdout.write(s)
    sys.stdout.flush()
    
def write_stderr(s):
    sys.stderr.write(s)
    sys.stderr.flush()
    
def main():
    while 1:
        # transition from ACKNOWLEDGED to READY
        write_stdout('READY\n')

        # read header line and print it to stderr
        line = sys.stdin.readline()

        write_stderr(line)

        with open('event.log', 'a') as f:
            f.write(line)
            f.write('\n')

        # read event payload and print it to stderr
        headers = dict([ x.split(':') for x in line.split() ])
        data = sys.stdin.read(int(headers['len']))
        write_stderr(data)

        # transition from READY to ACKNOWLEDGED
        write_stdout('RESULT 2\nOK')


        
if __name__ == '__main__':
    main()