score = 0
ignored = 0
number = int(input())

while number != 0 :
    if number > score:
        score += number
    else :
        ignored += 1
        number = int(input())
        continue

    number = int(input())

print(score)
print(ignored)
