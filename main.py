from collections import defaultdict as D
def enc(string):
    return not (r:=[]) and [r.extend(int(i) for i in bin(ord(ch))[2:].zfill(8)[::-1]) for ch in string] and r
def boolfuck(t, utf='',ptr=-1,p=0,j=0):
    utf,C,a,res = enc(utf),D(lambda:False),[],[]
    while (ptr:=ptr+1) < len(t):
        op = t[ptr]
        if op == '[':
            if C[j]:a+=[ptr]
            else:
                l_ptr = 1
                while ptr+1 < len(t) and l_ptr:
                    ptr += 1
                    if t[ptr] == '[':l_ptr += 1
                    elif t[ptr] == ']':l_ptr -= 1
        if op == ']':
            if C[j]: ptr = a[-1]
            else:a.pop()
        if op == '>':j += 1
        if op == '<':j -= 1
        if op == '+':C[j] = not C[j]
        if op == ';':res+=[int(C[j])]
        if op == ',':C[j]=(utf[p],p:=p+1)[0] if p<len(utf) else 0;
    return ''.join(chr(int(''.join(str(i) for i in res[i:i + 8][::-1]), 2)) for i in range(0, len(res), 8))