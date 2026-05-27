crop_data = {
    "red_lentil": {
        "name": "Red Lentil",
        "scientific_name": "Lens culinaris",
        "family": "Fabaceae",
        "category": "Pulse Crop",
        "crop_type": "Rabi season leguminous pulse crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Rabi (October–November sowing)",
        "duration_days": "100–120 days",
        "climate": "Cool dry climate during growth and warm dry weather at maturity",
        "ideal_temperature": "18°C – 25°C",
        "germination_temperature": "15°C – 22°C",
        "rainfall_requirement_mm": "350 – 500 mm",
        "water_requirement_level": "Low to Moderate",
        "sunlight_requirement": "Requires full sunlight for proper flowering and pod development",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained loamy to clay loam soils",
        "soil_ph_range": "6.0 – 7.5",
        "soil_depth_requirement": "Medium to deep soils preferred",
        "salinity_tolerance": "Low",
        "drainage_requirement": "Very sensitive to waterlogging; good drainage essential",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Assam",
            "Bihar",
            "Chhattisgarh",
            "Jharkhand",
            "Madhya Pradesh",
            "Rajasthan",
            "Tripura",
            "Uttar Pradesh",
            "West Bengal",

        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "One deep ploughing followed by 2 harrowings",
            "Remove weeds and previous crop residues",
            "Incorporate 5–8 tons FYM per acre",
            "Level field for uniform irrigation",
            "Fine tilth required for good seed-soil contact"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Certified disease-free high-yielding varieties",
            "seed_rate_per_acre": "12–15 kg",
            "seed_selection": "Bold, uniform seeds with high germination percentage",
            "seed_treatment": [
                "Treat seeds with Carbendazim or Thiram before sowing",
                "Inoculate with Rhizobium culture",
                "Use PSB (Phosphate Solubilizing Bacteria)",
                "Trichoderma treatment for soil-borne disease prevention"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Line sowing using seed drill",
        "row_spacing": "20–30 cm",
        "plant_spacing": "8–10 cm",
        "sowing_depth": "3–5 cm",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "germination_stage": {
                "duration": "0–8 days",
                "details": "Seed imbibes moisture and radicle emerges; primary root establishment begins."
            },
            "seedling_stage": {
                "duration": "8–20 days",
                "details": "Development of first true leaves; nodulation starts."
            },
            "vegetative_stage": {
                "duration": "20–50 days",
                "details": "Branching and canopy formation; nitrogen fixation increases."
            },
            "flowering_stage": {
                "duration": "45–70 days",
                "details": "Small white or pale blue flowers appear; pollination occurs."
            },
            "pod_development_stage": {
                "duration": "60–90 days",
                "details": "Pods form containing 1–2 seeds; seeds enlarge rapidly."
            },
            "maturity_stage": {
                "duration": "90–120 days",
                "details": "Plants turn yellow-brown; pods dry and seeds harden."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_sowing": "Light irrigation if soil moisture is insufficient",
            "critical_stages": [
                "Branching stage",
                "Flowering stage",
                "Pod filling stage"
            ],
            "frequency": "1–2 irrigations depending on rainfall",
            "avoid": "Excess irrigation causing waterlogging"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "5–8 tons FYM per acre",
            "nitrogen": "15–20 kg/ha as starter dose",
            "phosphorus": "40–60 kg/ha at sowing",
            "potassium": "20 kg/ha if soil deficient",
            "biofertilizers": "Rhizobium and PSB recommended"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "chenopodium": {
                "description": "Common winter broadleaf weed.",
                "damage": "Competes for nutrients and sunlight.",
                "control": "Hand weeding at 25–30 DAS."
            },
            "phalaris_minor": {
                "description": "Grass weed common in Rabi season.",
                "damage": "Heavy nutrient competition.",
                "control": "Use selective herbicide."
            },
            "amaranthus": {
                "description": "Fast-growing weed.",
                "damage": "Reduces crop vigor.",
                "control": "Mechanical removal."
            }
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "aphids": {
                "description": "Sap-sucking insects attacking tender shoots.",
                "symptoms": "Leaf curling and sticky secretion.",
                "control": "Neem oil spray or systemic insecticide."
            },
            "pod_borer": {
                "description": "Larvae feed inside pods.",
                "symptoms": "Damaged seeds and holes in pods.",
                "control": "Pheromone traps and recommended insecticides."
            },
            "cutworm": {
                "description": "Soil-dwelling larvae cutting seedlings at base.",
                "symptoms": "Seedlings collapse suddenly.",
                "control": "Soil treatment and proper field sanitation."
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "rust": {
                "description": "Fungal disease forming reddish-brown pustules.",
                "symptoms": "Leaf spots and premature defoliation.",
                "control": "Spray fungicide at early stage."
            },
            "wilt": {
                "description": "Soil-borne fungal infection.",
                "symptoms": "Yellowing and plant death.",
                "control": "Use resistant varieties and seed treatment."
            },
            "ascochyta_blight": {
                "description": "Fungal leaf and pod disease.",
                "symptoms": "Brown lesions on leaves and pods.",
                "control": "Fungicide spray and crop rotation."
            },
            "powdery_mildew": {
                "description": "White powdery growth on foliage.",
                "symptoms": "Reduced photosynthesis.",
                "control": "Sulfur-based fungicide spray."
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "100–120 days after sowing",
            "maturity_indicators": [
                "Plants turn yellow-brown",
                "Pods dry completely",
                "Seeds become hard"
            ],
            "method": "Cut plants, dry in field, then thresh"
        },

        "average_yield_per_acre": "5–8 quintals",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Dry seeds to 10–12% moisture",
            "Clean and grade properly",
            "Store in moisture-proof containers",
            "Protect from bruchid infestation"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "352 kcal",
            "protein": "25 g",
            "carbohydrates": "60 g",
            "fiber": "11 g",
            "iron": "6.5 mg",
            "magnesium": "122 mg"
        },

        "nutrition_explanation": [
            "Rich source of plant protein",
            "High iron content supports hemoglobin production",
            "Good dietary fiber for digestive health",
            "Low fat and cholesterol-free"
        ],

        "health_benefits": [
            "Supports muscle growth",
            "Improves digestion",
            "Helps regulate blood sugar",
            "Boosts immunity",
            "Supports heart health"
        ],

        "economic_importance": [
            "Major pulse in Indian diet",
            "Important source of vegetarian protein",
            "Enhances soil fertility via nitrogen fixation",
            "Good market demand in domestic and export sectors"
        ],

        "risk_factors": [
            "Sensitive to waterlogging",
            "Highly susceptible to rust disease",
            "Pod shattering if harvest delayed"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/red_lentil.jpg",
            "pests": [
                "static/images/pests/aphids.jpg",
                "static/images/pests/pod_borer.jpg",
                "static/images/pests/cutworm.jpg"
            ],
            "diseases": [
                "static/images/diseases/rust.jpg",
                "static/images/diseases/wilt.jpg",
                "static/images/diseases/ascochyta_blight.jpg",
                "static/images/diseases/powdery_mildew.jpg"
            ],
            "weeds": [
                "static/images/weeds/chenopodium.jpg",
                "static/images/weeds/phalaris_minor.jpg",
                "static/images/weeds/amaranthus.jpg"
            ]
        }
    }
}