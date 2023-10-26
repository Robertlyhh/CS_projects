import random
import time

OPERATORS = ["+","-","*"]
min_operand = 3
max_operand = 12
TOTAL_PROBLEMS = 10

def generate_problems():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    print(expr)
    return expr, answer

wrong = 0
input("press anything to start")
print("-----------------------")

start_time = time.time()


for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problems()
    while True:
        guess = input("problem #" + str(i + 1) + ":" + expr + "=")
        if guess == str(answer):
            break
        wrong+=1

end_time = time.time()
total_time = end_time - start_time
print("---------------")
print("nice work! you've finished in" , total_time , "seconds! with", wrong, "mistakes")



