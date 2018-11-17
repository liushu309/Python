## collections.namedtuple的理解
  将类的定义和生成这个类的对象在一行代码中完成，如：对象名 = collections.namedtuple('定义的类名', ['定义属性名1', '定义属性名2', ...])，再在第二行代码中，对这个对象进行赋值

import collections
# 定义类名，对象名
coordinate = collections.namedtuple('liushu', ['x', 'y']) 
# 对对象的属性进行赋值
co = coordinate(10,20)

print( co.x,co.y)
print( co[0],co[1])
co = coordinate._make([100,200])
print( co.x,co.y)
co = co._replace(x = 30)
print( co.x,co.y)
