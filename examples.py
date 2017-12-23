#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 12:32:19 2017

@author: cgao
"""


import tax_reform
import curve_plotting

'''
curve_plotting.comparison_curve(income_low = 150000, 
                                income_high = 350000,
                                family_size = 4, 
                                children = 2)
curve_plotting.AMT_planning(income_low = 150000,
                            income_high = 350000,
                            family_size = 3, 
                            children = 1)



curve_plotting.comparison_curve(income_low = 100000, 
                                income_high = 550000,
                                family_size = 4, 
                                children = 2,
                                UPB = 1000000,
                                rate = 0.04,
                                efficient_state_rate = 0.09,
                                local_tax = 15000
                                )


curve_plotting.comparison_curve(income_low = 100000, 
                                income_high = 550000,
                                family_size = 2, 
                                children = 0,
                                UPB = 1000000,
                                rate = 0.04,
                                efficient_state_rate = 0.09,
                                local_tax = 15000
                                )
'''


curve_plotting.comparison_curve(income_low = 100000, 
                                income_high = 800000,
                                family_size = 2, 
                                children = 0,
                                UPB = 1500000,
                                rate = 0.03,
                                efficient_state_rate = 0.09,
                                local_tax = 20000,
                                joint = True
                                )


#tax_reform.tax_comparison(400000, 2, 0, 1500000, 0.03, 0.09, 20000, joint = True, detail = True)  


curve_plotting.comparison_curve(income_low = 100000, 
                                income_high = 800000,
                                family_size = 1, 
                                children = 0,
                                UPB = 750000,
                                rate = 0.03,
                                efficient_state_rate = 0.09,
                                local_tax = 10000,
                                joint = False,
                                existing_mtg = True
                                )


tax_reform.tax_comparison(600000, 2, 0, 1500000, 0.03, 0.09, 20000, joint = True, existing_mtg = True, detail = True)  
tax_reform.tax_comparison(300000, 1, 0, 750000, 0.03, 0.09, 10000, joint = False, existing_mtg = True, detail = True)  

tax_reform.tax_comparison(300000, 3, 1, 100000, 0.03, 0.09, 10000, joint = False, existing_mtg = True, detail = True)  


curve_plotting.AMT_planning(income_low = 150000,
                            income_high = 350000,
                            income_interval = 10000,
                            family_size = 3,
                            children = 1,
                            UPB = 74000,
                            rate = 0.02625,
                            efficient_state_rate = 0.05,
                            local_tax = 10000,
                            joint = True,
                            existing_mtg = False)
