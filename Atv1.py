# 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

#Resposta: Saída = 91

indice = 13
soma = 0
K = 0

while( K < indice):
    K += 1
    soma +=K

print(soma)