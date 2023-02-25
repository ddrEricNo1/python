"""
def关键字定义的函数，可以带有名称
lambda关键字，可以定义匿名函数（无名称）
无名称的匿名函数，只可以临时使用一次
"""

def test_func(compute):
    result = compute(1, 2)
    print(result)


test_func(lambda x,y: x + y)
