n = int(input("Enter number of transactions: "))
transactions = [0] * n

for i in range(n):
    transactions[i] = int(input(f"Enter transaction {i+1}: "))

normal = [0] * n
large = [0] * n
high_risk = [0] * n
invalid = [0] * n

normal_index = 0
large_index = 0
high_index = 0
invalid_index = 0

for t in transactions:

    if t <= 0:
        invalid[invalid_index] = t
        invalid_index += 1

    elif 1 <= t <= 500:
        normal[normal_index] = t
        normal_index += 1

    elif 501 <= t <= 2000:
        large[large_index] = t
        large_index += 1

    else:
        high_risk[high_index] = t
        high_index += 1

normal_final = normal[:normal_index]
large_final = large[:large_index]
high_final = high_risk[:high_index]
invalid_final = invalid[:invalid_index]

categories = {
    "normal": normal_final,
    "large": large_final,
    "high_risk": high_final,
    "invalid": invalid_final
}

valid_transactions = [t for t in transactions if t > 0]

count = len(transactions)
total = sum(valid_transactions)

summary = (count, total)

if count > 5:
    frequent = True
else:
    frequent = False

if total > 5000:
    large_spending = True
else:
    large_spending = False

if len(high_final) >= 3:
    suspicious = True
else:
    suspicious = False

risk_score = 0

if frequent:
    risk_score += 1
if large_spending:
    risk_score += 1
if suspicious:
    risk_score += 1

if risk_score == 0:
    risk = "Low Risk"
elif risk_score == 1:
    risk = "Moderate Risk"
else:
    risk = "High Risk"

if len(invalid_final) > 0:
    print("Invalid transactions detected !!")

if total < 1000:
    print("Suggestion: Your spending is well controlled")

elif 1000 <= total <= 5000:
    print("Suggestion: Keep monitoring your spending")

else:
    print("Suggestion: High spending detected! Be cautious")

print("Categorized Transactions:")
print(categories)

print("Total Transaction Value:", total)
print("Number of Transactions:", count)

print("Final Risk Classification:", risk)
