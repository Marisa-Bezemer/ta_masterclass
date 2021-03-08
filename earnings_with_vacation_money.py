def calculate_yearly_income_with_vacation_money(yearly_income):
    """This function takes a yearly income as input and returns
    yearly income plus vacation interest"""

    if yearly_income >= 0:
        interest = yearly_income * 0.08
        return interest + yearly_income

    else:
        return "Yearly income cannot be negative"

