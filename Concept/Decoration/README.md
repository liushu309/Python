# python装饰器
  面向切面编程，为了不修改原来函数的代码，又达到增加功能的作用。

## 0. python闭包
  如果在一个函数的内部定义了另一个函数，外部的我们叫他外函数，内部的我们叫他内函数。
  在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用。这样就构成了一个闭包。
#闭包函数的实例
### 0.1 标例
    # outer是外部函数 a和b都是外函数的临时变量
    def outer( a ):
        b = 10
        # inner是内函数
        def inner():
            #在内函数中 用到了外函数的临时变量
            print(a+b)
        # 外函数的返回值是内函数的引用
        return inner

    if __name__ == '__main__':
        # 在这里我们调用外函数传入参数5
        # 此时外函数两个临时变量 a是5 b是10 ，并创建了内函数，然后把内函数的引用返回存给了demo
        # 外函数结束的时候发现内部函数将会用到自己的临时变量，这两个临时变量就不会释放，会绑定给这个内部函数
        demo = outer(5)
        # 我们调用内部函数，看一看内部函数是不是能使用外部函数的临时变量
        # demo存了外函数的返回值，也就是inner函数的引用，这里相当于执行inner函数
        demo() # 15
        demo2 = outer(7)
        demo2()#17

## 1. 装饰器
  装饰器实现使用了闭包
    #定义一个新的函数
    def title(show = '标题参数'):
        def printStar(func = '函数名参数'):
            def f(a = '被装饰函数的原参数', b = '被装饰函数的原参数'):
                print(show,'*************************************')
                return func(a, b)
            return f
        return printStar

    @title('被调用了！')
    def add(a, b):    
        return a + b

    @title('sub')
    def sub(a, b):    
        return a - b
    print(add(1, 1))
    print(sub(2, 1))
### 1.1 [out]
    被调用了！ *************************************
    2
    sub *************************************
    1

## 2. @property
  既能检查参数，又可以用类似属性这样简单的方式来访问类的变量
## 2.1 示例
    class Student(object):

        @property
        def score(self):
            return self._score

        @score.setter
        def score(self, value):
            if not isinstance(value, int):
                raise ValueError('score must be an integer!')
            if value < 0 or value > 100:
                raise ValueError('score must between 0 ~ 100!')
            self._score = value

    s = Student()
    s.score = 60 # OK，实际转化为s.set_score(60)
    print(s.score) # OK，实际转化为s.get_score()
    s.score = 9999
### [out]
    60
    Traceback (most recent call last):
      File "test.py", line 19, in <module>
        s.score = 9999
      File "test.py", line 12, in score
        raise ValueError('score must between 0 ~ 100!')
    ValueError: score must between 0 ~ 100!
