print('Olá Recrutador(a). Seja bem vindo a plataforma de processos seletivos! ')
nome_recrutador= str(input('Digite seu nome'))

num_de_candidatos = int(input("Digite o número de candidatos que participaram da entrevista: "))
candidato_zero = 0    #Será utilizado para definir o número de solicitações de notas do usuario na estrutura de repetição da linha 6. 
nome_candidato = 1    #Será utilizado para localizar de qual candidato estamos digitando as notas. 
lista_candidatos = [] #Lista onde será armazenado as notas dos candidatos.

while candidato_zero < num_de_candidatos:
    lista_notas = []                            #Lista utilizada para salvar as notas dos candidatos. 
    
    entrevista = int(input(f"Digite a nota do canditato(a) {nome_candidato} na entrevista: "))
    teorico = int(input(f"Digite a nota do canditato(a) {nome_candidato} no teste teórico: "))
    pratico = int(input(f"Digite a nota do canditato(a) {nome_candidato} no teste prático: "))
    softskills = int(input(f"Digite a nota do canditato(a) {nome_candidato} na avaliação das softskills: "))

    lista_notas.append(entrevista)                      #Adicionando as notas dentro da "lista_notas" criada na linha 7.
    lista_notas.append(teorico)
    lista_notas.append(pratico)
    lista_notas.append(softskills)

    lista_candidatos.append(lista_notas)       #Adicionando a "lista_notas" dentro da "lista_candidatos".
    candidato_zero += 1
    nome_candidato += 1

lista_notas_minimas = []                        #Criação da lista com as notas mínimas para aprovação no processo seletivo. 

e_nota_minima = int(input('Digite a nota minima para aprovação na entrevista: '))             #Solicitando as notas mínimas para aprovação.
t_nota_minima = int(input('Digite a nota minima para aprovação no teste teórico: '))
p_nota_minima = int(input('Digite a nota minima para aprovaçâo no teste prático: '))
s_nota_minima = int(input('Digite a nota minima para aprovação no teste soft skills: '))

lista_notas_minimas.append(e_nota_minima)                       #Adicionando as notas mínimas dentro da lisra "lista_notas_minimas" criada na linha 23.
lista_notas_minimas.append(t_nota_minima)
lista_notas_minimas.append(p_nota_minima)
lista_notas_minimas.append(s_nota_minima)

print("Segue a lista com os candidatos aprovados: ")

#Comparação das notas

def imprime(lista_candidatos, lista_notas_minimas):
    coun1 = 0
    candidatos_aprovados = []                                        #Lista criada para adicionar os candidados que cumpriram todos os pré-requisitos para aprovação.
    for concorrentes, notas in enumerate(lista_candidatos):
        for indice, valor in enumerate(notas):
            if lista_notas_minimas[indice] <= valor:
                coun1 += 1
        if coun1 == 4: 
            candidatos_aprovados.append(lista_candidatos[concorrentes])
            coun1 = 0
    for finalistas, notas in enumerate (candidatos_aprovados):                          
        print(f' Resultados do candidato {finalistas}: e{notas[0]}_t{notas[1]}_p{notas[2]}_s{notas[3]}')
            
imprime(lista_candidatos, lista_notas_minimas)

