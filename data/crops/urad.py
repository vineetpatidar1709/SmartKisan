crop_data = {
    "urad": {
        "name": "Urad (Black Gram)",
        "scientific_name": "Vigna mungo",
        "family": "Fabaceae",
        "category": "Pulse Crop",
        "crop_type": "Leguminous Kharif pulse",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Kharif (Jun-Jul), Rabi (Feb-Mar in South)",
        "duration_days": "60–90 days (variety dependent)",
        "climate": "Tropical and subtropical climate",
        "ideal_temperature": "25°C – 35°C",
        "germination_temperature": "25°C – 30°C",
        "rainfall_requirement_mm": "600 – 900 mm",
        "water_requirement_level": "Moderate",
        "sunlight_requirement": "Full sunlight required",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained loamy to sandy loam soil",
        "soil_ph_range": "5.5 – 7.5",
        "soil_depth_requirement": "Medium deep",
        "salinity_tolerance": "Low to moderate",
        "drainage_requirement": "Good drainage essential",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Assam",
            "Bihar",
            "Chhattisgarh",
            "Gujarat",
            "Haryana",
            "Jharkhand",
            "Karnataka",
            "Madhya Pradesh",
            "Maharashtra",
            "Punjab",
            "Rajasthan",
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
            "Prepare beds"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Improved varieties",
            "seed_rate_per_hectare": "20-25 kg/ha",
            "varieties": "PU 19, T 9, Barkha"
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Line sowing",
        "row_spacing": "30-45 cm",
        "plant_spacing": "10-15 cm",
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
                "duration": "15-35 days",
                "details": "Vegetative growth and branching."
            },
            "flowering_stage": {
                "duration": "35-55 days",
                "details": "Flowering and pod set."
            },
            "maturity_stage": {
                "duration": "55-90 days",
                "details": "Pod development and harvest."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_sowing": "First irrigation",
            "critical_stages": [
                "Flowering",
                "Pod development"
            ],
            "frequency": "4-5 light irrigations",
            "avoid": "Water stagnation"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "10-15 t/ha FYM",
            "nitrogen": "20-25 kg/ha N",
            "phosphorus": "40-50 kg/ha P",
            "potassium": "20-25 kg/ha K"
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
            "mosaic_virus": {
                "description": "Viral disease",
                "symptoms": "Mottled leaves",
                "control": "Resistant varieties"
            },
            "root_rot": {
                "description": "Fungal disease",
                "symptoms": "Root rotting, wilting",
                "control": "Crop rotation"
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "60-90 days after sowing",
            "maturity_indicators": [
                "Pods turn black",
                "Leaves shed",
                "Seeds hard"
            ],
            "method": "Hand picking or cutting"
        },

        "average_yield_per_hectare": "800-1200 kg/ha",

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "341 kcal",
            "protein": "24 g",
            "carbohydrates": "60 g",
            "fiber": "18 g",
            "iron": "7.3 mg"
        },

        "nutrition_explanation": [
            "High protein content",
            "Rich in fiber",
            "Good iron source",
            "Low fat"
        ],

        "health_benefits": [
            "Improves digestion",
            "Boosts energy",
            "Supports heart health",
            "Strengthens bones"
        ],

        "economic_importance": [
            "Major pulse crop",
            "Export commodity",
            "Processing industry",
            "Local consumption"
        ],

        "risk_factors": [
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
            "crop": "static/images/crops/urad.jpg",
            "pests": [
                "static/images/pests/aphids.jpg",
                "static/images/pests/pod_borer.jpg"
            ],
            "diseases": [
                "static/images/diseases/mosaic_virus.jpg",
                "static/images/diseases/root_rot.jpg"
            ],
            "weeds": [
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/trianthema.jpg"
            ]
        }
    }
}
