# -*- coding: utf-8 -*-
'''
Created on 2013-7-18

@author: grenb
'''
from ctypes import *
from google.protobuf import message
from google.protobuf import descriptor
from google.protobuf import descriptor_pool 
from google.protobuf import message_factory
from google.protobuf import descriptor_pb2
from Protocol import command_pb2
import time

class keywords(Structure): 
    _fields_ = [('words', c_char *10),] 
 
class outStruct(Structure): 
    _fields_ = [ ('opt',c_char_p), ('arg',c_char_p),  ('res',c_char_p),  ] 

def pys():
    for i in range(1):
        run = command_pb2.command()
        run.opt = 'logi'
        run.arg = 'neww'
        res = run.SerializeToString()
        print res
        name = run.DESCRIPTOR.full_name
        print name
        com = createMessage(name)
        com.ParseFromString(res)
        print com.opt
        print com.arg

def createMessage(type_name):
    msg = None
    dp = descriptor_pool.DescriptorPool()
    command_fd = descriptor_pb2.FileDescriptorProto.FromString(command_pb2.DESCRIPTOR.serialized_pb)
    dp.Add(command_fd)
    des = dp.FindMessageTypeByName(type_name)
    if (des):
        mf = message_factory.MessageFactory()
        prototype = mf.GetPrototype(des)
        if (prototype):
            msg = prototype()
    return msg
    
def cs():
#    MessageBox = windll.user32.MessageBoxW
#    MessageBox(0,u"Great",u"Hello World", 0)
#    dll = CDLL("D:\Documents\Documents\Visual Studio 2010\Projects\ctest\Debug\ctest.dll")#加载cdecl的dll。另外加载stdcall的dll的方式是WinDLL("dllpath") 
#    dll = WinDLL("ctest.dll")
    dll = CDLL("C:\LMS\programme\C++\PROJECT\ctest\Debug\ctest.dll")
    for i in range(100000):
        o = outStruct() 
        o.opt = c_char_p('logi')
        o.arg = c_char_p('neww')
    #    dll.test(byref(o)) 
    #     
    #    print (o.kws[0].words) 
    #    print (o.kws[1].words) 
    #    print (o.len) 
        
    
        dll.bm(byref(o))
#        print o.res
        dll.freeo(byref(o))

def s():
    for i in range(100000):
        print '1'
    
if __name__ == '__main__':
    starttime = time.time()
    pys()
#    s()
#    cs()
    print time.time()-starttime
    
    

        
        
        
        
        
    