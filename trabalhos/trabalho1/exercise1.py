# Variável para inicializar e fazer a verificação do while
continua = "1"

# Lógica criada para saber em qual ensino a criança está
# Utilizei a função 'elif', uma simplificação das funções 'else if'
# Utilizei a simplicação do 'and', onde remove-se o boilerplate, deixando apenas a lógica booleana que necessita
while continua == "1":
    # Variável criada para atribuir o nome da criança, utilizando a função input para ler o dado
    nome = input("Nome da criança: ")
    # Variável idade para atribuir a idade do aluno, convertendo o resultado do input para integer
    idade = int(input("Idade: "))

    if 0 < idade <= 5:
        print("O aluno {} tem {} ano (s) e está no Educação Infantil".format(nome, idade))
    elif 5 < idade <= 10:
        print("O aluno {} tem {} ano (s) e está no Ensino Fundamental I".format(nome, idade))
    elif 10 < idade <= 14:
        print("O aluno {} tem {} ano (s) e está no Ensino Fundamental II".format(nome, idade))
    elif 15 < idade:
        print("O aluno {} tem {} ano (s) e está no Ensino Médio".format(nome, idade))
    else:
        print("Idade inválida!")

    continua = input("Você quer continuar? 1-SIM ou 2-NÃO")

print("Obrigado pela reposta!")






