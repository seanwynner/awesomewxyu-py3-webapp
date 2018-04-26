import logging
logging.basicConfig(level=logging.INFO)

'''
asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。
asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引\
用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
'''
import asyncio
import os
import json
import time

from datetime import datetime

'''
aiohttp则是基于asyncio实现的HTTP框架。
asyncio可以实现单线程并发IO操作。如果仅用在客户端，发挥的威力不大。如果把asynci\
o用在服务器端，例如Web服务器，由于HTTP连接就是IO操作，因此可以用单线程+coroutine实现多用户的高并发支持。
asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架。
'''
from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', headers={'content-type': 'text/html'})


'''
@asyncio.coroutine把init（loop）标记为coroutine类型，目的是采用异步并发处理的方式处理请求
'''


@asyncio.coroutine
def init(loop):
    '''
    app使用aiohttp的web异步框架
    '''
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


'''
get_event_loop,进行异步IO处理
'''
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
