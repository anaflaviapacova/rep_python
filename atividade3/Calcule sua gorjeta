def dolares_para_float(d):
    # Remove o símbolo de $ e converte a string para float
    return float(d.replace('$', ''))

def percentual_para_float(p):
    # Remove o símbolo de % e converte a string para float, dividindo por 100
    return float(p.replace('%', '')) / 100

# Solicita o custo da refeição e o percentual de gorjeta
dolares = dolares_para_float(input("Quanto custou a refeição? "))
percentual = percentual_para_float(input("Qual percentual você gostaria de deixar de gorjeta? "))

# Calcula a gorjeta
gorjeta = dolares * percentual

# Exibe o valor da gorjeta formatado
print(f"Deixe ${gorjeta:.2f}")