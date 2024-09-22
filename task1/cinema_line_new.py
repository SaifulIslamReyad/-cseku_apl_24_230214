numberOfPeople = input()

# Initialize counters for 25 ruble and 50 ruble bills
count_25 = 0
count_50 = 0

# Read the list of bills people have
bills = list(map(int, input().split()))

# Process each bill in the line
for bill in bills:
    if bill == 25:
        count_25 += 1  # Take 25 rubles, no change needed
    elif bill == 50:
        count_50 += 1  # Take 50 rubles, give back 25 rubles as change
        count_25 -= 1  # We need one 25 rubles bill for the change
    elif bill == 100:
        if count_50 > 0:
            count_50 -= 1  # Give back one 50 rubles bill
            count_25 -= 1  # Give back one 25 rubles bill
        else:
            count_25 -= 3  # Otherwise, give back three 25 rubles bills

    # If at any point we have negative count of 25 or 50 rubles, return "NO"
    if count_25 < 0 or count_50 < 0:
        print("NO")
        exit()

# If all transactions were successful, return "YES"
print("YES")
