lclvar = 10
def CheckScope():
    lclvar = 20
    print(lclvar)
print(lclvar)
CheckScope()
print(lclvar)