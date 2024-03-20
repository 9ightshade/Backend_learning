def count_down(start, end):
    for i in range(start, end, -1):
        print(i)


def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end, -1):
        total += i
        return total


# Don't edit below this line


def test(start, end):
    print(f"Printing numbers from {start} to {end + 1}:")
    print(f"total: {sum_of_numbers(start, end)}")
    print("=====================================")


def main():
    test(10, 0)
    test(20, 10)
    test(15, 11)


main()

