# 10-LINE SOLUTION (Copy-Paste Ready)  
import numpy as np  
def safety_stock(daily_stddev, lead_time_days, service_level=1.65):  
    return round(service_level * daily_stddev * np.sqrt(lead_time_days))  
print(safety_stock(20, 7))  # → 88 units  