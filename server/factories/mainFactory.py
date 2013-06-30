# -*- coding: utf-8 -*-
'''
Created on 2013-6-22

@author: GRENB
'''

from twisted.internet.protocol import Factory,ClientFactory
from twisted.python import log
from server.protocols.mainProtocol import mainProtocol

class MyServerFactory(Factory):
    '''
    classdocs
    '''


    protocol = mainProtocol

    def __init__(self, service):
        self.service = service
        
    def startFactory(self):
        log.msg('start MyServerFactory')
        
    def stopFactory(self):
        log.msg('stop MyServerFactory')
        
class MyClientFactory(ClientFactory):
    protocol = mainProtocol
    
    def __init__(self, service):
        self.service = service
    
    def startFactory(self):
        log.msg('start MyClientFactory')
    
    def stopFactory(self):
        log.msg('stop MyClientFactory')
        
    def startedConneting(self, connector):
        log.msg( 'startedConneting')

    def clientConnectionLost(self, connector, reason):
        log.msg( 'clientConnectionLost:%s'% reason)
        #reactor.connectTCP('192.168.16.231',4506, MyClientFactory())
    def clientConnectionFailed(self, connector, reason):
        log.msg( 'clientConnectionFailed:%s'% reason)
        #reactor.connectTCP('192.168.16.231',4506, MyClientFactory())