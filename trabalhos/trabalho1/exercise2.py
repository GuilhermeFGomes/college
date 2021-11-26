# Chamada da função input para atribuir o nome a variável nome
nome = input("Digite o seu nome: ")

# Transformando o nome em caixa alta utilizando a função upper()
print(nome.upper())

# Modificando as vogais da variável nome utilizando a função replace()
name1 = nome.replace("a", "@")
name2 = name1.replace("e", "&")
name3 = name2.replace("i", "!")
name4 = name3.replace("o", "#")
name5 = name4.replace("u", "*")

# Printando no terminal a variável já com caixa alta utilizando a função upper()
print(name5.upper())
