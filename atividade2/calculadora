def comentar_idade():
    idade = input("Digite sua idade: ")

    # Verifica se a entrada é um número positivo
    if not idade.isdigit() or int(idade) < 0:
        return "Valor informado é inválido."

    idade = int(idade)

    # Condicionais para comentar a idade
    if idade < 18:
        return "Você é menor de idade."
    elif idade < 60:
        return "Você é adulto."
    else:
        return "Você é idoso."

# Chamada da função e impressão do resultado
print(comentar_idade())