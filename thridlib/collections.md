## collections.namedtuple的理解
  将类的定义和生成这个类的对象在一行代码中完成，如：
    类别名 = collections.namedtuple('定义的类名', ['定义属性名1', '定义属性名2', ...])，
  再在第二行代码中，引用别名构造对象，如下图所示
![image](https://github.com/liushu309/Python/blob/master/collections_namedtuple.png)

    import collections
    # 定义类名，类别名
    coordinate = collections.namedtuple('liushu', ['x', 'y']) 
    # 引用别名构造对象
    co = coordinate(10,20)

    print( co.x,co.y)
    print( co[0],co[1])
    co = coordinate._make([100,200])
    print( co.x,co.y)
    co = co._replace(x = 30)
    print( co.x,co.y)
