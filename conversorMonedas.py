valor_EUR = 1.009558 #Euro

dolarUSD = input("Cuanto Dinero USD tiene?: ")
dolarUSD = float(dolarUSD)

EUR = (dolarUSD * valor_EUR)
EUR = round(EUR, 2)
EUR = str(EUR)
print("Tienes " + EUR + " EUR")