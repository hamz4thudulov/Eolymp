a,b,c=input().split(" ")
a,b,c=int(a),int(b),int(c)
if a==b and b==c:
    print(1)
elif a==b or a==c or b==c:
    print(2)
else:
    print(3)