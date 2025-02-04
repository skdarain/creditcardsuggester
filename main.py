from fastapi import FastAPI
from endpoint.creditcard import credit_card_router

app = FastAPI()

app.include_router(credit_card_router)

@app.get("/")
def test():
    return ["Test"]
