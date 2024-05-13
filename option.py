#!/usr/bin/env python
# coding: utf-8


############################ IMPORTS ###################################
import numpy as np
########################################################################


########################## BASIC CLASSES ###############################
class Option:
    
    Allowed_kinds = ['European', 'Bermudean', 'American']
    def __init__(self, payoff, maturity, kind='European', exercising_times=[], left_boundary=None, right_boundary=None):
        
        assert kind in Option.Allowed_kinds, f"Option kind must be one of {Option.Allowed_kinds}."
        if maturity not in exercising_times:
                raise ValueError(f"Maturity is not in the passed exercising times. exercising_times = {exercising_times}")
                
        self.payoff = payoff
        self.maturity = maturity
        self.kind = kind
        self.exercising_times = exercising_times
        
        self.left_boundary = left_boundary
        self.right_boundary = right_boundary
    
    def __call__(self, x):
        return self.payoff(x)
    
    def is_exercisable(self, t):
        european_condition = (self.kind == 'European' and t == self.maturity)
        bermudean_condition = (self.kind == 'Bermudean' and t in self.exercising_times)
        american_condition = (self.kind == 'American' and t <= self.maturity)
        
        return european_condition or bermudean_condition or american_condition
########################################################################

