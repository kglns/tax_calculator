from tax_calculator import TaxCalculator
import pytest

tc = TaxCalculator({10: 7000, 20: 15000, 25: 20000, 30: 40000, 35: 140000, 40: 1e15})

def test_returns_result_keys():
    res = tc.run(140000)
    assert(isinstance(res, dict))

def test_lowest_bracket():
    res = tc.run(6000)
    assert(res["summary"]["tax_owed"] == 600)

def test_returns_gross_income_error():
    assert(tc.run(-1) == {"error": "Gross income must be greater than 0"})