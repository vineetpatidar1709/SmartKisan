# data/crop_database.py

CROP_DATABASE = {

    # ================== KHARIF CROPS ==================

    "Rice": {
        "Major States": ["West Bengal", "Punjab", "Uttar Pradesh", "Andhra Pradesh", "Tamil Nadu", "Chhattisgarh"],
        "Suitable Months": [6, 7, 8, 9],
        "Soil": "Clay Loamy Alluvial",
        "Water Requirement": "High",
        "Water Availability (mm)": "1000-2000",
        "Market Price": 2200
    },

    "Maize": {
        "Major States": ["Karnataka", "Madhya Pradesh", "Bihar", "Uttar Pradesh"],
        "Suitable Months": [6, 7, 8],
        "Soil": "Loamy Sandy",
        "Water Requirement": "Medium",
        "Water Availability (mm)": "500-800",
        "Market Price": 1900
    },

    "Bajra": {
        "Major States": ["Rajasthan", "Gujarat", "Haryana"],
        "Suitable Months": [6, 7, 8],
        "Soil": "Sandy Black",
        "Water Requirement": "Low",
        "Water Availability (mm)": "300-500",
        "Market Price": 1800
    },

    "Jowar": {
        "Major States": ["Maharashtra", "Karnataka"],
        "Suitable Months": [6, 7],
        "Soil": "Black Loamy",
        "Water Requirement": "Low",
        "Water Availability (mm)": "350-500",
        "Market Price": 3000
    },

    "Soybean": {
        "Major States": ["Madhya Pradesh", "Maharashtra", "Rajasthan"],
        "Suitable Months": [6, 7, 8],
        "Soil": "Black Loamy",
        "Water Requirement": "Medium",
        "Water Availability (mm)": "500-900",
        "Market Price": 4000
    },

    "Cotton": {
        "Major States": ["Maharashtra", "Gujarat", "Punjab", "Haryana"],
        "Suitable Months": [6, 7],
        "Soil": "Black",
        "Water Requirement": "Medium",
        "Water Availability (mm)": "600-1000",
        "Market Price": 6000
    },

    "Groundnut": {
        "Major States": ["Gujarat", "Tamil Nadu", "Karnataka"],
        "Suitable Months": [6, 7],
        "Soil": "Sandy Loamy",
        "Water Requirement": "Low",
        "Water Availability (mm)": "500-1000",
        "Market Price": 5000
    },

    "Tur (Arhar)": {
        "Major States": ["Maharashtra", "Karnataka", "Uttar Pradesh"],
        "Suitable Months": [6, 7],
        "Soil": "Loamy",
        "Water Requirement": "Medium",
        "Water Availability (mm)": "600-1000",
        "Market Price": 7000
    },

    "Moong": {
        "Major States": ["Rajasthan", "Maharashtra", "Karnataka"],
        "Suitable Months": [6, 7],
        "Soil": "Sandy Loamy",
        "Water Requirement": "Low",
        "Water Availability (mm)": "400-600",
        "Market Price": 6500
    },

    "Urad": {
        "Major States": ["Madhya Pradesh", "Uttar Pradesh"],
        "Suitable Months": [6, 7],
        "Soil": "Loamy",
        "Water Requirement": "Low",
        "Water Availability (mm)": "400-600",
        "Market Price": 6000
    },

    # ================== RABI CROPS ==================

    "Wheat": {
        "Major States": ["Punjab", "Haryana", "Uttar Pradesh", "Madhya Pradesh"],
        "Suitable Months": [10, 11, 12, 1],
        "Soil": "Loamy Clay",
        "Water Requirement": "Medium",
        "Water Availability (mm)": "450-650",
        "Market Price": 2100
    },

    "Barley": {
        "Major States": ["Rajasthan", "Uttar Pradesh"],
        "Suitable Months": [10, 11],
        "Soil": "Loamy",
        "Water Requirement": "Low",
        "Water Availability (mm)": "300-500",
        "Market Price": 1900
    },

    "Gram (Chana)": {
        "Major States": ["Madhya Pradesh", "Rajasthan", "Maharashtra"],
        "Suitable Months": [10, 11],
        "Soil": "Loamy Black",
        "Water Requirement": "Low",
        "Water Availability (mm)": "400-600",
        "Market Price": 5000
    },

    "Mustard": {
        "Major States": ["Rajasthan", "Haryana", "Uttar Pradesh"],
        "Suitable Months": [10, 11],
        "Soil": "Sandy Loamy",
        "Water Requirement": "Low",
        "Water Availability (mm)": "350-500",
        "Market Price": 5500
    },

    "Peas": {
        "Major States": ["Uttar Pradesh", "Punjab"],
        "Suitable Months": [10, 11],
        "Soil": "Loamy",
        "Water Requirement": "Medium",
        "Water Availability (mm)": "400-600",
        "Market Price": 4500
    },

    "Lentil (Masoor)": {
        "Major States": ["Madhya Pradesh", "Uttar Pradesh"],
        "Suitable Months": [10, 11],
        "Soil": "Loamy",
        "Water Requirement": "Low",
        "Water Availability (mm)": "350-500",
        "Market Price": 6000
    },

    # ================== CASH CROPS ==================

    "Sugarcane": {
        "Major States": ["Uttar Pradesh", "Maharashtra", "Karnataka"],
        "Suitable Months": [2, 3, 4, 5],
        "Soil": "Loamy Clay",
        "Water Requirement": "High",
        "Water Availability (mm)": "1000-1500",
        "Market Price": 3400
    },

    "Tea": {
        "Major States": ["Assam", "West Bengal"],
        "Suitable Months": [3, 4, 5, 6],
        "Soil": "Acidic Loamy",
        "Water Requirement": "High",
        "Water Availability (mm)": "1200-2500",
        "Market Price": 20000
    },

    "Coffee": {
        "Major States": ["Karnataka", "Kerala"],
        "Suitable Months": [6, 7, 8],
        "Soil": "Loamy",
        "Water Requirement": "Medium",
        "Water Availability (mm)": "1000-1500",
        "Market Price": 15000
    },

    "Jute": {
        "Major States": ["West Bengal", "Bihar"],
        "Suitable Months": [4, 5, 6],
        "Soil": "Alluvial",
        "Water Requirement": "High",
        "Water Availability (mm)": "1000-1500",
        "Market Price": 4500
    },

    # ================== VEGETABLES ==================

    "Potato": {
        "Major States": ["Uttar Pradesh", "West Bengal"],
        "Suitable Months": [10, 11],
        "Soil": "Loamy",
        "Water Requirement": "Medium",
        "Water Availability (mm)": "500-700",
        "Market Price": 1500
    },

    "Tomato": {
        "Major States": ["Karnataka", "Maharashtra"],
        "Suitable Months": [6, 7, 10],
        "Soil": "Loamy",
        "Water Requirement": "Medium",
        "Water Availability (mm)": "600-800",
        "Market Price": 2000
    },

    "Onion": {
        "Major States": ["Maharashtra", "Gujarat"],
        "Suitable Months": [6, 10],
        "Soil": "Loamy",
        "Water Requirement": "Medium",
        "Water Availability (mm)": "350-550",
        "Market Price": 1800
    },

    "Brinjal": {
        "Major States": ["West Bengal", "Karnataka"],
        "Suitable Months": [6, 10],
        "Soil": "Loamy",
        "Water Requirement": "Medium",
        "Water Availability (mm)": "400-600",
        "Market Price": 2200
    },

    "Cabbage": {
        "Major States": ["Uttar Pradesh", "Punjab"],
        "Suitable Months": [10, 11],
        "Soil": "Loamy",
        "Water Requirement": "Medium",
        "Water Availability (mm)": "400-600",
        "Market Price": 2000
    },

    # ================== FRUITS ==================

    "Banana": {
        "Major States": ["Tamil Nadu", "Maharashtra"],
        "Suitable Months": [2, 3, 4],
        "Soil": "Loamy",
        "Water Requirement": "High",
        "Water Availability (mm)": "1000-1500",
        "Market Price": 3000
    },

    "Mango": {
        "Major States": ["Uttar Pradesh", "Andhra Pradesh"],
        "Suitable Months": [3, 4],
        "Soil": "Loamy",
        "Water Requirement": "Medium",
        "Water Availability (mm)": "500-800",
        "Market Price": 2500
    },

    "Apple": {
        "Major States": ["Himachal Pradesh", "Jammu and Kashmir"],
        "Suitable Months": [2, 3],
        "Soil": "Loamy",
        "Water Requirement": "Medium",
        "Water Availability (mm)": "500-800",
        "Market Price": 6000
    },

    "Orange": {
        "Major States": ["Maharashtra", "Madhya Pradesh"],
        "Suitable Months": [6, 7],
        "Soil": "Black Loamy",
        "Water Requirement": "Medium",
        "Water Availability (mm)": "600-900",
        "Market Price": 4000
    },

    # ================== SPICES ==================

    "Chili": {
        "Major States": ["Andhra Pradesh", "Karnataka"],
        "Suitable Months": [6, 7],
        "Soil": "Loamy",
        "Water Requirement": "Medium",
        "Water Availability (mm)": "500-800",
        "Market Price": 8000
    },

    "Turmeric": {
        "Major States": ["Telangana", "Maharashtra"],
        "Suitable Months": [6, 7],
        "Soil": "Loamy",
        "Water Requirement": "High",
        "Water Availability (mm)": "1000-1500",
        "Market Price": 7000
    },

    "Coriander": {
        "Major States": ["Rajasthan", "Madhya Pradesh"],
        "Suitable Months": [10, 11],
        "Soil": "Sandy Loamy",
        "Water Requirement": "Low",
        "Water Availability (mm)": "250-400",
        "Market Price": 6000
    },

    "Cumin": {
        "Major States": ["Rajasthan", "Gujarat"],
        "Suitable Months": [10, 11],
        "Soil": "Sandy",
        "Water Requirement": "Low",
        "Water Availability (mm)": "250-400",
        "Market Price": 12000
    }

}

# --- Aliases / normalization ---
# Some modules (and datasets) use different common names for the same crop.
# Keep canonical keys above, but expose friendly aliases so lookups work everywhere.
_CROP_ALIASES = {
    "Chickpea": "Gram (Chana)",
    "Red Lentil": "Lentil (Masoor)",
    "Green Gram": "Moong",
    "Pigeon Pea": "Tur (Arhar)",
}

for _alias, _canonical in _CROP_ALIASES.items():
    if _canonical in CROP_DATABASE and _alias not in CROP_DATABASE:
        CROP_DATABASE[_alias] = CROP_DATABASE[_canonical]
