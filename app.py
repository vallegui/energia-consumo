print("--- Calculadora de Consumo de Energia ---")

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência (em watts): "))
horas_dia = float(input("Horas de uso por dia: "))
dias_mes = int(input("Dias de uso no mês: "))

# Cálculo do consumo em kWh
consumo_kwh = (potencia * horas_dia * dias_mes) / 1000

print(f"\nO consumo do(a) {aparelho} é de {consumo_kwh:.2f} kWh por mês.")