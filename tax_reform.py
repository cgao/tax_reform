#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 11:56:41 2017

@author: cgao
"""

from beautifultable import BeautifulTable



#1. 新旧税率Bracket
def tax_calculator(taxable_income, bracket, rate):
    bracket2 = bracket[1:]
    bracket2.append(float('Inf'))
    bracket3 = [y-x for x,y in zip(bracket, bracket2)]
    income_seg = [min(max(0, taxable_income - x), y) for x, y in zip(bracket, bracket3)]
    return sum([x*y for x, y in zip(income_seg, rate)])

def old_bracket(taxable_income, joint = True):
    rate= [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]
    if not joint:
        bracket = [0, 9325, 37950, 91900, 191650, 416700, 418400]
    else:
        bracket = [0, 18650, 75900, 153100, 233350, 416700, 470700]
    return tax_calculator(taxable_income, bracket, rate) 

def new_bracket(taxable_income, joint = True):
    rate= [0.12, 0.25, 0.35, 0.396]
    if not joint:
        bracket = [0, 45000, 200000, 500000]
    else:
        bracket = [0, 90000, 260000, 1000000]
    return tax_calculator(taxable_income, bracket, rate) 


def AMT_bracket(taxable_income, joint = True):
    rate= [0.26, 0.28]
    if not joint:
        bracket = [0, 93900]
    else:
        bracket = [0, 187800]
    return tax_calculator(taxable_income, bracket, rate) 

#2. 增加标准扣除(Standard Deduction)额度
'''
    if joint:
        old_standard_deduction = 12600
        new_standard_deduction = 24000
    else:
        old_standard_deduction = 6300
        new_standard_deduction = 12000
'''

#3. 减少利息扣除
def MTG_IR_deduction_old(UPB, rate):
    return min(1000000.0, UPB)*rate
# existing_mtg = True: existing loan. Grand fathered 1.0 Million limit
def MTG_IR_deduction_new(UPB, rate, existing_mtg = False):
    if existing_mtg:
        return min(1000000.0, UPB)*rate
    else:
        return min(750000.0, UPB)*rate

#4. 减少州与地方税收(房产税等)扣除
def SALT_deduction_old(taxable_income, efficient_state_rate, local_tax):
    return taxable_income*efficient_state_rate + local_tax

def SALT_deduction_new(taxable_income, efficient_state_rate, local_tax):
    return min(10000.0, taxable_income*efficient_state_rate + local_tax)

#5. 取消Personal Exemption
def PersonalExemption_deduction_old(taxable_income, member, joint = True):
    if joint:
        phaseout = min(0.02*round((max(taxable_income - 311300, 0)/2500 + 1e-7)), 1)
        return int(4050*member*(1 - phaseout))
    else:
        phaseout = min(0.02*round(max(taxable_income - 259000, 0)/2500 + 1e-7), 1)
        return int(4050*member*(1 - phaseout))
    
def PersonalExemption_deduction_new():
    return 0

#6. Child Care Tax Credit
def ChildCare_Credit_old(taxable_income, child, joint = True):
    if joint:
        phaseout = round(max(taxable_income - 110000, 0)/20 + 1e-7)
        return int(max(0,1000*child -  phaseout))
    else:
        phaseout = round(max(taxable_income - 55000, 0)/20 + 1e-7)
        return int(max(0,1000*child -  phaseout))

    
def ChildCare_Credit_new(taxable_income, child, joint = True):
    if joint:
        phaseout = round(max(taxable_income - 230000, 0)/20 + 1e-7)
        return int(max(0,1600*child -  phaseout))
    else:
        phaseout = round(max(taxable_income - 115000, 0)/20 + 1e-7)
        return int(max(0,1600*child -  phaseout))
    
#7. 取消AMT (Alternative Minimum Tax)
def AMT_exemption(taxable_income, joint = True):
    if joint:
        return max(0, 84500 - max(taxable_income - 160900, 0)/4)
    else:
        return max(0, 54300 - max(taxable_income - 120700, 0)/4)
    
#8. 逐步取消遗产税 (Estate Tax)

#9. 综合影响
def tax_comparison(taxable_income, member, child, UPB, rate, efficient_state_rate, local_tax, joint = True, existing_mtg = False, display = True, detail = False):
# Personal exemption (applied to both standard and itemized)
    old_PersonalExemption_deduction = PersonalExemption_deduction_old(taxable_income, member, joint = joint)
# Child care tax credit (applied to both standard and itemized)
    old_ChildCare_Credit = ChildCare_Credit_old(taxable_income, child, joint = joint)
    new_ChildCare_Credit = ChildCare_Credit_new(taxable_income, child, joint = joint)
# Mortgage Interest Rate deduction (applied to itemized and AMT)
    old_MTG_IR_deduction= MTG_IR_deduction_old(UPB, rate)
    new_MTG_IR_deduction= MTG_IR_deduction_new(UPB, rate, existing_mtg = existing_mtg)
# State and local tax (applied to itemized only)
    old_SALT_deduction = SALT_deduction_old(taxable_income, efficient_state_rate, local_tax)       
    new_SALT_deduction = SALT_deduction_new(taxable_income, efficient_state_rate, local_tax)
# calculate standard tax
    if joint:
        old_standard_deduction = 12600
        new_standard_deduction = 24000
    else:
        old_standard_deduction = 6300
        new_standard_deduction = 12000
    # tax before Child care credit
    old_tax_beforeCCTC_standard = old_bracket(taxable_income - old_standard_deduction - old_PersonalExemption_deduction, joint = joint)
    new_tax_beforeCCTC_standard = new_bracket(taxable_income - new_standard_deduction, joint = joint)
    # tax before Child after credit
    old_tax_standard = max(0, old_tax_beforeCCTC_standard - old_ChildCare_Credit)
    new_tax_standard = max(0, new_tax_beforeCCTC_standard - new_ChildCare_Credit)
# calculate itemized tax    
    # tax before Child care credit
    old_tax_beforeCCTC_itemized = old_bracket(taxable_income - old_MTG_IR_deduction - old_SALT_deduction - old_PersonalExemption_deduction, joint = joint)
    new_tax_beforeCCTC_itemized = new_bracket(taxable_income - new_MTG_IR_deduction - new_SALT_deduction, joint = joint)
    # tax before Child after credit
    old_tax_itemized = max(0, old_tax_beforeCCTC_itemized - old_ChildCare_Credit)
    new_tax_itemized = max(0, new_tax_beforeCCTC_itemized - new_ChildCare_Credit)
# calculate AMT tax    
    AMT_exemption_amount = AMT_exemption(taxable_income, joint = joint)
    # tax before Child care credit
    old_tax_beforeCCTC_AMT = AMT_bracket(taxable_income - AMT_exemption_amount - old_MTG_IR_deduction, joint = joint)
    # tax before Child after credit
    old_tax_AMT = max(0, old_tax_beforeCCTC_AMT - old_ChildCare_Credit)
    tax_old = max(min(old_tax_standard, old_tax_itemized),old_tax_AMT)
    tax_new = min(new_tax_standard, new_tax_itemized)
    if display:
        print("Current Tax Should Pay: $%3.2f"%tax_old)
        print("    Standard: $%3.2f"%old_tax_standard)
        print("    Itemized: $%3.2f"%old_tax_itemized)
        print("     AMT tax: $%3.2f"%old_tax_AMT)
        print("New Tax Should Pay: $%3.2f"%tax_new)
        print("    Standard: $%3.2f"%new_tax_standard)
        print("    Itemized: $%3.2f"%new_tax_itemized) 
    if detail:
        print("***********************************************")
        print("${:,} taxable income".format(taxable_income) + ', joint = %r'%joint)
        print("%d Family Member, %d child(ren)"%(member, child))
        print('Existing Mortgage: %r'%existing_mtg + ', ${:,} Mortgage Balance'.format(UPB) + ', %3.2f%% Interest Rate'%(rate*100),)
        print('${:,} Local Tax'.format(local_tax) + ', %d%% State/City Tax Rate'%(efficient_state_rate*100),)
        print("***********************************************")
        table = BeautifulTable()
        table.column_headers = ["Item", "Current", "New"]
        table.append_row(["Standard Deduction", old_standard_deduction, new_standard_deduction])
        table.append_row(["Personal Exemption", old_PersonalExemption_deduction, 'NA'])
        table.append_row(["Child Care Tax Credit", old_ChildCare_Credit, new_ChildCare_Credit])
        table.append_row(["Mortgage Interest Deduction", old_MTG_IR_deduction, new_MTG_IR_deduction])
        table.append_row(["State and Local Tax Deduction", old_SALT_deduction, new_SALT_deduction])
        table.append_row(["AMT Exemption (not including MTG Interest)", AMT_exemption_amount, "NA"])
        table.append_row(["Tax", tax_old, tax_new])
        print(table)
    return [tax_old, tax_new, old_tax_standard, new_tax_standard, old_tax_itemized, new_tax_itemized, old_tax_AMT]

