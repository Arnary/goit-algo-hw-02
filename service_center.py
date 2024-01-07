from queue import Queue
import random
import time


queue = Queue()
request_id = 1
t = random.randint(1, 12)

def generate_request():
    global request_id
    queue.put(request_id)
    request_id += 1
    q = list(queue.queue)
    print(f"Queue of requests: {q}")

def process_request():
    if not queue.empty():
        req = queue.queue[0]
        queue.get(queue.queue[0])
        print(f"The request #{req} is being processed, please wait.")
        time.sleep(t)
        print("Waiting for request..")
    else:
        print("The queue is empty. Waiting for request..")

while True:
    try:
        generate_request()
        process_request()
        time.sleep(2)
    except KeyboardInterrupt:
        print("Oops! You interrupted the program.")
        break
