notas = []
nota = input("qual nota do primeiro aluno ?")
notas.append(float(nota))
nota = input("qual nota do segundo aluno ?")
notas.append(float(nota))
nota = input("qual nota do terceiro aluno ?")
notas.append(float(nota))
nota = input("qual nota do quarto aluno ?")
notas.append(float(nota))
nota = input("qual nota do quinto aluno ?")
notas.append(float(nota))

maior_nota = max(notas)
menor_nota = min(notas)
media_notas = sum(notas) / len(notas)

print(f"A maior nota é: {maior_nota}")
print(f"A menor nota é: {menor_nota}")
print(f"A média das notas é: {media_notas}")
