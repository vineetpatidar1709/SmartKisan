crop_data = {
    "chili": {
        "name": "Chili (Hot Pepper)",
        "scientific_name": "Capsicum annuum",
        "family": "Solanaceae",
        "category": "Vegetable/Spice Crop",
        "crop_type": "Solanaceous Vegetable",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Kharif (Jun-Jul), Rabi (Oct-Nov), Summer (Feb-Mar)",
        "duration_days": "90–120 days (variety dependent)",
        "climate": "Warm season crop, tropical to subtropical",
        "ideal_temperature": "25°C – 30°C",
        "germination_temperature": "25°C – 30°C",
        "rainfall_requirement_mm": "600 – 1000 mm",
        "water_requirement_level": "Moderate to High",
        "sunlight_requirement": "Full sunlight required",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained sandy loam to loamy soil",
        "soil_ph_range": "6.0 – 7.0",
        "soil_depth_requirement": "Medium deep, well-drained",
        "salinity_tolerance": "Moderate",
        "drainage_requirement": "Good drainage essential",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
"major_states": [
            "Andhra Pradesh",
            "Karnataka",
            "Maharashtra",
            "Nagaland",
            "Odisha",
            "Tamil Nadu",
            "Telangana",
            "West Bengal",

        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "2-3 ploughings",
            "Add FYM 15-20 t/ha",
            "Form raised beds",
            "Apply basal fertilizers"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Hybrid or OP varieties",
            "seed_rate_per_hectare": "1.0-1.5 kg/ha",
            "varieties": "Byadgi, Guntur, Kashmiri, Jwala"
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
                "details": "Plant growth and branching."
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
                "description": "Capsicum fruit borer",
                "symptoms": "Holes in fruits",
                "control": "Insecticides, pheromone traps"
            },
            "thrips": {
                "description": "Sap-sucking insects",
                "symptoms": "Leaf curling, silvery patches",
                "control": "Neem oil, insecticides"
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "powdery_mildew": {
                "description": "Fungal disease",
                "symptoms": "White powdery coating on leaves",
                "control": "Sulfur fungicides"
            },
            "bacterial_wilt": {
                "description": "Bacterial disease",
                "symptoms": "Wilting, brown vascular tissues",
                "control": "Resistant varieties"
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "75-90 days after transplanting",
            "maturity_indicators": [
                "Fruits turn red/green",
                "Flesh becomes firm",
                "Seeds not fully mature (for green chili)"
            ],
            "method": "Hand picking at intervals"
        },

        "average_yield_per_hectare": "10-15 tonnes/ha (green), 2-3 tonnes/ha (dry)",

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "40 kcal",
            "carbohydrates": "9 g",
            "protein": "2 g",
            "fiber": "1.5 g",
            "vitamin_C": "144 mg",
            "vitamin_A": "370 IU"
        },

        "nutrition_explanation": [
            "Extremely rich in vitamin C",
            "Good source of vitamin A",
            "Contains capsaicin",
            "Antioxidant properties"
        ],

        "health_benefits": [
            "Boosts metabolism",
            "Pain relief",
            "Heart health",
            "Immune support"
        ],

        "economic_importance": [
            "Major spice crop",
            "Export commodity",
            "Processing industry",
            "Local market demand"
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
            "crop": "static/images/crops/chili.jpg",
            "pests": [
                "static/images/pests/fruit_borer.jpg",
                "static/images/pests/thrips.jpg"
            ],
            "diseases": [
                "static/images/diseases/powdery_mildew.jpg",
                "static/images/diseases/bacterial_wilt.jpg"
            ],
            "weeds": [
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/amaranthus.jpg"
            ]
        }
    }
}
