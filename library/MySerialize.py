# -*- coding: utf-8 -*-
'''
Created on 2013-8-4

@author: GRENB
'''
from google.protobuf import message
from google.protobuf import descriptor
from google.protobuf import descriptor_pool 
from google.protobuf import message_factory
from google.protobuf import descriptor_pb2

class MySerialize():
    '''
    classdocs
    '''


    def __init__(self,package):
        '''
        Constructor
        '''
        self.generated_pool(package)
        
    def generated_pool(self,package):
        self.dp = descriptor_pool.DescriptorPool()
        for name in dir(package):
            if name.find('pb2')!=-1:
                obj = getattr(package, name)
                obj_fd = descriptor_pb2.FileDescriptorProto.FromString(obj.DESCRIPTOR.serialized_pb)
                self.dp.Add(obj_fd)
        
    def createMessage(self,type_name):
        msg = None
        des = self.dp.FindMessageTypeByName(type_name)
        if des:
            mf = message_factory.MessageFactory()
            prototype = mf.GetPrototype(des)
            if prototype:
                msg = prototype()
        return msg
    
    def SerializeToString(self,msg):
        return msg.SerializeToString()
    
    def ParseFromString(self,type_name,data):
        msg = ms.createMessage(type_name)
        msg.ParseFromString(data)
        return msg
    
    def GetTypeName(self,msg):
        return msg.DESCRIPTOR.full_name
    
    def Serialize(self,msg):
        if msg:
            data = ''
            data += self.GetTypeName(msg)+'\0'
            data += self.SerializeToString(msg)
            return data
        else:
            return 0
    
    def UnSerialize(self,data):
        if data:
            datalist = data.split('\0')
            lenth = len(datalist[0])
            return self.ParseFromString(datalist[0], data[lenth+1:])
        else:
            return 0
        


if __name__ == '__main__':
    import Protocol  
    from Protocol import command_pb2
    ms = MySerialize(Protocol)
    run = command_pb2.command()
    run.opt = 'logi'
    run.arg = 'neww'
    res = ms.Serialize(run)
    print res
    com = ms.UnSerialize(res)
    print com.opt
    print com.arg
    
    