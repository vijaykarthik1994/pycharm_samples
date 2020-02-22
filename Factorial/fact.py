def CalcFact(n):
    if type(n) == int and n > 0:
        return n * CalcFact(n-1)
    else:
        return 1


if __name__ == "__main__":
    try:
        print("Calculating factorial")
        ValToCalCFact = input("Enter a value to which factorial is to be calculated")
        print("The Factorial is {}".format(CalcFact(int(ValToCalCFact))))
    except ArithmeticError:
        print("Invalid input3")




