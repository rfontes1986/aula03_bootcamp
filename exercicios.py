# Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores 
# positivos para quantidade e preço. Escreva um programa que verifique esses campos e imprima "Dados válidos" 
# se ambos forem positivos ou "Dados inválidos" caso contrário.

#quantidade = 40
#preco = -20

#if quantidade > 0 and preco > 0:
    #print ("valores validos")
#else:
    #print ("valores invalidos")

#Exercicio 6: conte quantas vezes cada palavra apareceu em um texto

texto = "hoje o dia amanheceu com um sol lindo mas o tempo pode mudar se em vez do sol aparecer começar a chover, aí não será lindo"

palavras = texto.split(" ")

contagem_palavras = { }

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] = +1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)