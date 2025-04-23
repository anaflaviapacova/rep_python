def validar_entrada_temperatura():
    try:
        temperatura = float(input("Informe a temperatura (em °C): "))
        return temperatura
    except ValueError:
        print("Valor inválido! A temperatura deve ser um número decimal ou inteiro.")
        return None

def calcular_media_e_variacao(temp_max, temp_min):
    media = (temp_max + temp_min) / 2
    variacao = temp_max - temp_min
    return media, variacao

def soma_dos_digitos():
    numero_str = input("Informe um número para somar seus dígitos: ")
    if not numero_str.isdigit():
        print("Valor inválido! O número deve ser inteiro.")
        return None
    soma = sum(int(digit) for digit in numero_str)
    return soma

def main():

    print("Informe a temperatura mínima e máxima do dia:")
    
    temp_min = None
    while temp_min is None:
        temp_min = validar_entrada_temperatura()
    
    temp_max = None
    while temp_max is None:
        temp_max = validar_entrada_temperatura()
    
    media, variacao = calcular_media_e_variacao(temp_max, temp_min)
    print(f"A média das temperaturas é: {media:.2f}°C")
    print(f"A variação entre as temperaturas é: {variacao:.2f}°C")
    
    soma = soma_dos_digitos()
    if soma is not None:
        print(f"A soma dos dígitos do número informado é: {soma}")

if __name__ == "__main__":
    main()