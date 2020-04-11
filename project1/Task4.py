"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoing_calls = set()
incoming_calls = set()

outgoing_texts = set()
incoming_texts = set()

telemarketers = set()


def find_telemarketers():
    for call in calls:
        outgoing_calls.add(call[0])
        incoming_calls.add(call[1])

    for text in texts:
        outgoing_texts.add(text[0])
        incoming_texts.add(text[1])

    print("These numbers could be telemarketers:")

    for phone_number in sorted(outgoing_calls):
        if (phone_number not in incoming_calls) and (phone_number not in outgoing_texts) and (phone_number not in incoming_texts):
            print(phone_number)


find_telemarketers()
