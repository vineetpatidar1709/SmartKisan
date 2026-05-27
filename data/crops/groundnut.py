crop_data = {
    "groundnut": {
        "name": "Groundnut",
        "scientific_name": "Arachis hypogaea",
        "family": "Fabaceae",
        "category": "Oilseed Crop",
        "crop_type": "Leguminous cash crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Kharif (June–July), Rabi (Oct–Nov in South India)",
        "duration_days": "110–130 days",
        "climate": "Warm tropical and semi-arid",
        "ideal_temperature": "25°C – 35°C",
        "germination_temperature": "20°C – 30°C",
        "rainfall_requirement_mm": "500 – 1000 mm",
        "water_requirement_level": "Moderate",
        "sunlight_requirement": "Full sunlight required for pod development",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Sandy loam, well-drained soil",
        "soil_ph_range": "6.0 – 7.5",
        "soil_depth_requirement": "Loose soil for easy peg penetration",
        "salinity_tolerance": "Low",
        "drainage_requirement": "Excellent drainage essential to prevent pod rot",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Andhra Pradesh",
            "Chhattisgarh",
            "Gujarat",
            "Jharkhand",
            "Karnataka",
            "Madhya Pradesh",
            "Maharashtra",
            "Nagaland",
            "Odisha",
            "Rajasthan",
            "Tamil Nadu",
            "Telangana",

        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "2–3 deep ploughings to make soil loose",
            "Remove stones and weeds",
            "Incorporate 8–10 tons FYM per acre",
            "Level field properly",
            "Ensure fine tilth for good germination"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Certified bold seeds of high-yielding varieties",
            "seed_rate_per_acre": "40–50 kg (variety dependent)",
            "seed_selection": "Healthy, disease-free seeds",
            "seed_treatment": [
                "Treat with fungicide before sowing",
                "Rhizobium inoculation for nitrogen fixation",
                "Trichoderma for soil-borne disease protection"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Line sowing using seed drill",
        "row_spacing": "30–45 cm",
        "plant_spacing": "10–15 cm between plants",
        "sowing_depth": "5–6 cm depth",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "germination_stage": {
                "duration": "0–10 days",
                "details": "Seeds sprout and primary roots develop."
            },
            "vegetative_stage": {
                "duration": "10–30 days",
                "details": "Rapid leaf and branch growth."
            },
            "flowering_stage": {
                "duration": "30–45 days",
                "details": "Yellow flowers appear; self-pollination occurs."
            },
            "peg_formation_stage": {
                "duration": "45–60 days",
                "details": "Pegs penetrate soil to form pods underground."
            },
            "pod_development_stage": {
                "duration": "60–100 days",
                "details": "Pods enlarge and kernels develop."
            },
            "maturity_stage": {
                "duration": "100–130 days",
                "details": "Leaves turn yellow; pods harden."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_sowing": "Light irrigation if soil dry",
            "critical_stages": [
                "Flowering stage",
                "Peg formation stage",
                "Pod development stage"
            ],
            "frequency": "Every 10–15 days if rainfall insufficient",
            "avoid": "Waterlogging as it causes pod rot"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "8–10 tons FYM per acre",
            "nitrogen": "15–25 kg/ha as starter dose",
            "phosphorus": "40–60 kg/ha at sowing",
            "potassium": "40 kg/ha",
            "gypsum": "200 kg/acre during flowering for better pod filling",
            "biofertilizers": "Rhizobium culture recommended"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "trianthema": {
                "description": "A fast-growing broadleaf weed competing heavily during early crop growth.",
                "damage": "Reduces nutrient availability and pod formation.",
                "control": "Early hand weeding and herbicide if needed."
            },
            "cyperus": {
                "description": "Also called nut grass, spreads through underground tubers.",
                "damage": "Competes for moisture and nutrients.",
                "control": "Deep ploughing and repeated removal."
            },
            "parthenium": {
                "description": "Invasive weed common in open fields.",
                "damage": "Reduces yield and may cause allergies.",
                "control": "Manual uprooting before flowering."
            },
            "digera_arvensis": {
                "description": "Rainy-season weed common in oilseed crops.",
                "damage": "Aggressive competitor during vegetative stage.",
                "control": "Timely mechanical weeding."
            }
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "leaf_miner": {
                "description": "Larvae mine inside leaves creating zig-zag tunnels.",
                "symptoms": "Leaves dry and curl.",
                "control": "Early insecticide spray."
            },
            "aphids": {
                "description": "Sap sucking insects found on tender shoots.",
                "symptoms": "Yellowing and curling of leaves.",
                "control": "Neem oil or systemic spray."
            },
            "white_grub": {
                "description": "Soil pest feeding on roots underground.",
                "symptoms": "Sudden wilting and plant death.",
                "control": "Soil treatment before sowing."
            },
            "spodoptera": {
                "description": "Leaf eating caterpillar active at night.",
                "symptoms": "Large holes in leaves.",
                "control": "Pheromone traps and spray."
            },
            "thrips": {
                "description": "Tiny insects damaging flowers and leaves.",
                "symptoms": "Silvering of leaves and poor flowering.",
                "control": "Spray recommended insecticide."
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "tikka_disease": {
                "description": "Fungal disease causing brown circular leaf spots.",
                "symptoms": "Premature leaf fall.",
                "control": "Fungicide spray at early stage."
            },
            "rust": {
                "description": "Rust colored pustules appear on leaves.",
                "symptoms": "Yellowing and drying of foliage.",
                "control": "Resistant varieties and fungicide."
            },
            "collar_rot": {
                "description": "Soil borne fungus rotting stem base.",
                "symptoms": "Plant collapse.",
                "control": "Seed treatment and good drainage."
            },
            "stem_rot": {
                "description": "Fungal infection at soil line.",
                "symptoms": "White fungal growth near base.",
                "control": "Improve drainage and apply fungicide."
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "110–130 days after sowing",
            "maturity_indicators": [
                "Leaves turn yellow",
                "Pods mature and shells hard",
                "Inner shell shows dark markings"
            ],
            "method": "Uproot plants and dry in field for 2–3 days"
        },

        "average_yield_per_acre": "8–15 quintals",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Dry pods to 8–10% moisture",
            "Store in dry ventilated place",
            "Avoid fungal contamination (aflatoxin risk)"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "567 kcal",
            "protein": "25 g",
            "fat": "49 g",
            "fiber": "8.5 g",
            "magnesium": "168 mg",
            "vitamin_E": "8 mg"
        },

        "nutrition_explanation": [
            "High protein content",
            "Rich in healthy fats",
            "Good source of magnesium",
            "Contains antioxidants"
        ],

        "health_benefits": [
            "Supports heart health",
            "Improves brain function",
            "Provides long-lasting energy",
            "Helps in weight management",
            "Boosts immunity"
        ],

        "economic_importance": [
            "Major oilseed crop",
            "Used for edible oil",
            "Export commodity",
            "Used in peanut butter industry"
        ],

        "risk_factors": [
            "Waterlogging reduces yield",
            "Aflatoxin contamination risk",
            "Pest outbreaks during flowering"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/groundnut.jpg",
            "pests": [
                "static/images/pests/leaf_miner.jpg",
                "static/images/pests/aphids.jpg",
                "static/images/pests/white_grub.jpg",
                "static/images/pests/spodoptera.jpg",
                "static/images/pests/thrips.jpg"
            ],
            "diseases": [
                "static/images/diseases/tikka_disease.jpg",
                "static/images/diseases/rust.jpg",
                "static/images/diseases/collar_rot.jpg",
                "static/images/diseases/stem_rot.jpg"
            ],
            "weeds": [
                "static/images/weeds/trianthema.jpg",
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/digera_arvensis.jpg"
            ]
        }
    }
}