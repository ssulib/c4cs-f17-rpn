import readline
from prettytable import PrettyTable

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b;

table = PrettyTable(["Equation","Result"])
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

ops = {"+": add, "-": subtract,"*": multiply,"/":divide}

def calculate(string):
    stack=list()
    if (len(string.split()) < 3) & (string != "end"):
        print(bcolors.WARNING + "Not valid expression" + bcolors.HEADER)
    for token in string.split():
        if token not in ops.keys():
            if token == "end":
                print(table)
                exit()
            try:
                stack.append(int(token))
            except ValueError:
                print(bcolors.WARNING + "Not valid symbol used" + bcolors.HEADER)
        else:
            if len(stack)<2:
                print(bcolors.WARNING + "Not valid expression" + bcolors.HEADER)
                return
            arg2 = stack.pop()
            arg1 = stack.pop()
            function = ops[token]
            result = function(arg2,arg1)
            table.add_row([str(arg2) +" "+ str(arg1) +" "+ token,str(result)])
            print(bcolors.OKGREEN + str(arg2) +" "+ str(arg1) +" "+ bcolors.OKBLUE + token +" "+ bcolors.OKGREEN+str(result) + bcolors.HEADER)
            stack.append(result)

    return stack.pop()

def main():
    print(bcolors.HEADER + "Staring RPN")
    while True:
        calculate(input("rpn calc "))


if __name__ == "__main__":
    main()
