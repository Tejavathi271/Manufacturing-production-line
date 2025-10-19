# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 17:35:06 2025

@author: tejavathi teju
"""

from datetime import datetime


def output_report(supervisor):
    """Print total output for each production line"""
    print("\n OUTPUT REPORT")
    print("-" * 40)
    if not supervisor.lines:
        print("No production lines available.")
        return

    for line in supervisor.lines.values():
        print(f"{line.name} ({line.line_id}) → Total Output: {line.output} {line.item}(s)")
    print("-" * 40)


def efficiency_report(supervisor):
    """Calculate and display efficiency (output/capacity * 100)"""
    print("\n EFFICIENCY REPORT")
    print("-" * 40)
    if not supervisor.lines:
        print("No production lines available.")
        return

    for line in supervisor.lines.values():
        efficiency = (line.output / line.capacity) * 100 if line.capacity else 0
        print(f"{line.name} ({line.line_id}) → Efficiency: {efficiency:.2f}%")
    print("-" * 40)


def downtime_report(supervisor):
    """Summarize start/stop activity for each production line"""
    print("\n DOWNTIME REPORT")
    print("-" * 40)
    if not supervisor.lines:
        print("No production lines available.")
        return

    for line in supervisor.lines.values():
        start_count = sum(1 for log in line.history if log["action"] == "started")
        stop_count = sum(1 for log in line.history if log["action"] == "stopped")
        print(f"{line.name} ({line.line_id}) → Started: {start_count} times, Stopped: {stop_count} times")
    print("-" * 40)