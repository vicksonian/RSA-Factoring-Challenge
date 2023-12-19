import sys


def factorize(n):
    i = 2
    while i <= n:
        if n % i == 0:
            print(f"{n}={i}*{n//i}")
            n //= i
        else:
            i += 1


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)

    with open(sys.argv[1], "r") as file:
        for line in file:
            number = int(line.strip())
            factorize(number)

    if __name__ == "__main__":
        main()
