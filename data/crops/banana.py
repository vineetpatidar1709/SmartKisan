crop_data = {
    "banana": {
        "name": "Banana",
        "scientific_name": "Musa spp.",
        "family": "Musaceae",
        "category": "Fruit Crop",
        "crop_type": "Tropical Fruit",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Planting in Spring (Feb-Mar) or Monsoon (Jun-Jul)",
        "duration_days": "300–360 days (variety dependent)",
        "climate": "Tropical to subtropical humid climate",
        "ideal_temperature": "25°C – 30°C",
        "germination_temperature": "25°C – 30°C",
        "rainfall_requirement_mm": "1500 – 2500 mm",
        "water_requirement_level": "High",
        "sunlight_requirement": "Full sunlight required for fruit development",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Deep, well-drained alluvial or loamy soil",
        "soil_ph_range": "5.5 – 7.0",
        "soil_depth_requirement": "Deep soil (60-90 cm) for root development",
        "salinity_tolerance": "Low to Moderate",
        "drainage_requirement": "Excellent drainage essential",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Andhra Pradesh",
            "Arunachal Pradesh",
            "Assam",
            "Chhattisgarh",
            "Gujarat",
            "Karnataka",
            "Kerala",
            "Madhya Pradesh",
            "Maharashtra",
            "Meghalaya",
            "Nagaland",
            "Tamil Nadu",
            "Telangana",
            "Tripura",

        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "Deep ploughing 2-3 times",
            "Pit digging (45cm x 45cm x 45cm)",
            "Add FYM and compost",
            "Ensure proper drainage"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Tissue culture plants or suckers",
            "seed_rate_per_hectare": "1200-1500 plants/ha",
            "varieties": "Grand Naine, Dwarf Cavendish, Robusta, Nendran"
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Pit planting with suckers",
        "row_spacing": "1.5-2.0 m",
        "plant_spacing": "1.5-2.0 m",
        "sowing_depth": "30 cm depth",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "vegetative_stage": {
                "duration": "0-180 days",
                "details": "Leaf production and pseudostem development."
            },
            "flowering_stage": {
                "duration": "180-240 days",
                "details": " emergence."
            },
            "fruit_development": {
                "duration": "240-360 days",
                "details": "Fruit bunch development and maturation."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_planting": "First irrigation after planting",
            "critical_stages": [
                "Vegetative growth",
                "Flowering",
                "Fruit development"
            ],
            "frequency": "7-10 days interval",
            "avoid": "Water stagnation"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "10-15 kg FYM per plant",
            "nitrogen": "200-250 g N per plant",
            "phosphorus": "100-150 g P per plant",
            "potassium": "300-400 g K per plant"
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "banana_weevil": {
                "description": "Stem borer",
                "symptoms": "Yellowing, tunneling in corm",
                "control": "Insecticides, clean planting material"
            },
            "aphids": {
                "description": "Sap-sucking insects",
                "symptoms": "Leaf curling, virus transmission",
                "control": "Neem oil, insecticides"
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "panama_wilt": {
                "description": "Fungal disease",
                "symptoms": "Yellowing and wilting of leaves",
                "control": "Resistant varieties, soil fumigation"
            },
            "sigatoka_leaf_spot": {
                "description": "Fungal disease",
                "symptoms": "Leaf spots and streaks",
                "control": "Fungicides"
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "300-360 days after planting",
            "maturity_indicators": [
                "Fruits become plump",
                "Flower wilts and dries",
                "Individual fingers turn yellowish"
            ],
            "method": "Cut bunches with sharp knife"
        },

        "average_yield_per_hectare": "30-50 tonnes/ha",

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "89 kcal",
            "carbohydrates": "23 g",
            "protein": "1.1 g",
            "fiber": "2.6 g",
            "vitamin_C": "8.7 mg",
            "potassium": "358 mg"
        },

        "nutrition_explanation": [
            "Rich in potassium",
            "Good source of vitamin B6",
            "Contains dietary fiber",
            "Provides quick energy"
        ],

        "health_benefits": [
            "Supports heart health",
            "Aids digestion",
            "Boosts energy",
            "Helps manage blood pressure"
        ],

        "economic_importance": [
            "Major fruit crop",
            "Export potential",
            "Processing (chips, puree)",
            "Employment generation"
        ],

        "risk_factors": [
            "Cyclone damage",
            "Disease outbreaks",
            "Price fluctuation",
            "Short shelf life"
        ],

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "cyperus": {
                "description": "Nut grass, spreads through underground tubers",
                "damage": "Competes for nutrients and moisture",
                "control": "Deep ploughing and repeated removal"
            },
            "parthenium": {
                "description": "Invasive weed common in open fields",
                "damage": "Reduces yield and may cause allergies",
                "control": "Manual uprooting before flowering"
            },
            "amaranthus": {
                "description": "Fast-growing broadleaf weed",
                "damage": "Competes during early growth stage",
                "control": "Mechanical weeding"
            }
        },

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/banana.jpg",
            "pests": [
                "static/images/pests/banana_weevil.jpg",
                "static/images/pests/aphids.jpg"
            ],
            "diseases": [
                "static/images/diseases/panama_wilt.jpg",
                "static/images/diseases/sigatoka_leaf_spot.jpg"
            ],
            "weeds": [
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/amaranthus.jpg"
            ]
        }
    }
}
