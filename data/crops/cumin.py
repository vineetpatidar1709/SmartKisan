crop_data = {
    "cumin": {
        "name": "Cumin",
        "scientific_name": "Cuminum cyminum",
        "family": "Apiaceae",
        "category": "Spice Crop",
        "crop_type": "Herbaceous Spice",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Rabi (Oct-Dec)",
        "duration_days": "100–120 days (variety dependent)",
        "climate": "Semi-arid to subtropical climate",
        "ideal_temperature": "20°C – 30°C",
        "germination_temperature": "20°C – 25°C",
        "rainfall_requirement_mm": "300 – 500 mm",
        "water_requirement_level": "Low to Moderate",
        "sunlight_requirement": "Full sunlight required",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained sandy loam to loamy soil",
        "soil_ph_range": "6.5 – 8.0",
        "soil_depth_requirement": "Medium deep",
        "salinity_tolerance": "Moderate",
        "drainage_requirement": "Good drainage essential",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Gujarat",
            "Rajasthan",
            "Madhya Pradesh",
            "Uttar Pradesh",
            "Punjab"
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
            "seed_type": "Improved varieties",
            "seed_rate_per_hectare": "12-15 kg/ha",
            "varieties": "GC 1, GC 2, GC 3, RZ 19"
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Line sowing",
        "row_spacing": "25-30 cm",
        "plant_spacing": "10-15 cm",
        "sowing_depth": "1-2 cm",

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
                "details": "Plant growth and branching."
            },
            "flowering_stage": {
                "duration": "45-75 days",
                "details": "Flowering and fruit set."
            },
            "maturity_stage": {
                "duration": "75-120 days",
                "details": "Seed maturity and harvest."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_sowing": "Light irrigation",
            "critical_stages": [
                "Flowering",
                "Fruit development"
            ],
            "frequency": "4-5 light irrigations",
            "avoid": "Waterlogging"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "10-15 t/ha FYM",
            "nitrogen": "40-50 kg/ha N",
            "phosphorus": "40-50 kg/ha P",
            "potassium": "20-30 kg/ha K"
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
            "pod_borer": {
                "description": "Larvae feeding on pods",
                "symptoms": "Holes in pods",
                "control": "Insecticides"
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "wilt": {
                "description": "Fungal wilt",
                "symptoms": "Wilting of plants",
                "control": "Resistant varieties"
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
            "harvest_time": "100-120 days after sowing",
            "maturity_indicators": [
                "Leaves turn yellowish",
                "Plants dry",
                "Seeds turn brown"
            ],
            "method": "Hand picking or cutting"
        },

        "average_yield_per_hectare": "400-600 kg/ha",

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "375 kcal",
            "carbohydrates": "44 g",
            "protein": "18 g",
            "fiber": "11 g",
            "iron": "66 mg"
        },

        "nutrition_explanation": [
            "Rich in iron",
            "High in dietary fiber",
            "Good protein source",
            "Contains essential oils"
        ],

        "health_benefits": [
            "Aids digestion",
            "Anti-inflammatory",
            "Blood sugar control",
            "Immune support"
        ],

        "economic_importance": [
            "Major export commodity",
            "Spice industry",
            "Medicinal uses",
            "Local market demand"
        ],

        "risk_factors": [
            "Drought sensitivity",
            "Pest infestation",
            "Price fluctuation",
            "Disease outbreaks"
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
            "crop": "static/images/crops/cumin.jpg",
            "pests": [
                "static/images/pests/aphids.jpg",
                "static/images/pests/pod_borer.jpg"
            ],
            "diseases": [
                "static/images/diseases/wilt.jpg",
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
