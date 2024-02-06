                                # Break statement
for i in range(12):
    if i == 10:
        break #It means to skip over a part of a code and break statement terminates the loop
    print("5 *", i, "=", 5 * i)

print("Loop is Break")

                                # Continue statement
for i in range(12):
    if i == 10:
        print("Skip the iteration")
        continue #It can skip the iteration
    print("5 *", i, "=", 5 * i)

                                # Using Do While loop
i = 0
while True:
    print(i)
    i += 1
    if i%100 == 0:
        break
