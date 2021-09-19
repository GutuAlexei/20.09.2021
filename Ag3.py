Grade=[11,11,12,13,13,14,14,14,15,16,17,18,18,19,19,20,21,22,23,22,21,19,17,14]
ora=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','0']
z=max(Grade)
Mx=Grade.index(z)
d=min(Grade)
Mi=Grade.index(d)
print('a)', sum(Grade)/24)
print('b)', max(Grade) , min(Grade) )
print('c)', ora[Mx])
print('d)', ora[Mi])