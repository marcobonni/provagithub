from cs50 import get_int


def main():
    times = get_int("how many times? ")
    meow(times)


def meow(n):
    for i in range(n):
        print("meow")


main()
