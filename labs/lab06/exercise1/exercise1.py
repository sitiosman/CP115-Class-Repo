#total for each item
Total_coffee = 3.50 * 2
Total_muffin = 2.10 * 3
Total_water = 1.00 * 1
Subtotal = float(Total_coffee + Total_muffin + Total_water)
Tax = float(Subtotal * 0.06)
Total = float(Subtotal + Tax)

receipt = print(f
    "========== RECEIPT ==========\n Item\t Price\t Qty\t Total\n Coffee\t $3.50\t 2\t ${Total_coffee}\n Muffin\t $2.10\t 3\t ${Total_muffin}\n Water\t $1.00\t 1\t ${Total_water} "

)