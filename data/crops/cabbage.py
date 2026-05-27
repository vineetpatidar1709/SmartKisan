crop_data = {
    "cabbage": {
        "name": "Cabbage",
        "scientific_name": "Brassica oleracea var. capitata",
        "family": "Brassicaceae",
        "category": "Vegetable Crop",
        "crop_type": "Leafy Vegetable",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Rabi (Oct-Dec), Summer in hills (Mar-May)",
        "duration_days": "70–100 days (variety dependent)",
        "climate": "Cool season crop, temperate origin",
        "ideal_temperature": "15°C – 20°C",
        "germination_temperature": "20°C – 25°C",
        "rainfall_requirement_mm": "500 – 700 mm",
        "water_requirement_level": "Moderate to High",
        "sunlight_requirement": "Full sunlight, tolerant to partial shade",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained fertile loamy soil",
        "soil_ph_range": "6.0 – 7.5",
        "soil_depth_requirement": "Medium deep, rich in organic matter",
        "salinity_tolerance": "Moderate",
        "drainage_requirement": "Good drainage essential",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
"major_states": [
            "Odisha",
            "West Bengal",
            "Maharashtra",
            "Karnataka",
            "Tamil Nadu",
            "Uttar Pradesh",
            "Madhya Pradesh"
        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "2-3 ploughings",
            "Add well-decomposed FYM 20-25 t/ha",
            "Form raised beds",
            "Apply NPK basal dose"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Hybrid or OP varieties",
            "seed_rate_per_hectare": "400-500 g/ha",
            "varieties": "Pusa Cabbage, Golden Acre, Pride of India"
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Transplanting seedlings",
        "row_spacing": "45-60 cm",
        "plant_spacing": "30-45 cm",
        "sowing_depth": "1-2 cm",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "seedling_stage": {
                "duration": "0-25 days",
                "details": "Nursery raising and seedling growth."
            },
            "vegetative_stage": {
                "duration": "25-50 days",
                "details": "Leaf expansion and head initiation."
            },
            "head_formation": {
                "duration": "50-80 days",
                "details": "Head development and compacting."
            },
            "maturity": {
                "duration": "80-100 days",
                "details": "Head maturity and harvest."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_transplanting": "Light irrigation",
            "critical_stages": [
                "Head formation",
                "Head maturation"
            ],
            "frequency": "5-7 days interval",
            "avoid": "Drought stress"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "20-25 t/ha FYM",
            "nitrogen": "100-150 kg/ha N",
            "phosphorus": "75-100 kg/ha P",
            "potassium": "75-100 kg/ha K"
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "diamondback_moth": {
                "description": "Leaf-feeding caterpillar",
                "symptoms": "Skeletonized leaves",
                "control": "Insecticides, biological control"
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
            "black_rot": {
                "description": "Bacterial disease",
                "symptoms": "V-shaped yellow lesions on leaves",
                "control": "Resistant varieties, copper fungicides"
            },
            "clubroot": {
                "description": "Soil-borne disease",
                "symptoms": "Wilting, root swelling",
                "control": "Lime application, crop rotation"
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "70-90 days after transplanting",
            "maturity_indicators": [
                "Head becomes firm and compact",
                "Outer leaves turn yellowish",
                "Proper size attained"
            ],
            "method": "Cut with sharp knife leaving outer leaves"
        },

        "average_yield_per_hectare": "30-50 tonnes/ha",

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "25 kcal",
            "carbohydrates": "6 g",
            "protein": "1.3 g",
            "fiber": "2.5 g",
            "vitamin_C": "36.6 mg",
            "vitamin_K": "76 mcg"
        },

        "nutrition_explanation": [
            "Rich in vitamin C",
            "Good source of vitamin K",
            "Contains antioxidants",
            "Low calorie vegetable"
        ],

        "health_benefits": [
            "Supports immune system",
            "Aids digestion",
            "Anti-inflammatory properties",
            "Heart health"
        ],

        "economic_importance": [
            "Popular vegetable",
            "Processing industry (pickles)",
            "Export potential",
            "Year-round cultivation"
        ],

        "risk_factors": [
            "Bolting in warm weather",
            "Pest infestation",
            "Disease outbreaks",
            "Price fluctuation"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "chenopodium_album": {
                "description": "Common lambsquarters, broadleaf weed",
                "damage": "Competes for nutrients in early growth",
                "control": "Mechanical weeding"
            },
            "cyperus": {
                "description": "Nut grass, spreads through underground tubers",
                "damage": "Competes for nutrients and moisture",
                "control": "Deep ploughing and repeated removal"
            },
            "parthenium": {
                "description": "Invasive weed common in open fields",
                "damage": "Reduces yield and may cause allergies",
                "control": "Manual uprooting before flowering"
            }
        },

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/cabbage.jpg",
            "pests": [
                "static/images/pests/diamondback_moth.jpg",
                "static/images/pests/aphids.jpg"
            ],
            "diseases": [
                "static/images/diseases/black_rot.jpg",
                "static/images/diseases/clubroot.jpg"
            ],
            "weeds": [
                "static/images/weeds/chenopodium_album.jpg",
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/parthenium.jpg"
            ]
        }
    }
}
