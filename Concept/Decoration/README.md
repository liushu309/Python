# python装饰器
  面向切面编程，为了不修改原来函数的代码，又达到增加功能的作用。
## 1. 示例
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
