overtake_round = 0
round_num = 0
a = int(input())

while a != -1 :
    b = int(input())
    round_num += 1

    if b <= a :
        a = int(input())
        continue

    if overtake_round == 0:
        overtake_round = round_num

    a = int(input())
    
print(overtake_round)
