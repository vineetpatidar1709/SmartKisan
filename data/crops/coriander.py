crop_data = {
    "coriander": {
        "name": "Coriander",
        "scientific_name": "Coriandrum sativum",
        "family": "Apiaceae",
        "category": "Spice/Herb Crop",
        "crop_type": "Herb",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Rabi (Oct-Dec), Kharif (Jun-Jul)",
        "duration_days": "60–90 days (variety dependent)",
        "climate": "Cool season herb, tropical to subtropical",
        "ideal_temperature": "20°C – 25°C",
        "germination_temperature": "20°C – 25°C",
        "rainfall_requirement_mm": "250 – 500 mm",
        "water_requirement_level": "Low to Moderate",
        "sunlight_requirement": "Full sunlight to partial shade",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained sandy loam to loamy soil",
        "soil_ph_range": "6.0 – 8.0",
        "soil_depth_requirement": "Shallow to medium deep",
        "salinity_tolerance": "Moderate",
        "drainage_requirement": "Good drainage essential",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Rajasthan",
            "Gujarat",
            "Madhya Pradesh",
            "Andhra Pradesh",
            "Tamil Nadu",
            "Uttar Pradesh"
        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "Fine seedbed preparation",
            "2-3 ploughings",
            "Add FYM 10-15 t/ha",
            "Level the field"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Local varieties",
            "seed_rate_per_hectare": "10-15 kg/ha",
            "varieties": "Co 1, Co 2, Rajendra Swati"
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Broadcasting or line sowing",
        "row_spacing": "20-30 cm",
        "plant_spacing": "Broadcasting",
        "sowing_depth": "1-2 cm",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "vegetative_stage": {
                "duration": "0-40 days",
                "details": "Leaf growth."
            },
            "flowering_stage": {
                "duration": "40-60 days",
                "details": "Stem elongation and flowering."
            },
            "seed_development": {
                "duration": "60-90 days",
                "details": "Seed formation and maturity."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_sowing": "Light irrigation",
            "critical_stages": [
                "Vegetative growth",
                "Flowering"
            ],
            "frequency": "5-7 days interval",
            "avoid": "Waterlogging"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "10-15 t/ha FYM",
            "nitrogen": "30-50 kg/ha N",
            "phosphorus": "40-60 kg/ha P",
            "potassium": "40-60 kg/ha K"
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "aphids": {
                "description": "Sap-sucking insects",
                "symptoms": "Leaf curling, yellowing",
                "control": "Neem oil, insecticides"
            },
            "leaf_eater": {
                "description": "Caterpillars",
                "symptoms": "Holes in leaves",
                "control": "Insecticides"
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "powdery_mildew": {
                "description": "Fungal disease",
                "symptoms": "White powder on leaves",
                "control": "Sulfur fungicides"
            },
            "stem_rot": {
                "description": "Fungal disease",
                "symptoms": "Stem rotting",
                "control": "Crop rotation"
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "60-75 days for leaves, 90-120 days for seed",
            "maturity_indicators": [
                "Leaves ready for harvest",
                "Seeds turn brown",
                "Plants dry out"
            ],
            "method": "Hand picking or cutting"
        },

        "average_yield_per_hectare": "5-8 tonnes/ha (leaves), 500-800 kg/ha (seed)",

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "23 kcal",
            "carbohydrates": "4 g",
            "protein": "2 g",
            "fiber": "3 g",
            "vitamin_C": "21 mg"
        },

        "nutrition_explanation": [
            "Rich in vitamins",
            "Contains essential oils",
            "Good antioxidant content",
            "Low calorie herb"
        ],

        "health_benefits": [
            "Aids digestion",
            "Anti-inflammatory",
            "Blood sugar control",
            "Heart health"
        ],

        "economic_importance": [
            "Export commodity",
            "Spice industry",
            "Fresh market",
            "Processing"
        ],

        "risk_factors": [
            "Bolting in warm weather",
            "Pest infestation",
            "Price fluctuation"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
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
            "chenopodium": {
                "description": "Common weed in herb crops",
                "damage": "Competes for nutrients",
                "control": "Mechanical weeding"
            }
        },

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/coriander.jpg",
            "pests": [
                "static/images/pests/aphids.jpg",
                "static/images/pests/leaf_eater.jpg"
            ],
            "diseases": [
                "static/images/diseases/powdery_mildew.jpg",
                "static/images/diseases/stem_rot.jpg"
            ],
            "weeds": [
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/chenopodium.jpg"
            ]
        }
    }
}
