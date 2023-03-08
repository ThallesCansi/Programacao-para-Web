def verify():
    x = 'This is a simple test :)'
    print(x)

verify()

try:
    print(x) # type: ignore
except:
    print('It seems that the variable is not accessible outside its scope :(')