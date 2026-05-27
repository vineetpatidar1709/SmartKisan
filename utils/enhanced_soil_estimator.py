# Enhanced Soil NPK Estimator
# Uses state, season, and soil type for more accurate NPK estimation

# Base NPK values by soil type
SOIL_NPK_BASE = {
    "Black": {"N": 80, "P": 45, "K": 40},
    "Alluvial": {"N": 70, "P": 50, "K": 35},
    "Red": {"N": 60, "P": 35, "K": 30},
    "Sandy": {"N": 50, "P": 30, "K": 25},
    "Clay": {"N": 75, "P": 40, "K": 38},
}

# Regional adjustments - different states have different soil profiles
STATE_NPK_ADJUSTMENTS = {
    "Andhra Pradesh": {"N": 5, "P": 3, "K": 3},
    "Arunachal Pradesh": {"N": 5, "P": 2, "K": 5},
    "Assam": {"N": 8, "P": 3, "K": 5},
    "Bihar": {"N": 5, "P": 3, "K": 3},
    "Chhattisgarh": {"N": -3, "P": 0, "K": 3},
    "Gujarat": {"N": -5, "P": 0, "K": 5},
    "Haryana": {"N": 10, "P": 8, "K": 5},
    "Himachal Pradesh": {"N": 5, "P": 3, "K": 5},
    "Jammu & Kashmir": {"N": 5, "P": 3, "K": 5},
    "Jharkhand": {"N": -3, "P": 0, "K": 3},
    "Karnataka": {"N": -8, "P": -5, "K": 5},
    "Kerala": {"N": 5, "P": 3, "K": 3},
    "Madhya Pradesh": {"N": -5, "P": 0, "K": 5},
    "Maharashtra": {"N": -10, "P": -5, "K": 5},
    "Meghalaya": {"N": 5, "P": 2, "K": 5},
    "Nagaland": {"N": 5, "P": 2, "K": 5},
    "Odisha": {"N": 3, "P": 2, "K": 3},
    "Punjab": {"N": 15, "P": 10, "K": 5},
    "Rajasthan": {"N": -15, "P": -10, "K": 0},
    "Sikkim": {"N": 5, "P": 2, "K": 5},
    "Tamil Nadu": {"N": 3, "P": 2, "K": 3},
    "Telangana": {"N": 3, "P": 2, "K": 3},
    "Tripura": {"N": 5, "P": 2, "K": 5},
    "Uttar Pradesh": {"N": 5, "P": 5, "K": 0},
    "Uttarakhand": {"N": 5, "P": 3, "K": 5},
    "West Bengal": {"N": 8, "P": 3, "K": 5},
}

# Seasonal adjustments - NPK availability varies by season
SEASON_NPK_ADJUSTMENTS = {
    "Kharif": {"N": 10, "P": 0, "K": 0},      # Monsoon - more N available
    "Rabi": {"N": -5, "P": 5, "K": 0},         # Winter - less N
    "Zaid": {"N": 0, "P": 0, "K": 0},          # Summer
}


def get_season_from_month(month):
    """Get season from month number"""
    if month in [6, 7, 8, 9]:
        return "Kharif"
    elif month in [10, 11, 12, 1, 2]:
        return "Rabi"
    else:  # 3, 4, 5
        return "Zaid"


def estimate_npk(soil_type, state=None, month=None):
    """
    Enhanced NPK estimation using soil type, state, and season
    
    Args:
        soil_type: Type of soil (Black, Alluvial, Red, Sandy, Clay)
        state: State name (optional, for regional adjustment)
        month: Month (1-12) for seasonal adjustment
    
    Returns:
        dict with N, P, K values
    """
    # Get base NPK from soil type
    base_npk = SOIL_NPK_BASE.get(
        soil_type,
        {"N": 65, "P": 40, "K": 35}  # Default values
    )
    
    N = base_npk["N"]
    P = base_npk["P"]
    K = base_npk["K"]
    
    # Apply state-based adjustments
    if state and state in STATE_NPK_ADJUSTMENTS:
        adj = STATE_NPK_ADJUSTMENTS[state]
        N += adj["N"]
        P += adj["P"]
        K += adj["K"]
    
    # Apply seasonal adjustments
    if month:
        season = get_season_from_month(month)
        if season in SEASON_NPK_ADJUSTMENTS:
            adj = SEASON_NPK_ADJUSTMENTS[season]
            N += adj["N"]
            P += adj["P"]
            K += adj["K"]
    
    # Ensure non-negative values
    N = max(20, N)
    P = max(10, P)
    K = max(10, K)
    
    return {
        "N": round(N),
        "P": round(P),
        "K": round(K)
    }


# Keep backward compatibility
def estimate_npk_simple(soil_type):
    """Simple NPK estimation (backward compatible)"""
    return estimate_npk(soil_type)
