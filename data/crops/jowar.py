crop_data = {
    "jowar": {
        "name": "Jowar (Sorghum)",
        "scientific_name": "Sorghum bicolor",
        "family": "Poaceae",
        "category": "Cereal Crop",
        "crop_type": "Kharif fodder and grain crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Kharif (Jun-Jul), Rabi (Oct-Nov)",
        "duration_days": "90–120 days (variety dependent)",
        "climate": "Tropical and subtropical semi-arid climate",
        "ideal_temperature": "25°C – 35°C",
        "germination_temperature": "25°C – 30°C",
        "rainfall_requirement_mm": "400 – 600 mm",
        "water_requirement_level": "Low to Moderate",
        "sunlight_requirement": "Full sunlight required",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained deep loamy to clayey soil",
        "soil_ph_range": "5.5 – 8.0",
        "soil_depth_requirement": "Deep soil preferred",
        "salinity_tolerance": "Moderate to high",
        "drainage_requirement": "Good drainage essential",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Arunachal Pradesh",
            "Bihar",
            "Gujarat",
            "Haryana",
            "Jammu and Kashmir",
            "Karnataka",
            "Madhya Pradesh",
            "Maharashtra",
            "Nagaland",
            "Punjab",
            "Rajasthan",
            "Uttar Pradesh",
            "Uttarakhand",

        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "2-3 ploughings",
            "Add FYM 10-15 t/ha",
            "Level the field",
            "Prepare fine seedbed"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Improved varieties",
            "seed_rate_per_hectare": "8-10 kg/ha",
            "varieties": "CSV 15, CSV 18, SPV 1617"
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Line sowing",
        "row_spacing": "45-60 cm",
        "plant_spacing": "15-20 cm",
        "sowing_depth": "3-4 cm",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "seedling_stage": {
                "duration": "0-15 days",
                "details": "Germination and seedling establishment."
            },
            "vegetative_stage": {
                "duration": "15-45 days",
                "details": "Stem and leaf growth."
            },
            "flowering_stage": {
                "duration": "45-75 days",
                "details": "Panicle emergence and flowering."
            },
            "grain_development_stage": {
                "duration": "75-120 days",
                "details": "Grain filling and maturity."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_sowing": "First irrigation",
            "critical_stages": [
                "Flowering",
                "Grain filling"
            ],
            "frequency": "3-4 irrigations",
            "avoid": "Excess moisture"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "10-15 t/ha FYM",
            "nitrogen": "80-100 kg/ha N",
            "phosphorus": "40-50 kg/ha P",
            "potassium": "40-50 kg/ha K"
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "stem_borer": {
                "description": "Stem boring larvae",
                "symptoms": "Dead heart",
                "control": "Insecticides"
            },
            "shoot_fly": {
                "description": "Sap-sucking insect",
                "symptoms": "Dead seedlings",
                "control": "Seed treatment"
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "grain_mold": {
                "description": "Fungal disease",
                "symptoms": "Grain discoloration",
                "control": "Resistant varieties"
            },
            "rust": {
                "description": "Fungal disease",
                "symptoms": "Orange pustules on leaves",
                "control": "Fungicides"
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "90-120 days after sowing",
            "maturity_indicators": [
                "Grain hardens",
                "Panicle turns golden",
                "Leaves dry"
            ],
            "method": "Hand cutting or combine harvest"
        },

        "average_yield_per_hectare": "15-25 quintals/ha",

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "329 kcal",
            "protein": "10 g",
            "carbohydrates": "68 g",
            "fiber": "6 g",
            "iron": "4.4 mg"
        },

        "nutrition_explanation": [
            "Good carbohydrate source",
            "High in fiber",
            "Contains protein",
            "Gluten-free grain"
        ],

        "health_benefits": [
            "Provides sustained energy",
            "Aids digestion",
            "Heart health",
            "Blood sugar control"
        ],

        "economic_importance": [
            "Major cereal crop",
            "Fodder crop",
            "Industrial uses",
            "Export potential"
        ],

        "risk_factors": [
            "Drought sensitivity",
            "Pest infestation",
            "Bird damage",
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
            "trianthema": {
                "description": "Fast-growing broadleaf weed",
                "damage": "Competes during early growth stage",
                "control": "Mechanical weeding"
            }
        },

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/jowar.jpg",
            "pests": [
                "static/images/pests/stem_borer.jpg",
                "static/images/pests/shoot_fly.jpg"
            ],
            "diseases": [
                "static/images/diseases/grain_mold.jpg",
                "static/images/diseases/rust.jpg"
            ],
            "weeds": [
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/trianthema.jpg"
            ]
        }
    }
}
