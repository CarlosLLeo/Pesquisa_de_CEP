import requests
from acesso_CEP import BuscarEndereco

cep = input('Digite o CEP desejável: ')

while len(cep) != 8 or not cep.isdigit():
    print("CEP deve conter 8 dígitos numéricos.")
    cep = input('Digite o CEP desejável novamente: ')

objeto_cep = BuscarEndereco(cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro,cidade, uf)






