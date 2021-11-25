# Variável criada para atribuir o nome da criança, utilizando a função input para ler o dado
nome = input("Nome da criança: ")
# Variável idade para atribuir a idade do aluno, convertendo o resultado do input para integer
idade = int(input("Idade: "))

# Lógica criada para saber em qual ensino a criança está
# Utilizei a função 'elif', uma simplificação das funções 'else if'
# Utilizei a simplicação do 'and', onde remove-se o boilerplate, deixando apenas a lógica booleana que necessita
if 0 < idade <= 5:
    print("O aluno {} tem {} ano (s) e está no Educação Infantil".format(nome, idade))
elif 5 < idade <= 10:
    print("O aluno {} tem {} ano (s) e está no Ensino Fundamental I".format(nome, idade))
elif 10 < idade <= 14:
    print("O aluno {} tem {} ano (s) e está no Ensino Fundamental II".format(nome, idade))
elif idade > 15:
    print("O aluno {} tem {} ano (s) e está no Ensino Médio".format(nome, idade))

#
# else:
#     continua = int(input("Você quer coninuar? 1-SIM ou 2-NÃO"))
# if (continua == 1):
#
# elif continua == 2:
#     print("Cancelado!")
