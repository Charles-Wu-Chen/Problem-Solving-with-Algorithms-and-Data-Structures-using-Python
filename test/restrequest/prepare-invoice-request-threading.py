import requests
import json

import threading
import time

url = 'http://localhost:8090/invoice-prepare-to-send-service/invoice/batch-invoices'

head = {'Content-type': "application/json"}

empObj = {'customerNumber': 75975,
          'invoiceNumbers': [12345]}
payload = json.dumps(empObj)

resp = requests.post(url, headers=head, data=payload)

print(resp)

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)


def print_time(threadname, delay, counter):
    while counter:
        if exitFlag:
            threadname.exit()
        time.sleep(delay)
        print("%s: %s" % (threadname, time.ctime(time.time())))
        counter -= 1


# Create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exiting Main Thread")
