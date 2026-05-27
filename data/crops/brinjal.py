crop_data = {
    "brinjal": {
        "name": "Brinjal (Eggplant)",
        "scientific_name": "Solanum melongena",
        "family": "Solanaceae",
        "category": "Vegetable Crop",
        "crop_type": "Solanaceous Vegetable",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Kharif (Jun-Jul), Rabi (Oct-Nov), Summer (Feb-Mar)",
        "duration_days": "90–120 days (variety dependent)",
        "climate": "Warm season crop, tropical to subtropical",
        "ideal_temperature": "25°C – 30°C",
        "germination_temperature": "25°C – 30°C",
        "rainfall_requirement_mm": "400 – 600 mm",
        "water_requirement_level": "Moderate",
        "sunlight_requirement": "Full sunlight required",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained loamy soil",
        "soil_ph_range": "5.5 – 6.5",
        "soil_depth_requirement": "Medium deep soil",
        "salinity_tolerance": "Moderate",
        "drainage_requirement": "Good drainage essential",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
"major_states": [
            "West Bengal",
            "Odisha",
            "Karnataka",
            "Maharashtra",
            "Tamil Nadu",
            "Andhra Pradesh",
            "Bihar"
        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "2-3 ploughings",
            "Add FYM 10-15 t/ha",
            "Form raised beds",
            "Ensure fine tilth"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Hybrid or OP varieties",
            "seed_rate_per_hectare": "400-500 g/ha",
            "varieties": "Pusa Purple, Pusa Kranti, Arka Keshav"
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Transplanting seedlings",
        "row_spacing": "60-75 cm",
        "plant_spacing": "45-60 cm",
        "sowing_depth": "1-2 cm",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "seedling_stage": {
                "duration": "0-30 days",
                "details": "Nursery raising and seedling growth."
            },
            "vegetative_stage": {
                "duration": "30-60 days",
                "details": "Plant growth and branch development."
            },
            "flowering_stage": {
                "duration": "60-90 days",
                "details": "Flowering and fruit set."
            },
            "fruit_development": {
                "duration": "90-120 days",
                "details": "Fruit growth and harvest."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_transplanting": "Light irrigation",
            "critical_stages": [
                "Flowering",
                "Fruit development"
            ],
            "frequency": "5-7 days interval",
            "avoid": "Waterlogging"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "15-20 t/ha FYM",
            "nitrogen": "100-150 kg/ha N",
            "phosphorus": "75-100 kg/ha P",
            "potassium": "75-100 kg/ha K"
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "fruit_borer": {
                "description": "Lepidopteran pest",
                "symptoms": "Holes in fruits, frass excretion",
                "control": "Insecticides, pheromone traps"
            },
            "aphids": {
                "description": "Sap-sucking insects",
                "symptoms": "Leaf curling, honeydew",
                "control": "Neem oil, insecticides"
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "wilt": {
                "description": "Fungal/bacterial wilt",
                "symptoms": "Wilting, yellowing",
                "control": "Resistant varieties, crop rotation"
            },
            "leaf_spot": {
                "description": "Fungal disease",
                "symptoms": "Brown spots on leaves",
                "control": "Fungicides"
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "60-75 days after transplanting",
            "maturity_indicators": [
                "Fruits develop glossy appearance",
                "Seeds not hardened",
                "Flesh still tender"
            ],
            "method": "Hand picking with scissors"
        },

        "average_yield_per_hectare": "25-40 tonnes/ha",

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "25 kcal",
            "carbohydrates": "6 g",
            "protein": "1 g",
            "fiber": "3 g",
            "vitamin_C": "2 mg",
            "potassium": "229 mg"
        },

        "nutrition_explanation": [
            "Low calorie vegetable",
            "Good fiber content",
            "Contains antioxidants",
            "Rich in minerals"
        ],

        "health_benefits": [
            "Aids digestion",
            "Weight management",
            "Heart health",
            "Blood sugar control"
        ],

        "economic_importance": [
            "Popular vegetable",
            "Year-round cultivation",
            "Good market demand",
            "Export potential"
        ],

        "risk_factors": [
            "Pest infestation",
            "Disease outbreaks",
            "Price fluctuation",
            "Drought sensitivity"
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
            "crop": "static/images/crops/brinjal.jpg",
            "pests": [
                "static/images/pests/fruit_borer.jpg",
                "static/images/pests/aphids.jpg"
            ],
            "diseases": [
                "static/images/diseases/wilt.jpg",
                "static/images/diseases/leaf_spot.jpg"
            ],
            "weeds": [
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/amaranthus.jpg"
            ]
        }
    }
}
