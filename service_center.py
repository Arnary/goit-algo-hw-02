from queue import Queue
import random
import time


queue = Queue()
t = random.randint(1, 12)

def generate_request():
    request_num = random.randint(1, 3)
    for _ in range(request_num):
        request_id = random.randint(1, 1000)
        if request_id not in queue.queue:
            queue.put(request_id)
        else:
            generate_request()
    q = list(queue.queue)
    print(f"Queue of requests: {q}")

def process_request():
    if not queue.empty():
        req = queue.queue[0]
        queue.get(queue.queue[0])
        print(f"The request #{req} is being processed, please wait.")
        time.sleep(t)
        print(f"The request #{queue.queue[0]} is next.") if not queue.empty() else print("Waiting for request..")
    else:
        print("The queue is empty. Waiting for request..")

while True:
    generate_request()
    process_request()
    time.sleep(2)
