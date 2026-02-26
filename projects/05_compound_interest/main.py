# Compund Interest Calculator

# Compound Interest Formula:
# A = P(1 + r/n)^t
#
# Where:
# A = final amount
# P = initial principal balance
# r = interest rate
# t = number of time periods elapsed

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be zero.")
    else:
        break
    
while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Rate can't be zero.")
    else:
        break

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be zero.")
    else:
        break

result = principle * pow((1 + (rate / 100)), time)

print(f"Principle: {principle} Rate: {rate} Time: {time} year/s  Final Amount: ${result:.2f}")
