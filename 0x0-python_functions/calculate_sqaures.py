def calculate_squares(start, end):
    for i in range(start, end):
        Square = i * i
        print(f"{i} squared = {Square}")



def test(start, end):
    print(f"Calculating squares from {start} to {end - 1}:")
    calculate_squares(start, end)
    print("=====================================")


def main():
    test(100, 105)
    test(1, 3)
    test(11, 14)


main()
    
