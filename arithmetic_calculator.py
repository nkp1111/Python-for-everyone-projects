# This program show basic addition and subtraction

# This program takes argument in list format 
# Items inside the list must be a string
# e.g. ["1 + 2", "5 - 3", "4 + 6"]

def arithmetic_arranger(problems, answer=False):
    num = len(problems)
    problem_set = []

    if num > 5:
        return "Error: Too many problems."

    for i in range(len(problems)):
        element = problems[i].split()
        problem_set.append(element)

    for i in range(num):
        if problem_set[i][1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if len(problem_set[i][0]) > 4 or len(problem_set[i][2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        try:
            if int(problem_set[i][0]) and int(problem_set[i][2]):
                continue
        except ValueError:
            return "Error: Numbers must only contain digits."

    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    area_between_problem = "    "

    for i in range(num):
        max_len = max(len(problem_set[i][0]), len(problem_set[i][2]))
        space_cover = max_len + 2
        first_line += f"{problem_set[i][0]:>{space_cover}}" + area_between_problem
        space_between = max_len + 1 - len(problem_set[i][2])
        second_line += problem_set[i][1] + " " * space_between + problem_set[i][2] + area_between_problem
        third_line += "-" * (max_len + 2) + area_between_problem

        if problem_set[i][1] == "+":
            fourth_line += f"{int(problem_set[i][0]) + int(problem_set[i][2]):>{space_cover}}" + area_between_problem
        else:
            fourth_line += f"{int(problem_set[i][0]) - int(problem_set[i][2]):>{space_cover}}" + area_between_problem

    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + third_line.rstrip()
    if answer is not False:
        arranged_problems += "\n" + fourth_line.rstrip()

    return arranged_problems
