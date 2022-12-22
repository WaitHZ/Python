# Python高级语法



## 一、闭包

函数执行完，函数内的变量就会被释放，但有时需要保存函数内的这个变量。

### 1.基本概念

**闭包的定义**:

> 在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数，我们把这个使用外部函数变量的内部函数称为闭包

**构成条件**：

- 在函数嵌套（函数内再定义函数）的前提下
- 内部函数使用了外部函数的变量（包括外部函数的参数）
- 外部函数返回了内部函数

```py
def func_out():
    num1 = 10

    def func_inner():
        result = num1 + 10
        print(result)

    return func_inner


if __name__ == '__main__':
    func = func_out()  # func就是函数闭包
    func()

```

*参数或返回值为函数时，称函数为高阶函数

也可以将两个固定的数值修改为参数：

```py
def func_out(num1):
    def func_inner(num2):
        result = num1 + num2
        print(result)

    return func_inner


if __name__ == '__main__':
    func = func_out(1)  # func就是函数闭包
    func(2)

```

闭包就是对外部函数变量进行保存，并在闭包中进行使用。需要注意的是，由于闭包引用了外部函数的变量，外部函数的变量没有及时释放，消耗内存，直到闭包释放后才会进行释放

### 2.闭包的使用

模拟信息交互，外部函数用来保存人名

```py
def name_config(name: str):

    def func_inner(msg: str):
        print(f'{name}: {msg}')

    return func_inner


if __name__ == '__main__':
    chat1 = name_config('xiao ming')
    chat2 = name_config('xiao_hong')

    chat1('吃了吗')
    chat2('吃过了')

```

### 3.修改闭包内使用的外部变量

如果直接使用赋值语句，相当于在内部函数新建了局部变量，如果希望对于外部变量进行修改，需要使用nonlocal关键字

```py
def name_config(name: str):

    def func_inner(msg: str):
        nonlocal name
        name = 'gai'

        print(f'{name}: {msg}')

    func_inner('aaa')
    print(name)

    return func_inner


if __name__ == '__main__':
    chat1 = name_config('xiao ming')

    chat1('吃了吗')
```



## 二、装饰器

对已有函数进行功能扩展

### 1.基本概念

> 就是给已有函数增加额外功能的函数，它本质是**闭包函数**

功能特点：

1. 不修改已有函数的代码
2. 不修改已有函数的调用方式
3. 给已有函数增加额外功能

```py
def decorator(func):  # 有且仅有一个参数是函数，就是装饰器
    def inner():
        print("已添加登陆验证")
        func()
    return inner


@decorator  # 装饰器的语法糖写法，简单的装饰函数
def comment():
    print("发表评论")


if __name__ == '__main__':
    comment()

```

执行原理：

等价于执行decorator中inner这个函数，并运用外部函数的参数comment，其与下方代码等价：

```py
def decorator(func):  # 有且仅有一个参数是函数，就是装饰器
    def inner():
        print("已添加登陆验证")
        func()
    return inner


def comment():
    print("发表评论")


if __name__ == '__main__':
    comment = decorator(comment)
    comment()
```

**装饰器执行的时机是当前模块加载完成后，装饰器就会对于函数进行装饰**。如果在装饰器中存在输出语句可以很明显的看到：

```py
def decorator(func):  # 有且仅有一个参数是函数，就是装饰器
    print("装饰器执行...")

    def inner():
        print("已添加登陆验证")
        func()
    
    return inner


@decorator
def comment():
    print("发表评论")

# 装饰器执行...
```

因此，如果再使用该模块中的comment函数，本质都是执行闭包中的inner函数

### 2.装饰器的使用

- 函数执行时间的统计
- 输出日志信息

```py
import time


def time_counter(func):
    def inner():
        start = time.time()
        s = func()
        end = time.time()
        print(f'函数执行了{end-start:.4f}s')
        return s  # 已经实现了偷梁换柱

    return inner


@time_counter
def calc():
    s = 0
    for i in range(1, 1000001):
        s += i
    return s


if __name__ == '__main__':
    print(calc())

```

### 3.通用装饰器的使用

函数可能存在参数，有可能有返回值

装饰带有参数和返回值的函数

```py
import time


def time_counter(func):
    def inner(num):
        print('正在努力完成完成计算...')
        start = time.time()
        s = func(num)
        end = time.time()
        print(f'函数执行了{end-start:.4f}s')
        return s  # 已经实现了偷梁换柱

    return inner


@time_counter
def calc(num):
    s = 0
    for i in range(1, num+1):
        s += i
    return s


if __name__ == '__main__':
    print(calc(10000000))

```

**待装饰函数的参数和返回值应该和内部函数相同**

从这里出发，我们可以得到通用的装饰器：

```py
def decotator(func):
    def inner(*args, **kwargs):
        # 装饰代码
        retVal = func(*args, **kwargs)  
        # *args是一般的元组拆包合法操作 **kwargs只在函数参数时支持字典拆包
        # 装饰代码
        return retVal  # func函数没有返回值，返回None，保持一致
        
```

对于任意的函数，我们都可以使用通用装饰器进行装饰

<hr>

直接对于字典进行迭代，访问的是字典的key值

<hr>

### 4.多个装饰器

**多个装饰器同时装饰一个函数，则先执行内部的装饰器，再执行外部的**

```py
def make_p(func):
    def inner():
        ret_val = '<p>' + func() + '</p>'
        return ret_val
    return inner


def make_div(func):
    def inner():
        ret_val = '<div>' + func() + '</div>'
        return ret_val
    return inner


@make_div
@make_p
def show():
    return "人生苦短，我学Python!"


if __name__ == '__main__':
    print(show())

```

输出为\<div>\<p>人生苦短，我学Python!\</p>\</div>，**由内到外装饰**

执行顺序类似于make_div(make_p(show()))，第一次装饰完，show是make_p的inner函数，func是show；第二次装饰完show是make_div中的inner函数，func则是make_p的inner函数

### 5.带有参数的装饰器

装饰器外再使用一个外部函数，则装饰器本身也称为闭包，其可以使用外层函数的参数

```py
def return_decorator(tag: int):  # 外层再套一层函数
    def decorator(func):
        def inner(a, b):
            if tag == 1:
                print('执行加法运算')
                ret_val = func(a, b)
            elif tag == 0:
                print('执行减法运算')
                ret_val = func(a, b)
            return ret_val
        return inner
    return decorator


@return_decorator(1)  # 理解应该是@(return_decorator(1))
def add(a, b):
    return a + b


@return_decorator(0)
def sub(a, b):
    return a - b


if __name__ == '__main__':
    print(add(2, 4))
    print(sub(1, 6))

```

### 6.类装饰器

> 使用类装饰已有函数

```py
class MyDecorator(object):
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        print("课讲完了")
        self.__func()  # 函数应该设为私有的


@MyDecorator
def show():
    print("可以下课了")


if __name__ == '__main__':
    show()
    print(dir(show))  # 内部含有__call__方法

```



## 三、property属性

> property属性就是把一个方法当作属性进行使用，可以用于简化代码

有两种定义方式：

- 装饰器方式
- 类属性方法

### 1.装饰器方式

```py
class Dog(object):
    def __init__(self):
        self.__age = 0

    @property   # 本质是一个类装饰器
    def age(self):
        print("获取属性")
        return self.__age

    @age.setter  # 与之前的名称必须相同，需与方法名保持一致
    def age(self, val):
        print("设置属性")
        self.__age = val


if __name__ == '__main__':
    dog = Dog()
    print(dog.age)  # 直接用调用属性的方式使用方法
    dog.age = 100  # 直接用修改属性的方式调用方法
    print(dog.age)

```

### 2.类属性方式

```py
class Dog(object):
    def __init__(self):
        self.__age = 0

    def get_age(self):
        return self.__age

    def set_age(self, val):
        self.__age = val

    age = property(get_age, set_age)


if __name__ == '__main__':
    dog = Dog()
    print(dog.age)  # 直接用调用属性的方式使用方法
    dog.age = 100  # 直接用修改属性的方式调用方法
    print(dog.age)

```



## 四、with语句和上下文管理器

### 1.with语句

在文件使用过程中，存在一个安全隐患

```py
f = open('1.txt', 'r')

f.write('aaa')

f.close()
```

文件会因报错终止没有被关闭，可以通过捕获异常来规避IOError，但代码较长

Python提供with语句，会（即使存在异常）自动关闭文件

```py
with open('1.txt', 'r') as file:
    file_data = file.read()
    print(file_data)
```

### 2.上下文管理器

> 一个类只要实现了\_\_enter\_\_()和\_\_exit\_\_()两个方法，通过该类创建的对象就称作上下文管理器

with语句的强大正是基于上下文管理器

```py
class File(object):
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode
    
    def __enter__(self):  # 上文方法，负责返回操作对象资源，比如文件对象、数据库连接对象
        self.file = open(self.file_name, self.file_mode)
        return self.file
        
    # 结合with语句使用，自动执行exit函数
    def __exit__(self, exc_type, exc_val, exc_tb):  # 下文方法，负责释放对象资源，如关闭文件
        self.file.close()
        

if __name__ == '__main__':
    with File('1.txt', 'r') as file:
        file.read()

```

with后都是上下文管理器对象，open函数创建的也是上下文管理器对象

with无论是否存在错误，都会执行exit方法

也可以借助装饰器实现上下文管理器

```py
from contextlib import contextmanager


@contextmanager
def my_open(path, mode):
    try:
        file = open(path, mode)
        yield file  # 返回文件 之前为上文方法 之后为下文方法
    except Exception as err:
        print(err)
    finally:
        print('over')
        file.close()


if __name__ == '__main__':
    with my_open('1.txt', 'rb') as f:
        f.read()
   
```

**普通函数不能和with结合使用，with只能和上下文管理器结合使用**。普通函数可以通过修饰器进行修饰



## 五、生成器

> 根据程序员指定的规则循环生成数据，当条件不成立时生成数据结束。数据不是一次性全部处理，而是使用一个生成一个，可以节约大量内存

有两种创建方式：

- 生成器推导式
- yield关键字

### 1.生成器推导式

适用于简单的情形

```py
if __name__ == '__main__':
    my_generator = (i * 2 for i in range(5))  # 小括号
    print(my_generator)

    # value = next(my_generator)
    # print(value)  # 生成器取值只能向后，且不能越界
    
    for i in my_generator:
        print(i)  # for语句迭代访问就是my_generator每一个值

```

需要注意的是：

```py
if __name__ == '__main__':
    my_generator = (i * 2 for i in range(5))  # 小括号
    print(my_generator)

    value = next(my_generator)
    print(value)  # 0
    
    for i in my_generator:
        print(i)  # 2 4 6 8

```

### 2.函数方式

适用于复杂情形

```py
def my_generator():
    for i in range(5):
        print('a')
        # 遇到yield就在这里暂停，并将i的值返回，再次调用生成器时，继续向下执行
        yield i  # 在函数中出现yield，函数就是生成器
        print('b')  # 再次调用才会执行


if __name__ == '__main__':
    print(my_generator())  # <generator object my_generator at 0x000002214C664350>
    # 不再是函数

```



生成器将所有数据生成结束后，再次启动会抛出**StopIteration**异常

### 3.使用场景

```py
def fib_generator(num):
    a = 0
    b = 1
    current_index = 0

    while current_index < num:
        yield a
        a, b = b, a + b
        current_index += 1


if __name__ == '__main__':
    for i in fib_generator(5000):
        print(i)

```

相较于迭代算法的好处是，不占用空间；相较于递归算法的好处是没有深度限制



## 六、拷贝

深浅拷贝都是针对可变数据而言，由于Python的存储特性，不可变数据类型只是复制引用

### 1.浅拷贝

> 只对可变类型的第一层对象进行拷贝，对拷贝的对象开辟新的内存空间进行存储，不会拷贝对象内部的子对象

```py
import copy

if __name__ == '__main__':
    # 不可变类型：数字、字符串、元组 浅拷贝就是拷贝引用
    a = 'aaa'
    b = copy.copy(a)

    print(id(a), id(b))  # 1602270444592 1602270444592  相同的引用

    # 可变类型
    c = [1, 2, 3]
    d = copy.copy(c)

    print(id(c), id(d))  # 2170123037248 2170415076288

    e = [1, 2, [1, 2, 3]]
    f = copy.copy(e)

    print(id(e), id(f))  # 2211754513344 2211754512832
    print(id(e[2]), id(f[2]))  # 2211754513088 2211754513088
    # 更深层也只进行了引用的拷贝

```

### 2.深拷贝

> 深拷贝只要发现对象有可变类型就会对该对象到最后一个可变类型的每一层对象进行拷贝，对每一层拷贝的对象都会开辟新的内存空间进行存储

对于不可变数据类型，仍只是拷贝引用

```py
import copy

if __name__ == '__main__':
    # 不可变类型：数字、字符串、元组 浅拷贝就是拷贝引用
    a = 'aaa'
    b = copy.deepcopy(a)

    print(id(a), id(b))  # 1602270444592 1602270444592  相同的引用

    # 可变类型
    c = [1, 2, 3]
    d = copy.deepcopy(c)

    print(id(c), id(d))  # 2170123037248 2170415076288

    e = [1, 2, [1, 2, 3]]
    f = copy.deepcopy(e)

    print(id(e), id(f))  # 2211754513344 2211754512832
    print(id(e[2]), id(f[2]))  # 1843770082944 1843770082432
    # 更深层也进行了拷贝

```

**元组是容器，其内部若有可变数据类型也会做拷贝**

**可变数据类型的容器，其内部的不可变类型仍是原来的引用**

```py
import copy

if __name__ == '__main__':
    a = (1, 2, 3, [1, 2])
    b = copy.deepcopy(a)

    print(id(a), id(b))  # 2093755220032 2091888091168

    c = [1, 'aaa', (1, [1, 2])]
    d = copy.deepcopy(c)

    print(id(c[1]), id(d[1]))  # 1768037661872 1768037661872
    print(id(c[2]), id(d[2]))  # 2236254939008 2236254940096
    print(id(c[2][1]), id(d[2][1]))  # 2661548325760 2661548324928

```

逐渐深入，见到不可变数据类型或存有可变类型的元组就进行深拷贝



**列表的copy方法是浅拷贝**

```py
if __name__ == '__main__':
    a = [1, 2, [1, 2]]
    b = a.copy()

    print(id(a), id(b))  # 2341883859328 2341884104064
    print(id(a[2]), id(b[2]))  # 2341591624256 2341591624256

```



## 七、正则表达式

> 正则表达式就是记录文本规则的代码

在实际过程中，经常会有查找符合某些复杂规则**字符串**的需要，如邮箱、图片地址、手机号码等

正则表达式的特点：

- 语法复杂，可读性差
- 通用性强，能够用于多种编程语言

### 1.re模块的使用

```py
import re


if __name__ == '__main__':
    result = re.match('itcast', 'itcast.cn')  # 第一个参数正则，第二个参数待匹配字符串

    print(result.group())  # 获取到才可以使用
```

### 2.匹配单个字符

| 代码 | 功能                                                  |
| :--: | :---------------------------------------------------- |
|  .   | 匹配任意一个字符（除了\n）                            |
|  []  | 匹配[]中列举的字符，也支持[0-9]，[a-zA-Z]等连续的写法 |
|  \d  | 匹配数字，即0-9                                       |
|  \D  | 匹配非数字，即不是数字                                |
|  \s  | 匹配空白，即空格、tab                                 |
|  \S  | 匹配非空白                                            |
|  \w  | 匹配非特殊字符，即英文字母、数字、_、汉字             |
|  \W  | 匹配特殊字符，即非英文字母、非数字、非汉字、非_       |

```py
import re


if __name__ == '__main__':
    result = re.match('it\sast', 'it\tast.cn')

    if result:
        print(result.group())
    else:
        print('No matched!')
```

### 3.匹配多个字符

|  代码  | 功能                                       |
| :----: | ------------------------------------------ |
|   *    | 匹配前一个字符，0次到无限次，可有可无      |
|   +    | 匹配前一个字符，至少出现一次               |
|   ？   | 匹配前一个字符，出现1次或0次               |
|  {m}   | 匹配前一个字符出现m次                      |
| {m, n} | 匹配前一个字符出现m到n次，{m, }至少出现m次 |

**前一个字符均不算入正则表达式，而是以组合形式出现**

```py
import re


if __name__ == '__main__':
    result = re.match('https?', 'https')  # 结合任意字符使用多个字符匹配

    if result:
        print(result.group())
    else:
        print('No matched!')
```

可以结合任意字符使用

```py
import re


if __name__ == '__main__':
    result = re.match('i.*t', 'itcast.cn')  # 结合任意字符使用多个字符匹配
    # 任意字符出现0次或多次

    if result:
        print(result.group())
    else:
        print('No matched!')

```

### 4.匹配开头和结尾

| 代码 | 功能           |
| :--: | -------------- |
|  ^   | 匹配字符串开头 |
|  $   | 匹配字符串结尾 |

```py
import re


if __name__ == '__main__':
    result = re.match('^\d.*', '0https')  # 匹配数字开头
    result = re.match('.*\d$', '0https1')  # 匹配数字结尾
    result = re.match('^\d.*\d$', '0https1')  # 匹配以数字开头且以数字结尾

    if result:
        print(result.group())
    else:
        print('No matched!')
```

### 5.除了指定字符以外都匹配

[^指定字符] 表示除了指定字符都匹配

```
[^aeiou]
```

除了aeiou外的单个字符都匹配

```py
import re


if __name__ == '__main__':
    result = re.match('^\d.*[^47]$', '0https4')

    if result:
        print(result.group())
    else:
        print('No matched!')
```

### 6.匹配分组相关的正则表达式

|     代码     | 功能                             |
| :----------: | -------------------------------- |
|      \|      | 匹配左右任意一个表达式           |
|     (ab)     | 将括号中的字符作为一个分组       |
|     \num     | 引用分组num匹配到的字符串        |
| (?P\<name\>) | 分组起别名                       |
|  (?P=name)   | 引用别名为name分组匹配到的字符串 |

```py
import re


if __name__ == '__main__':
    fruits = ['apple', 'orange', 'banana', 'pear', 'peach']

    for i in fruits:
        match_obj = re.match('apple|pear', i)
        
        if match_obj:
            print(match_obj.group())

```

```py
re.match('[a-zA-Z0-9_]{4, 20}@(qq|163|126)\.com')
```

括号用于将字符串进行分组，\\.对正则表达式进行转义，只能匹配.字符

出现一个小括号就表示一个分组，序号从1开始，若出现多个小括号，顺序是从左到右

group函数的参数若为0，则获取整个匹配数据，若为正整数就是对应的分组匹配数据

```py
import re


if __name__ == '__main__':

    match_obj = re.match('qq:([1-9]\d{4,11})', 'qq:3014587')  # 4 11之间没有空格
    print(match_obj.group())  # qq:3014587
    print(match_obj.group(1))  # 3014587

```

\num的使用

```py
import re


if __name__ == '__main__':

    match_obj = re.match('<([a-zA-Z1-6]+)>.*</\\1>', '<html>aa</html>')

    if match_obj:
        print(match_obj.group())

```

\\\\1是需要进行反转义

为分组起别名：

```py
import re


if __name__ == '__main__':

    match_obj = re.match('<(?P<name1>[a-zA-Z1-6]+)>.*</(?P=name1)>', '<html>aa</html>')

    if match_obj:
        print(match_obj.group())
```

