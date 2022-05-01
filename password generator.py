import random

uppercase_letters = "ABCDEFGHIKJLMNOP"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},;/||?#="

upper, lower, nums, syms = True, False, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if syms:
    all += symbols
if nums:
    all += digits

length = 20
amount = 10

for x in range(amount):
    password = "",join(random.sample(all, length))

print(password)
