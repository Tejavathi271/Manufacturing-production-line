# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 17:16:02 2025

@author: tejavathi teju
"""

import random

def generate_id(prefix):
    random_number = random.randint(100, 999)  # generates a 3-digit random number
    new_id = f"{prefix}{random_number}"
    return new_id