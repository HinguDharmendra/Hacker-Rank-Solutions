# Enter your code here. Read input from STDIN. Print output to STDOUT
import xml.etree.ElementTree as etree
from xml.etree.ElementTree import XMLParser

class DepthXMLParser:
	max_depth=0
	depth=-1
	def start(self, tag, attrib):
		self.depth+=1
		self.max_depth=max(self.depth,self.max_depth)
	def end(self, tag):
		self.depth-=1
	def data(self,data):
		pass
	def close(self):
		return self.max_depth

parser=XMLParser(target=DepthXMLParser())
for i in range(int(raw_input())):
	parser.feed(raw_input())
print parser.close()

'''
## Almost correct
def getDepth(root, maxDepth):
    #print "Node,", root.tag, "has", len(root), "child nodes MaxDepth:", maxDepth
    if len(root) == 0:
        return 0
    else:
        for child in root:
            print "BEFORE: depth when at node", child.tag, "is NOT DEFINED", "maxDepth", maxDepth            
            depth = getDepth(child, maxDepth) + 1
            maxDepth = max(depth, maxDepth)
            print "AFTER: depth when at node", child.tag, "is", depth, "maxDepth", maxDepth
        return maxDepth

xml = ''
for i in range(int(raw_input())):
    xml += raw_input()

tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot() ## to get the root element of an XML tree
#print len(root)## to get number of child nodes

print getDepth(root, 0)
'''
