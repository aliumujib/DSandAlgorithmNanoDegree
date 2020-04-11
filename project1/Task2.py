import operator

"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import os

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

"""
INPUTS:
OUTPUTS:
ALGORITHM:
"""


list_of_phones = {}


def init_data_holders():
    for call in calls:
        list_of_phones[call[0]] = 0
        list_of_phones[call[1]] = 0


def print_most_talkative_phone_number():
    for call in calls:
        list_of_phones[call[0]] = list_of_phones[call[0]] + int(call[3])
        list_of_phones[call[1]] = list_of_phones[call[0]] + int(call[3])

    max_time_phone_pair = max(list_of_phones.iteritems(), key=operator.itemgetter(1))
    max_time = max_time_phone_pair[1]
    max_phone = max_time_phone_pair[0]

    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_phone, max_time))


init_data_holders()
print_most_talkative_phone_number()
