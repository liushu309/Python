## python装饰器
  面向切面编程，为了不修改原来函数的代码，又达到增加功能的作用。
## 示例
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
### [out]
    被调用了！ *************************************
    2
    sub *************************************
    1
