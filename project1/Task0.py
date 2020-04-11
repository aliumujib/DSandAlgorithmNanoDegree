"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import os

"""
In case python doesn't find the data files, try changing your CWD like below
print(os.getcwd())
os.chdir('/Users/aliumujib/Downloads/P0')
"""


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
first_incoming_phone_number = texts[0][0]
first_answering_phone_number = texts[0][1]
first_text_time = texts[0][2]

print("First record of texts, {} texts {} at time {}".format(
    first_incoming_phone_number, first_answering_phone_number, first_text_time))

last_index = len(calls) - 1
last_incoming_phone_number = calls[last_index][0]
last_answering_phone_number = calls[last_index][1]
last_call_time = calls[last_index][2]
last_call_duration = calls[last_index][3]
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
    last_incoming_phone_number, last_answering_phone_number, last_call_time, last_call_duration))
