from fastapi import APIRouter, Depends
from schemas.creditcard import CreditCard
from services.creditcard import CreditCardService

credit_card_router = APIRouter()


@credit_card_router.post("/create_credit_card")
def create_credit_card(credit_card: CreditCard):
    return CreditCardService.create_credit_card(credit_card)


@credit_card_router.get("/get_all_credit_card")
def get_all_credit_card():
    return CreditCardService.get_all_credit_card()