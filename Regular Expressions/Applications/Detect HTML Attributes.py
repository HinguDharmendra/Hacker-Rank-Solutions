# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

st = []; l = []
pattern = r'(<\s*[a-z0-9]+\s*>?)?(?:([a-z]+)(?=\=[\"\']))?'
for line in xrange(int(raw_input().strip())):
    html = raw_input().strip()
    result = list(re.findall(pattern, html))
    for tag, attrib in result:
        tag = re.sub('<', '', re.sub('>', '', tag).strip()).strip()
        if len(tag) < 1 and len(attrib) < 1:
            continue
        else:
            if len(tag) > 0:
                l.append(tag.strip()+':'+attrib.strip())
            else:
                l.append(attrib.strip())
p = l[0]
for i in range(1, len(l)):
    if ':' not in l[i]:
        p+=','+l[i]
    else:
        st.append(p)
        p = l[i]
st.append(p)
ans = sorted(st)
tags = []; attribs = []
for e in ans:
    tags.append(e.split(':')[0])
    attribs.append(e.split(':')[1].split(','))
final = set()
for i in range(len(tags)):
    j = len(tags) - tags[::-1].index(tags[i]) - 1
    if i != j:
        final.add(tags[j]+':'+','.join(sorted(list(set([k for x in attribs[i:j+1] for k in x])))))
    else:
        final.add(tags[j]+':'+','.join(sorted(attribs[j])))
f = []
for i in sorted(list(final)):
    if i.split(':')[0] in [j.split(':')[0] for j in f]:
        continue
    else:
        print i
        f.append(i)