valor_EUR = 1.01 #Euro
valor_USD = 1.00 #USD
valor_CAD = 1.31 #CAD

def conversion(dollarType, dollarValue, finalConv):
    type = float(input("Cuanto Dinero " + dollarType + " tiene?: "))
    dollar = (type * dollarValue)
    dollar = round(dollar, 2)
    dollar = str(dollar)
    print("Tendrias " + dollar + finalConv)

menu = """A que moneda desea convertir? \n1. USD to EUR\n2.EUR to USD\n3.USD to CAD\n4.CAD to USD
Elige una opcion: """
userSelection = int(input(menu))

if userSelection == 1:
    conversion("USD", 1.01, " EUR")

elif userSelection == 2:
    conversion("EUR", .99, " USD")

elif userSelection == 3:
    conversion("USD", 1.31, "CAD")

elif userSelection == 4:
    conversion("CAD", .76, "USD")
