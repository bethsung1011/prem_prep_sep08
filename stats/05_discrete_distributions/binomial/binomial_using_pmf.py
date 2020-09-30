def factorial(n):
    prod = 1

    for num in range(1, n+1):
        prod *= num

    return prod

# print(factorial(5))

def combinations(n, k):
    return int(factorial(n) / (factorial(n - k) * factorial(k)))



'''
PMF: Probability Mass Function
- giving us the probability of a certain specific outcome.
- can answer the binomial question:
- 3 params:
    n : number of trials
    k : represents the number of successes
    p : is the probability of success of a single trial
'''

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * (1-p)**(n-k)

'''
"What is the probability in 12 coin flips of a fair coin, that you get 7 heads?"
'''
# print(binomial_pmf(12, 7, p=0.5)) # 0.193359375


'''
"You have 14 components in a circuit. At any given time, there is a 95% chance that a given component is functioning. What is the probability that 12 components are functioning? Assume that each component functions independently of every other."
'''
# print(binomial_pmf(14, 12, p=0.95)) # 0.1229


'''
You are sitting on a park bench watching geese walk by. There is a probability of 0.3 that any given goose will have feet that are more red than normal. What is the probability that in the next 20 geese you observe, 6 of them will have feet that are more red than usual?
'''
# print(binomial_pmf(20, 6, p=0.3))


'''
On any weekday morning, a certain bus route has 10 buses in operation. If the probability of any given bus arriving late at a stop is 15% (ha!), and assuming that buses arrive at a given stop independently of each other, what is the likelihood that 2 consecutive buses will arrive late at a given stop?
'''
# print(0.15**2)
# print(binomial_pmf(2, 2, p=0.15))

'''What is the likelihood that 2 in 12 buses will arrive late at a given stop?'''
# print(binomial_pmf(12, 2, p=0.15))


'''
There are 30 cars in a used car lot. At any given time, there's a 60% chance that each car is working as-is. What is the probability that the 10 cars the dealer sold today are working?
'''
# Given the constraints:
#   The sale of any given car is not dependent on the person starting the car
#   Time of day/year is irrelevant
# print(0.6**10)
# print(binomial_pmf(10, 10, p=0.60))


'''
you go to chipotle every Tuesday, there’s 14 workers at chipotle and 7 of them work on Tuesdays. whats the chances you’ll see the same worker at the counter 5 out of the next 10 times that you go, if only 3 of them work the counter at any given time?
'''
n = 10
k = 5
p = 3/7
# print(binomial_pmf(10, 5, p=(3/7)))


'''
In 30 vehicles, it is known that 2 of them will be motorcycles. Knowing this, in 40 vehicles, what is the probability 5 of them will be motorcycles?
'''
p = 2/30
n = 40
k = 5
# print(binomial_pmf(n, k, p))


'''
CDF:
'''