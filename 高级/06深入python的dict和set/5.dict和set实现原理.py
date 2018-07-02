__author__ = 'jiangjun'
__date__ = '2018/6/23 上午11:32'

# 1：dict的key或者set的值，都必须是可以hash的
# 2：不可变对象 都是可hash的，str，frozenset，tuple，自己实现的类__hash__
# 3：dict的内存花销大，但是查询速度快，自定义的对象或者python内部的对象都是用dict包装的
# 4：dict的存储顺序和元素的添加顺序有关（hash冲突可能导致存储位置变化）
# 5：添加数据有可能改变已有数据的顺序（存储空间不足时，扩展存储空间后，重新计算hash位置）