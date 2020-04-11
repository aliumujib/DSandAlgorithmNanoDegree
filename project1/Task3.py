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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

BANGALORE_CODE = '080'


def is_telemarketer_number(number):
    return not is_fixed_line(number) and not is_mobile_number(number)


def is_mobile_number(number):
    return ' ' in number and (number[0] == '7' or number[0] == '8' or number[0] == '9')


def is_fixed_line(number):
    return '(' in number and ')' in number


def extract_mobile_prefix(number):
    return number[0:4]


def extract_area_code(number):
    return number.partition(')')[0].partition('(')[2]


def find_part_to_extract(number):
    if(is_telemarketer_number(number)):
        return number[0:3]
    elif(is_fixed_line(number)):
        return extract_area_code(number)
    elif(is_mobile_number(number)):
        return extract_mobile_prefix(number)


def find_recipient_area_codes():
    list_of_codes_prefixes = set()
    for call in calls:
        if(extract_area_code(call[0]) == BANGALORE_CODE):
            code_prefix = find_part_to_extract(call[1])
            list_of_codes_prefixes.add(code_prefix)

    print("The numbers called by people in Bangalore have codes:")
    for item in sorted(list_of_codes_prefixes):
        print(item)


def find_percentage_from_bangalore_to_fixed_bangalore():
    number_of_fixed_from_banglore = 0
    number_of_fixed_to_banglore = 0
    for call in calls:
        if(extract_area_code(call[0]) == BANGALORE_CODE):
            number_of_fixed_from_banglore = number_of_fixed_from_banglore + 1
            if(extract_area_code(call[1]) == BANGALORE_CODE):
                number_of_fixed_to_banglore = number_of_fixed_to_banglore + 1

    percentage = (number_of_fixed_to_banglore/float(number_of_fixed_from_banglore)) * 100
    print("{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))


def test_util_procedures():
    assert extract_area_code("(04344)228249") == "04344"
    assert extract_area_code("(080)65647085") == "080"
    assert extract_area_code("(080)29483476") == "080"
    assert extract_area_code("(022)21884607") == "022"


test_util_procedures()

find_recipient_area_codes()
find_percentage_from_bangalore_to_fixed_bangalore()
