from sympy import symbols, And, Equivalent, satisfiable
from helper import print_truth_table
from pprint import pprint 
from test import statements, symbols_list


print(symbols_list)
pprint(statements)
print_truth_table(statements, symbols_list)

dct = satisfiable(And(*statements), all_models=False)
_mpp = {False: "Knave", True: "Knight"}

if dct is False:
    print("No solution")
else:
    mapped = {str(k): _mpp[v] for k, v in dct.items()}
    print()
    print(mapped)


# Statement : (Propositional Logic, Answer(Is A a knight or knave))
dct = {
    "A says A is knave": ("PARADOX", "No soln"),
    "A says A is knight": ("A → A", "AMBIGUOUS: If A is knight, statement is true. If A is knave, statement is false"),
    "A says B is knave": ("A → ¬B", "AMBIGUOUS: IF A is knight, B is knave. If A is knave B is knight"),
    "A says B is knight": ("A → B", "AMBIGUOUS: IF A is knight, B is knight. If A is knave B is knave"),
    "A says they are both knaves": ("A → (¬A ∧ ¬B)", "A is knave and B is knight"),
    "A says they are both knights": ("A → (A ∧ B)", "AMBIGUOUS: IF A is knight, B is knight. If A is knave B is knave"),
}