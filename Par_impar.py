def par_ou_impar(numero):
    if numero % 2 == 0:
        return f"O número {numero} é par."
    else: 
        return f"O número {numero} é ímpar."

numero = int(input("Digite um número: "))
resultado = par_ou_impar(numero)
print(resultado)