from tax_calculator import TaxCalculator
import pytest

tc = TaxCalculator({})

def test_returns_result_keys():
    res = tc.run(140000)
    assert(isinstance(res, dict))

def test_returns_gross_income_error():
    assert(tc.run(-1) == {"error": "Gross income must be greater than 0"})