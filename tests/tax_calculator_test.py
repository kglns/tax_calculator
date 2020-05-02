import tax_calculator 
import pytest

def test_returns_result_keys():
    tc = tax_calculator.TaxCalculator({})
    res = tc.run(140000)
    assert(isinstance(res, dict))