__author__ = 'jiangjun'
__date__ = '2018/6/14 上午11:06'

def testFun():
    temp = [lambda x: i * x for i in range(4)]
    print(temp)
    return temp


# for everyLambda in testFun():
#     print(everyLambda(2))

testFun()[0]