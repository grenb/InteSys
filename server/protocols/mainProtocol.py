# -*- coding: utf-8 -*-
'''
Created on 2013-6-22

@author: GRENB
'''

from twisted.internet.protocol import  Protocol
from twisted.python import log

class mainProtocol(Protocol):
    '''
    classdocs
    '''
    name = ''

    def connectionMade(self):
        address = self.transport.getPeer()
        self.name = str(address.host)+':'+str(address.port)
        self.factory.service.connectionMade(self.transport,self.name)
        
    def dataReceived(self, data):        
        self.factory.service.dataReceived(data,self.name)

    def connectionLost(self,reason):
        self.factory.service.connectionLost(reason,self.name)
