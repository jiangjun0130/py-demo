"""
 This is doc
"""

print('name:' + __name__)
print('package:' + (__package__ or '当前模块不属于任何包'))
print('file:' + __file__)
print('doc:' + (__doc__ or '当前模块没有文档注释'))