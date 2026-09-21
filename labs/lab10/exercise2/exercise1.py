num_rounds = int(input())

final_score = 0
rounds_processed = 0

for  number in range(num_rounds):
    score = int(input())
    rounds_processed += 1

    if score > 100:
        final_score += (score + (score * 0.2))
    else:
        final_score += score


print(f"{final_score:.1f}")
print(rounds_processed)
