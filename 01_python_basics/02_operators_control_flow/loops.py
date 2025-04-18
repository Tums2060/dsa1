# while
count = 1
while count < 5:
    print(count)
    count = count +1
    count += 1

# for loop or for each
names = ["a","b","c","d"]
for name in names:
    print(name)


# range

""" doc string
for i in range(11):
    print(i)
"""


#New code added by Tumaini Wekesa(189813)
rows = 5

for i in range(1, rows + 1):
    for space in range(rows - i):
        print(" ", end="")
    for star in range(2 * i - 1):
        print("*", end="")
    print()







