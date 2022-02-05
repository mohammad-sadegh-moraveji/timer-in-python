# We will use the time module
import time
 
# Create a function that will print the time
def create_countdown_timer(time):
    print(time,"......")
 
time_in_sec=int(input("Please entert the time in seconds:"))
 
for times in range(time_in_sec):
    # call the function and pass the current time left
    create_countdown_timer(time_in_sec-times)
    # call the function in every 1 second.
    time.sleep(1)
     
print("In the finish")