__author__ = "Alex Li"

import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")   #元素树
root = tree.getroot()
print(root.tag)  #标签名


# 遍历xml文档
# for child in root:  #一个内存对象，通过循环来读取数据
#     print(child.tag, child.attrib)
#     for i in child:
#         print(i.tag, i.text,i.attrib)

# 只遍历year 节点
for node in root.iter('year'):  #root.iter 方法
    print(node.tag, node.text)