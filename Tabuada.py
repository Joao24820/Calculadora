import time

print("Tabuada em python de 0 a 10 !!")

num = float(input("Informe o numero escolhido:"))
es = int(input("Escolha abaixo a tabuada que deseja visualizar:\n"
         "1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n\nEscolha uma opção acima: "))

time.sleep(2)
if es == 1:
    print("{} + 1 = {:.2f} ".format(num, (num + 1)))
    print("{} + 2 = {:.2f} ".format(num, (num + 2)))
    print("{} + 3 = {:.2f} ".format(num, (num + 3)))
    print("{} + 4 = {:.2f} ".format(num, (num + 4)))
    print("{} + 5 = {:.2f} ".format(num, (num + 5)))
    print("{} + 6 = {:.2f} ".format(num, (num + 6)))
    print("{} + 7 = {:.2f} ".format(num, (num + 7)))
    print("{} + 8 = {:.2f} ".format(num, (num + 8)))
    print("{} + 9 = {:.2f} ".format(num, (num + 9)))
    print("{} + 10 = {:.2f} ".format(num, (num + 10)))
    print("Calculo Finalizado !!")

elif es == 2:
    print("{} - 1 = {:.2f} ".format(num, (num - 1)))
    print("{} - 2 = {:.2f} ".format(num, (num - 2)))
    print("{} - 3 = {:.2f} ".format(num, (num - 3)))
    print("{} - 4 = {:.2f} ".format(num, (num - 4)))
    print("{} - 5 = {:.2f} ".format(num, (num - 5)))
    print("{} - 6 = {:.2f} ".format(num, (num - 6)))
    print("{} - 7 = {:.2f} ".format(num, (num - 7)))
    print("{} - 8 = {:.2f} ".format(num, (num - 8)))
    print("{} - 9 = {:.2f} ".format(num, (num - 9)))
    print("{} - 10 = {:.2f} ".format(num, (num - 10)))
    print("Calculo Finalizado !!")

elif es == 3:
    print("{} * 1 = {:.2f} ".format(num, (num * 1)))
    print("{} * 2 = {:.2f} ".format(num, (num * 2)))
    print("{} * 3 = {:.2f} ".format(num, (num * 3)))
    print("{} * 4 = {:.2f} ".format(num, (num * 4)))
    print("{} * 5 = {:.2f} ".format(num, (num * 5)))
    print("{} * 6 = {:.2f} ".format(num, (num * 6)))
    print("{} * 7 = {:.2f} ".format(num, (num * 7)))
    print("{} * 8 = {:.2f} ".format(num, (num * 8)))
    print("{} * 9 = {:.2f} ".format(num, (num * 9)))
    print("{} * 10 = {:.2f} ".format(num, (num * 10)))
    print("Calculo Finalizado !!")

elif es == 4:
    print("{} / 1 = {:.2f} ".format(num, (num / 1)))
    print("{} / 2 = {:.2f} ".format(num, (num / 2)))
    print("{} / 3 = {:.2f} ".format(num, (num / 3)))
    print("{} / 4 = {:.2f} ".format(num, (num / 4)))
    print("{} / 5 = {:.2f} ".format(num, (num / 5)))
    print("{} / 6 = {:.2f} ".format(num, (num / 6)))
    print("{} / 7 = {:.2f} ".format(num, (num / 7)))
    print("{} / 8 = {:.2f} ".format(num, (num / 8)))
    print("{} / 9 = {:.2f} ".format(num, (num / 9)))
    print("{} / 10 = {:.2f} ".format(num, (num / 10)))
    print("Calculo Finalizado !!")

else:
    print("A opção escolhida foi invalida !!\nReinicie o programa !!")
