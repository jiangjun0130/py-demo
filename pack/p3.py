"""
 This is doc
"""
import pack.t.p3

print('~~~~~~~~~~~~p3~~~~~~~~~~~~~~~~')
print('name:' + __name__)
print('package:' + (__package__ or '当前模块不属于任何包'))
print('file:' + __file__)
print('doc:' + (__doc__ or '当前模块没有文档注释'))

# 入口类package为空，说明：入口类不属于任何包
# 入口类的__name__值为：__main__
# 入口类与引用的模块，在内置变量方面是有差异的