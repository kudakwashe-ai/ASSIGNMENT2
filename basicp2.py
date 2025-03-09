total_purchase = float(input("Enter the total purchase amount: "))

if total_purchase > 100000:
    discount = total_purchase * 0.1
elif total_purchase > 50000:
    discount = total_purchase * 0.05
else:
    discount = 0

print(f"Total amount to be paid: {total_purchase - discount}")

