class atm():
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
    
    def cashWithDrawl(self):
        print("Money has been successfully withdrawled")
    
    def balanceEnquiry(self):
        print("You have enough balance")
    
    def cashDeposit(self):
        print("Your cash has been safely deposited")

sbi_bank = atm('4535826747', '3562')

print(sbi_bank.cashWithDrawl())
print(sbi_bank.balanceEnquiry())
print(sbi_bank.cashDeposit())
print("Card Number:", sbi_bank.card_number)
print("Pin Number:", sbi_bank.pin_number)