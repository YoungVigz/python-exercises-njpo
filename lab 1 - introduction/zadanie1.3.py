import random

draw_counter = 1000000

def draw_average(draw_counter):
    sum = 0
    for _ in range(draw_counter):
        sum += random.randint(1, 10)
    average = sum / draw_counter
    return average

average = draw_average(draw_counter)
print("Przybliżona wartość oczekiwana:", average)