#abrindo o arquivo "ProximalPhalanxTW" e renomeu para "input"
arquivo = open("input.txt","r")

#lendo e armazenamos na variavel "a" n linhas
a = arquivo.readlines()[0:1]

#Criou uma lista de lista de "a" 
for i in range(len(a)):
  a[i] = a[i].split()
  
#uma lista vazia, para armazenar as subsequencias
Cs = []

#for criado com a finalidade de variar entre as 10 linhas
for S in range(len(a)):
#for criado para gerar janelas de todos os tamanhos possiveis
  for k in range(3,len(a[S][0:80])):
    W = len(a[S])-k
#for criado para deslizar a janela das subsequencias 
    for j in range(W):
     Cs.append(a[S][j:j + k])

#Converteu a variavel "Cs"(Todas as subssequencias possiveis) em string, para poder armazenar
STR = str (Cs)

#replace para limpeza da string, tirando conchetes, virgulas e aspas
X = STR.replace("[['", '')
Z = X.replace("']]", "")
Y = Z.replace("', '", " ")
W = Y.replace("'], ['","SOS") #SOS separador das subsequencias


#print(W)

#criando um arquivo txt "subs"
subs = open("subs.txt","w")
#escrevendo no txt "subs" o arquivo STR (as subsequencias)
subs.writelines(W)

subs.close()




#abre e lê o arquivo subs.txt e é armazenado na variavel s
subs = open('subs.txt','r')
s = subs.readlines()

T = 1 #intervalo escolhido da serie temporal 

#abre e lê o arquivo new.txt e é armazenado na variavel n
new = open('new.txt','r') #new.txt serie temporal
n = new.readlines(T)

#criado uma lista para "new.txt"
for j in range(len(n)):
  n[j] = n[j].split()


new.close()
subs.close()


#separa em listas, pelo "SOS" como parametro de separação
for i in range(len(s)):
  s[i] = s[i].split("SOS")


s = s[0]
for l in range(len(s)):

#feito uma lista dentro das listas de subsequencias
  s[l] = s[l].split("', '")

for l in range(len(s)):
#feito uma lista dentro de cada ponto dentro das subsequencias
  s[l] = s[l][0].split()


#converte a lista de listas da variavel s em float
for j in range(len(s[0])):

  for i in range(len(s)):
    s[i][j] = float(s[i][j])

#faz o mesmo com a variavel n
for j in range(len(n[0])):

  for i in range(len(n)):
    n[i][j] = float(n[i][j])

        

# x é a subsequencia cs de tamanho 3
# y é a serie temporal T(n) 
x = s
y = n


#for p in range((len(y)) - (len(x))):

for p in range(len(y - (len(x)))):
  sm = 0
  sm = float(sm)
  for v in range(len(x)):
    sm = x[v] - y[v+p] + sm
  D = ((sm)**2)**(1/2)
#(x ** (y/z) )


'''OP = []

for S in range(len(a)):

  for k in range(3,len(a[S][0:80])):
    W = len(a[S])-k
    for j in range(W):
     Cs.append(a[S][j:j + k])


OP = str (vazio)


#criando um arquivo TXT
subs = open("output.txt","OP")
subs.writelines(OP)

subs.close()'''

print(s)

#print(D)

#print(n)
