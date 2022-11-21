def verificaID():
    ID=[]
    x=str(input("ID \n"))

    for i in range(len(x)):
        ID.append(x[i])
    ID.sort()
    new1=int(ID[0] + ID[3])
    new2=int(ID[1] + ID[2])

    if new1+new2<=100:
        print("valido")
    else:
        print("inválido")


def ContaVotos(votos:list): #uma função que recebe como parâmetro uma lista com votos
    
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
    verificaID()
    ContaVotos()
    cadastrarSenha()