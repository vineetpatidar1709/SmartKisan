crop_data = {
    "rice": {
        "name": "Rice",
        "scientific_name": "Oryza sativa",
        "family": "Poaceae",
        "category": "Cereal Crop",
        "crop_type": "Staple Food Grain Crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS - PARAGRAPHS
        # -------------------------------------------------
        "season": "Rice is primarily a Kharif crop sown in June-July with harvest in October-November. It can also be grown as Rabi crop in South India (November-December sowing) and Summer crop in irrigated areas (January-February sowing). The crop requires warm humid conditions for optimal growth and development.",
        "duration_days": "Rice varieties typically take 100-150 days from sowing to harvest, depending on the variety and growing conditions. Short duration varieties take around 100-120 days while long duration varieties require 140-150 days for complete maturity.",
        "climate": "Rice thrives in warm and humid tropical to subtropical climates with temperatures between 20-35°C. It requires high humidity during vegetative growth and moderately dry conditions during grain ripening stage. Extreme temperatures above 40°C during flowering can cause spikelet sterility.",
        "ideal_temperature": "The ideal temperature range for rice cultivation is 20°C to 35°C. Optimal temperature for germination is 25-30°C, for tillering 25-30°C, for panicle initiation 24-28°C, and for grain filling 22-27°C. Temperatures above 35°C during flowering reduce grain set.",
        "germination_temperature": "18°C – 32°C",
        "rainfall_requirement_mm": "1000 – 2000 mm",
        "water_requirement_level": "High",
        "sunlight_requirement": "Full sunlight required for high grain yield",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Clayey loam to clay soil with good water retention",
        "soil_ph_range": "5.5 – 7.5",
        "soil_depth_requirement": "Deep fertile soil with puddling capacity",
        "salinity_tolerance": "Low to moderate (salt-tolerant varieties available)",
        "drainage_requirement": "Poor drainage tolerated during vegetative stage; drainage required at maturity",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Andhra Pradesh",
            "Arunachal Pradesh",
            "Assam",
            "Bihar",
            "Chhattisgarh",
            "Gujarat",
            "Haryana",
            "Himachal Pradesh",
            "Jammu and Kashmir",
            "Jharkhand",
            "Kerala",
            "Meghalaya",
            "Nagaland",
            "Odisha",
            "Punjab",
            "Sikkim",
            "Tamil Nadu",
            "Telangana",
            "Tripura",
            "Uttar Pradesh",
            "Uttarakhand",
            "West Bengal",

        ],


        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "Plough field 2–3 times for fine tilth",
            "Flood and puddle soil to reduce percolation",
            "Level field properly for uniform water distribution",
            "Incorporate 10–12 tons FYM per acre",
            "Construct bunds to retain irrigation water"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Certified high-yielding or hybrid varieties",
            "seed_rate_per_acre": "8–10 kg (transplanting), 20–25 kg (direct seeding)",
            "seed_selection": "Healthy, fully matured, disease-free seeds",
            "seed_treatment": [
                "Soak seeds in salt solution to remove floaters",
                "Treat with fungicide to prevent seed-borne diseases",
                "Biofertilizer (Azospirillum) treatment for better root growth"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Nursery raising and transplanting or direct seeded rice (DSR)",
        "row_spacing": "20 cm",
        "plant_spacing": "15 cm between hills",
        "sowing_depth": "2–3 cm depth",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "germination_stage": {
                "duration": "0–10 days",
                "details": "Seeds germinate and seedlings emerge."
            },
            "nursery_stage": {
                "duration": "0–25 days",
                "details": "Seedlings raised in nursery before transplanting."
            },
            "tillering_stage": {
                "duration": "20–45 days",
                "details": "Multiple tillers emerge from base."
            },
            "panicle_initiation_stage": {
                "duration": "45–65 days",
                "details": "Formation of panicle primordia."
            },
            "flowering_stage": {
                "duration": "70–90 days",
                "details": "Pollination and grain setting occur."
            },
            "grain_filling_stage": {
                "duration": "90–120 days",
                "details": "Grains accumulate starch and nutrients."
            },
            "maturity_stage": {
                "duration": "120–150 days",
                "details": "Grains harden and turn golden yellow."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_transplanting": "Maintain shallow water (2–3 cm)",
            "critical_stages": [
                "Tillering stage",
                "Panicle initiation stage",
                "Flowering stage"
            ],
            "frequency": "Continuous standing water of 3–5 cm during vegetative stage",
            "avoid": "Drain water 10–15 days before harvest"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "10–12 tons FYM per acre",
            "nitrogen": "120 kg/ha split doses (basal, tillering, panicle stage)",
            "phosphorus": "60 kg/ha basal dose",
            "potassium": "40–60 kg/ha",
            "zinc": "25 kg/ha zinc sulphate if deficient",
            "biofertilizers": "Azospirillum and PSB recommended"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "echinochloa_crus_galli": {
                "description": "Barnyard grass resembling rice in early stage.",
                "damage": "Competes heavily for nutrients and sunlight.",
                "control": "Pre-emergence herbicide and manual weeding."
            },
            "cyperus_difformis": {
                "description": "Sedge weed common in paddy fields.",
                "damage": "Reduces crop vigor.",
                "control": "Timely herbicide application."
            },
            "monochoria": {
                "description": "Broadleaf aquatic weed.",
                "damage": "Competes in flooded fields.",
                "control": "Mechanical removal and herbicide."
            },
            "parthenium": {
                "description": "Invasive weed in upland rice.",
                "damage": "Competes for nutrients.",
                "control": "Manual uprooting."
            }
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "stem_borer": {
                "description": "Larvae bore into stem.",
                "symptoms": "Dead heart and white ear heads.",
                "control": "Pheromone traps and insecticide."
            },
            "brown_planthopper": {
                "description": "Sap sucking insect at plant base.",
                "symptoms": "Hopper burn and plant drying.",
                "control": "Resistant varieties and spray."
            },
            "leaf_folder": {
                "description": "Larvae fold and feed on leaves.",
                "symptoms": "Reduced photosynthesis.",
                "control": "Biological control and insecticide."
            },
            "rice_hispa": {
                "description": "Beetle scraping leaf surface.",
                "symptoms": "White streaks on leaves.",
                "control": "Insecticide application."
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "blast": {
                "description": "Fungal disease affecting leaves and panicles.",
                "symptoms": "Diamond-shaped lesions.",
                "control": "Resistant varieties and fungicide spray."
            },
            "bacterial_leaf_blight": {
                "description": "Bacterial disease under humid conditions.",
                "symptoms": "Yellowing and drying of leaf margins.",
                "control": "Use resistant varieties."
            },
            "sheath_blight": {
                "description": "Fungal infection in dense crops.",
                "symptoms": "Lesions on leaf sheath.",
                "control": "Balanced fertilization and fungicide."
            },
            "false_smut": {
                "description": "Fungal disease forming green balls on grains.",
                "symptoms": "Reduced grain quality.",
                "control": "Clean cultivation and fungicide."
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "100–150 days after sowing",
            "maturity_indicators": [
                "Grains turn golden yellow",
                "Moisture content around 20–25%",
                "Panicles bend downwards"
            ],
            "method": "Manual cutting or combine harvester"
        },

        "average_yield_per_acre": "20–30 quintals (variety dependent)",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Thresh grains properly",
            "Dry grains to 12–14% moisture",
            "Store in dry ventilated storage"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "130 kcal (cooked)",
            "carbohydrates": "28 g",
            "protein": "2.7 g",
            "fiber": "0.4 g",
            "iron": "0.2 mg",
            "magnesium": "12 mg"
        },

        "nutrition_explanation": [
            "Primary energy source",
            "Low fat content",
            "Gluten-free grain",
            "Easily digestible carbohydrate"
        ],

        "health_benefits": [
            "Provides quick energy",
            "Gluten-free for sensitive individuals",
            "Supports digestive health",
            "Staple food for billions worldwide"
        ],

        "economic_importance": [
            "Major staple crop of India",
            "Export commodity (Basmati and Non-Basmati)",
            "Supports food security",
            "Employment for millions of farmers"
        ],

        "risk_factors": [
            "High water requirement",
            "Pest outbreaks in humid conditions",
            "Climate change affecting yield",
            "Price fluctuation"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/rice.jpg",
            "pests": [
                "static/images/pests/stem_borer.jpg",
                "static/images/pests/brown_planthopper.jpg",
                "static/images/pests/leaf_folder.jpg",
                "static/images/pests/rice_hispa.jpg"
            ],
            "diseases": [
                "static/images/diseases/blast.jpg",
                "static/images/diseases/bacterial_leaf_blight.jpg",
                "static/images/diseases/sheath_blight.jpg",
                "static/images/diseases/false_smut.jpg"
            ],
            "weeds": [
                "static/images/weeds/echinochloa_crus_galli.jpg",
                "static/images/weeds/cyperus_difformis.jpg",
                "static/images/weeds/monochoria.jpg",
                "static/images/weeds/parthenium.jpg"
            ]
        }
    }
}