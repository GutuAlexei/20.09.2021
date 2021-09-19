x=[1,4,-1,4,5,3,2,5,]
y=[1,45,21,34,5,23,2,-450,]
s=0
p=1
a=0
d=0
for z in range(0, len(x)):
    s=x[0]+x[1]+x[2]
print('a)', s)
print('b)', sum(y))
for z in range(0, len(x)):
    p=p*x[z]
print('c)', p)
a=abs(x[2])
print('d)', a)
d=x[0]+y[0]
print('e)', d)