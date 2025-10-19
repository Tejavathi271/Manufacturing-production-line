# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 17:16:27 2025

@author: tejavathi teju
"""

from production_line import ProductionLine
from exceptions import LineNotFoundError, InvalidOperationError
from report import output_report, efficiency_report, downtime_report


class Supervisor:
    def __init__(self):
        self.lines = {}  # {line_id: ProductionLine}

    def add_line(self, name, item, capacity):
        """Add a new production line"""
        new_line = ProductionLine(name, item, capacity)
        self.lines[new_line.line_id] = new_line
        print(f"Added new line: {new_line}")
        return new_line.line_id

    def remove_line(self, line_id):
        """Remove a line by ID"""
        if line_id not in self.lines:
            raise LineNotFoundError(f"Line ID '{line_id}' not found.")
        removed = self.lines.pop(line_id)
        print(f" Removed line: {removed.name}")

    def start_line(self, line_id):
        """Start a specific line"""
        if line_id not in self.lines:
            raise LineNotFoundError(f"Line ID '{line_id}' not found.")
        self.lines[line_id].start()

    def stop_line(self, line_id):
        """Stop a specific line"""
        if line_id not in self.lines:
            raise LineNotFoundError(f"Line ID '{line_id}' not found.")
        self.lines[line_id].stop()

    def log_output(self, line_id, quantity):
        """Record output for a running line"""
        if line_id not in self.lines:
            raise LineNotFoundError(f"Line ID '{line_id}' not found.")
        line = self.lines[line_id]
        if not line.is_running:
            raise InvalidOperationError("Cannot log output — line not running.")
        line.add_output(quantity)
    def output_report(self):
        """Generate the total output report by calling the function from report.py."""
        output_report(self) 

    def efficiency_report(self):
        """Generate the efficiency report by calling the function from report.py."""
        efficiency_report(self) 

    def downtime_report(self):
        """Generate the downtime report by calling the function from report.py."""
        downtime_report(self)
    def generate_reports(self):
        """Display all production line summaries"""
        print("\n Production Report:")
        for line in self.lines.values():
            print(line)