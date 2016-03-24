from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if(len(data) > 1):
            print ">>> Data"
            print data
        
    def handle_comment(self, comment):
        if ("\n" not in comment):
            print ">>> Single-line Comment"
        else:
            print ">>> Multi-line Comment"
        print comment
        
html = ""       
for i in range(int(raw_input())):
    html += raw_input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
