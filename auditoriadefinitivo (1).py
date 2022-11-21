def verificaID():
    ID=[]#cria uma lista vazia que armazenará os caracteres do ID
    x=str(input("ID \n")) #A variavel x guarda o ID digitado pelo usuario

    for i in range(len(x)): #O laço é executado len(x) vezes
        ID.append(x[i]) #Cada caractere na variável x é adicionado à lista ID, um por vez
    ID.sort() #Organiza a lista ID em ordem crescente
    new1=int(ID[0] + ID[3]) #Junta em uma unica string o menor número com o maior e o número resultante é convertido para inteiro
    new2=int(ID[1] + ID[2]) #Cria uma string com o 2 menor número e o 2 maior número
    #Os números new1 e new2 são os que resultam na menor soma pois as menores dezenas são somadas
    
    if new1+new2<=100: #Se new1 + new2 for menor ou igual a 100, é um ID válido
        print("valido")
    else:              #Senão, o ID é inválido
        print("inválido")


def ContaVotos(votos): #uma função que recebe como parâmetro uma lista com votos
    
    votosOrganizados = [] #não consegui pensar em um nome bom para a lista, no decorrer do code vcs vão ver para o q ela serve
    votosFaltando = [] #a mesma coisa da de cima
    for i in range(1, len(votos) + 1):
        votosOrganizados.append(i) #se a lista de votos tem n elementos, a lista de votosOrganizados terá os elementos de 1 até n.

    for j in votosOrganizados: # j vai assumir o valor de cada voto
        if not(j in votos): #se algum voto está presente em votosOrganizado e não está em votos, este voto não foi computado
            votosFaltando.append(j)

    print(votosFaltando)



def cadastrarSenha():
    senha = str(input("Digite a senha: ")).lower().replace(" ","")#armazena a senha que o usuario digitar na variável senha.Obs: 'lower()' deixa tudo minúsculo e 'replace(" ","")' retira os espaços da senha caso o usuario seja um neandertal que não sabe usar o teclado

    senhaCaracteres = [] #cria uma lista que armazenará os caracteres da senha
    
    for i in senha: #esse laço adiciona cada caracter da string senha na lista senhaCaracteres
        senhaCaracteres.append(i)

    frequenciaCaracteres = [] #uma lista que vai armazenar quantas vezes cada caracter da senha aparece

    for j in senhaCaracteres:
        frequenciaCaracteres.append(senhaCaracteres.count(j)) #a variavel 'j' do laço assume o valor de cada caracter da senha em cada interação e a função count(j) conta quantas vezes o caracter 'j' aparece na senha(exemplo: oioioi - count(o) = 3). A quantidade de vezes que o caractere aparece na senha é adicionado à lista frequenciaCaracteres

    #A função set(lista) transforma a lista em um conjunto(outra estrutura de dados). Mas, em um conjunto, não se adiciona caracteres repetidos. Exemplo( o conjunto {a,a,b,b,c,c} é igual ao conjunto {a,b,c}).Logo a função set cria uma lista com todos os caracteres da lista, mas sem repetição.

    #Se todos os carcteres aparecem x vezes na lista, a lista frequenciaCaracteres será [x,x,x,x,...x] e ao transformarmos essa lista em um set ficaria set(frequenciaCaracteres) = {x}. Logo se todos os caracteres aparecem uma única vez o set tem só um elemento e então a lista é valida
    if len(set(frequenciaCaracteres)) == 1:
        print("Senha Válida")

    else: 
        print("Senha inválida")

def Auditoria():
    y = 0
    votos = []
    resp = ''
    while resp =='s':
        y = int(input("Digite o voto a ser adicionado à lista de votos: "))
        votos.append(y)
    verificaID()
    ContaVotos()
    cadastrarSenha()
