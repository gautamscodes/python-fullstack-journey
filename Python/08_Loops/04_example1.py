scores = [2,45, 102, 4, 9, 12, 45, 90, 1,0, 1]
print(len(scores))

total = 0
# for score in scores:
#     total = total + score

total = sum(scores)
print(f"Total runs Scored is {total}")

# Find the Highest Score
highest = scores[0] # assume that the first value is highest.

for score in scores:
    if(highest < score):
        highest = score
print(f"Highest score is {highest}")

# Find the Lowest Score.
