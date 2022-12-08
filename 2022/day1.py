data = open('input_day1.txt').read().splitlines()


## Part I (version NSI)
most_calories = 0
current_calories = 0
for cal in data:
    if cal != '':
        current_calories += int(cal)
    else:
        most_calories = max(most_calories, current_calories)
        current_calories = 0
    

## Part II
calories = [0]
for cal in data:
    if cal != '':
        calories[-1] += int(cal)
    else:
        calories.append(0)

print(sum(sorted(calories, reverse=True)[:3]))
