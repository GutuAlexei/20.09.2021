x=int(input('Introduceti numarul de elemente din vector='))
a=[]
if x>10:
    print('eror')
else:
    print('introduceti' , x , 'elemente pentru vectorul creat')
    for i in range(0,x):
        y=int(input('Dati elemente='))
        a.extend([y])
    print(a)

    print('a)	 afişează pe ecran componentele tabloului la un interval de 5 poziţii;',  )
print('b)	 afişează pe ecran numerele în ordinea inversă a introducerii în calculator;' , a[::-1])
c=sorted(a)
c.sort(reverse=True)
print('c)	 sortează componentele tabloului în ordine descrescătoare;' , c)
print('d)	 afişează pe ecran doar componentele pare;', )
d=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        d.extend({y})
print(d)
print('e)	 afişează pe ecran media aritmetică a componentelor pare;' , (sum(d)/len(d)))
print('f)	 afişează pe ecran doar componentele impare;')
f=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        y=a[i]
        f.extend({y})
print(f)
x=int(input("Introduceti X="))
y=int(input("Introduceti Y="))
print('g)	 afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
g=[]
for q in range(0,len(a)):
    if a[q]>x and a[q]%y!=0:
        y=a[q]
        g.extend({y})
print(g)
print('h)	 afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
h=[]
for w in range(0,len(a)):
    if a[w]>x and a[w]<y:
        p=a[w]
        h.extend({p})
print(h)
print('i)	 afişează pe ecran poziţiile (indicii) componentelor impare negative;')
i=[]
for e in a:
        if e%2!=0 and e<0:
            qq = a.index(e)
            i.extend([qq])
print(i)
print('j)	 afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
r=[]
for cs in a:
    if (((abs(cs)//10)<10) and ((abs(cs)//10)>0)):
            ab= a.index(cs)
            r.extend([ab])
print(r)
print('k)	 înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
print('l)	 înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
print('m)	creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
print(d) 
print('n)	 creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
n=[]
for aaa in a:
    if aaa%3==0:
        n.extend([aaa])
print(n)
print('o)	 creează un tablou nou, format doar din acele componente ale tabloului introdus de la tastatură care au cel mult patru divizori.')


