import tokenize
import sys
from StringIO import StringIO

s=sys.argv[1]
#s="NUMINITATTACHSUCCESS/(NUMINITATTACHSUCCESS+NUMINITATTACHFAIL)*100"

vars=set()
divs=set()
div=''
start_div=False
it=tokenize.generate_tokens(StringIO(s).readline)
for type,value,_,_,_ in it:
    if value=='/':
        if div:
            divs.add(div)
            div=''
        start_div=True
    elif value=='*':
        if div:
            divs.add(div)
            div=''
        start_div=False
    elif value==')':
        if div:
            divs.add(div)
            div=''
        start_div=False
    else:
        if type == 1:
            vars.add(value)
        if start_div and value !="(":
            div+=value



print(vars)
print(divs)
