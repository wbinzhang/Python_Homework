# Python内置对象类型“列表（list）”的综述

列表是一种有序的集合，其中的元素可以随时添加和删除，是 Python 中最基本的数据结构之一。

## 一、列表的定义
列表（list）使用中括号[ ]定义，里面元素可以是任意类型，包括列表本身，也可以是字典、元组等。

```python
list1 = ['ABC', 'student', 2020]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
list4 = [2020, 'A', (1,2,3), list1, {'name':'xiaoming'}]
print(list1, '\n', list2, '\n', list3, '\n', list4)
```

![列表的定义](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-28/1603896624778-image.png)

## 二、访问列表

列表中的每个元素都被分配一个数字索引，从**0**开始。第一个索引是0，第二个索引是 1，之后依此类推。

```python
list1 = ['ABC', 'student', 2020]
# 获取列表第一个元素‘ABC’
print('列表的第一个元素为：', list1[0])
# 获取列表第二个元素‘student’
print('列表的第二个元素为：', list1[1])
```

![访问列表](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-29/1603935516362-image.png)

## 三、修改和增加列表的值
- **修改：** 对列表数据项的修改可以直接通过索引号进行修改
- **增加：** 对列表数据项的增加可以通过append( )和insert( )方法进行增加。
>insert( index, vaule)在列表的指定位置插入值，它接受两个参数，第一个参数为索引号，第二个参数是待添加的新的元素。

```python
# 修改列表
list1 = [1, 2, 3, 4, 5]
print('list1原始列表为：\n', list1)
# 修改列表的第二个值
list1[1] = 6
print('list1修改后的列表为：\n', list1)
```

![列表的修改](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-28/1603897303811-image.png)

```python
# 增加列表
list1 = [1, 2, 3, 4, 5]
print('list1原始列表为：\n', list1)
# 在列表尾部增加一个元素
list1.append(9)
print('list1增加后的列表为：\n', list1)
```

![列表的增加](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-28/1603897752904-image.png)

```python
# 列表插入元素
list1 = [1, 2, 3, 4, 5]
print('list1原始列表为：\n', list1)
# 在列表第一个位置插入一个元素
list1.insert(0,7)
print('list1增加后的列表为：\n', list1)
```

![列表插入元素](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-29/1603901158827-image.png)

## 四、列表删除元素
列表删除元素的方法有del、pop( )、remove( )，其中，最常用到的是pop()，其次是remove( )，最后是del。
- **pop( )** 通过索引号删除元素

pop(index)是列表的内置方法，通过列表索引号来删除列表元素；如果不指定索引号，列表删除最后一个元素。
>pop( )一次只能删除一个元素。

```python
list1 = [1, 2, 3, 4, 5]
print('list1原始列表为：\n', list1)
# 使用pop()删除列表第二个元素，索引为1
list1.pop(1)
print('list1使用pop删除元素后的列表为(指定索引）：\n', list1)
# 使用pop删除元素，不指定索引
list1.pop()
print('list1使用pop删除元素后的列表为（不指定索引）：\n', list1)
```

![pop删除元素](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-29/1603935154021-image.png)

- **remove( )** 删除列表中第一个符合条件的元素
remove( )是列表的内置方法，根据给定的值查找列表，在列表中找到符合条件的第一个值删除。
>remove只能一次删除一个元素。

```python
list1 = [1, 3, 4, 3, 5]
print('list1原始列表为：\n', list1)
# 使用remove()删除列表第2个元素:3，remove括号中输入3
list1.remove(3)
print('list1使用remove删除元素后的列表为：\n', list1)
```

![remove删除元素](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-29/1603936748415-image.png)


- **del** 通过指定具体值删除
del是Python内置的用于删除变量的命令。
```python
list1 = [1, 3, 2, 3, 5]
print('list1原始列表为：\n', list1)
# 使用del删除列表第2个元素:3
del list1[1]
print('list1使用del删除元素后的列表为：\n', list1)
```

![del删除元素](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-29/1603937377211-image.png)

## 五、列表的切片

切片是Python序列的重要操作之一，适用于列表、元组、字符串、range对象等类型。

切片使用2个冒号分隔的3个数字来完成：

`[num_1 : num_2 : num_3]`。

其中，第一个数字**num_1**表示切片的开始位置，默认为0；第二个数字**num_2**表示切片的截止（但不包含）位置（默认为列表长度），第三个数字**num_3**表示切片的步长(默认为1)，当步长省略时，最后一个冒号也可以省略。

>可以使用切片来截取列表中的任何部分，得到一个新列表，也可以通过切片来修改和删除列表中部分元素，甚至可以通过切片操作为列表对象增加元素。与使用下标访问列表元素不同，切片操作不会因为下标越界而抛出异常，而是简单地在列表尾部截断或者返回一个空列表，代码具有更强的健壮性。

- 切片的使用

```python
list1 = [3, 5, 6, 7, 8, 12, 13, 16]
print(list1[::])    # 输出全部数据
print(list1[::-1])    # 倒序输出列表全部数据 
print(list1[3:6])    # 输出列表第四、第五、第六个数据
```

![切片的使用](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-29/1603971960527-image.png)

- 使用切片增加列表元素

```python
list1 = [3, 5, 6, 7, 8, 12, 13, 16]
print('list1原始列表为：\n', list1)
list1[len(list1):] = [18]    # 使用切片在原始数列上增加一个元素
print('使用切片增加元素后的list1为：\n', list1)
```

![使用切片增加元素](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-29/1603972537610-image.png)

- 使用切片修改元素

```python
list1 = [3, 5, 6, 7, 8, 12, 13, 16]
print('list1原始列表为：\n', list1)
list1[:3] = [19, 20]    # 使用切片在修改列表第一、第二个元素
print('使用切片修改元素后的list1为：\n', list1)
```

![使用切片修改元素](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-29/1603972722071-image.png)

## 六、列表的常用运算

- 列表的‘**+**’与‘**\***’运算

使用‘**+**’号连接两个列表，使用‘**\***’重复复制多个列表。

```python
list1 = [1, 3, 5]
list2 = [2, 4, 6]
list3 = list1 + list2    # 使用+号连接两个列表
print('list1为：\n', list1)
print('list2为：\n', list2)
print('连接后的列表list3为：\n', list3)
```

![使用+号连接列表](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-29/1603973483599-image.png)

```python
list1 = [1, 2] * 3    # 使用*重复列表三次
print(list1)
```

![使用*号重复列表](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-29/1603973648737-image.png)

## 七、列表常用的函数
- `len(list)`返回列表的长度
- `max( list )`返回列表中元素最大值，必须是相同类型对比
- `min( list )`返回列表元素最小值，必须是相同类型对比
- `list(tuple)`将元组转换为列表

```python
list1 = [3, 5, 6, 7, 8, 12, 13, 16]
tup = (1, 2, 3)
print('列表的长度为：\n', len(list1))    # 计算列表的长度
print('列表的最大值为：\n', max(list1))    # 计算列表的最大值
print('列表的最大值为：\n', min(list1))    # 计算列表的最小值
print('元组tup为：\n', tup)
print('将元组转换为列表：\n', list(tup))    # 将元组转换为列表
```

![列表常用函数](https://cdn.jsdelivr.net/gh/wbinzhang/Map-Bed/2020-10-29/1603977208090-image.png)

## 八、列表和数组间的异同

在Python中，列表（list）是Python的内置对象，而数组（array）是numpy库中所定义的。

>在list中的数据类型保存的是数据的存放的地址，简单的说就是指针，并非数据，这样保存一个list就太麻烦了，例如list = [1,2,3,'a']需要4个指针和四个数据，增加了存储和消耗cpu。numpy中封装的array有很强大的功能，里面存放的都是相同的数据类型。

- 列表（list）的特点

  1. 列表是以方括号“[ ]”包围的数据集合，不同元素用“，”分隔。例如List = [1, 2, 3]。
  2. 列表是可变的数据类型，可以对其中的元素进行增删改查，列表中可以包含任何数据类型，也可以包含另一个列表。如： List = [1, 2, [3, 4]]。
  3. 列表可以通过索引访问其中的元素，索引从0开始。
  4. 列表没有shape操作。
  5. 空列表（0个元素的列表）：List = [ ]； 一个元素的列表：List = [1]；多个元素的列表List = [1,2,3]。

- 数组（array）的特点
  1. 数组是以方括号“[ ]”包围的数据集合，不同元素用空格“ ”分隔。如Array = [1 2 3 4]。
  2. 数组的数据成员必须是相同数据类型属性，不同于列表。
  3. 数组可以是多维的，而列表是一维的。数组的每个维度之间以换行分隔开，单个维度内的数组成员也以换行分隔开,每个并列（单个）维度内的成员个数需要一致，不同维度的成员个数可以不一样。
  4. 数组通过索引号（下标）来访问数组元素,数组每个维度的元素的起始索引号为0，或者以逗号分隔的整数表示元素的维数和索引。
  5. 有很多可以直接使用的函数。
  6. 有形状大小shape，即维度，获取的两种方式np.shape(a)或者a.shape，即可得到数组的大小。