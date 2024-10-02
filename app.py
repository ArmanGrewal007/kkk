from sympy import symbols, And, Or, Equivalent, satisfiable
from generate_test import generate
from pl_to_nl import parse_equivalent
from tthelper import get_truth_table, get_solution
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

symbols_list, statements = [], []

@app.get("/generate_puzzle")
def get(num_symbols: int):
    global symbols_list, statements
    # Recrusively generate statements, until we get a valid solution
    while True:
        symbols_list, statements = generate(num_symbols)
        if get_solution(statements):
            return {"statements": parse_equivalent(statements)}

@app.get("/solution")
def get():
    global statements    
    dct = get_solution(statements)
    if dct is False:
        return {"solution": "No solution"}
    else:
        return {"solution": dct}

@app.get("/truth_table")
def get():
    global symbols_list, statements
    truth_table = get_truth_table(statements, symbols_list)
    return {"truth_table": truth_table}


if __name__ == "__main__":
    import uvicorn, os
    uvicorn.run("app:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=True)