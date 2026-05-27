crop_data = {
    "mango": {
        "name": "Mango",
        "scientific_name": "Mangifera indica",
        "family": "Anacardiaceae",
        "category": "Fruit Crop",
        "crop_type": "Tropical Fruit",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Kharif ( monsoon planting)",
        "duration_days": "Perennial (first harvest 3-6 years)",
        "climate": "Tropical to subtropical climate",
        "ideal_temperature": "24°C – 30°C",
        "germination_temperature": "25°C – 30°C",
        "rainfall_requirement_mm": "750 – 1500 mm",
        "water_requirement_level": "Moderate to High",
        "sunlight_requirement": "Full sunlight required",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Deep well-drained alluvial or laterite soil",
        "soil_ph_range": "5.5 – 7.5",
        "soil_depth_requirement": "Deep (1.5-2m)",
        "salinity_tolerance": "Low to moderate",
        "drainage_requirement": "Good drainage essential",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Andhra Pradesh",
            "Chhattisgarh",
            "Gujarat",
            "Jharkhand",
            "Karnataka",
            "Kerala",
            "Madhya Pradesh",
            "Rajasthan",
            "Telangana",
            "Uttar Pradesh",
            "West Bengal",

        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "Pit digging (1m x 1m x 1m)",
            "Add FYM and soil amendment",
            "Refill pits before planting",
            "Irrigate after planting"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Grafted saplings (vegetative propagation)",
            "planting_distance": "8-10m",
            "varieties": "Alphonso, Dashehari, Langra, Totapuri, Kesar"
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Planting grafted saplings",
        "row_spacing": "8-10 m",
        "plant_spacing": "8-10 m",
        "planting_depth": "At root collar",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "vegetative_growth": {
                "duration": "After planting to first harvest",
                "details": "Tree establishment and growth."
            },
            "flowering": {
                "duration": "Spring (Feb-April)",
                "details": "Panicle emergence and flowering."
            },
            "fruit_development": {
                "duration": "90-120 days",
                "details": "Fruit growth and maturity."
            },
            "harvest": {
                "duration": "June-August",
                "details": "Fruit ripening and harvest."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_planting": "First irrigation",
            "critical_stages": [
                "Flowering",
                "Fruit development"
            ],
            "frequency": "Monthly in dry season",
            "avoid": "Water stagnation"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "50-100 kg FYM per tree",
            "nitrogen": "1-2 kg N per tree",
            "phosphorus": "0.5-1 kg P per tree",
            "potassium": "1-1.5 kg K per tree"
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "mango_hopper": {
                "description": "Sap-sucking insect",
                "symptoms": "Leaf curling, honeydew",
                "control": "Insecticides"
            },
            "fruit_fly": {
                "description": "Fruit damaging pest",
                "symptoms": "Fruit rotting",
                "control": "Bagging, insecticides"
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "anthracnose": {
                "description": "Fungal disease",
                "symptoms": "Leaf spots, fruit rot",
                "control": "Fungicides"
            },
            "powdery_mildew": {
                "description": "Fungal disease",
                "symptoms": "White powder on leaves",
                "control": "Sulfur fungicides"
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "June-August",
            "maturity_indicators": [
                "Fruit develops characteristic color",
                "Stem end gives sweet smell",
                "Specific gravity changes"
            ],
            "method": "Hand picking"
        },

        "average_yield_per_hectare": "10-15 tonnes/ha",

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "60 kcal",
            "carbohydrates": "15 g",
            "protein": "0.8 g",
            "fiber": "1.6 g",
            "vitamin_C": "36 mg",
            "vitamin_A": "1082 IU"
        },

        "nutrition_explanation": [
            "Rich in vitamin A and C",
            "Good fiber content",
            "Contains antioxidants",
            "Natural sweetness"
        ],

        "health_benefits": [
            "Boosts immunity",
            "Aids digestion",
            "Eye health",
            "Heart health"
        ],

        "economic_importance": [
            "King of fruits",
            "Export commodity",
            "Processing industry",
            "Local market demand"
        ],

        "risk_factors": [
            "Alternate bearing",
            "Storm damage",
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
            "crop": "static/images/crops/mango.jpg",
            "pests": [
                "static/images/pests/mango_hopper.jpg",
                "static/images/pests/fruit_fly.jpg"
            ],
            "diseases": [
                "static/images/diseases/anthracnose.jpg",
                "static/images/diseases/powdery_mildew.jpg"
            ],
            "weeds": [
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/trianthema.jpg"
            ]
        }
    }
}
