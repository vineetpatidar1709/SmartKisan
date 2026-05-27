"""
Constants used across the application
"""

# States list - 26 states for ML models
STATES = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Gujarat", "Haryana", "Himachal Pradesh", "Jammu & Kashmir", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Meghalaya",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
    "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

# Months list
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Soil types
SOIL_TYPES = ["Black", "Alluvial", "Red", "Sandy", "Clay"]

# Irrigation methods
IRRIGATION_METHODS = ["Rainfed", "Canal", "Tube Well", "Drip", "Sprinkler"]

# Page configurations
PAGE_CONFIGS = {
    "main": {"title": "SMART KISAN", "icon": "🌾", "layout": "wide"},
    "crop_advisory": {"title": "Crop Advisory", "icon": "📘", "layout": "wide"},
    "yield_estimator": {"title": "Yield Estimator", "icon": "📈", "layout": "wide"},
    "profit_calculator": {"title": "Profit Calculator", "icon": "💰", "layout": "wide"},
    "market_prices": {"title": "Market Prices", "icon": "💰", "layout": "wide"},
    "crop_recommendation": {"title": "Crop Recommendation", "icon": "🌾", "layout": "wide"}
}

# Default values
DEFAULT_TEMPERATURE = 25.0
DEFAULT_RAINFALL = 100.0
DEFAULT_PH = 6.5
DEFAULT_LAND_SIZE = 1.0
DEFAULT_YIELD_PER_ACRE = 25.0

# API settings
CACHE_TTL = 300  # 5 minutes for market prices

# Error messages
ERROR_CROP_NOT_FOUND = "Crop not found"
ERROR_INVALID_CROP_STRUCTURE = "Invalid crop structure"
ERROR_MODEL_NOT_FOUND = "Model not found. Please train the model first."
