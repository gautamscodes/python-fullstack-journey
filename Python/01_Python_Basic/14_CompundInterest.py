"""
Amount = p(1 + r / 100) ** 100
P = principal
rate = rate
t = time
ci = Amount - p
"""

principal = float(input("Enter the principal amount : "))
rate = float(input("Enter the interest rate : "))
time = float(input("Enter the time : "))
amount = principal * (1 + rate/100) ** time
amount1 = principal * pow((1 + rate/100), time)
print(amount, amount1)
print(round(amount1, 2))
ci = amount - principal
print(f"Compound interest {ci}")
