

import importlib
"""场景说明，在lib的python_package类的文件夹中新建了aa.py模块文件，文件中建了类C
"""

#第一种导入模块方式

lib = __import__('lib.aa')  # 该步骤中，只导入了lib模块，但是必须用lib.aa形式导入，只有这样才能在后面导入aa模块
print(lib)
print(lib.aa.C().name)

#第二种导入方式
aa = importlib.import_module('lib.aa') #官方建议用这个,此时导入的模块为aa模块
print(aa)
print(aa.C().name)