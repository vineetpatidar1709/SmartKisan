crop_data = {
    "chickpea": {
        "name": "Chickpea",
        "scientific_name": "Cicer arietinum",
        "family": "Fabaceae",
        "category": "Pulse Crop",
        "crop_type": "Leguminous protein-rich Rabi crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Rabi (October–November sowing)",
        "duration_days": "100–120 days (Desi), 120–140 days (Kabuli)",
        "climate": "Cool and dry climate",
        "ideal_temperature": "20°C – 25°C",
        "germination_temperature": "15°C – 20°C",
        "rainfall_requirement_mm": "400 – 600 mm",
        "water_requirement_level": "Low to Moderate",
        "sunlight_requirement": "Requires full sunlight during flowering and pod filling",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained loamy or sandy loam soil",
        "soil_ph_range": "6.0 – 8.0",
        "soil_depth_requirement": "Deep soil preferred for strong root development",
        "salinity_tolerance": "Low to Moderate",
        "drainage_requirement": "Good drainage required to avoid root rot",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Andhra Pradesh",
            "Arunachal Pradesh",
            "Assam",
            "Bihar",
            "Chhattisgarh",
            "Jharkhand",
            "Karnataka",
            "Madhya Pradesh",
            "Maharashtra",
            "Rajasthan",
            "Telangana",
            "Tripura",
            "Uttar Pradesh",

        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "1–2 deep ploughings to loosen soil",
            "Remove weeds and previous crop residues",
            "Apply 6–8 tons FYM per acre",
            "Level field properly",
            "Prepare firm and fine seedbed"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Certified Desi or Kabuli varieties",
            "seed_rate_per_acre": "30–40 kg (Desi), 40–50 kg (Kabuli)",
            "seed_selection": "Bold, uniform, disease-free seeds",
            "seed_treatment": [
                "Treat with fungicide to prevent wilt and rot",
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
        "sowing_depth": "5–8 cm depth",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "germination_stage": {
                "duration": "0–10 days",
                "details": "Seed germinates and root system develops."
            },
            "vegetative_stage": {
                "duration": "10–35 days",
                "details": "Leaf and branch development occurs."
            },
            "flowering_stage": {
                "duration": "35–60 days",
                "details": "Small white or pink flowers appear."
            },
            "pod_formation_stage": {
                "duration": "60–85 days",
                "details": "Pods form and begin seed development."
            },
            "pod_filling_stage": {
                "duration": "85–110 days",
                "details": "Seeds accumulate nutrients and enlarge."
            },
            "maturity_stage": {
                "duration": "100–140 days",
                "details": "Plants dry and pods turn brown."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "first_irrigation": "At branching stage if soil moisture low",
            "critical_stages": [
                "Flowering stage",
                "Pod formation stage"
            ],
            "frequency": "1–3 irrigations depending on rainfall",
            "avoid": "Waterlogging during flowering"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "6–8 tons FYM per acre",
            "nitrogen": "20–25 kg/ha as starter dose",
            "phosphorus": "40–60 kg/ha at sowing",
            "potassium": "20–30 kg/ha",
            "biofertilizers": "Rhizobium culture recommended",
            "micronutrients": "Zinc if deficiency observed"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "chenopodium_album": {
                "description": "Common broadleaf winter weed.",
                "damage": "Competes for nutrients and sunlight.",
                "control": "Manual weeding at early stage."
            },
            "phalaris_minor": {
                "description": "Grass weed in Rabi crops.",
                "damage": "Reduces crop growth and yield.",
                "control": "Pre-emergence herbicide."
            },
            "melilotus": {
                "description": "Winter season weed.",
                "damage": "Suppresses chickpea growth.",
                "control": "Mechanical removal."
            },
            "wild_mustard": {
                "description": "Broadleaf weed found in pulse fields.",
                "damage": "Competes for moisture and nutrients.",
                "control": "Hand weeding before flowering."
            }
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "pod_borer": {
                "description": "Most destructive pest in chickpea.",
                "symptoms": "Holes in pods and damaged seeds.",
                "control": "Pheromone traps and insecticide spray."
            },
            "aphids": {
                "description": "Sap sucking insects.",
                "symptoms": "Yellowing and curling of leaves.",
                "control": "Neem oil spray."
            },
            "cutworm": {
                "description": "Soil insect cutting seedlings.",
                "symptoms": "Seedlings collapse.",
                "control": "Soil treatment before sowing."
            },
            "leaf_miner": {
                "description": "Larvae mine inside leaves.",
                "symptoms": "White streaks on leaves.",
                "control": "Early insecticide spray."
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "fusarium_wilt": {
                "description": "Soil-borne fungal disease.",
                "symptoms": "Sudden wilting and plant death.",
                "control": "Use resistant varieties."
            },
            "ascochyta_blight": {
                "description": "Fungal disease causing leaf spots.",
                "symptoms": "Dark lesions on leaves and pods.",
                "control": "Fungicide spray."
            },
            "botrytis_gray_mold": {
                "description": "Disease under humid conditions.",
                "symptoms": "Gray mold on flowers and pods.",
                "control": "Improve air circulation."
            },
            "collar_rot": {
                "description": "Fungal infection at stem base.",
                "symptoms": "Rotting near soil line.",
                "control": "Seed treatment before sowing."
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "100–140 days after sowing",
            "maturity_indicators": [
                "Plants turn yellow and dry",
                "Pods become brown and hard",
                "Seeds rattle inside pods"
            ],
            "method": "Uproot plants and dry before threshing"
        },

        "average_yield_per_acre": "8–12 quintals",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Dry grains to 10–12% moisture",
            "Clean and grade properly",
            "Store in dry ventilated area",
            "Protect from storage pests"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "364 kcal",
            "protein": "19 g",
            "carbohydrates": "61 g",
            "fiber": "17 g",
            "iron": "6.2 mg",
            "magnesium": "115 mg"
        },

        "nutrition_explanation": [
            "Excellent plant protein source",
            "High dietary fiber",
            "Rich in iron",
            "Supports sustained energy release"
        ],

        "health_benefits": [
            "Supports muscle growth",
            "Improves digestion",
            "Helps control blood sugar",
            "Supports heart health",
            "Boosts immunity"
        ],

        "economic_importance": [
            "Major pulse crop in India",
            "Export commodity",
            "Used in dal and flour production",
            "Important protein source for vegetarian diet"
        ],

        "risk_factors": [
            "Wilt outbreaks in poorly drained soils",
            "Pod borer heavy infestation",
            "Excess rainfall during maturity reduces quality"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/chickpea.jpg",
            "pests": [
                "static/images/pests/pod_borer.jpg",
                "static/images/pests/aphids.jpg",
                "static/images/pests/cutworm.jpg",
                "static/images/pests/leaf_miner.jpg"
            ],
            "diseases": [
                "static/images/diseases/fusarium_wilt.jpg",
                "static/images/diseases/ascochyta_blight.jpg",
                "static/images/diseases/botrytis_gray_mold.jpg",
                "static/images/diseases/collar_rot.jpg"
            ],
            "weeds": [
                "static/images/weeds/chenopodium_album.jpg",
                "static/images/weeds/phalaris_minor.jpg",
                "static/images/weeds/melilotus.jpg",
                "static/images/weeds/wild_mustard.jpg"
            ]
        }
    }
}