# -*- coding: utf-8 -*-
'''
Created on 2013-8-4

@author: GRENB
'''
import msgpack

class outStruct(): 
    opt=None
    arg=None
    res=None

    
if __name__ == '__main__':
    o = outStruct()
    o.opt = 'logi'
    o.arg = 'neww'
    msgpack.packb(o)
    print o.res
    print msgpack.unpackb(o.res)