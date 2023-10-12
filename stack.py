# Create an empty stack
stack = []

# Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

# Pop elements from the stack
while stack:
    item = stack.pop()
    print("Popped:", item)
