#这是原始版，输出时是kwargs作为字典的格式
def fun0(**kwargs):
    print(kwargs)
#输入时需要为键赋值后才能正常输出

#这是进阶版本，输出格式更美观
def fun1(**kwargs):
    name=kwargs.get('name')
    age=kwargs.get('age')
    print(f"I am {name} \nand I am {age}")

#与缺省参数联用,缺省在前！！！
def fun2(sex="none",height="none",**kwargs):
    name=kwargs.get('name')
    age=kwargs.get('age')
    print(f"I am {name} \nand I am {age} \nand my gender is {sex} and my height is {height}")
