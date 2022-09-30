class TooManyProblems(Exception):
    pass

def arithmetic_arranger(problems, ans=False):

    try:
        if len(problems) > 5:
            raise TooManyProblems
    except TooManyProblems:
        return ("Error: Too many problems.")

    arranged_problems = "Solution to come"
    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True));
