# -*- coding: utf-8 -*-
'''
Created on 2013-6-30

@author: GRENB
'''
from mainService import mainService
from twisted.python import log

class serverService(mainService):
    '''
    classdocs
    '''
    clients = {}

    def connectionMade(self,transport,name = 'server'):
        log.msg('connectionMade:%s'%str(transport.getPeer()))
#        address = transport.getPeer()
        self.clients[name] = transport
#        self.clients[str(address.host)+':'+str(address.port)] = transport

        
    def dataReceived(self,data,name = 'server'):
        log.msg('dataReceived',data)
        self.clients[name].write(data)
#        for k in self.clients.keys():
#            print k
#            self.clients[k].write(data)
    
    def connectionLost(self,reason,name = 'server'):
        log.msg('connectionLost',reason)
        self.clients.__delitem__(name)
#        for k in self.clients.keys():
#            try:
#                self.clients[k].getTcpKeepAlive()
#            except:
#                self.clients.__delitem__(k)
        
        
        