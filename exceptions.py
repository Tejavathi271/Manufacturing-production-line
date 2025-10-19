# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 17:16:13 2025

@author: tejavathi teju
"""

"""
Custom exceptions for Manufacturing Production Line.
"""

class LineNotFoundError(Exception):
    """Raised when a specified production line ID does not exist."""
    pass

class InvalidOperationError(Exception):
    """Raised when an invalid action is attempted (e.g., logging output on a stopped line)."""
    pass