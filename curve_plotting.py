#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 12:05:30 2017

@author: cgao
"""
import matplotlib
import matplotlib.pyplot as plt
import tax_reform

#tax_reform.tax_comparison(240000, 3, 1, 700000, 0.03, 0.06, 18000, joint = True, detail = True)  

def comparison_curve(
        income_low = 10000,
        income_high = 500000,
        income_interval = 10000,
        family_size = 3,
        children = 1,
        UPB = 700000,
        rate = 0.0275,
        efficient_state_rate = 0.05,
        local_tax = 16500,
        joint = True,
        existing_mtg = False
        ):
    taxable_incomes = [income_interval*x for x in range(int(income_low/income_interval), int(income_high/income_interval)+1)]
    taxes = [tax_reform.tax_comparison(taxable_income, family_size, children, UPB, rate, efficient_state_rate, local_tax, joint = joint, existing_mtg = existing_mtg, display = False)  for taxable_income in taxable_incomes]
    taxes_old = [x[0] for x in taxes]
    taxes_new = [x[1] for x in taxes]
    tax_reductions = [x[0] - x[1] for x in taxes]
    
    plt.figure(figsize=(10,5))
    plt.plot(taxable_incomes, taxes_old, 'r', label = 'Current Federal Tax ($)') 
    plt.plot(taxable_incomes, taxes_new, 'b', label = 'New Federal Tax ($)')
    plt.xlabel('taxable income ($)', fontsize = 10)
    ax = plt.gca()
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.legend(fontsize = 10)
    plt.grid()
    plt.show()
    # tax reduction plot
    plt.figure(figsize=(10,5))
    plt.plot(taxable_incomes, tax_reductions, 'g', label = 'Tax Reduction Under New Tax Proposal ($)') 
    plt.xlabel('taxable income ($)', fontsize = 10)
    ax = plt.gca()
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax.text(0.05, 0.80, 'Family = %d; Children = %d'%(family_size, children),
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color='red', fontsize=10)
    ax.text(0.05, 0.75, 'Existing Mortgage = %r'%existing_mtg + '; UPB = ${:,}'.format(UPB) + '; Rate = %3.2f%%'%(rate*100),
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color='red', fontsize=10)
    ax.text(0.05, 0.70, 'State Rate = %3.2f%%'%(efficient_state_rate*100) + '; Local Tax = ${:,}'.format(local_tax),
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color='red', fontsize=10)
    ax.text(0.05, 0.65, 'Joint = %s'%(joint),
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color='red', fontsize=10)
    plt.legend(fontsize = 10)
    plt.grid()
    plt.show()    


def AMT_planning(
        income_low = 10000,
        income_high = 500000,
        income_interval = 10000,
        family_size = 3,
        children = 1,
        UPB = 700000,
        rate = 0.0275,
        efficient_state_rate = 0.05,
        local_tax = 16500,
        joint = True,
        existing_mtg = False
        ):
    taxable_incomes = [income_interval*x for x in range(int(income_low/income_interval), int(income_high/income_interval)+1)]
    taxes = [tax_reform.tax_comparison(taxable_income, family_size, children, UPB, rate, efficient_state_rate, local_tax, joint = joint, existing_mtg = existing_mtg, display = False)  for taxable_income in taxable_incomes]
    #  return [tax_old, tax_new, old_tax_standard, new_tax_standard, old_tax_itemized, new_tax_itemized, old_tax_AMT]
    old_tax = [x[0] for x in taxes]
    old_tax_standard = [x[2] for x in taxes]
    old_tax_itemized = [x[4] for x in taxes]
    old_tax_AMT = [x[6] for x in taxes]
    AMT_penalty = [x[0] - x[4] for x in taxes]
    # compare standard tax, itemized tax and AMT tax.
    plt.figure(figsize=(10,5))
    plt.plot(taxable_incomes, old_tax, 'rd', label = 'Federal Tax ($)') 
    plt.plot(taxable_incomes, old_tax_standard, 'b', label = 'Federal Tax by Standard ($)') 
    plt.plot(taxable_incomes, old_tax_itemized, 'g', label = 'Federal Tax by Itemized ($)') 
    plt.plot(taxable_incomes, old_tax_AMT, 'k', label = 'Federal Tax by ATM ($)') 
    plt.xlabel('taxable income ($)', fontsize = 10)
    #plt.xticks(np.arange(0, 1.0*1e6, 50000))
    #plt.yticks(np.arange(0, 4e5, 10000))
    ax = plt.gca()
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax.text(0.05, 0.60, 'Family = %d; Children = %d'%(family_size, children),
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color='red', fontsize=10)
    ax.text(0.05, 0.55, 'Existing Mortgage = %r'%existing_mtg + '; UPB = ${:,}'.format(UPB) + '; Rate = %3.2f%%'%(rate*100),
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color='red', fontsize=10)
    ax.text(0.05, 0.50, 'State Rate = %3.2f%%'%(efficient_state_rate*100) + '; Local Tax = ${:,}'.format(local_tax),
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color='red', fontsize=10)
    ax.text(0.05, 0.65, 'Joint = %s'%(joint),
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color='red', fontsize=10)
    plt.legend(fontsize = 10)
    plt.grid()
    plt.show()
    #AMT penalty curve
    plt.figure(figsize=(10,5))
    plt.plot(taxable_incomes, AMT_penalty, 'g', label = 'AMT penalty ($)') 
    plt.xlabel('taxable income ($)', fontsize = 10)
    ax = plt.gca()
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax.text(0.05, 0.80, 'Family = %d; Children = %d'%(family_size, children),
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color='red', fontsize=10)
    ax.text(0.05, 0.75, 'Existing Mortgage = %r'%existing_mtg + '; UPB = ${:,}'.format(UPB) + '; Rate = %3.2f%%'%(rate*100),
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color='red', fontsize=10)
    ax.text(0.05, 0.70, 'State Rate = %3.2f%%'%(efficient_state_rate*100) + '; Local Tax = ${:,}'.format(local_tax),
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color='red', fontsize=10)
    ax.text(0.05, 0.65, 'Joint = %s'%(joint),
            verticalalignment='bottom', horizontalalignment='left',
            transform=ax.transAxes,
            color='red', fontsize=10)
    plt.legend(fontsize = 10)
    plt.grid()
    plt.show()
