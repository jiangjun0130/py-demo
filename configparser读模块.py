__author__ = 'jiangjun'
__date__ = '2018/5/15 下午9:28'

import configparser

conf = configparser.ConfigParser()
conf.read("example.ini")

print(conf.defaults())
print(conf['bitbucket.org']['user'])
#print(conf.sections())
sec = conf.remove_section('bitbucket.org')
conf.write(open('example.ini', "w"))