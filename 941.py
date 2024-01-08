import math
a=abs(int(input()))

f=((a//100))
s=((a//10)%10)
t=((a%100)%10)

print((f*s*t)-(f+s+t))