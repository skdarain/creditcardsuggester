from pydantic import BaseModel

class CreditCard(BaseModel):
    bank_name: str
    card_name: str
    charges: float