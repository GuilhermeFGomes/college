def menu(e):
    print("*" * 10 + " MENU " + "*" * 10)
    print("1 - Nova inscrição")
    print("2 - Vizualizar inscrição")
    print("0 - Encerrar\n")
    print("-" * 30)
    e = str(input("Insira a opção desejada: "))
    print("-" * 30)
    return e


while True:
    if menu("1") == "1":
        nome = input("Digite seu nome: ")
        email = input("Digite seu e-mail: ")
        telefone = input("Digite seu telefone: ")
        curso = input("Digite seu curso: ")
    elif menu("2") == "2":
        print("rw")

    elif menu("0") == "0":


    break
