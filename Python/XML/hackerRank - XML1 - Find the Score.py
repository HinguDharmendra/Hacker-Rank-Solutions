# Enter your code here. Read input from STDIN. Print output to STDOUT
import xml.etree.ElementTree as etree

xml = ''
attribs = 0
for i in range(int(raw_input())):
    xml += raw_input()

tree = etree.ElementTree(etree.fromstring(xml))
#print tree.getroot() ## to get the root element of an XML tree
for element in tree.getiterator():
    attribs += len(element.attrib)

print attribs