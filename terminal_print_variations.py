# Display Functions
import random  # for randomized replies etc
import sys
import time  # for pauses

####################
# Display Functions
####################

# in case easier to remember
def pause_seconds(seconds):
    time.sleep(seconds)
    pass


# making text print-out look like it is being typed
def slow_print(input_text):
    # staggered times
    random_times = [0.4]
    # stagger each character
    for i in input_text:
        time.sleep(random.choice(random_times))
        print(i, end="")
        # prints each time (before loop is finished)
        sys.stdout.flush()
    # end
    pass


# making text print-out look like it is being typed
def typed_print(input_text):
    # staggered times
    random_times = [
        0.03,
        0.04,
        0.04,
        0.05,
        0.05,
        0.05,
        0.06,
        0.07,
        0.07,
        0.08,
        0.08,
        0.08,
        0.1,
        0.3,
    ]
    # stagger each character
    for i in input_text:
        time.sleep(random.choice(random_times))
        print(i, end="")
        # prints each time (before loop is finished)
        sys.stdout.flush()
    # end
    pass


typed_print("I was thinking, but then decided not to... \n")
slow_print("LASER ON \n")
