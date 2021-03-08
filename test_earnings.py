from earnings import calculate_yearly_income
from earnings_with_vacation_money import calculate_yearly_income_with_vacation_money


# Test cases for calculate_yearly_earning
def test_calculate_positive_input():
    assert calculate_yearly_income(1) == 12


# Test cases for calculate_yearly_income_with_vacation_money
def test_calculate_vacation_positive_input():
    assert calculate_yearly_income_with_vacation_money(12) == 12.96
