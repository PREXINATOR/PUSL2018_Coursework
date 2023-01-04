import random
#list of three random integers
#where 1 represents a boy
#where 2 represents a girl

# Entering the number of events that should consider
ECount = int(input("Enter the number of events:"))

def SimulateProbability():
    Gender = [random.randint(1, 2) for _ in range(3)]

    # check whether the random values
    #at least one child is a girl and all are girls(three)

    at_least_one_girl = 1 in Gender
    all_are_girls = Gender = [2, 2, 2]
    return at_least_one_girl and all_are_girls

# Run the program upto 1000 times and count number of times it satisfy the condition, at least one child is a girl and all are girls
# Condition is "Number of times at least one chid is a girl and all are girls"
Number_Of_Satisfactions = 0
# eventsCount = 1000

for _ in range(ECount):
    if SimulateProbability():
        Number_Of_Satisfactions += 1

#calculate the probability
Probability = Number_Of_Satisfactions/ECount

#print the result 
print("Number of events checked: ", ECount, end="\n")
print("At least one of the children is a girl, all are girls: ",
      Number_Of_Satisfactions, end="\n")
print("Total Probability is: ", Probability)
