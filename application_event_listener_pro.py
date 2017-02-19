#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
import json

from supervisor import childutils


def main():
    while 1:
        headers, payload = childutils.listener.wait(sys.stdin, sys.stdout)
        
        with open('event.pro.log', 'a') as f:
            f.write(json.dumps(headers))

        childutils.listener.ok(sys.stdout)
      

if __name__ == '__main__':
    main()
