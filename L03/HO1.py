a = int(input())
s = int(input())
d = int(input())
if a>d and a>s and d>s:
 print(s,d,a)
elif a>d and a>s and s>d:
 print(d,s,a)
elif d>a and d>s and s>a:    
 print(a,s,d)
elif d>a and d>s and a>s:
 print(s,a,d)
elif s>a and s>d and d>a:
 print(a,d,s)
elif s>a and s>d and a>d:
 print(d,a,s)