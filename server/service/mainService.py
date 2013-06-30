# -*- coding: utf-8 -*-
'''
Created on 2013-6-22

@author: GRENB
'''
from twisted.application import service
from twisted.python import log
from server.remod.basemod import basemod
import sys, os
from library.MyCmd import MyCmd


class mainService(service.Service):
    '''
    classdocs
    '''

    def __init__(self, reactor):
        self.cmdmod = basemod(self)
        self.reactor = reactor

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

            
            
        