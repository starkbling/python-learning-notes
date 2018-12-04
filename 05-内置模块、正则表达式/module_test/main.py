__author__ = "Alex Li"
# import module_alex
#module_alex=all_code   module_alex.name module_alex.logger()
import sys,os
print(sys.path)

# os.path.abspath(__file__) 获取当前文件的路径
x=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(x)
#sys.path.insert(x) 把插入的对象置于列表的最前面，确保如其他目录下有同名的模块，这个模块先被调用
import module_alex

say_hello()
