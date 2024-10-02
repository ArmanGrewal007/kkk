from sympy import Symbol, Not, Or, And
from pprint import pprint

def parse_expression(expr):
    if isinstance(expr, Symbol):
        return f"{expr} is a knight"
    elif isinstance(expr, Not):
        return f"{expr.args[0]} is a knave"
    elif isinstance(expr, Or):
        return " or ".join(parse_expression(arg) for arg in expr.args)
    elif isinstance(expr, And):
        return " and ".join(parse_expression(arg) for arg in expr.args)

def parse_equivalent(statements, test=False):
    out = []
    for equiv in statements:
        antecedent, consequent = equiv.args
        out.append(f"{antecedent} says &rarr; {parse_expression(consequent)}")
    if test: pprint(out)
    return out

