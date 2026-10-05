correct_password = "python123"
max_attempts = 3
attempts_used = 0
login_successful = False

while attempts_used < max_attempts :
    user_password = input()
    attempts_used += 1
    if user_password == correct_password :
        login_successful = True
        break



print(login_successful)
print(attempts_used)
