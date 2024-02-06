import random

choices = ["Heads" , "Tails"]
numberOfChoices = int(input("How many flips you wanna do bruuuuu: "))
heads = 0
tails = 0

for i in range(numberOfChoices):
    choice = random.choice(choices)

    if (choice == "Heads"):
        heads += 1

    else:
        tails += 1

percentageHeads = round((heads / numberOfChoices * 100), 5)
percentageTails = round((tails / numberOfChoices * 100), 5)

print("Precentage heads is ", percentageHeads, "%")
print("Percentage tails is ", percentageTails, "%")

