crop_data = {
    "jute": {
        "name": "Jute",
        "scientific_name": "Corchorus capsularis / Corchorus olitorius",
        "family": "Malvaceae",
        "category": "Fiber Crop",
        "crop_type": "Fiber Crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Kharif (Mar-Jul planting)",
        "duration_days": "120–150 days (variety dependent)",
        "climate": "Tropical humid climate",
        "ideal_temperature": "25°C – 35°C",
        "germination_temperature": "25°C – 30°C",
        "rainfall_requirement_mm": "1000 – 1500 mm",
        "water_requirement_level": "High",
        "sunlight_requirement": "Full sunlight required",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained alluvial loamy soil",
        "soil_ph_range": "5.5 – 7.0",
        "soil_depth_requirement": "Medium to deep",
        "salinity_tolerance": "Moderate",
        "drainage_requirement": "Good drainage essential",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Andhra Pradesh",
            "Assam",
            "Bihar",
            "Meghalaya",
            "Odisha",
            "Tripura",
            "Uttar Pradesh",
            "West Bengal",

        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "2-3 ploughings",
            "Add FYM 10-15 t/ha",
            "Level the field",
            "Prepare raised beds"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Improved varieties",
            "seed_rate_per_hectare": "5-8 kg/ha",
            "varieties": "JRO 524, JRO 7835, S 19"
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Line sowing",
        "row_spacing": "25-30 cm",
        "plant_spacing": "Broadcasting",
        "sowing_depth": "2-3 cm",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "seedling_stage": {
                "duration": "0-15 days",
                "details": "Germination and seedling establishment."
            },
            "vegetative_stage": {
                "duration": "15-60 days",
                "details": "Rapid stem growth."
            },
            "flowering_stage": {
                "duration": "60-90 days",
                "details": "Flowering."
            },
            "maturity_stage": {
                "duration": "90-150 days",
                "details": "Fiber maturity and harvest."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_sowing": "First irrigation",
            "critical_stages": [
                "Vegetative growth",
                "Fiber formation"
            ],
            "frequency": "4-6 irrigations",
            "avoid": "Water stagnation"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "10-15 t/ha FYM",
            "nitrogen": "60-80 kg/ha N",
            "phosphorus": "30-40 kg/ha P",
            "potassium": "30-40 kg/ha K"
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "jute_weevil": {
                "description": "Stem borer",
                "symptoms": "Holes in stems",
                "control": "Insecticides"
            },
            "aphids": {
                "description": "Sap-sucking insects",
                "symptoms": "Leaf curling",
                "control": "Neem oil"
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "root_rot": {
                "description": "Fungal disease",
                "symptoms": "Root rotting, wilting",
                "control": "Crop rotation"
            },
            "leaf_curl": {
                "description": "Viral disease",
                "symptoms": "Leaf curling",
                "control": "Resistant varieties"
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "120-150 days after sowing",
            "maturity_indicators": [
                "Leaves turn yellow",
                "Stem becomes cylindrical",
                "Fiber easily separates"
            ],
            "method": "Cut stems at base"
        },

        "average_yield_per_hectare": "25-35 quintals/ha (fiber)",

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "Non-edible fiber crop",
            "fiber": "High",
            "cellulose": "60-70%"
        },

        "nutrition_explanation": [
            "Not a food crop",
            "Rich in natural fiber",
            "Biodegradable",
            "Eco-friendly material"
        ],

        "health_benefits": [
            "Jute fiber products are eco-friendly",
            "Used in medical textiles",
            "Sustainable material"
        ],

        "economic_importance": [
            "Major fiber crop",
            "Export commodity",
            "Textile industry",
            "Employment generation"
        ],

        "risk_factors": [
            "Weather fluctuations",
            "Pest infestation",
            "Price fluctuation",
            "Competition with synthetic fibers"
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
            "crop": "static/images/crops/jute.jpg",
            "pests": [
                "static/images/pests/jute_weevil.jpg",
                "static/images/pests/aphids.jpg"
            ],
            "diseases": [
                "static/images/diseases/root_rot.jpg",
                "static/images/diseases/leaf_curl.jpg"
            ],
            "weeds": [
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/trianthema.jpg"
            ]
        }
    }
}
