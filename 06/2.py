principal = 0 
taxa = 0
tempo = 0

while principal <= 0:
    principal = float(input("Insira o valor principal: "))
    if principal <= 0:
        print("Só é valido valor acima de zero! ")

while taxa <= 0:
    taxa = float(input("Insira ao valor de interesse da taxa: "))
    if taxa <= 0:
        print("A taxa não pode ser um valor menor ou igual a zero!")

while tempo <= 0:
    tempo = int(input("Insira o tempo em anos: "))
    if tempo <= 0:
        print("O tempo não pode ser menor ou igual a zero!")

total = principal * pow((taxa + 1/100), tempo)

print(f"o total junto com a taxa de {taxa}% e os {tempo} anos, é: R${total:.2f}")