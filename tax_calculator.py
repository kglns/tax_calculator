from collections import OrderedDict
from pandas import DataFrame
from copy import deepcopy
class TaxCalculator(object):
    def __init__(self, tax_brackets):
        self.tax_brackets = OrderedDict(sorted(tax_brackets.items()))
    
    def run(self, gross_income):
        original_gross_income = deepcopy(gross_income)
        tax_owed = 0
        table = []
        for percent, cutoff in self.tax_brackets.items():
            if gross_income < 1:
                break
            taxable = min(gross_income, cutoff)
            tax = round(percent * 0.01 * taxable)
            tax_owed += tax
            gross_income -= cutoff
            table.append([percent, taxable, tax])
        table.append([0, original_gross_income, tax_owed])
        df = DataFrame(table, columns=['percent', 'taxable_amount', 'tax'])
        print(f"Total Taxable Amount = {original_gross_income}")
        print(f"Tax Owed = {tax_owed}")
        print('Breakdown table ')
        print(df)
        return (df, tax_owed)

if __name__ == '__main__':
    tc = TaxCalculator({10: 7000, 20: 15000, 25: 20000, 30: 40000, 35: 140000, 40: 1e15})
    tc.run(140000)