# -*- coding: utf-8 -*-
'''
Created on 2013-6-22

@author: GRENB
'''
from zope.interface import implements
from twisted.python import usage
from twisted.plugin import IPlugin
from twisted.application.service import IServiceMaker


from twisted.application import internet, service
from twisted.internet.protocol import ServerFactory, Protocol
from twisted.python import log
from twisted.python.log import ILogObserver, FileLogObserver, PythonLoggingObserver
from twisted.python.logfile import DailyLogFile

from server.factories.mainFactory import MyServerFactory, MyClientFactory
from server.protocols.mainProtocol import mainProtocol
from server.service.mainService import mainService

#import logging
#from twisted.internet import iocpreactor
#iocpreactor.reactor.install()
#from twisted.internet import reactor
#import sys
#print sys.modules['twisted.internet.reactor']


class Options(usage.Options):
    optParameters = [ ['port', 'p', 10000, 'The port number to listen on.'],
                      ['poem', None, 'poetry/ecstasy.txt', 'The file containing the poem.'],
                      ['type', 't', 'server', 'The type of the system to run.'],
                      ['iface', 'ip', 'localhost', 'The interface to listen on.'],]
class MyServiceMaker(object):
    implements(IServiceMaker, IPlugin)
    tapname = "InteSys"
    description = "A system for connect"
    options = Options
    def makeService(self, options):

        top_service = service.MultiService()

        poetry_service = mainService(options['poem'])
        poetry_service.setServiceParent(top_service)
        if options['type']=='server':
            factory = MyServerFactory(poetry_service)
            tcp_service = internet.TCPServer(int(options['port']), factory, interface=options['iface'])
        else:
            factory = MyClientFactory(poetry_service)
            tcp_service = internet.TCPClient(options['iface'], int(options['port']), factory)
        tcp_service.setServiceParent(top_service)

        return top_service
# Now construct an object which *provides* the relevant interfaces
# The name of this variable is irrelevant, as long as there is *some*
# name bound to a provider of IPlugin and IServiceMaker.
serviceMaker = MyServiceMaker()
#from twisted.plugin import IPlugin, getPlugins
#list(getPlugins(IPlugin))
#port = 10000
#iface = 'localhost'
#poetry_file = 'poetry/ecstasy.txt'
#
## this will hold the services that combine to form the poetry server
#top_service = service.MultiService()
#
## the poetry service holds the poem. it will load the poem when it is
## started
#poetry_service = mainService(poetry_file)
#poetry_service.setServiceParent(top_service)
#
## the tcp service connects the factory to a listening socket. it will
## create the listening socket when it is started
##factory = MyServerFactory(poetry_service)
##tcp_service = internet.TCPServer(port, factory, interface=iface)
#factory = MyClientFactory(poetry_service)
#tcp_service = internet.TCPClient(iface,port, factory)
#
#tcp_service.setServiceParent(top_service)
#
## this variable has to be named 'application'
#application = service.Application("InteSys")
#
#
##logger=logging.getLogger('InteSys')
##shandler = logging.StreamHandler()
##logger.addHandler(shandler)
##application.setComponent(ILogObserver, PythonLoggingObserver('InteSys').emit)
##
##logfile = DailyLogFile("my.log", "tmp")
##application.setComponent(ILogObserver, FileLogObserver(logfile).emit)
#
## this hooks the collection we made to the application
#top_service.setServiceParent(application)
