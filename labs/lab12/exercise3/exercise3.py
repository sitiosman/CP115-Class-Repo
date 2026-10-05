valid_count = 0
total_sum = 0
grade = float(input())

while grade != -1 :
    if grade < 0 or grade > 100 :
        grade = float(input())
        continue

    valid_count += 1
    total_sum += grade
    grade = float(input())


average = total_sum / valid_count

print(valid_count)
print(f"{average:.2f}")
