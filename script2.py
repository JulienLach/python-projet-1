animals = ["lion", "elephant", "giraffe", "zebra", "monkey", "tiger", "panda"]


animals.append('unicorn')
# Use len() to get the length of the list
print(animals)
print(len(animals))

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")


i = 1

while i <= 4:
    print(i)
    # i += 1