Questão 1- 
k = 1
while(k<=100):
    if(k%2==0):
        print(k)
k+=1

Questão 2- 
Vp = list()
Vn = list()
for i in range(6):
    valor = int(input())
    if (valor < 0): ln.append(valor)
    else:lv.append(valor)
print("Valor positivo: ",Vp )
print("Valor negativo: ",Vn)

Questão 3-
c = int(input())
for i in range(c):
    v1 = float(input())
    v2 = float(input())
    v3 = float(input())
     calculo = (v1*2)+(v2*3)+(v3*5)/3.0
print("Média Ponderada: %.1f"%(calculo))

Questão 4-
k = 0
y = 0
for i in range(15):
    n = int(input())
    
    if n > maior:
        maior = n
        posicao = i+1
        
print("%d\n%d"%(k, y));

Questão 5-
k = 0
y = 0
i = 0
while (i<6):
    n = float(input())
    if n>0:
        som+=n
        cont+=1
    i+=1
        
print("%d valores positivos" %cont)
print("%.1f" %(k/ y))

Questão 6-
pizzades = int(input("Digite o total de pizzas desejadas: "))
precopizza = float(input("Valor pizza: "))
custo = pizzades*precopizza
imposto = custo-custo*0.8
total = custo + imposto
print("O valor do pedido é: R$ %.2f" %(total))

Questão 7-
v = int(input())
t = list()
tn = 1

for i in range(1,v+1,1);
    tn = tn*i

print(tn)

Questão 8- 
vi1 = int(input())
vi2 = int(input())
print(vi1**vi2)

Questão 9-
n = int(input())
con = 0
for i in range(1,n+1,1):
    con+=i
print(con)

Questão 10-
numCigarro = int(input())
anosFumando = int(input())
totalCigarro = (anosFumando * 365)*numCigarro
qtdeDias = (totalCigarro * 10)/24

print (qtdeDias) 

Questão 11-
num = int(input("Digite seu número: "))
i = str(num)
print (len(i))

Questão 12-
vp = float(input())
td = list()
while (vp != 0):
    diasatr = int(input())
    if (diasatr==0):
        print("O valor total da Prestação: R$ %.2f" %(vp))
        td.append(vp)
    else:
        juros = vp+(10*0.3)+((10*0.01)*diasatr)
        print("O valor total da Prestação: R$ %.2f" %(juros))
        td.append(juros)
    vp = float(input())


calculoF = sum(td)

print("Total de prestações pagas no dia de hoje: R$ %.2f" %(calculoF))
