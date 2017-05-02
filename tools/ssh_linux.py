#!/usr/bin/python
#-*-coding:utf-8-*-  
'''
Created on 2017年3月27日

@author: sunying
作用：用于ssh连接linux,执行shell命令
'''
#!/usr/bin/env python
import paramiko
class SSH():
    def __init__(self,hostname,username,password):
        paramiko.util.log_to_file('paramiko.log')
        s=paramiko.SSHClient()
        s.load_system_host_keys()
        s.connect(hostname=hostname,username=username,password=password)
    def exec_shell(self):
        #这里输了了多个命令
        stdin,stdout,stderr=self.s.exec_command('ifconfig;free;df')
        print stdout.read()
        self.s.close()
if __name__=='__main__':
    ssh =  SSH("192.168.1.1","root","123456")
    ssh.exec_shell()