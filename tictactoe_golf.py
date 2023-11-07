#!/usr/bin/env python3
s=3
def a(r):
 while 1:
  u=input(f"which {r} ? ")
  if u.isdigit()and int(u)<s:return int(u)
  p("invalid")
S=s*s
x,o="x","o"
l=range(s)
p=print
v=input('Enter->1 v 1, or 1 vs ia : ')
e=('+-'*s+'+\n')
for i in(b:=[*" "*S]):
 for j in l:p(e,*b[s*j:s*j+s],'',sep='|')
 p(e+"\nplayer",x,"turn")
 if v and x=='o':c=b.index(' ')
 else:
  while b[(c:=a("line")*s+a("col"))]!=' ':p("occupied")
 b[c]=x
 if -1 in map(lambda e:len(set(e))*~e.count(' '),[b[s-1:S-1:s-1]]+[b[:S:s+1]]+[b[k*3:k*3+s]for k in l]+[b[k:S:s]for k in l]):p(x,"win !"),exit()
 x,o=o,x
p("it's a draw !")
