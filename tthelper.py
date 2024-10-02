from itertools import product
from sympy import symbols, And, Or, Equivalent, satisfiable


'''
Function to print single truth table from given
statements and variable names.
I didn't find this in SymPy library so I implemented it.💪
The solution is printed in bold green
'''
def get_truth_table(statements, variables):
    statement_dct = {
        stmt: f"{str(stmt).split(',', 1)[0].split('(')[1]}<->({str(stmt).split(',', 1)[1].strip(' )')})"
        for stmt in statements
    }
    variable_names = [str(var) for var in variables]

    padding = 5  # Padding for header
    # Calculate the maximum width for headers based on the longest variable name and statement
    header_items = variable_names + list(statement_dct.values())
    header_widths = [len(item) + padding for item in header_items]
    
    # Accumulate the output in a list
    output = []
    
    # Print the header
    header = ' '.join(f"{var:<{header_widths[i]}}" for i, var in enumerate(variable_names))
    header += ' '.join(statement_dct[stmt].ljust(header_widths[len(variable_names) + i]) 
                       for i, stmt in enumerate(statement_dct))
    
    output.append(header)
    output.append("-" * sum(header_widths))
    
    # Update the header widths for the results
    result_widths = create_centered_padding([len(item) for item in header_items], padding)
    # Makes 2^n rows of truth table for n variables
    for values in product([False, True], repeat=len(variables)):
        # Evaluate each statement for the current combination of variable values
        results = [bool(stmt.subs(dict(zip(variables, values)))) 
                   for stmt in statement_dct.keys()]
        if all(results):
            output.append('<span class="green">' +
                        ' '.join(f"{'T' if val else 'F':<{width}}" 
                       for val, width in zip(values + tuple(results), result_widths))
                       + '</span>'
                       )
        else:
            output.append(' '.join(f"{'T' if val else 'F':<{width}}" 
                       for val, width in zip(values + tuple(results), result_widths)))
    return '\n'.join(output) 

# More simple functions to handle formatting      
def print_bold(text):
    print(f"\033[1m{text}\033[0m")

def print_bold_underline(text):
    print(f"\033[1m\033[4m{text}\033[0m")

def print_bold_green(text):
    print(f"\033[1m\033[32m{text}\033[0m")

def create_centered_padding(input_list, padding):
    # This logic can be handled elsewhere too
    # but I am keeping it here to keep it simple
    input_list.pop(0)    # Remove the front (rotate left)
    input_list.append(1) # Add 1 padding to the end (just to print)
    result = []
    for i in range(len(input_list)):
        if input_list[i] == 1: result.append(padding + 1)
        else:
            left_half  = input_list[i-1] // 2 if i > 0 and input_list[i-1] != 1 else 0
            right_half = input_list[i] // 2
            result.append(left_half + padding + right_half)
    return result


def get_solution(statements, check=False):
    dct = satisfiable(And(*statements), all_models=False)
    if dct is False: return False
    elif check:      return True
    else:
        _mpp = {False: "Knave", True: "Knight"}
        result = "\n".join(f"{k} &rarr; {_mpp[v]}" 
                    for k, v in sorted(dct.items(), 
                                        key=lambda item: str(item[0])))
        return result