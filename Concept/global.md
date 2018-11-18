## python global
  当要在一个函数里对一个全局变量进行赋值操作时，可以使用global，例如：

    a = 10

    def test_fu():
        global a
        a = 100

    print(a, 'before')
    test_fu()
    print(a, 'after')
    
    # [out]：
    # 10 before
    # 100 after
    
  而不使用global时，也可以访问全局变量a，但是对它进行赋值后的作用域只在函数内，离开函数就没有用了
  
    a = 10

    def test_fu():
        a = 100

    print(a, 'before')
    test_fu()
    print(a, 'after')

    # [out]：
    # 10 before
    # 10 after
