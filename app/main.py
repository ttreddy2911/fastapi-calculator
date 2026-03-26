from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from app.operations import add, subtract, multiply, divide
from app.logger import logger

app = FastAPI(title="Dynamic FastAPI Calculator")


#  Home
@app.get("/")
def home():
    return {"message": "Dynamic FastAPI Calculator Running"}


#  API ENDPOINTS

@app.get("/add")
def add_numbers(a: float, b: float):
    result = add(a, b)
    logger.info(f"ADD: {a} + {b} = {result}")
    return {"result": result}


@app.get("/subtract")
def subtract_numbers(a: float, b: float):
    result = subtract(a, b)
    logger.info(f"SUBTRACT: {a} - {b} = {result}")
    return {"result": result}


@app.get("/multiply")
def multiply_numbers(a: float, b: float):
    result = multiply(a, b)
    logger.info(f"MULTIPLY: {a} * {b} = {result}")
    return {"result": result}


@app.get("/divide")
def divide_numbers(a: float, b: float):
    try:
        result = divide(a, b)
        logger.info(f"DIVIDE: {a} / {b} = {result}")
        return {"result": result}
    except ValueError as e:
        logger.error("Divide by zero error")
        raise HTTPException(status_code=400, detail=str(e))


#  RESPONSIVE + PROFESSIONAL UI

@app.get("/calculator", response_class=HTMLResponse)
def calculator():
    return """
    <html>
    <head>
        <title>Dynamic Calculator</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>
            * {
                box-sizing: border-box;
                font-family: 'Segoe UI', sans-serif;
            }

            body {
                margin: 0;
                background: linear-gradient(135deg, #667eea, #764ba2);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .container {
                background: white;
                padding: 30px;
                border-radius: 15px;
                width: 90%;
                max-width: 400px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
                text-align: center;
            }

            h2 {
                margin-bottom: 20px;
                color: #333;
            }

            input {
                width: 100%;
                padding: 12px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 8px;
                font-size: 16px;
            }

            .buttons {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 10px;
                margin-top: 15px;
            }

            button {
                padding: 12px;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                cursor: pointer;
                background: #667eea;
                color: white;
                transition: 0.3s;
            }

            button:hover {
                background: #5a67d8;
            }

            #result {
                margin-top: 20px;
                font-size: 20px;
                font-weight: bold;
                color: green;
            }

            .error {
                color: red;
            }

            @media (max-width: 500px) {
                .container {
                    padding: 20px;
                }
            }
        </style>
    </head>

    <body>

        <div class="container">
            <h2>🧮 FastAPI Calculator</h2>

            <input type="number" id="a" placeholder="Enter first number">
            <input type="number" id="b" placeholder="Enter second number">

            <div class="buttons">
                <button onclick="calculate('add')">➕ Add</button>
                <button onclick="calculate('subtract')">➖ Subtract</button>
                <button onclick="calculate('multiply')">✖ Multiply</button>
                <button onclick="calculate('divide')">➗ Divide</button>
            </div>

            <div id="result"></div>
        </div>

        <script>
        async function calculate(operation) {
            let a = document.getElementById("a").value;
            let b = document.getElementById("b").value;
            let resultBox = document.getElementById("result");

            if (!a || !b) {
                resultBox.innerText = "⚠ Please enter both values";
                resultBox.className = "error";
                return;
            }

            let operationName = {
                "add": "Addition",
                "subtract": "Subtraction",
                "multiply": "Multiplication",
                "divide": "Division"
            };

            try {
                let response = await fetch(`/${operation}?a=${a}&b=${b}`);
                let data = await response.json();

                if (data.detail) {
                    resultBox.innerText = "❌ " + data.detail;
                    resultBox.className = "error";
                } else {
                    resultBox.innerText = "✅ " + operationName[operation] + " Result: " + data.result;
                    resultBox.className = "";
                }

            } catch (error) {
                resultBox.innerText = "❌ Server error";
                resultBox.className = "error";
            }
        }
        </script>

    </body>
    </html>
    """