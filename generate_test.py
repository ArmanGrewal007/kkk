import random
from sympy import symbols, Equivalent
from sympy.logic.boolalg import Or, And, Not

# Wrapper to generate statements
def generate(num_symbols=2):
    symbol_str = " ".join([chr(ord('A') + i) for i in range(num_symbols)])
    symbols_list = symbols(symbol_str)
    statements = []
    for sym in symbols_list:
        while True:
            statement = random_statement(symbols_list)
            equiv_statement = Equivalent(sym, statement)
            # Ensure the statement is not trivially True or False
            if not (equiv_statement == True or equiv_statement == False):
                statements.append(equiv_statement)
                break
    return symbols_list, statements

'''
RANDOM STATEMENT GENERATOR
1. Randomly choose an operator (OR, AND).
2. Randomly chooses number of symbols to use.
3. Randomly choose the symbols.
4. Randomly negate each chosen symbol
'''
def random_statement(symbols):
    op_type = random.choice(['or', 'and'])
    num_operands = random.randint(1, len(symbols))
    chosen_symbols = random.sample(symbols, num_operands)
    negated_symbols = [
        Not(sym) if random.choice([True, False]) 
                else sym for sym in chosen_symbols
    ]
    if op_type == 'or':
        return Or(*negated_symbols)
    elif op_type == 'and':
        return And(*negated_symbols)
