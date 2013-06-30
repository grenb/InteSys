# -*- coding: utf-8 -*-
'''
Created on 2013-6-30

@author: GRENB
'''
import inspect
from twisted.python import log

class basemod(object):
    '''
    classdocs
    '''


    def __init__(self, service):
        self.service = service
    
    def runcmd(self,argv):
        cmd = inspect.stack()[1][3]
        exec('self.'+cmd+'(argv)')
    
    def cmd_test(self,argv):
        log.msg('test cmd') 
    
    def cmd_tt1(self,argv):
        pass
        
        