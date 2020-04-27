import pprint
from collections import OrderedDict
from pandas import DataFrame
from copy import deepcopy

'''
Given a dictionary of tax brackets, calculate tax owed for each bracket and add them up
The highest bracket must have a large number such as 1e15
e.g. >> TaxCalculator({10: 7000, 20: 15000, 25: 20000, 30: 40000, 35: 140000, 40: 1e15})
'''
class TaxCalculator(object):
    def __init__(self, tax_brackets):
        self.tax_brackets = OrderedDict(sorted(tax_brackets.items()))
    
    def run(self, gross_income):
        original_gross_income = deepcopy(gross_income)
        tax_owed = 0
        table, result = [], {}
        for percent, cutoff in self.tax_brackets.items():
            if gross_income < 1:
                break
            taxable = min(gross_income, cutoff)
            tax = round(percent * 0.01 * taxable)
            tax_owed += tax
            gross_income -= cutoff
            table.append([percent, taxable, tax])
        
        effective_tax_rate = round((tax_owed / original_gross_income * 100), 2)
        
        # Set up detail tax breakdown table
        table.append([effective_tax_rate, original_gross_income, tax_owed])
        df = DataFrame(table, columns=['percent', 'taxable_amount', 'tax'])
        
        result.update({
            "summary": {
                "gross_income": original_gross_income,
                "tax_owed": tax_owed,
                "effective_tax_rate": effective_tax_rate
            },
            "details": df
        })

        return result

if __name__ == '__main__':
    tc = TaxCalculator({10: 7000, 20: 15000, 25: 20000, 30: 40000, 35: 140000, 40: 1e15})
    pprint.pprint(tc.run(140000))