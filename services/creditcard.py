from schemas.creditcard import CreditCard

class CreditCardService:
    temp_credit_card_store = []
    @classmethod
    def create_credit_card(self, credit_card: CreditCard):
        self.temp_credit_card_store.append(credit_card)
        return {"message": "Credit card created successfully"}
    
    @classmethod
    def get_all_credit_card(self):
        return self.temp_credit_card_store
