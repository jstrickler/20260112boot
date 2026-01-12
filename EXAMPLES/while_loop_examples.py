print("Welcome to ticket sales\n")

# not used in python
i = 0
while i < 3:
    print(i)
    i += 1


while True:  # Loop "forever"
    raw_quantity = input("Enter quantity to purchase (or q to quit): ")
    if raw_quantity == '':
        print("please enter # of tickets")
        continue  # Skip rest of loop; start back at top
    if raw_quantity.lower() == 'q':
        print("goodbye!")
        break  # Exit loop

    quantity = int(raw_quantity)  # could validate via try/except
    print(f"sending {quantity} ticket(s)")
