name1 = input("enter your name1:")
name2 = input("enter your name2: ")

amount_of_the_consonant1 = 0
amount_of_the_consonant2 = 0

for char in name1:
    if char not in "aeiou":
        amount_of_the_consonant1 += 1
for char in name2:
    if char not in "aeiou":
        amount_of_the_consonant2 += 1

if amount_of_the_consonant1 > amount_of_the_consonant2:
    print("amount of the consonant is more in name1 and it contains {}".format(amount_of_the_consonant1))
elif amount_of_the_consonant2 > amount_of_the_consonant1:
    print("amount of the consonant is more in name2 and it contains {}".format(amount_of_the_consonant2))
else:
    print("they have equal amount of the consonant")






