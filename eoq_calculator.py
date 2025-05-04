"""
EOQ (Economic Order Quantity) Calculator
Optimizes inventory order quantity to minimize costs.
"""

import math
import matplotlib.pyplot as plt
import numpy as np

def calculate_eoq(demand: float, order_cost: float, holding_cost: float) -> float:
    """
    Args:
        demand: Annual demand (units)
        order_cost: Cost per order ($)
        holding_cost: Annual holding cost per unit ($)
    Returns:
        Optimal order quantity (units)
    """
    return math.sqrt((2 * demand * order_cost) / holding_cost)

# Example usage
if __name__ == "__main__":
    DEMAND = 5000    # Annual demand (units)
    ORDER_COST = 100 # Cost per order ($)
    HOLDING_COST = 2 # Holding cost per unit/year ($)
    
    eoq = calculate_eoq(DEMAND, ORDER_COST, HOLDING_COST)
    print(f"Optimal Order Quantity: {eoq:.0f} units")