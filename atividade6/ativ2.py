numero_str = input("Digite um número inteiro: ")

if numero_str.isdigit():
    numero = int(numero_str)
    
    soma_digitos = sum(int(digito) for digito in numero_str)
    
    print(f"A soma dos dígitos de {numero} é: {soma_digitos}")
else:
    print("Erro: O valor digitado não é um número inteiro.")