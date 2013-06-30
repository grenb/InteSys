# -*- coding: utf-8 -*-
'''
Created on 2013-6-30

@author: GRENB
'''
from twisted.internet import threads
from twisted.python import log
#from server.service import mainService


class MyCmd(object):
    '''
    classdocs
    '''

    def __init__(self, service,aclass):
        self.service = service
        self.init_cmd(aclass)
        cmd = threads.deferToThread(raw_input)
        cmd.addCallback(self.docmd)
    
    def init_cmd(self,aclass):
        self.command = []
        for d in  aclass.__dict__:
            if d.find('cmd_')!=-1:
                self.command.append(d[4:])
        log.msg('init_cmd:'+str(self.command))
    
    def deal_cmd(self,cmd):
        oper = ''
        argv = []
        li = str(cmd).split(' ')
        oper = str(li[0])
        argv = li[1:]
        return oper,argv     
        
    def docmd(self,cmd):
        log.msg( 'cmd:' + cmd)        
        oper,argv = self.deal_cmd(cmd)
        if oper == 'reload':
            exec('self.service.cmd_'+oper+'(argv)')
#        print oper,argv
        elif oper in self.command:
#            self.command[oper](argv)
#            exec('self.service.cmdmod.cmd_'+oper+'(argv)')
            getattr(self.service.cmdmod,'cmd_'+oper)(argv)
        else:
            log.msg( 'nonsupport this commond')
            log.msg( 'commonds:'+str(self.command))
        cmd = threads.deferToThread(raw_input, "InteSys:")
        cmd.addCallback(self.docmd)
        

        
     

        