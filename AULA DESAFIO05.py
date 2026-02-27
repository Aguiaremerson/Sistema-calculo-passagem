

print ("  Viagens até 200 km são 0,50 centavos por km\n    agora se for  mais que 200km ficara 0,45")
km= float (input ("   Digite quantos km você vai fazer nessa vigem:"))
n1= 0.50
n2 = 0.45
res1 = km * n1
res2 =  km * n2

if km <=200:
    print ("Sua viagem é de {}km e o valor da passagem sera {:.2f} Reais ".format (km,res1))
else:
    print ("Sua vigem é de {}km e o valor da passagem sera {:.2f} Reais ".format (km,res2))

print ("Boa Viagem!!!!")


            # Gustavo gaunabara
distancia = float (input('Qual é a distancia da sua viagem'))
print ("Voce esta preste a comecar uma viagem de {}km".format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distançia * 0.45
print ('E o preço da sua passagem sra de r$ {:.2f}'.format(preço))