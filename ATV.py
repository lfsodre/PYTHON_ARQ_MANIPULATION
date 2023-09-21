
#---------------IMPRIMA O NOME DOS ALUNOS QUE FIZERAM A AV3--------------#
def atividade1():
    arquivo = open("./arqnotas.txt", "r" , encoding="utf8")
    conteudoAtual = arquivo.readlines()
    for linha in conteudoAtual:
            valores = linha.split(";")
            qdadeItens = len(valores)
            if (qdadeItens > 3):
                    print('Nome:', valores[0],'AV1:', valores[1],'AV2:', valores[2],'AV3:', valores[3])
    arquivo.close

#---------------GRAVAR O NOME DOS ALUNOS QUE FIZERAM A AV3--------------#
def atividade2():
    arq = open ("./arqnotas.txt","r")
    cont = arq.readlines()
    print (cont)
    arqAV3 = open ("./av3.txt","w")
    for linha in cont:
            valores = linha.split(";")
            qdadeItens = len (valores)
            if (qdadeItens > 3):
                    print ("Nome:", valores [0],"AV1:",valores [1],"AV2:",valores [2],"AV3:",valores [3])
                    av3 = "Nome:", valores [0],"AV1:",valores [1],"AV2:",valores [2],"AV3:",valores [3]
                    arqAV3.writelines (av3)
    arq.close()
    arqAV3.close()

#----------------------CALCULAR A MÉDIA DOS ALUNOS-----------------------#
def atividade3():
    arquivo = open("./arqnotas.txt", "r" , encoding="utf8")
    conteudoAtual = arquivo.readlines()
    for linha in conteudoAtual:
        valores = linha.split(";")
        qdadeItens = len(valores)
        media = 0.0
        if (qdadeItens > 3):
                media = (float (valores[1]) + float (valores[2]) + float (valores[3]))/3
        else:
                media = (float (valores[1]) + float (valores[2]))/3
        print('Nome:', valores[0],'Média:',round(media,2))
    arquivo.close
    
#--------------------CALCULAR A NOTA MÁXIMA E MÍNIMA--------------------#
def atividade4():
    arquivo = open("arqnotas.txt", "r" ,encoding="utf8")
    conteudoAtual = arquivo.readlines()
    for linha in conteudoAtual:
            print("----------------------------------------------------------")
            valores = linha.split(";")
            menor = 110.0
            maior = 0.0
            for nota in valores:
                    nota = nota.replace("\n","")
                    print ("Item: " ,nota)
                    if ((nota.isdigit()) and (float(nota) > maior)):
                            maior = float(nota)
                    if ((nota.isdigit()) and (float(nota) < menor)):
                            menor = float(nota)
            
            print('Nome:', valores[0],"Maior Nota: " , maior,"Menor Nota: " , menor)
    print("----------------------------------------------------------")
    arquivo.close

#--------PARA FUNCIONAR TIRE O HASHTAG DE ALGUMA FUNÇÃO---------#

#atividade1()
#atividade2()
#atividade3()
#atividade4()