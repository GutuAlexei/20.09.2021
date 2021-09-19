v=[12000, 2100 , 3212 ,2121, 7000, 0, 4300]
zi=['Lu', 'Ma', 'Mi', 'Jo', 'Vi', 'Si', 'Du']
z=max(v)
Mx=v.index(z)
d=min(v)
Mi=v.index(d)
print('a)', sum(v))
print('b)', sum(v)/7)
print('c)', zi[Mx])
print('d', zi[Mi])