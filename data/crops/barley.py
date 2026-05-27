crop_data = {
    "barley": {
        "name": "Barley",
        "scientific_name": "Hordeum vulgare",
        "family": "Poaceae",
        "category": "Cereal Crop",
        "crop_type": "Rabi food and fodder grain crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Rabi (October–November sowing)",
        "duration_days": "120–150 days",
        "climate": "Cool and dry climate",
        "ideal_temperature": "12°C – 25°C",
        "germination_temperature": "15°C – 20°C",
        "rainfall_requirement_mm": "300 – 500 mm",
        "water_requirement_level": "Low to Moderate",
        "sunlight_requirement": "Full sunlight required for proper grain filling",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Loamy and well-drained soils",
        "soil_ph_range": "6.0 – 8.0",
        "soil_depth_requirement": "Moderate depth with good tilth",
        "salinity_tolerance": "Moderate (more tolerant than wheat)",
        "drainage_requirement": "Good drainage required to prevent root diseases",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Bihar",
            "Haryana",
            "Himachal Pradesh",
            "Jammu and Kashmir",
            "Madhya Pradesh",
            "Punjab",
            "Rajasthan",
            "Sikkim",
            "Uttar Pradesh",
            "Uttarakhand",
            "West Bengal",

        ],


        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "1–2 deep ploughings followed by harrowing",
            "Remove weeds and crop residues",
            "Apply 6–8 tons FYM per acre",
            "Level the field properly",
            "Prepare fine seedbed for uniform germination"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Certified high-yielding and disease-resistant varieties",
            "seed_rate_per_acre": "35–45 kg (irrigated), 30–35 kg (rainfed)",
            "seed_selection": "Bold, uniform and disease-free seeds",
            "seed_treatment": [
                "Treat seeds with fungicide to prevent smut diseases",
                "Use biofertilizer for better root growth",
                "Ensure proper drying before sowing"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Line sowing using seed drill",
        "row_spacing": "20–25 cm",
        "plant_spacing": "5–7 cm between plants",
        "sowing_depth": "4–5 cm depth",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "germination_stage": {
                "duration": "0–10 days",
                "details": "Seeds sprout and root system begins development."
            },
            "tillering_stage": {
                "duration": "20–40 days",
                "details": "Multiple shoots develop from base of plant."
            },
            "stem_elongation_stage": {
                "duration": "40–70 days",
                "details": "Rapid vertical growth and internode elongation."
            },
            "booting_stage": {
                "duration": "70–90 days",
                "details": "Head develops inside the leaf sheath."
            },
            "heading_and_flowering_stage": {
                "duration": "90–110 days",
                "details": "Spike emerges and flowering occurs."
            },
            "grain_filling_stage": {
                "duration": "110–140 days",
                "details": "Grains accumulate starch and mature."
            },
            "maturity_stage": {
                "duration": "120–150 days",
                "details": "Crop turns golden yellow and grains harden."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "first_irrigation": "At tillering stage",
            "critical_stages": [
                "Tillering stage",
                "Booting stage",
                "Grain filling stage"
            ],
            "frequency": "2–4 irrigations depending on rainfall",
            "avoid": "Excess irrigation at maturity stage"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "6–8 tons FYM per acre",
            "nitrogen": "40–60 kg/ha",
            "phosphorus": "30–40 kg/ha",
            "potassium": "20–30 kg/ha",
            "split_application": "Nitrogen applied in two splits",
            "biofertilizers": "Azotobacter culture recommended"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "phalaris_minor": {
                "description": "Grass weed resembling wheat in early stage.",
                "damage": "Competes heavily for nutrients and reduces yield.",
                "control": "Pre-emergence herbicide and timely hand weeding."
            },
            "chenopodium_album": {
                "description": "Broadleaf weed common in Rabi crops.",
                "damage": "Reduces plant population density.",
                "control": "Mechanical weeding during early stage."
            },
            "wild_oats": {
                "description": "Competitive grassy weed.",
                "damage": "Competes for sunlight and nutrients.",
                "control": "Use selective herbicide."
            },
            "melilotus": {
                "description": "Common winter weed in cereal crops.",
                "damage": "Suppresses barley growth.",
                "control": "Manual removal before flowering."
            }
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "aphids": {
                "description": "Sap sucking insects found on leaves and spikes.",
                "symptoms": "Yellowing and curling of leaves.",
                "control": "Neem oil or insecticide spray."
            },
            "armyworm": {
                "description": "Caterpillar feeding on leaves.",
                "symptoms": "Irregular holes in foliage.",
                "control": "Pheromone traps and spray."
            },
            "cutworm": {
                "description": "Soil insect cutting young seedlings at base.",
                "symptoms": "Seedlings fall suddenly.",
                "control": "Soil treatment before sowing."
            },
            "stem_borer": {
                "description": "Larvae bore into stems.",
                "symptoms": "Dry central shoot (dead heart).",
                "control": "Use recommended insecticide."
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "powdery_mildew": {
                "description": "White powdery fungal growth on leaves.",
                "symptoms": "Reduced photosynthesis and stunted growth.",
                "control": "Fungicide spray at early stage."
            },
            "rust": {
                "description": "Orange-brown pustules on leaf surface.",
                "symptoms": "Leaves dry prematurely.",
                "control": "Use resistant varieties."
            },
            "smut": {
                "description": "Fungal disease affecting grains.",
                "symptoms": "Grains replaced by black powdery mass.",
                "control": "Seed treatment before sowing."
            },
            "leaf_blight": {
                "description": "Fungal infection causing brown leaf lesions.",
                "symptoms": "Reduced grain filling.",
                "control": "Fungicide application."
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "120–150 days after sowing",
            "maturity_indicators": [
                "Crop turns golden yellow",
                "Grains hard and dry",
                "Moisture around 18–20%"
            ],
            "method": "Harvest using sickle or combine harvester"
        },

        "average_yield_per_acre": "12–20 quintals",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Dry grains to 12% moisture",
            "Clean and grade properly",
            "Store in cool and dry place",
            "Protect from storage pests"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "354 kcal",
            "protein": "12 g",
            "carbohydrates": "73 g",
            "fiber": "17 g",
            "iron": "3.6 mg",
            "magnesium": "133 mg"
        },

        "nutrition_explanation": [
            "Rich source of dietary fiber",
            "Helps in digestion",
            "Provides sustained energy",
            "Contains essential minerals"
        ],

        "health_benefits": [
            "Improves heart health",
            "Controls blood sugar levels",
            "Supports digestion",
            "Helps in weight management",
            "Reduces cholesterol"
        ],

        "economic_importance": [
            "Used in malt and beer industry",
            "Animal feed crop",
            "Health food products",
            "Export commodity"
        ],

        "risk_factors": [
            "Excess moisture reduces grain quality",
            "Rust outbreaks in humid weather",
            "Storage pest infestation"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/barley.jpg",
            "pests": [
                "static/images/pests/aphids.jpg",
                "static/images/pests/armyworm.jpg",
                "static/images/pests/cutworm.jpg",
                "static/images/pests/stem_borer.jpg"
            ],
            "diseases": [
                "static/images/diseases/powdery_mildew.jpg",
                "static/images/diseases/rust.jpg",
                "static/images/diseases/smut.jpg",
                "static/images/diseases/leaf_blight.jpg"
            ],
            "weeds": [
                "static/images/weeds/phalaris_minor.jpg",
                "static/images/weeds/chenopodium_album.jpg",
                "static/images/weeds/wild_oats.jpg",
                "static/images/weeds/melilotus.jpg"
            ]
        }
    }
}