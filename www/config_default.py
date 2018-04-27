""" 
关键知识点：
1 web框架/orm框架的配置

有了Web框架和ORM框架，我们就可以开始装配App了。
通常，一个Web App在运行时都需要读取配置文件，比如数据库的用户名、口令等，在不同的环境中运行时，
Web App可以通过读取不同的配置文件来获得正确的配置。
由于Python本身语法简单，完全可以直接用Python源代码来实现配置，而不需要再解析一个单独的
.properties或者.yaml等配置文件。 

如果要部署到服务器时，通常需要修改数据库的host等信息，直接修改config_default.py不是一个好办法，
更好的方法是编写一个config_override.py，用来覆盖某些默认设置：

应用程序读取配置文件需要优先从config_override.py读取。为了简化读取配置文件，
可以把所有配置读取到统一的config.py中：
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Michael Liao'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'www',
        'password': 'www',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}