import shelve
import datetime
d = shelve.open('shelve_test')  # 打开一个文件

#将值导入到d中
info =  {'age':22,"job":'it'}
name = ["alex", "rain", "test"]
d["name"] = name  # 持久化列表
d["info"] = info  # 持久dict
d['date'] = datetime.datetime.now()

#从d中提取数据
print(d.get("name"))
print(d.get("info"))
print(d.get("date"))
d.close()

import xml.etree.ElementTree as ET

new_xml = ET.Element("personinfolist")
personinfo = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "yes"})
name = ET.SubElement(personinfo, "name")
name.text = "Alex Li"
age = ET.SubElement(personinfo, "age", attrib={"checked": "no"})
sex = ET.SubElement(personinfo, "sex")
sex.text = "M"
age.text = '56'
personinfo2 = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "no"})
name = ET.SubElement(personinfo2, "name")
name.text = "Oldboy Ran"
age = ET.SubElement(personinfo2, "age")
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("personinfo.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式

