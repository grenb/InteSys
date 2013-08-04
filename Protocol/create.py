# -*- coding: utf-8 -*-
'''
Created on 2013-8-4

@author: GRENB
'''
import os
if __name__ == '__main__':
    print os.system('protoc -I=./ --python_out=./ *.proto')