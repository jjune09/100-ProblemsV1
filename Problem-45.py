def calculate_annual_return(initial_investment: float, final_investment: float, years: int) -> float:
    annual_return = ((final_investment / initial_investment) ** (1 / years) - 1) * 100
    return round(annual_return, 2)
print(calculate_annual_return(1000, 1500, 5)) 
# Output: 8.45