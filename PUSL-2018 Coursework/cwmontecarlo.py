# importing libraries
import random

def montecarlo(n):
    range1 = 0
    range2 = 0
    range3 = 0
    total = []

    for x in range(n):
        #list store durations for each activity
        #list total duration
        # assigning values for activities in A,B,C
        a = random.randint(8, 12)
        b = random.randint(10, 14)
        c = random.randint(12, 16)

        # calculating the duration of completion
        duration_of_completion = a + b + c
        total.append(duration_of_completion)

        # checking which range the duration of completion falls to
        if duration_of_completion in range(30, 36):
            range1 += 1

        elif duration_of_completion in range(36, 39):
            range2 += 1

        elif duration_of_completion in range(39, 42):
            range3 += 1

    #calculating the probability for each range
    range1 = (range1 / n) * 100
    range2 = (range2 / n) * 100
    range3 = (range3 / n) * 100
    return (print("\n30-35 = {}%  \n36-38 = {}%  \n39-42 = {}%  \n\nDates that were being generated = {}".format(range1, range2, range3, total)))

# getting the input from the user
iterative_no = int(input("\nEnter the number of iterations that you want : "))
montecarlo(iterative_no)
