# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for t in xrange(int(raw_input().strip())):
    stmt = raw_input().strip().split(' ')[1]
    print 'VALID' if bool(re.search(r'^(CPP|CLISP|CLOJURE|C|JAVASCRIPT|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|BASH|SCALA|ERLANG|LUA|BRAINFUCK|JAVA|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$', stmt, re.I)) == True else 'INVALID'