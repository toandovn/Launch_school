import json
with open('Morgage_loan_message.json', 'r') as file:
    Message = json.load(file)
def prompt(message):
    print(f"=> {message}")
def call_money(money):
    dollar = int(money)
    cents = round((money - dollar),2) * 100
    return f"${dollar} and {cents} cents"
def mortgage_calculator():
    prompt(Message['loan amount'])
    loan_amount = float(input())
    prompt(Message['loan interest'])
    loan_apr = float(input())
    prompt(Message["loan duration"])
    loan_duration = float(input())
    monthly_interest_rate = loan_apr / 1200
    loan_duration_in_month = loan_duration * 12
    monthly_payment = loan_amount * (monthly_interest_rate / (1 -(1 + monthly_interest_rate)**(-(loan_duration_in_month))))
    prompt(f"{Message['monthly payment']}${round(monthly_payment,2)}({call_money(monthly_payment)})")
mortgage_calculator()
