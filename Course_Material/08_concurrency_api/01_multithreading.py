"""
Topic: Multithreading
Section:  Concurrency and API
Description:
multithreading = Used to perform multiple tasks concurrently (multitasking)
                 Good for I/O bound tasks like reading files or fetching data from APIs
                 threading.Thread(target=my_function)
"""

import threading 
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking the {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")
    
        # module -> constructor
chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo")) # return object
chore2 = threading.Thread(target=take_out_trash)
chore3 = threading.Thread(target=get_mail)

chore1.start() # object method start to run the function
chore2.start()
chore3.start()

# if you want to wait for thread to complete in order to go to the next part you need "join method"
chore1.join()
chore2.join()
chore3.join()

print("All chores Completed")