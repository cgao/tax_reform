#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 12:32:19 2017

@author: cgao
"""


import tax_reform
import curve_plotting

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