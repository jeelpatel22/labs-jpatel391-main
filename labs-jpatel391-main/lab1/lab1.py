# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Jeelkumar Vinodkumar Patel
# Student Number:115766222
#

def wins_rock_scissors_paper(player_throw, opponent_throw):
    player_throw = player_throw.lower()
    opponent_throw = opponent_throw.lower()
    
    if player_throw == opponent_throw:
        return False
    
    if (player_throw == 'rock' and opponent_throw == 'scissors') or \
       (player_throw == 'paper' and opponent_throw == 'rock') or \
       (player_throw == 'scissors' and opponent_throw == 'paper'):
        return True
    
    return False

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def sum_to_goal(numbers, goal):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == goal:
                return numbers[i] * numbers[j]
    return 0

class UpCounter:
    def __init__(self, step_size=1):
        self.step_size = step_size
        self.count_value = 0
    
    def count(self):
        return self.count_value
    
    def update(self):
        self.count_value += self.step_size

class DownCounter(UpCounter):
    def update(self):
        self.count_value -= self.step_size