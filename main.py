from sympy import symbols, And, Or, Not, Equivalent, simplify, satisfiable
from sympy.logic.boolalg import truth_table
from itertools import product


def print_bold(text):
    print(f"\033[1m{text}\033[0m")

def print_bold_underline(text):
    print(f"\033[1m\033[4m{text}\033[0m")

def print_bold_green(text):
    print(f"\033[1m\033[32m{text}\033[0m")

'''
Function to print single truth table from given
statements and variable names.
I didn't find this in SymPy library so I implemented it.💪
The solution is printed in bold green
'''
def print_truth_table(statements, variable_names):
    statement_dct = {
        stmt: f"{str(stmt).split(',', 1)[0].split('(')[1]}<->({str(stmt).split(',', 1)[1].strip(' )')})"
        for stmt in statements
    }
    variables = symbols(variable_names)  # Create symbols
    padding = 5 # Padding for header
    # Calculate the maximum width for headers based on the longest variable name and statement
    header_items = variable_names + list(statement_dct.values())
    header_widths = [len(item) + padding for item in header_items]
    # Print the header
    header = ' '.join(f"{var:<{header_widths[i]}}" for i, var in enumerate(variable_names))
    header += ' ' + ' '.join(f"{variable_names[i]}<->({statement_dct[stmt]})".ljust(header_widths[len(variable_names) + i]) 
                             for i, stmt in enumerate(statement_dct))
    print_bold_underline(header)
    # Update the header widths for the results
    header_widths.pop(0) # To make it shift left
    header_widths.append(1) # padding of 1 for last column (just to print it)

    # Makes 2^n rows of truth table for n variables
    for values in product([False, True], repeat=len(variables)):
        # Evaluate each statement for the current combination of variable values
        results = [bool(stmt.subs(dict(zip(variables, values)))) 
                   for stmt in statement_dct.keys()]
        if all(results):
            print_bold_green(' '.join(f"{'T' if val else 'F':<{width}}" 
                       for val, width in zip(values+tuple(results), header_widths)))
        else:
            print(' '.join(f"{'T' if val else 'F':<{width}}" 
                       for val, width in zip(values+tuple(results), header_widths)))

A, B, C = symbols('A B C')
statements = [
    Equivalent(A, And(A, Not(B))),  
    Equivalent(B, Or(A, C)),         
    Equivalent(C, Not(A))            
]
print_truth_table(statements, ['A', 'B', 'C'])
print(satisfiable(And(*statements), all_models=False))

'''
Two entities, A and B, are on an island. 
A is a knight, who always tells the truth, 
and B is a knave, who always lies.

A says, "B is a knave." A -> ~B
B says, "We are both knights." B -> A ^ B
'''

# Statement : (Propositional Logic, Answer(Is A a knight or knave))
dct = {
    "A says A is knave": ("PARADOX", "No soln"),
    "A says A is knight": ("A → A", "AMBIGUOUS: If A is knight, statement is true. If A is knave, statement is false"),
    "A says B is knave": ("A → ¬B", "AMBIGUOUS: IF A is knight, B is knave. If A is knave B is knight"),
    "A says B is knight": ("A → B", "AMBIGUOUS: IF A is knight, B is knight. If A is knave B is knave"),
    "A says they are both knaves": ("A → (¬A ∧ ¬B)", "A is knave and B is knight"),
    "A says they are both knights": ("A → (A ∧ B)", "AMBIGUOUS: IF A is knight, B is knight. If A is knave B is knave"),
}