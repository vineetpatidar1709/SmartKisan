crop_data = {
    "potato": {
        "name": "Potato",
        "scientific_name": "Solanum tuberosum",
        "family": "Solanaceae",
        "category": "Vegetable Crop",
        "crop_type": "Tuber Crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Rabi (Oct–Nov), Kharif in hills (May–June)",
        "duration_days": "90–120 days (variety dependent)",
        "climate": "Cool temperate to subtropical climate",
        "ideal_temperature": "15°C – 25°C",
        "germination_temperature": "18°C – 22°C",
        "rainfall_requirement_mm": "500 – 700 mm",
        "water_requirement_level": "Moderate",
        "sunlight_requirement": "Full sunlight required for tuber formation",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained sandy loam to loamy soil",
        "soil_ph_range": "5.5 – 6.8",
        "soil_depth_requirement": "Loose deep soil for tuber expansion",
        "salinity_tolerance": "Low",
        "drainage_requirement": "Excellent drainage to prevent tuber rot",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Arunachal Pradesh",
            "Assam",
            "Bihar",
            "Gujarat",
            "Haryana",
            "Himachal Pradesh",
            "Jharkhand",
            "Madhya Pradesh",
            "Meghalaya",
            "Nagaland",
            "Punjab",
            "Sikkim",
            "Tripura",
            "Uttarakhand",
            "Uttar Pradesh",
            "West Bengal",

        ],


        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "2–3 deep ploughings to loosen soil",
            "Remove stones and crop residues",
            "Incorporate 10–12 tons FYM per acre",
            "Prepare ridges and furrows",
            "Ensure fine tilth for proper tuber development"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Certified disease-free seed tubers",
            "seed_rate_per_acre": "800–1000 kg seed tubers",
            "seed_selection": "Healthy medium-sized tubers (25–50 g each)",
            "seed_treatment": [
                "Treat with fungicide before planting",
                "Avoid damaged or cut infected tubers",
                "Bio-fungicide treatment for soil disease prevention"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Planting seed tubers in ridges",
        "row_spacing": "60 cm",
        "plant_spacing": "20 cm between plants",
        "sowing_depth": "5–7 cm depth",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "sprouting_stage": {
                "duration": "0–15 days",
                "details": "Sprouts emerge from planted tubers."
            },
            "vegetative_stage": {
                "duration": "15–40 days",
                "details": "Rapid leaf and stem growth."
            },
            "tuber_initiation_stage": {
                "duration": "30–50 days",
                "details": "Small tubers begin forming underground."
            },
            "tuber_development_stage": {
                "duration": "50–90 days",
                "details": "Tuber enlargement and starch accumulation."
            },
            "maturity_stage": {
                "duration": "90–120 days",
                "details": "Leaves yellow and dry; tubers reach full size."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_planting": "Light irrigation for sprouting",
            "critical_stages": [
                "Tuber initiation stage",
                "Tuber development stage"
            ],
            "frequency": "Every 7–10 days depending on soil type",
            "avoid": "Waterlogging as it causes tuber rot and late blight"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "10–12 tons FYM per acre",
            "nitrogen": "120 kg/ha split doses",
            "phosphorus": "60 kg/ha basal dose",
            "potassium": "100 kg/ha",
            "micronutrients": "Zinc and Boron if deficient",
            "biofertilizers": "Azotobacter recommended"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "cyperus_rotundus": {
                "description": "Nut grass spreading through underground tubers.",
                "damage": "Competes for nutrients and moisture.",
                "control": "Deep ploughing and manual removal."
            },
            "amaranthus": {
                "description": "Fast growing broadleaf weed.",
                "damage": "Shades young potato plants.",
                "control": "Mechanical weeding."
            },
            "chenopodium": {
                "description": "Common winter weed.",
                "damage": "Reduces crop growth during early stages.",
                "control": "Timely hand weeding."
            },
            "parthenium": {
                "description": "Invasive weed in open fields.",
                "damage": "Competes heavily for nutrients.",
                "control": "Manual uprooting."
            }
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "cutworm": {
                "description": "Caterpillar cutting plants at soil surface.",
                "symptoms": "Young plants collapse overnight.",
                "control": "Soil insecticide and field sanitation."
            },
            "aphids": {
                "description": "Sap sucking insects transmitting viral diseases.",
                "symptoms": "Leaf curling and yellowing.",
                "control": "Systemic insecticide spray."
            },
            "potato_tuber_moth": {
                "description": "Larvae bore into tubers.",
                "symptoms": "Tunnels in tubers.",
                "control": "Proper earthing up and storage hygiene."
            },
            "white_grub": {
                "description": "Soil pest feeding on roots and tubers.",
                "symptoms": "Wilting and damaged tubers.",
                "control": "Soil treatment before planting."
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "late_blight": {
                "description": "Serious fungal disease under cool humid conditions.",
                "symptoms": "Brown leaf lesions and tuber rot.",
                "control": "Preventive fungicide spray."
            },
            "early_blight": {
                "description": "Fungal disease causing concentric leaf spots.",
                "symptoms": "Leaf drying and reduced yield.",
                "control": "Fungicide spray and crop rotation."
            },
            "black_scurf": {
                "description": "Soil-borne fungal disease affecting tubers.",
                "symptoms": "Black patches on tubers.",
                "control": "Seed treatment and crop rotation."
            },
            "bacterial_wilt": {
                "description": "Bacterial infection causing sudden wilting.",
                "symptoms": "Plant collapse and brown vascular tissues.",
                "control": "Use resistant varieties and sanitation."
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "90–120 days after planting",
            "maturity_indicators": [
                "Leaves turn yellow and dry",
                "Skin of tubers becomes firm",
                "Tuber size fully developed"
            ],
            "method": "Uproot using digger or manually; avoid bruising"
        },

        "average_yield_per_acre": "80–120 quintals",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Cure tubers in shade before storage",
            "Store in cool, ventilated storage",
            "Avoid exposure to sunlight (prevents greening)"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "77 kcal",
            "carbohydrates": "17 g",
            "protein": "2 g",
            "fiber": "2.2 g",
            "vitamin_C": "19 mg",
            "potassium": "425 mg"
        },

        "nutrition_explanation": [
            "Rich source of carbohydrates",
            "Good source of vitamin C",
            "Contains dietary fiber",
            "High potassium content"
        ],

        "health_benefits": [
            "Provides energy",
            "Supports heart health",
            "Improves digestion",
            "Boosts immunity",
            "Helps maintain blood pressure"
        ],

        "economic_importance": [
            "Staple vegetable crop",
            "Used in chips and processing industry",
            "High market demand",
            "Export potential crop"
        ],

        "risk_factors": [
            "Late blight outbreak risk",
            "Price fluctuation",
            "Storage losses due to rot",
            "Pest attack during tuber stage"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/potato.jpg",
            "pests": [
                "static/images/pests/cutworm.jpg",
                "static/images/pests/aphids.jpg",
                "static/images/pests/potato_tuber_moth.jpg",
                "static/images/pests/white_grub.jpg"
            ],
            "diseases": [
                "static/images/diseases/late_blight.jpg",
                "static/images/diseases/early_blight.jpg",
                "static/images/diseases/black_scurf.jpg",
                "static/images/diseases/bacterial_wilt.jpg"
            ],
            "weeds": [
                "static/images/weeds/cyperus_rotundus.jpg",
                "static/images/weeds/amaranthus.jpg",
                "static/images/weeds/chenopodium.jpg",
                "static/images/weeds/parthenium.jpg"
            ]
        }
    }
}