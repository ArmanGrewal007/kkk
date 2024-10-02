function updateSliderValue() {
    const slider = document.getElementById("num-symbols");
    document.getElementById("slider-value").innerText = slider.value;
}

function generatePuzzle() {
    const numSymbols = document.getElementById("num-symbols").value;
    fetch(`https://kkk-8t4m.onrender.com/generate_puzzle?num_symbols=${numSymbols}`)
    // fetch(`http://localhost:8000/generate_puzzle?num_symbols=${numSymbols}`)
        .then(response => response.json())
        .then(data => {
            if (data.statements && Array.isArray(data.statements)) {
                document.getElementById("puzzle-content").innerHTML = 
                    `<br>${data.statements.join("<br>")}`;
            } else {
                document.getElementById("puzzle-content").innerHTML = 
                    `<strong>Error:</strong> Statements data is not available or is not an array.`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById("puzzle-content").innerHTML = 
                `<strong>Error:</strong> Could not fetch the puzzle. Make sure the server is running.`;
        });
}

function showSolution() {
    fetch('https://kkk-8t4m.onrender.com/solution')
        .then(response => response.json())
        .then(data => {
            const soln = data.solution;
            const formattedSoln = soln.replace(/\n/g, '<br>').replace(/"/g, '');
            document.getElementById("solution-content").innerHTML = 
                `<br> ${formattedSoln}`;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById("solution-content").innerHTML = 
                `<strong>Error:</strong> Could not fetch the solution. Make sure the server is running.`;
        });
}

function showTruthTable() {
    // Assuming an endpoint like /truth_table which provides the truth table
    fetch('https://kkk-8t4m.onrender.com/truth_table')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            const truthTableString = data.truth_table; 
            const formattedTable = truthTableString.replace(/\n/g, '<br>').replace(/"/g, '');
            document.getElementById("truth-table-content").innerHTML = 
                `<br> <pre>${formattedTable}</pre>`;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById("truth-table-content").innerHTML = 
                `<strong>Error:</strong> Could not fetch the truth table. Make sure the server is running.`;
        });
}
