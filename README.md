 awesomewxyu-py3-webapp
---
来之廖雪峰的python编程实例，具体如下

https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432170876125c96f6cc10717484baea0c6da9bee2be4000

# 程序目录结构：

```
- awesome-python3-webapp/  <-- 根目录
    - backup/               <-- 备份目录
    - conf/                 <-- 配置文件
    - dist/                 <-- 打包目录
    - www/                  <-- Web目录，存放.py文件
        - static/            <-- 存放静态文件
        - templates/         <-- 存放模板文件
    - ios/                  <-- 存放iOS App工程
    - LICENSE               <-- 代码LICENSE
 ```


 # 代码结构分析：
 一个典型的XXX架构（python常见的xx架构有XXX、XXX），后端数据库是mysql，采用ORM框架进行封装，中间层是XXXX，前端采用XXX架构。

后端使用的关键技术包括IO异步处理，包括数据的异步处理（XXX库）、中间层通过f构建了XXX中间件框架，分装了XXXt功能，提供了一个比较完整的XXX框架，可以处理前段都处理

## 代码结构：
核心代码在其中的www目录下，如下：
```
apis.py
app.py
config_default.py
config_override.py
config.py
coroweb.py
handlers.py
models.py
orm.py
```

- 三个config文件（config.py,config_override.py,config_default.py）：

主要提供配置信息，主要包括数据库信息、session信息、debug信息，其中config.py提供了一个配置信息读取类，config_default.py/config_override.py提供具体的配置。

- apis.py:

提供json串的处理API，主要是分页数据的读取，另外还包括异常处理等API实现

- app.py

整个项目的启动文件，引入了jinja2、aiohttp等框架，启动前端；
另外提供了logger_factory、data_factory、response_factory等中间件，提供前端处理中需要用到的公用能力；

- coroweb.py

前端请求映射框架，提供了各种请求映射的装饰符，感觉类似flask框架的具体实现，提供把url和处理函数进行映射的装饰符

- handlers.py

后端逻辑处理模块，提供了针对页面请求的各种业务逻辑处理，调用orm.py封装的具体操作来执行数据库操作（这个在总体框架中属于哪一层？属于mvc模型的中control，负责业务逻辑的处理）

- modles.py

定义持久化类，数据库的表、数据，在这里定义为对应的类、属性，方便后续使用（这个modles，就是mvc中的model，代表了需要传递给前段的数据）。

- orm.py

数据库的操作封装实现，实现了一个类似iBatis的框架功能，把数据库操作转化为sql串。

- templates->test.html

视图模板，反馈给用户（MVC中的vieww部分，反馈给最终用户的视图）

## python MVC
通过MVC，我们在Python代码中处理M：Model和C：Controller，而V：View是通过模板处理的，这样，我们就成功地把Python代码和HTML代码最大限度地分离了。

使用模板的另一大好处是，模板改起来很方便，而且，改完保存后，刷新浏览器就能看到最新的效果，这对于调试HTML、CSS和JavaScript的前端工程师来说实在是太重要了。

关于Django的MTC框架说明：
https://www.cnblogs.com/holbrook/archive/2012/01/29/2357360.html
http://www.jb51.net/article/107884.htm

http://www.cnblogs.com/luotianshuai/p/5386494.html
https://www.cnblogs.com/heilongorz/articles/6476437.html

```
Django也是一个MVC框架。但是在Django中，控制器接受用户输入的部分由框架自行处理，所以 Django 里更关注的是模型（Model）、模板(Template)和视图（Views），称为 MTV模式：

    M 代表模型（Model），即数据存取层。 该层处理与数据相关的所有事务： 如何存取、如何验证有效性、包含哪些行为以及数据之间的关系等。

    T 代表模板(Template)，即表现层。 该层处理与表现相关的决定： 如何在页面或其他类型文档中进行显示。

    V 代表视图（View），即业务逻辑层。 该层包含存取模型及调取恰当模板的相关逻辑。 你可以把它看作模型与模板之间的桥梁。

需要注意的是，不能简单的把 Django 视图认为是MVC控制器，把 Django 模板认为MVC视图。
区别在于：
     Django 视图 不处理用户输入，而仅仅决定要展现哪些数据给用户；
     Django 模板 仅仅决定如何展现Django视图指定的数据。

或者说, Django将MVC中的视图进一步分解为 Django视图 和 Django模板两个部分，分别决定 “展现哪些数据” 和 “如何展现”，使得Django的模板可以根据需要随时替换，而不仅仅限制于内置的模板。

至于MVC控制器部分，由Django框架的URLconf来实现 。URLconf设计非常巧妙，其机制是使用正则表达式匹配URL，然后调用合适的Python函数。虽然一开始有些不习惯，但是你很快就会喜欢上它，因为URLconf对于URL的规则没有任何限制，你完全可以设计成任意的URL风格，不管是传统的，RESTful的，或者是另类的。
```
MVC与SSH
```
MVC是比较直观的架构模式，用户操作->View（负责接收用户的输入操作）->Controller（业务逻辑处理）->Model（数据持久化）->View（将结果反馈给View）。

MVC使用非常广泛，比如JavaEE中的SSH框架（Struts/Spring/Hibernate），Struts（View, STL）-Spring（Controller, Ioc、Spring MVC）-Hibernate（Model, ORM）以及ASP.NET中的ASP.NET MVC框架，xxx.cshtml-xxxcontroller-xxxmodel。（实际上后端开发过程中是v-c-m-c-v，v和m并没有关系，下图仅代表经典的mvc模型）
```