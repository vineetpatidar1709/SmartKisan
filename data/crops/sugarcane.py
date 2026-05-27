crop_data = {
    "sugarcane": {
        "name": "Sugarcane",
        "scientific_name": "Saccharum officinarum",
        "family": "Poaceae",
        "category": "Cash Crop",
        "crop_type": "Industrial Sugar Crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Spring (Feb–Mar), Autumn (Sept–Oct), Suru (Jan–Feb in some regions)",
        "duration_days": "300–365 days (10–12 months)",
        "climate": "Tropical and subtropical climate",
        "ideal_temperature": "20°C – 35°C",
        "germination_temperature": "25°C – 32°C",
        "rainfall_requirement_mm": "1000 – 1500 mm",
        "water_requirement_level": "Very High",
        "sunlight_requirement": "Full sunlight essential for high sugar accumulation",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Deep fertile loam to clay loam soil",
        "soil_ph_range": "6.0 – 8.0",
        "soil_depth_requirement": "Deep soil (at least 1 meter) for root penetration",
        "salinity_tolerance": "Moderate (some tolerant varieties available)",
        "drainage_requirement": "Good drainage required to avoid root rot",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Arunachal Pradesh",
            "Assam",
            "Bihar",
            "Chhattisgarh",
            "Gujarat",
            "Haryana",
            "Jharkhand",
            "Karnataka",
            "Maharashtra",
            "Nagaland",
            "Odisha",
            "Punjab",
            "Rajasthan",
            "Tamil Nadu",
            "Tripura",
            "Uttar Pradesh",
            "Uttarakhand",
            "West Bengal",

        ],


        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "Deep ploughing up to 30 cm depth",
            "2–3 cross harrowings",
            "Incorporate 15–20 tons FYM per acre",
            "Prepare ridges and furrows",
            "Ensure proper irrigation channels"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Healthy disease-free cane setts (2–3 budded)",
            "seed_rate_per_acre": "3000–4000 two-budded setts",
            "seed_selection": "Select canes from 8–10 month old healthy crop",
            "seed_treatment": [
                "Hot water treatment to prevent red rot",
                "Fungicide dip before planting",
                "Trichoderma treatment for soil disease protection"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Planting cane setts in furrows",
        "row_spacing": "75–120 cm",
        "plant_spacing": "Setts placed end-to-end in furrows",
        "sowing_depth": "5–10 cm depth",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "germination_stage": {
                "duration": "0–30 days",
                "details": "Buds sprout and roots develop."
            },
            "tillering_stage": {
                "duration": "30–90 days",
                "details": "Multiple shoots emerge from base."
            },
            "grand_growth_stage": {
                "duration": "90–210 days",
                "details": "Rapid elongation and biomass accumulation."
            },
            "maturity_stage": {
                "duration": "210–365 days",
                "details": "Sugar accumulation increases; stalks harden."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_planting": "Light irrigation for sett germination",
            "critical_stages": [
                "Tillering stage",
                "Grand growth stage"
            ],
            "frequency": "Every 7–12 days depending on soil and climate",
            "avoid": "Waterlogging to prevent root diseases"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "15–20 tons FYM per acre",
            "nitrogen": "150–250 kg/ha split doses",
            "phosphorus": "60 kg/ha basal dose",
            "potassium": "100 kg/ha",
            "micronutrients": "Zinc and Iron if deficient",
            "biofertilizers": "Azotobacter and PSB recommended"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "cyperus_rotundus": {
                "description": "Nut grass spreading through underground tubers.",
                "damage": "Reduces yield and competes for nutrients.",
                "control": "Deep ploughing and herbicide."
            },
            "parthenium": {
                "description": "Invasive broadleaf weed.",
                "damage": "Heavy nutrient competition.",
                "control": "Manual removal before flowering."
            },
            "sorghum_halepense": {
                "description": "Johnson grass weed.",
                "damage": "Competes during early stage.",
                "control": "Pre-emergence herbicide."
            },
            "amaranthus": {
                "description": "Fast-growing weed.",
                "damage": "Reduces crop growth.",
                "control": "Mechanical weeding."
            }
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "early_shoot_borer": {
                "description": "Larvae bore into young shoots.",
                "symptoms": "Dead hearts in young plants.",
                "control": "Soil insecticide and field sanitation."
            },
            "top_borer": {
                "description": "Attacks growing point.",
                "symptoms": "White patches on leaves.",
                "control": "Pheromone traps and insecticide."
            },
            "pyrilla": {
                "description": "Sap sucking insect.",
                "symptoms": "Yellowing leaves and reduced sugar.",
                "control": "Biological control and spray."
            },
            "white_grub": {
                "description": "Soil pest feeding on roots.",
                "symptoms": "Wilting plants.",
                "control": "Soil treatment before planting."
            },
            "mealy_bug": {
                "description": "Sucks sap from stalks.",
                "symptoms": "Stunted growth.",
                "control": "Biological and chemical control."
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "red_rot": {
                "description": "Serious fungal disease of sugarcane.",
                "symptoms": "Red discoloration inside stalk.",
                "control": "Resistant varieties and hot water treatment."
            },
            "smut": {
                "description": "Fungal disease forming whip-like structures.",
                "symptoms": "Black whip emergence.",
                "control": "Use healthy seed cane."
            },
            "wilt": {
                "description": "Fungal soil-borne disease.",
                "symptoms": "Drying and yellowing of leaves.",
                "control": "Crop rotation."
            },
            "grassy_shoot": {
                "description": "Mycoplasma disease.",
                "symptoms": "Thin grassy shoots.",
                "control": "Remove infected clumps."
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "10–12 months after planting",
            "maturity_indicators": [
                "Stalk hardening",
                "Maximum sugar content",
                "Dry lower leaves"
            ],
            "method": "Cut close to ground level using knife or harvester"
        },

        "average_yield_per_acre": "300–400 quintals",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Transport immediately to sugar mill",
            "Avoid delay to prevent sugar loss",
            "Maintain cleanliness during transport"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "270 kcal (juice)",
            "carbohydrates": "73 g",
            "fiber": "0.5 g",
            "calcium": "13 mg",
            "iron": "0.6 mg",
            "potassium": "63 mg"
        },

        "nutrition_explanation": [
            "High natural sugar content",
            "Quick energy source",
            "Contains small amount of minerals",
            "Used in jaggery and sugar production"
        ],

        "health_benefits": [
            "Provides instant energy",
            "Hydrates body",
            "Supports liver health",
            "Used in traditional medicine"
        ],

        "economic_importance": [
            "Major industrial crop",
            "Raw material for sugar industry",
            "Used in ethanol production",
            "Provides rural employment"
        ],

        "risk_factors": [
            "High water requirement",
            "Disease outbreaks like red rot",
            "Price fluctuation",
            "Climate sensitivity"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/sugarcane.jpg",
            "pests": [
                "static/images/pests/early_shoot_borer.jpg",
                "static/images/pests/top_borer.jpg",
                "static/images/pests/pyrilla.jpg",
                "static/images/pests/white_grub.jpg",
                "static/images/pests/mealy_bug.jpg"
            ],
            "diseases": [
                "static/images/diseases/red_rot.jpg",
                "static/images/diseases/smut.jpg",
                "static/images/diseases/wilt.jpg",
                "static/images/diseases/grassy_shoot.jpg"
            ],
            "weeds": [
                "static/images/weeds/cyperus_rotundus.jpg",
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/sorghum_halepense.jpg",
                "static/images/weeds/amaranthus.jpg"
            ]
        }
    }
}