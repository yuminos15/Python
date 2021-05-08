def push(stack, data, max_length):
    if len(stack) < max_length:
        stack.append(data)
        print(stack)
    else:
        print("overflow")

    return stack


def pop(stack):
    if 0 < len(stack):
        del stack[-1]
        print(stack)
    else:
        print("underflow")
    return stack


max_length = 3
stack = []

while True:

    que = input("Enter push or pop :")

    if que == "push":
        data = int(input("Enter your number :"))
        stack = push(stack, data, max_length)

    if que == "pop":
        stack = pop(stack)
