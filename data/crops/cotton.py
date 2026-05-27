crop_data = {
    "cotton": {
        "name": "Cotton",
        "scientific_name": "Gossypium spp.",
        "family": "Malvaceae",
        "category": "Fiber Crop",
        "crop_type": "Commercial cash crop (Kharif)",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Kharif (May–July sowing depending on region)",
        "duration_days": "150–180 days (Hybrid varieties up to 200 days)",
        "climate": "Warm tropical and subtropical climate",
        "ideal_temperature": "21°C – 30°C",
        "germination_temperature": "18°C – 30°C",
        "rainfall_requirement_mm": "600 – 1000 mm",
        "water_requirement_level": "Moderate to High",
        "sunlight_requirement": "Requires abundant sunshine for boll development",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Black cotton soil (regur), well-drained loamy soil",
        "soil_ph_range": "6.0 – 8.0",
        "soil_depth_requirement": "Deep soil (at least 60 cm) for root penetration",
        "salinity_tolerance": "Moderate",
        "drainage_requirement": "Good drainage required to avoid root rot and wilting",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Andhra Pradesh",
            "Chhattisgarh",
            "Gujarat",
            "Haryana",
            "Madhya Pradesh",
            "Maharashtra",
            "Meghalaya",
            "Odisha",
            "Punjab",
            "Rajasthan",
            "Telangana",

        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "Deep ploughing during summer to destroy pests",
            "2–3 harrowings to obtain fine tilth",
            "Remove weeds and previous crop residues",
            "Apply 8–10 tons FYM per acre",
            "Prepare ridges and furrows for proper drainage"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Certified hybrid or Bt cotton seeds",
            "seed_rate_per_acre": "1–1.5 kg (hybrid), 4–5 kg (desi varieties)",
            "seed_selection": "High germination, disease-free seeds",
            "seed_treatment": [
                "Fungicide treatment to prevent seed rot",
                "Insecticide treatment against early sucking pests",
                "Biofertilizer treatment for root development"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Dibbling or seed drill on ridges",
        "row_spacing": "90–120 cm",
        "plant_spacing": "45–60 cm between plants",
        "sowing_depth": "3–5 cm depth",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "germination_stage": {
                "duration": "0–10 days",
                "details": "Seed sprouts and primary root system develops."
            },
            "vegetative_stage": {
                "duration": "10–45 days",
                "details": "Rapid growth of stem and leaves."
            },
            "square_formation_stage": {
                "duration": "45–60 days",
                "details": "Formation of flower buds called squares."
            },
            "flowering_stage": {
                "duration": "60–100 days",
                "details": "Yellow flowers appear and pollination occurs."
            },
            "boll_development_stage": {
                "duration": "100–140 days",
                "details": "Bolls enlarge and fibers develop inside."
            },
            "boll_opening_stage": {
                "duration": "140–180 days",
                "details": "Bolls burst open exposing white lint."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "first_irrigation": "Immediately after sowing if soil dry",
            "critical_stages": [
                "Square formation stage",
                "Flowering stage",
                "Boll development stage"
            ],
            "frequency": "Every 10–15 days depending on rainfall",
            "avoid": "Waterlogging and excess irrigation during boll opening"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "8–10 tons FYM per acre",
            "nitrogen": "80–120 kg/ha (split application)",
            "phosphorus": "40–60 kg/ha",
            "potassium": "40–60 kg/ha",
            "micronutrients": "Zinc and Boron if deficiency observed",
            "biofertilizers": "Azotobacter recommended"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "parthenium": {
                "description": "Invasive broadleaf weed common in cotton fields.",
                "damage": "Competes heavily for nutrients and sunlight.",
                "control": "Manual removal and pre-emergence herbicide."
            },
            "cyperus": {
                "description": "Nut grass spreading through underground tubers.",
                "damage": "Reduces moisture availability.",
                "control": "Deep ploughing and repeated removal."
            },
            "amaranthus": {
                "description": "Fast-growing broadleaf weed.",
                "damage": "Suppresses early cotton growth.",
                "control": "Mechanical weeding."
            },
            "echinochloa": {
                "description": "Grassy weed found in irrigated cotton.",
                "damage": "Competes during vegetative stage.",
                "control": "Selective herbicide."
            }
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "bollworm": {
                "description": "Most destructive pest attacking cotton bolls.",
                "symptoms": "Holes in bolls and damaged lint.",
                "control": "Pheromone traps and recommended insecticide."
            },
            "whitefly": {
                "description": "Sap sucking insect transmitting viral diseases.",
                "symptoms": "Yellowing and leaf curling.",
                "control": "Neem oil and insecticide spray."
            },
            "aphids": {
                "description": "Sap sucking pest on tender shoots.",
                "symptoms": "Sticky honeydew on leaves.",
                "control": "Systemic insecticide."
            },
            "thrips": {
                "description": "Tiny insects damaging leaves and flowers.",
                "symptoms": "Silvery patches on leaves.",
                "control": "Early spray application."
            },
            "pink_bollworm": {
                "description": "Larvae feed inside developing bolls.",
                "symptoms": "Rosette flowers and damaged seeds.",
                "control": "Timely picking and pheromone traps."
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "fusarium_wilt": {
                "description": "Soil-borne fungal disease causing wilting.",
                "symptoms": "Yellowing and plant collapse.",
                "control": "Use resistant varieties and proper drainage."
            },
            "verticillium_wilt": {
                "description": "Fungal infection blocking water transport.",
                "symptoms": "Leaf discoloration and stunted growth.",
                "control": "Crop rotation."
            },
            "bacterial_blight": {
                "description": "Bacterial disease causing leaf spots.",
                "symptoms": "Angular lesions on leaves.",
                "control": "Use disease-free seeds."
            },
            "leaf_curl_virus": {
                "description": "Viral disease spread by whiteflies.",
                "symptoms": "Upward curling of leaves.",
                "control": "Control whitefly population."
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "150–180 days after sowing",
            "maturity_indicators": [
                "Bolls burst open naturally",
                "Lint appears fluffy and white",
                "Leaves start drying"
            ],
            "method": "Hand picking in multiple rounds"
        },

        "average_yield_per_acre": "8–15 quintals (seed cotton)",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Dry picked cotton properly",
            "Avoid contamination with moisture",
            "Store in dry and ventilated place",
            "Send for ginning to separate lint and seeds"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "note": "Cotton is primarily a fiber crop and not used directly as food."
        },

        "nutrition_explanation": [
            "Cottonseed oil is edible after processing.",
            "Cottonseed cake used as animal feed."
        ],

        "health_benefits": [
            "Cottonseed oil contains healthy fats.",
            "Used in textile industry for clothing."
        ],

        "economic_importance": [
            "Major fiber crop of India",
            "Raw material for textile industry",
            "Cottonseed oil production",
            "Export commodity",
            "Supports millions of farmers and textile workers"
        ],

        "risk_factors": [
            "Bollworm infestation reduces yield drastically",
            "Excess rainfall affects boll opening",
            "Whitefly outbreaks cause viral diseases"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/cotton.jpg",
            "pests": [
                "static/images/pests/bollworm.jpg",
                "static/images/pests/whitefly.jpg",
                "static/images/pests/aphids.jpg",
                "static/images/pests/thrips.jpg",
                "static/images/pests/pink_bollworm.jpg"
            ],
            "diseases": [
                "static/images/diseases/fusarium_wilt.jpg",
                "static/images/diseases/verticillium_wilt.jpg",
                "static/images/diseases/bacterial_blight.jpg",
                "static/images/diseases/leaf_curl_virus.jpg"
            ],
            "weeds": [
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/amaranthus.jpg",
                "static/images/weeds/echinochloa.jpg"
            ]
        }
    }
}