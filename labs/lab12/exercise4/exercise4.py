customers = 0
total_minutes = 0
minutes = int(input())

while total_minutes < 60 :
    customers += 1
    total_minutes += minutes

    if total_minutes >= 60 :
        break

    minutes = int(input())


print(customers)
print(total_minutes)
