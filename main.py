import random # Import the random library to have access to random number generation.

# A solution to Lab Week 5
# 1
roster = ["James", "Ayman", "Ben", "Matt", "Kefron", "Emily", "Adam", "Shawn", "Mason", "Karan", "AJ", "Isaiah"]
print(f"The first name from the list using indexing is {roster[0]}.")
print(f"The second name from the list using indexing is {roster[1]}.")
number_of_students = len(roster)
# Recall random.randrange(12) will produce one of twelve numbers at random 0, 1, 2, ..., or 11.
print(f"A few names at random from the list are {roster[random.randrange(number_of_students)]}, "
      f"{roster[random.randrange(number_of_students)]}, {roster[random.randrange(number_of_students)]}.")
# (When we hit enter in the middle of a long line of code, Pycharm provides syntax to allow the code
# to continue on the next line. See above.)
# Note when I pick several names above, I might pick the same name more than once.
# 2
prizes = ['teddy bear', 'BSU Bears hoodie', 'air pods', 'corduroy tote bag']
values = [18.70, 45.50, 79.99, 10.99]
# a
print()
print("The prizes and their values are:")
for i in range(len(prizes)):
    print(f"{prizes[i]}: ${values[i]}")
# b
print()
random_index = random.randrange(len(prizes))
print(f"You won a {prizes[random_index]} worth ${values[random_index]}.")
# c
print()
random_index = random.randrange(len(prizes))
print(f"You won two {prizes[random_index]}s with a total value of ${round(values[random_index]*2, 2)}.")
# d
print()
values[2] = 89.99
random_index = random.randrange(len(prizes))
print(f"You won a {prizes[random_index]} worth ${values[random_index]}.")
# e
print()
print(f"The minimum prize value is ${min(values)}; the maximum is ${max(values)}, "
      f"and the total value of all the prizes is ${sum(values)}.")






