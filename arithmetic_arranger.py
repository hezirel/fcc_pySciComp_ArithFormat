class Err(Exception):
    pass
class TooManyProblems(Err):
    pass
class TooManyDigits(Err):
    pass
class InvalidOperator(Err):
    pass
class Numbers(Err):
    pass
    

class Problem():
    def __init__(self, problem):
        self.problem = problem
        self.num1 = problem.split()[0]
        self.num2 = problem.split()[2]
        self.result = str(eval(problem))
        self.padding = max(len(self.num1), len(self.num2))
        self.vert1 = self.num1.rjust(2 + self.padding)
        self.vert2 = self.problem.split()[1] + self.num2.rjust(1 + self.padding)
        self.vert3 = '-' * (2 + self.padding)
        self.vert4 = self.result.rjust(2 + self.padding)

class ProblemsList():
    def __init__(self, list, ans):
        self.blackboard = []
        self.ans = ans
        for elt in list:
            self.blackboard.append(Problem(elt))

    def __repr__(self):
        buffer = ''
        pad = lambda: self.blackboard.index(elt) < len(self.blackboard) - 1

        for elt in self.blackboard:
            buffer += elt.vert1 + '    ' if pad() else elt.vert1
        buffer += '\n'
        for elt in self.blackboard:
            buffer += elt.vert2 + '    ' if pad() else elt.vert2
        buffer += '\n'
        for elt in self.blackboard:
            buffer += elt.vert3 + '    ' if pad() else elt.vert3

        if self.ans:
            buffer += '\n'
            for elt in self.blackboard:
                buffer += elt.vert4 + '    ' if pad() else elt.vert4
        return buffer


def arithmetic_arranger(problems, ans=False):
    try:
        if len(problems) > 5:
            raise TooManyProblems

        for i in problems:
            if len(i.split()[0]) > 4 or len(i.split()[2]) > 4:
                raise TooManyDigits
            if i.split()[1] not in ['+', '-']:
                raise InvalidOperator
            if not i.split()[0].isdigit() or not i.split()[2].isdigit():
                raise Numbers

    except TooManyProblems:
        return ("Error: Too many problems.")
    except InvalidOperator:
        return ("Error: Operator must be '+' or '-'.")
    except Numbers:
        return ("Error: Numbers must only contain digits.")
    except TooManyDigits:
        return ("Error: Numbers cannot be more than four digits.")
    except BaseException:
        return ("Error: Unknown error.")

    return str(ProblemsList(problems, ans))

print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'], True))
