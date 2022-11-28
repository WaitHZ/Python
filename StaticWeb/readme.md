# Static Web Server



## What is this？

**A static web server written in Python.**

When you have prepared web page data but have no way to run it on your server, you can try the following module. You can write a script file to refer to this module, or you can run it directly through the command line.



## How to use it?

*The following uses are examples of the built-in examples.

0. Make sure your computer or server has a basic Python 3 environment configured.
1. Enter the following command in the project root directory:

```
python ./src/staticweb.py (port)
```

You can specify the port, if you don't, the default port is 8080.

2. Type the URL into your browser:http://localhost:8080/ or http://localhost:8080/index.html ,you will see this interface:

![](./img/index.jpg)

3. Enter any other resource path and you will get a 404 interface:

![](./img/404.jpg)



If you want to use this static web server to host your own web pages, you have to modify some necessary content in the module.

