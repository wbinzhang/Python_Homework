# 面向对象中类的三大特性：继承、多态、封装（私有化）

面向对象的设计思想是从自然界中来的。类（Class）是一种抽象概念，例如我们定义一个【学生】的类，是指学生这个概念，而实例（Instance）则是指一个个具体的学生，比如，小明和李华是两个具体的Student。

- **类和实例**

类(Class)和实例(Instance)是面向对象最重要的概念。

  - 类是指抽象出的模板。
  - 实例是根据类创建出来的具体的“对象”，每个对象都拥有从类中继承的相同的方法，但各自的数据可能不同。

在python中定义一个类:
```python
class Student:
    pass
```
关键字class后面跟着类名，类名通常是大写字母开头的单词。

定义好了类，就可以根据Student类创建实例：
```python
class Student(object):
     pass

bart = Student()   # bart是Student()的实例
```

python是面向对象的语言，支持面向对象的编程的三大特性：继承、封装、多态。

- **面向对象编程的基本流程：**

>1. 导入需要的外部库；
>2. 设计需要的全局变量；
>3. 设计需要的类；
>4. 为每个类提供完整的一组操作；
>5. 明确地使用继承来表现不同类之间的共同点；
>6. 根据需要，决定是否写一个main函数作为程序入口。

## 一、继承

面向对象的编程带来的主要好处之一是代码的重用，实现这种重用方法一种方法是通过继承机制。

- **类成员的继承和重写：**
  - 1.成员继承：子类继承了父类除构造方法之外的所有成员。
  - 2.方法重写：子类可以重新定义父类中的方法，这样就会覆盖父类中的方法，也称为重写。
  
#### 1.1 成员继承

如果一个新类继承自一个设计好的类，就直接具备了已有类的特征，就大大降低了工作难度。已有的类，被称为"**父类或基类**"，新的类，被称为“**子类或派生类**”。

object类是所有类的父类，所有类都有object类的属性和方法。object类里面定义了一些所有类共有的默认实现，比如 **\_\_init\_\_( )**，**\_\_new\_\_( )**。如果在类定义中没有指定父类，则默认父类是**object**类。

> Python支持多重继承，一个子类可以继承多个父类，这样就具备了多个父类的特点，但是由于这样会把“类的整体层次”搞得很复杂，尽量避免使用。

继承的语法格式如下：
```python
class  子类类名（父类1,父类2,…）:
    类体
```

> - 通过类的方法mro( )或者类的属性_mro_可以输出这个类的继承层次结构。
> - 通过类的方法dir( )查看对象属性。

定义子类时，必须在其构造函数中调用父类的构造函数(此处只是逻辑上的必须，语法上没有严格要求，但是一般要调)，调用格式如下：

```python
父类名.__init__(self,参数列表)
```

- **继承的基本使用**
```
'''定义一个Person类'''
class Person:
    def __init__(self, name, age):    #属性在构造器中
        self.name = name
        self.__age = age    #私有属性(子类可以调用，但是不能用，即子类继承了父类所有的属性方法，但是父类私有的属性方法子类不能用)
    def say_age(self):
        print(self.__age)
class Student(Person):
    def __init__(self, name, age, score):
        Person.__init__(self, name, age)    #必须显式的调用父类初始化方法，不然解释器不会去调用
        self.score = score
print(Student.mro())    #查看类的继承层次结构
s=Student("张无忌","18","100")    # 实例Student
s.say_age()
print(s.name)
# print(s.age)  父类的私有属性，子类不能用
print(dir(s))
'''
Python不允许实例化的类访问私有数据，但可以使用
object._className__attrName（对象名._类名__私有属性名）
访问属性
'''
print(s._Person__age)
```
> - 如果在子类中需要父类的构造方法就需要显式的调用父类的构造方法，或者重写父类的构造方法。
> - 如果子类不重写 **__init__**，实例化子类时，会自动调用父类定义的 **__init__**。
> - 如果重写了 **__init__**，要继承父类的构造方法，可以使用**super**关键字。

**super( )获得父类定义**

super( )函数是用于调用父类的一个方法，被用来解决多重继承问题。在使用单继承的时候，直接用类名调用父类方法是没有问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用等各种问题。

在子类中，如果想要获得父类的方法，我们可以通过super( )来做，super( )代表父类的**定义**，而不是**父类对象**。
```python
'''定义一个类A'''
class A:
     def add(self, x):
         y = x+1
         print(y)
'''定义类B，继承A'''
class B(A):
    def add(self, x):
        super().add(x)
b = B()    # 实例化B
b.add(6)  

# 7
```

#### 1.2 方法重写

在子类中出现和父类同名的函数，则认为该函数是对父类中函数的重写。

- **方法重写**

```python
'''定义一个Person类'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def say_age(self):
        print("我的年龄是",self.__age)
    def say_introduce(self):
        print(f"我的名字是{self.name}")
'''定义一个Student类，继承Person'''
class Student(Person):
    def __init__(self,name,age,score):
        Person.__init__(self,name,age)
        self.score=score
    def say_introduce(self):
        '''重写父类的方法'''
        print(f"报告老师，我的名字是{self.name}")

s=Student("张无忌",18,100)
s.say_age()
s.say_introduce()

'''打印结果'''
我的年龄是 18
报告老师，我的名字是张无忌
```

- **重写\_\_str\_\_方法：**

\_\_str\_\_方法用于返回一个对于“对象的描述”。如果一个类中定义了str()方法，那么在打印对象时，默认输出该方法的返回值。

```
class Person():
    def __init__(self,name):
        self.name=name

person=Person("张三丰")
print(person)

'''打印结果如下：  object类中__str__()的默认实现，打印类的信息'''
# <__main__.Person object at 0x00000221865FB1C0>

'''重写__str__()'''
class Person():
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "名字是:{}".format(self.name)
person=Person("张三丰")
print(person)

'''打印结果如下：'''
# 名字是:张三丰
```

## 二、多态

多态是指“多种状态”，在面向对象语言中，接口的多种不同的实现方式即为多态。简单的说，不同类的对象，接受到同一条指令，可以做出不同的反应。

- 1.多态是方法的多态，属性没有多态
- 2.多态的存在有两个必要条件：继承、方法重写

一个子类继承了一个父类，但是它又改写了父类的方法，这样在调用这个方法时，就会因为实例对象的不同而调用的方法不同，也就是说看这个实例对象实例化时是用父类实例化的，还是子类实例化的，是父类实例化的，结果就是父类的方法，是子类实例化的，结果就是子类的方法。

```python
'''定义一个学生类'''
class Student:
    def study(self):
        print("上课")
        
'''定义一个中国学生类'''      
class Chinese_Student(Student):
    def study(self):
        print("中国的学生用汉语上课")

'''定义一个英国学生类'''  
class English_Student(Student):
    def study(self):
        print("英国的学生用英语上课")

'''定义一个日本学生类'''  
class Jupan_Student(Student):
    def study(self):
        print("日本的学生用日语上课")

def studentStudy(m):
    if isinstance(m,Student):
        m.study()
    else:
        print("不能上课")

'''子类Chinese_Student实例化'''
studentStudy(Chinese_Student())
# 中国的学生用汉语上课

'''子类English_Student实例化'''
studentStudy(English_Student())
# 英国的学生用英语上课

'''Person这个实例化对象,父类实例化'''
Person=Student()
studentStudy(Person)
# 上课
```

## 三、封装

“封装”就是将抽象得到的数据和行为（或功能）相结合，形成一个有机的整体（即类），在类里面数据属性和行为用函数的形式封装起来，访问时直接调用，不需要知道类里面具体的实现方法。

封装的目的是增强安全性和简化编程，使用者不必了解具体的实现细节，而只是要通过外部接口，一特定的访问权限来使用类的成员。

封装，离不开“私有化”，Python 中私有化的方法就是在准备私有化的属性（包括方法、数据）名字前面加**双下划线**，这样这个变量只有内部可以访问，外部是不能访问的。
```python
class People:
    def __init__(self, name, age):
        self.name = name
        self.__age = age    # __age就是一个私有变量
people = People('小明', 18)
print(people.name)    # name并不是私有化的，可以访问name
print(people.age)    # age是私有化的不能访问
```

![](https://imgkr2.cn-bj.ufileos.com/a0376657-d163-490b-a46b-55fdee487b16.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=zANEUaDQdq3IYG0eTRa%252FSiqURIA%253D&Expires=1605504770)

此外，如果需要访问类中的私有化属性，则可以通过object._className__attrName（对象名._类名__私有属性名）或者@property装饰器或者编写get、set函数实现。

- 通过object._className__attrName输出私有化属性
```python
class People:
    def __init__(self, name, age):
        self.name = name
        self.__age = age    # __age就是一个私有变量
people = People('小明', 18)

'''可以通过object._className__attrName的方式访问'''
print(people._People__age)
# 18
```
- 通过property输出私有化属性。
```python
class People:
    def __init__(self, name, age):
        self.name = name
        self.__age = age    # __age就是一个私有变量
      
    @property
    def age(self):
        return self.__age
    
people = People('小明', 18)
print(people.age)
# 18
```

