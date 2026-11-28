from fastapi import FastAPI

app = FastAPI()

PRICES ={
    "Chai": 120,
    "Coffee": 150,
    "Paratha": 160
}

@app.get("/prices/{item}")
def price(item: str):
    return {
        "Hello"
        }
 


@app.get("/greet")
def greet(name:str = "friend", loud: bool = False):
    """Greet somebody by name."""
 
    message = f"Welcome, {name}"
 
    if loud:
        message = message.upper()
 
    return {"message": message}

