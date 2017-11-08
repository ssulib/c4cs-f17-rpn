def add(a,b):
    return a + b
def subtract(a,b):
    return a - b

ops = {"+": add, "-": subtract}

def calculate(string):
    stack=list()
    for token in string.split():
        try:
            stack.append(int(token))
        except ValueError:
            arg2 = stack.pop()
            arg1 = stack.pop()
            function = ops[token]
            result = function(arg2,arg1)
            stack.append(result)

    return stack.pop()

def main():
    while True:
        calculate(input("rpn calc"))


if __name__ == "__main__":
    main()
