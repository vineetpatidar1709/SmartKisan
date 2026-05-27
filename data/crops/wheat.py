crop_data = {
    "wheat": {
        "name": "Wheat",
        "scientific_name": "Triticum aestivum",
        "family": "Poaceae",
        "category": "Cereal Crop",
        "crop_type": "Staple Food Grain Crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
"season": "Wheat is a Rabi crop sown in October-December with harvest in March-April. It requires cool weather during vegetative growth and warm dry weather during ripening. Timely sowing in November gives highest yields.",
        "duration_days": "Wheat varieties take 110-150 days from sowing to harvest. Early sown varieties mature in 110-130 days while late sown varieties may take 140-150 days. Duration varies with variety, sowing time and environmental conditions.",
        "climate": "Wheat requires cool and dry climate during growth period and warm sunny weather during maturity. Optimum temperature for germination is 20-25°C, for vegetative growth 15-20°C, and for grain filling 21-26°C. Frost during flowering reduces yield.",
        "ideal_temperature": "Ideal temperature range for wheat is 15-25°C. Lower temperatures during tillering promote more tillers while higher temperatures during grain filling improve grain quality. Extreme heat above 35°C causes heat stress.",
        "germination_temperature": "20°C – 25°C",
        "rainfall_requirement_mm": "450 – 650 mm",
        "water_requirement_level": "Moderate",
        "sunlight_requirement": "Full sunlight required for grain filling",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained loam to clay loam soil",
        "soil_ph_range": "6.0 – 7.5",
        "soil_depth_requirement": "Deep fertile soil rich in organic matter",
        "salinity_tolerance": "Moderate",
        "drainage_requirement": "Good drainage essential to prevent root diseases",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Arunachal Pradesh",
            "Bihar",
            "Chhattisgarh",
            "Gujarat",
            "Haryana",
            "Himachal Pradesh",
            "Jammu and Kashmir",
            "Jharkhand",
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
            "2–3 ploughings to obtain fine tilth",
            "Remove weeds and previous crop residues",
            "Incorporate 8–10 tons FYM per acre",
            "Level field properly for uniform irrigation",
            "Ensure proper bunding"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Certified high-yielding or disease-resistant varieties",
            "seed_rate_per_acre": "40–50 kg",
            "seed_selection": "Healthy, bold and disease-free seeds",
            "seed_treatment": [
                "Treat with fungicide to prevent smut and rust",
                "Biofertilizer treatment for better root growth",
                "Use treated seeds to avoid seed-borne diseases"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Line sowing using seed drill",
        "row_spacing": "20–22 cm",
        "plant_spacing": "Continuous line sowing",
        "sowing_depth": "4–5 cm depth",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "germination_stage": {
                "duration": "0–7 days",
                "details": "Seed germination and emergence of coleoptile."
            },
            "tillering_stage": {
                "duration": "20–45 days",
                "details": "Formation of multiple tillers from base."
            },
            "jointing_stage": {
                "duration": "45–65 days",
                "details": "Stem elongation and node formation."
            },
            "booting_stage": {
                "duration": "65–85 days",
                "details": "Ear head develops inside leaf sheath."
            },
            "heading_stage": {
                "duration": "85–100 days",
                "details": "Ear emerges from sheath."
            },
            "grain_filling_stage": {
                "duration": "100–130 days",
                "details": "Grain accumulates starch and nutrients."
            },
            "maturity_stage": {
                "duration": "130–150 days",
                "details": "Grains harden and turn golden yellow."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_sowing": "Light irrigation if soil dry",
            "critical_stages": [
                "Crown root initiation stage (20–25 days)",
                "Tillering stage",
                "Flowering stage",
                "Grain filling stage"
            ],
            "frequency": "4–6 irrigations depending on soil type",
            "avoid": "Waterlogging during grain filling"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "8–10 tons FYM per acre",
            "nitrogen": "100–120 kg/ha split doses",
            "phosphorus": "60 kg/ha basal dose",
            "potassium": "40 kg/ha",
            "zinc": "If deficiency observed",
            "biofertilizers": "Azotobacter recommended"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "phalaris_minor": {
                "description": "Narrow leaf weed resembling wheat.",
                "damage": "Competes heavily for nutrients and reduces yield.",
                "control": "Post-emergence herbicide."
            },
            "chenopodium_album": {
                "description": "Broadleaf winter weed.",
                "damage": "Competes during early growth stage.",
                "control": "Mechanical weeding."
            },
            "avena_fatua": {
                "description": "Wild oat weed.",
                "damage": "Reduces grain yield significantly.",
                "control": "Selective herbicide."
            },
            "parthenium": {
                "description": "Invasive weed in upland fields.",
                "damage": "Competes for nutrients.",
                "control": "Manual removal."
            }
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "aphids": {
                "description": "Sap sucking insects.",
                "symptoms": "Yellowing and stunted growth.",
                "control": "Insecticide spray."
            },
            "termite": {
                "description": "Soil pest damaging roots.",
                "symptoms": "Drying patches in field.",
                "control": "Seed treatment and soil insecticide."
            },
            "armyworm": {
                "description": "Leaf feeding caterpillar.",
                "symptoms": "Defoliation.",
                "control": "Insecticide spray."
            },
            "wheat_stem_sawfly": {
                "description": "Larvae bore into stems.",
                "symptoms": "Stem breakage and lodging.",
                "control": "Crop rotation and resistant varieties."
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "rust": {
                "description": "Fungal disease (brown, yellow, black rust).",
                "symptoms": "Reddish or yellow pustules on leaves.",
                "control": "Resistant varieties and fungicide spray."
            },
            "loose_smut": {
                "description": "Seed-borne fungal disease.",
                "symptoms": "Black powdery masses instead of grains.",
                "control": "Seed treatment before sowing."
            },
            "powdery_mildew": {
                "description": "White powdery fungal growth on leaves.",
                "symptoms": "Reduced photosynthesis.",
                "control": "Fungicide application."
            },
            "karnal_bunt": {
                "description": "Fungal disease affecting grains.",
                "symptoms": "Blackened grains with foul smell.",
                "control": "Use certified seeds."
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "110–150 days after sowing",
            "maturity_indicators": [
                "Grains hard and golden yellow",
                "Moisture content around 20%",
                "Leaves dry completely"
            ],
            "method": "Manual harvesting or combine harvester"
        },

        "average_yield_per_acre": "18–25 quintals",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Thresh grains properly",
            "Dry grains to 12% moisture",
            "Store in dry ventilated storage",
            "Protect from storage pests"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "327 kcal",
            "carbohydrates": "71 g",
            "protein": "13 g",
            "fiber": "12 g",
            "iron": "3.5 mg",
            "magnesium": "138 mg"
        },

        "nutrition_explanation": [
            "Rich source of carbohydrates",
            "Good plant protein source",
            "High fiber content",
            "Contains essential minerals"
        ],

        "health_benefits": [
            "Provides sustained energy",
            "Supports digestive health",
            "Helps maintain blood sugar levels",
            "Supports heart health"
        ],

        "economic_importance": [
            "Major staple crop",
            "Used in flour production",
            "Essential for food security",
            "Provides employment to farmers"
        ],

        "risk_factors": [
            "Rust outbreak risk",
            "Climate sensitivity during flowering",
            "Weed competition",
            "Price fluctuation"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/wheat.jpg",
            "pests": [
                "static/images/pests/aphids.jpg",
                "static/images/pests/termite.jpg",
                "static/images/pests/armyworm.jpg",
                "static/images/pests/wheat_stem_sawfly.jpg"
            ],
            "diseases": [
                "static/images/diseases/rust.jpg",
                "static/images/diseases/loose_smut.jpg",
                "static/images/diseases/powdery_mildew.jpg",
                "static/images/diseases/karnal_bunt.jpg"
            ],
            "weeds": [
                "static/images/weeds/phalaris_minor.jpg",
                "static/images/weeds/chenopodium_album.jpg",
                "static/images/weeds/avena_fatua.jpg",
                "static/images/weeds/parthenium.jpg"
            ]
        }
    }
}