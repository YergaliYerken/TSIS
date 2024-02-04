def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        total_legs = 2 * num_chickens + 4 * num_rabbits
        if total_legs == numlegs:
            return num_chickens, num_rabbits
        
solution = solve(35, 94)
print("Number of chickens:", solution[0])
print("Number of rabbits:", solution[1])