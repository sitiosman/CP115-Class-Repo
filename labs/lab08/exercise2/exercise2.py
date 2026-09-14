employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

#Calculate
overtime_pay = overtime_hours * 35
gross = base_salary + overtime_pay

if tax_status =="Single":
    if gross >= 5000:
        tax_rate = 0.22
    else : 
        tax_rate = 0.18

elif tax_status == "Married":
    if gross >= 6000:
        tax_rate = 0.20
    else :
        tax_rate = 0.15

elif tax_status == "Head":
    if gross >= 5500:
        tax_rate = 0.25
    else :
        tax_rate = 0.19

else:
    tax_rate = 0.0

income_tax = gross * tax_rate
epf = gross * 0.11
sosco = gross * 0.005

net_salary = gross -income_tax - epf - sosco

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")
