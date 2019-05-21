from time import sleep as esperar


path = open('..\Simulador de Sistema operacional monoprogramável\Entrada.txt.txt')
texto = path.readlines()
nome_processo = []
tipo_processo = []
duracao = []
total = 0
condicao = True
tempoTotalCPU = 0
tempoTotalES = 0
tempototal = 0
for linha in texto :
    v = linha.split()
    nome_processo.append(v[0])
    tipo_processo.append(v[1])
    duracao.append(int(v[2]))


for i in range(len(nome_processo)):
    contador = duracao[i]
    
    for j in range(duracao[i]):
        print("Executando Processo :", nome_processo[i], end="", flush=True)
        esperar(1)
        print(".", end="", flush=True);
        esperar(1)
        print(".", end="", flush=True);
        esperar(1)
        print(".", end="\n", flush=True);
        esperar(1)
        if(condicao == True):
            contador -= 1
            print("Tipo Processo: ",tipo_processo[i])
            print("Duração: ",duracao[i])
            print("tempo restante: ", contador, "\n")
            
                         
        else:
            condicao = False
        

        
        if(contador == 0):
            condicao = True
            break

    if tipo_processo[i]==("CPU"):
        tempoTotalCPU += duracao[i]
    else:
        if tipo_processo[i] == ("ES"):
            tempoTotalES += duracao[i]

    print("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>> \n")


print("O tempo total do Processo CPU é: " + str(tempoTotalCPU))
print("O tempo total do Processo ES é: " + str(tempoTotalES))
print("Tempo Total dos Processos: " + str(sum(duracao)))
print("Tempo de espera médio dos processos é : " + str(sum(duracao)/len(tipo_processo))+ '\n')



tempotot1 = ("O tempo total do Processo CPU é: " + str(tempoTotalCPU))
tempotot2 = ("O tempo total do Processo ES é: " + str(tempoTotalES))
tempotot3 = ("Tempo Total dos Processos: " + str(sum(duracao)))
tempotot4 = ("Tempo de espera médio dos processos é : " + str(sum(duracao)/len(tipo_processo)))

print("Arquivo Gerado como * Saida.txt * ")

fileobj = open("Saida.txt","w")
fileobj.write(tempotot1+ '\n')
fileobj.write(tempotot2+ '\n')
fileobj.write(tempotot3+ '\n')
fileobj.write(tempotot4)

fileobj.close()
path.close()






