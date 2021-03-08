def calculate_yearly_income(monthly_income):
    """ This function takes a positive number as input
    and returns yearly earnings, else error message """

    if monthly_income >= 0:
        yearly_income = monthly_income * 12
        return yearly_income

    else:
        return "Monthly income cannot negative"




