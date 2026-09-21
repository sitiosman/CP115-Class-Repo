#User make an input
monthly_usage = int(input("Enter your monthly usage:"))
discount = 0

#Calculation
if monthly_usage < 50 :
    discount = monthly_usage
elif monthly_usage <= 100 :
    discount = monthly_usage + (monthly_usage * 0.05)
else :
    discount = monthly_usage + (monthly_usage * 0.20)

bill = monthly_usage

print ("Amount of the bill to be paid is :" ,  {discount})