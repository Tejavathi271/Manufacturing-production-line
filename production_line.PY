# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 17:16:43 2025

@author: tejavathi teju
"""

from datetime import datetime
from utils import generate_id


class ProductionLine:
    def __init__(self, name, item, capacity):
        self.line_id = generate_id("LINE")
        self.name = name
        self.item = item
        self.capacity = capacity
        self.is_running = False
        self.output = 0
        self.history = []  # store logs like {"timestamp": ..., "action": ...}

    def start(self):
        """Start the production line"""
        if not self.is_running:
            self.is_running = True
            self.history.append({
                "timestamp": datetime.now(),
                "action": "started"
            })
            print(f"{self.name} started at {self.history[-1]['timestamp']}")
        else:
            print(f" {self.name} is already running.")

    def stop(self):
        """Stop the production line"""
        if self.is_running:
            self.is_running = False
            self.history.append({
                "timestamp": datetime.now(),
                "action": "stopped"
            })
            print(f"{self.name} stopped at {self.history[-1]['timestamp']}")
        else:
            print(f"{self.name} is not running.")

    def add_output(self, quantity):
        """Increase output by given quantity"""
        if not self.is_running:
            print(" Cannot add output — line is not running.")
            return
        if self.output + quantity > self.capacity:
            print("Capacity exceeded! Cannot add more output.")
            return
        self.output += quantity
        self.history.append({
            "timestamp": datetime.now(),
            "action": f"Produced {quantity} {self.item}(s)"
        })
        print(f" Produced {quantity} {self.item}(s). Total output: {self.output}")

    def __str__(self):
        """Return a readable string representation"""
        return f"[{self.line_id}] {self.name} ({self.item}) - Capacity: {self.capacity}, Output: {self.output}, Running: {self.is_running}"
