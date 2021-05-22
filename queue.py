def enqueue(queue, data, max_length):
    if len(queue) < max_length:
        queue.append(data)
        print(queue)
    else:
        print("overflow")

    return queue

def dequeue(queue):
    if 0 < len(queue):
        del queue[0]
        print(queue)
    else:
        print("underflow")
    return queue


max_length = 3

queue = []

while True:

    que = input("Enter dequeue or enqueue : ")

    if que == "enqueue":
        data = int(input("Enter the number : "))
        queue = enqueue(queue, data, max_length)
    elif que == "dequeue":
        queue = dequeue(queue)

