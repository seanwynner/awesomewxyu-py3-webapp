# 前端构建代码：

对于复杂的HTML前端页面来说，我们需要一套基础的CSS框架来完成页面布局和基本样式。另外，jQuery作为操作DOM的JavaScript库也必不可少。

从零开始写CSS不如直接从一个已有的功能完善的CSS框架开始。有很多CSS框架可供选择。我们这次选择uikit这个强大的CSS框架。它具备完善的响应式布局，漂亮的UI，以及丰富的HTML组件，让我们能轻松设计出美观而简洁的页面。

可以从uikit首页下载打包的资源文件。

所有的静态资源文件我们统一放到www/static目录下，并按照类别归类：

    static/
    |   +- css/
    |  +- addons/
    |  |  +- uikit.addons.min.css
    |  |  +- uikit.almost-flat.addons.min.css
    |  |  +- uikit.gradient.addons.min.css
    |  +- awesome.css
    |  +- uikit.almost-flat.addons.min.css
    |  +- uikit.gradient.addons.min.css
    |  +- uikit.min.css
    +- fonts/
    |     +- fontawesome-webfont.eot
    |  +- fontawesome-webfont.ttf
    |  +- fontawesome-webfont.woff
    |  +- FontAwesome.otf
    +- js/
    +- awesome.js
    +- html5.js
    +- jquery.min.js
    +- uikit.min.js


*涉及到前端代码，本次不做详细分析*