from tax_calculator import TaxCalculator
import pytest

tc = TaxCalculator({
    10: '0-9700', 
    12: '9700-39475', 
    22: '39475-84200', 
    24: '84200-160725',
    32: '160725-204100', 
    35: '204100-510300',
    37: '510300-1e15'
})

def test_returns_result_keys():
    res = tc.run(140000)
    assert(isinstance(res, dict))

def test_calculate_bracket_thresholds():
    res = tc.calculate_bracket_thresholds()
    assert(10 in res.keys())

def test_lowest_bracket():
    res = tc.run(6000)
    assert(res["summary"]["tax_owed"] == 600)

def test_second_bracket():
    res = tc.run(12000)
    assert(res["summary"]["tax_owed"] == 970 + (12000-9700)*0.12)

def test_third_bracket():
    res = tc.run(50000)
    assert(res["summary"]["tax_owed"] == 970 + round((39475-9700)*0.12) + round((50000-39475)*0.22))

def test_returns_gross_income_error():
    assert(tc.run(-1) == {"error": "Gross income must be greater than 0"})