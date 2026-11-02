"""
Simple Interest = (P * R * T) / 100
P = Principal amount
R = Rate or Interest
T = Time duration
"""

principal = float(input("Enter the principal amount : "))
rate = float(input("Enter the interest rate : "))
time = float(input("Enter the time : "))

si = (principal * rate * time) / 100

print(f"Simple interest is {si}")
