#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    a: int = 10
    b: int = 5
    print(f"{a} + {b} = {calculator_1.add(a, b)}")
    print(f"{a} - {b} = {calculator_1.sub(a, b)}")
    print(f"{a} * {b} = {calculator_1.mul(a, b)}")
    print(f"{a} / {b} = {calculator_1.div(a, b)}")
