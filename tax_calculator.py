import pprint
from collections import OrderedDict
from pandas import DataFrame
from copy import deepcopy

'''
Given a dictionary of tax brackets, calculate tax owed for each bracket and add them up.
The highest bracket must have a large number such as 1e15
e.g. 
>> c = TaxCalculator({
    10: '0-9700', 
    12: '9700-39475', 
    22: '39475-84200', 
    24: '84200-160725',
    32: '160725-204100', 
    35: '204100-510300',
    37: '510300-1e15'
})
>> c.run(150000)
'''
class TaxCalculator(object):
    def __init__(self, input_brackets):
        self.input_brackets = input_brackets
        self.tax_brackets = self.calculate_bracket_thresholds()
    
    # Process the given input bracket into format suitable for run method below
    def calculate_bracket_thresholds(self):
        final = {}
        for k,v in self.input_brackets.items():
            low, high = [float(n) for n in v.split("-")]
            final[k] = high - low
        return OrderedDict(sorted(final.items()))

    # Main method for getting the results
    def run(self, gross_income):
        original_gross_income = deepcopy(gross_income)
        tax_owed = 0
        table, result = [], {}

        if gross_income < 0:
            return {"error": "Gross income must be greater than 0"}
        
        # Iterate an ordered dict of tax brackets, starting from lowest
        # Compare current gross income and bracket threshold
        # Pick the minimum as taxable and calculate the tax
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