# This program show basic addition and subtraction

# This program takes argument in list format 
# Items inside the list must be a string
# e.g. ["1 + 2", "5 - 3", "4 + 6"]

def arithmetic_arranger(num):
    top = []
    signs = []
    bottom = []

    for num1 in num:
        nums = num1.split()
        top.append(nums[0])
        signs.append(nums[1])
        bottom.append(nums[2])

    # It shows error if:    
    # items in list are more than 5
    # operation is other than addition and subtraction
    # length of values must be smaller than 4
    # arithmetic operation performed on other than integer
    
    if len(top) > 5:
        print("Error: Too many problems.")
        exit()

    for i in range(len(top)):

        if signs[i] not in ["+", "-"]:
            print(" Error: Operator must be '+' or '-'.")
            exit()

        if len(top[i]) > 4 or len(bottom[i]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            exit()

        try:
            int(top[i]), int(bottom[i])
        except ValueError:
            print("Error: Numbers must only contain digits.")
            exit()

    for i in range(len(top)):
        space_between = max(len(top[i]), len(bottom[i])) + 2
        print(f"{(top[i]):>{space_between}}", end="    ")
    print()

    for i in range(len(top)):
        space_between = max(len(top[i]), len(bottom[i])) + 1 - len(bottom[i])
        text = signs[i] + space_between * " " + bottom[i]
        print(f"{text}", end="    ")
    print()

    for i in range(len(top)):
        print("_" * (max(len(top[i]), len(bottom[i])) + 2), end="    ")
    print()

    for i in range(len(top)):
        space_between = max(len(top[i]), len(bottom[i])) + 2
        if signs[i] == "+":
            print(f"{int(top[i]) + int(bottom[i]):>{space_between}}", end="    ")
        else:
            print(f"{int(top[i]) - int(bottom[i]):>{space_between}}", end="    ")
