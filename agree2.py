from cs50 import get_string

s = get_string("Do you agree? ")

if s in ["y", "yes"]:
    print(s)
    print("agreed")
if s in ["n", "no"]:
    print(s)
    print("not agreed")
print(s)
