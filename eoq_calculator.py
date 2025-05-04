"""
📊 EOQ (Economic Order Quantity) Calculator
Calculates optimal order quantity to minimize inventory costs.
"""

import math

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
    DEMAND = 5000     # Annual demand (units)
    ORDER_COST = 100  # Cost per order ($)
    HOLDING_COST = 2  # Holding cost per unit/year ($)

    eoq = calculate_eoq(DEMAND, ORDER_COST, HOLDING_COST)
    orders_per_year = DEMAND / eoq
    total_cost = (DEMAND * ORDER_COST / eoq) + (eoq * HOLDING_COST / 2)

    print(f"""
    📊 EOQ Analysis Results:
    -------------------------
    Annual Demand: {DEMAND:,} units
    Cost per Order: ${ORDER_COST:,.2f}
    Holding Cost: ${HOLDING_COST:,.2f}/unit
    -------------------------
    Optimal Order Quantity: {eoq:,.0f} units
    Orders Needed per Year: {orders_per_year:,.1f}
    Total Annual Cost: ${total_cost:,.2f}
    """)