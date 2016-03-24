# Enter your code here. Read input from STDIN. Print output to STDOUT
from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        if(attrs):
            for attr in attrs:
                print "->",attr[0],">",attr[1]
    def handle_endtag(self, tag):
        print "End   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        if(attrs):
            for attr in attrs:
                print "->",attr[0],">",attr[1]        

parse = True
parser = MyHTMLParser()
for _ in range(int(raw_input())):
    # instantiate the parser and fed it some HTML
    line = raw_input()
    if "<!--" in line and "-->" in line:
        parse = True
    elif "<!--" in line:
        parse = False
    
    if parse == True:
        parser.feed(line)
        
    if "-->" in line:
        parse = True