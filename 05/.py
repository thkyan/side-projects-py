peso = float(input('Insira o seu peso: '))
altura = float(input('Insira a sua altura: '))
imc = peso / (altura**2)

print(f"o seu imc é {imc:.1f}")

def classificar_imc(imc):
    if imc <= 18.5:
        return "abaixo do peso"
    elif imc > 18.5 or imc <= 24.9:
        return "peso normal"
    elif imc > 24.9 or imc <= 29.9:
        return "sobrepeso"
    elif imc > 29.9 or imc <= 34.9:
        return "obesidade  grau 1"
    else:
        return "obesidade grau 3"
    
classificação = classificar_imc(imc)
    
print(f"Seu imc está classificado como: {classificação}")