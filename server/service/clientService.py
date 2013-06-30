# -*- coding: utf-8 -*-
'''
Created on 2013-6-30

@author: GRENB
'''
from mainService import mainService
from twisted.python import log
from twisted.internet import defer
import time


class clientService(mainService):
    '''
    classdocs
    '''
    server = []

    def connectionMade(self,transport,name = 'server'):
        log.msg('connectionMade:%s'%str(transport.getPeer()))
        self.server = transport
        transport.write('hello')
        
    def dataReceived(self,data,name = 'server'):
        log.msg('dataReceived',data)
#        self.server.write(data)
        self.reactor.callLater(10, self.se, data)
        self.reactor.callLater(2, self.se, data)
    
    def connectionLost(self,reason,name = 'server'):
        log.msg('connectionLost',reason)
        
    def sle(self,s):
        print s
        time.sleep(s)
        return str(s)
    
    def se(self,msg):
        print 'w'
        self.server.write(msg)
        
        