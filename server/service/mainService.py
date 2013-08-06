# -*- coding: utf-8 -*-
'''
Created on 2013-6-22

@author: GRENB
'''
from twisted.application import service
from twisted.python import log
from server.remod.basemod import basemod
import Protocol
import sys, os, struct, zlib
from library.MyCmd import MyCmd
from library.MySerialize import MySerialize


class mainService(service.Service):
    '''
    classdocs
    '''
    buff = {}
    str_end = '\0'
    def __init__(self, reactor):
        self.cmdmod = basemod(self)
        self.reactor = reactor
        self.myserialize = MySerialize(Protocol)

    def startService(self):
        service.Service.startService(self)
        log.msg('startService')
        self.cmd = MyCmd(self,basemod)

    
    
    
    def cmd_reload(self,argv):
        mod_names = ['server.remod.basemod']   
        for  mod_name  in  mod_names:   
            try :   
                module =  sys.modules[ mod_name ]  
            except Exception,ex:
                log.msg( ex )
                continue   
            mtime =  os.path.getmtime( module.__file__ )   
            try :   
                if  mtime > module.loadtime:   
                    log.msg( 'reload:%s'%mod_name)
                    reload ( module )   
            except :   
                log.msg( 'exreload:%s'%mod_name)
                reload ( module )   
            module.loadtime = mtime   
            self.cmdmod = getattr(module,'basemod')(self)            
            self.cmd.init_cmd(getattr(module,'basemod'))

    def senddata(self,transport,packagedata):
        transport.write(packagedata)
        
    def deal_data(self,data,name = 'server'):
        self.buff.setdefault(name,d='')
        self.buff[name] += data

        msglist = []
        if len(self.buff) < 0:
            return 0
        buff_len = len(self.buff)
        while buff_len > 10:
            #解析包头
            package_len = struct.unpack('>i', data[0:4])

            #如果buff不是完整的包则不处理该包
            if buff_len < package_len:
                return msglist
            msg = self.UnSerialize(self.buff[name][0:package_len])
            if msg:
                msglist.append(msg)
            self.buff[name] = self.buff[name][package_len:]
            buff_len = len(self.buff)
        return msglist

    def exec_data(self,msglist):
        for msg in msglist:
            msgname = self.myserialize.GetName(msg)
            getattr(self,'msg_'+msgname)(msg)
            
    def UnSerialize(self,package):
        data_len = struct.unpack('>i', package[0:4])
        type_name_len = struct.unpack('>h', package[4:6])
        checknum = struct.unpack('>i', package[6:10])
        packagebody = package[10:]
        if checknum==zlib.adler32(packagebody):
            msg = self.myserialize.UnSerialize(packagebody)
            if msg:
                return  msg
            else:
                return 0
        else:
            return -1

    def Serialize(self,msg):
        if msg:
            type_name = self.myserialize.GetTypeName(msg)
            type_name_len = len(type_name)
            packagebody = self.Serialize(msg)
            checknum = zlib.adler32(packagebody)
            body = ''
            body += struct.pack('>i',len(packagebody)+10)
            body += struct.pack('>h',type_name_len)
            body += struct.pack('>i',checknum)
            body += packagebody
            return body

    def msg_command(self,msg):
        pass