count = 0
biggest_jump = 0
previous_number = None

number = int(input())

while number != 0 :
    count += 1

    if previous_number is not None :
        jump = number - previous_number
        if jump > biggest_jump :
            biggest_jump = jump

    previous_number = number
    number = int(input())


print(count)
print(biggest_jump)
