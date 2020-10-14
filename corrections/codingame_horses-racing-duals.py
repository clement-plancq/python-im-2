import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# https://www.codingame.com/training/easy/horse-racing-duals

puissances = list()

n = int(input())
for i in range(n):
    puissances.append(int(input()))
    
puissances.sort(reverse=True)

min = 100
for i in range(n-1):
    diff = puissances[i] - puissances[i+1]
    if diff < min:
        min = diff

print(min)