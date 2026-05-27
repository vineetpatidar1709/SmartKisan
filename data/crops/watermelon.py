crop_data = {
    "watermelon": {
        "name": "Watermelon",
        "scientific_name": "Citrullus lanatus",
        "family": "Cucurbitaceae",
        "category": "Fruit Crop",
        "crop_type": "Summer season vine fruit crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Summer (January–March in North India; November–January in South India)",
        "duration_days": "80–110 days (variety dependent)",
        "climate": "Warm and dry climate with high sunlight intensity",
        "ideal_temperature": "22°C – 35°C",
        "germination_temperature": "25°C – 30°C",
        "rainfall_requirement_mm": "400 – 600 mm",
        "water_requirement_level": "Moderate (critical during flowering and fruit development)",
        "sunlight_requirement": "Requires full sunlight for proper vine growth and sugar accumulation",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained sandy loam to loamy soils",
        "soil_ph_range": "6.0 – 7.5",
        "soil_depth_requirement": "Deep soils preferred for extensive root spread",
        "salinity_tolerance": "Low",
        "drainage_requirement": "Very sensitive to waterlogging; raised beds recommended",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Uttar Pradesh",
            "Madhya Pradesh",
            "Karnataka",
            "Andhra Pradesh",
            "Telangana",
            "Tamil Nadu",
            "Rajasthan"
        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "Deep ploughing followed by 2–3 harrowings",
            "Remove weeds and residues",
            "Incorporate 10–15 tons FYM per acre",
            "Prepare raised beds or ridges for drainage",
            "Install drip irrigation system before sowing"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Hybrid or open-pollinated high-yielding varieties",
            "seed_rate_per_acre": "1–1.5 kg",
            "seed_selection": "Bold, uniform, high germination seeds",
            "seed_treatment": [
                "Treat with Thiram or Carbendazim before sowing",
                "Trichoderma treatment to prevent damping-off",
                "Soak seeds for 6–8 hours before sowing for better germination"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Dibbling method on raised beds or pits",
        "row_spacing": "1.5 – 2.5 meters",
        "plant_spacing": "60 – 90 cm",
        "sowing_depth": "2–3 cm",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "germination_stage": {
                "duration": "0–7 days",
                "details": "Seed absorbs moisture; cotyledons emerge above soil surface."
            },
            "seedling_stage": {
                "duration": "7–20 days",
                "details": "True leaves develop; root system establishes."
            },
            "vegetative_stage": {
                "duration": "20–40 days",
                "details": "Vine elongation and branching; rapid leaf growth."
            },
            "flowering_stage": {
                "duration": "30–50 days",
                "details": "Male and female flowers appear; pollination mainly by bees."
            },
            "fruit_development_stage": {
                "duration": "45–80 days",
                "details": "Fruit enlarges rapidly; sugar accumulation increases."
            },
            "maturity_stage": {
                "duration": "80–110 days",
                "details": "Fruit skin hardens; tendril near fruit dries; dull hollow sound on tapping."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_sowing": "Light irrigation for uniform germination",
            "critical_stages": [
                "Flowering stage",
                "Fruit setting stage",
                "Fruit enlargement stage"
            ],
            "frequency": "Every 5–7 days in summer (drip recommended)",
            "avoid": "Excess irrigation during maturity to prevent fruit cracking"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "10–15 tons FYM per acre",
            "nitrogen": "40–50 kg/acre split doses",
            "phosphorus": "25–30 kg/acre at sowing",
            "potassium": "30–40 kg/acre during fruit development",
            "micronutrients": "Boron and Zinc sprays improve fruit quality"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "parthenium": {
                "description": "Broadleaf invasive weed.",
                "damage": "Competes for nutrients and moisture.",
                "control": "Manual removal and mulching."
            },
            "cyperus": {
                "description": "Nut grass spreading via rhizomes.",
                "damage": "Reduces vine growth.",
                "control": "Deep ploughing and mechanical removal."
            },
            "amaranthus": {
                "description": "Fast-growing summer weed.",
                "damage": "Competes during early stages.",
                "control": "Hand weeding at 20–25 DAS."
            }
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "fruit_fly": {
                "description": "Female lays eggs inside fruits.",
                "symptoms": "Rotting and maggot infestation inside fruit.",
                "control": "Use pheromone traps and cover fruits with nets."
            },
            "aphids": {
                "description": "Sap-sucking insects on tender shoots.",
                "symptoms": "Leaf curling and virus transmission.",
                "control": "Neem oil or systemic insecticide spray."
            },
            "red_pumpkin_beetle": {
                "description": "Feeds on leaves and flowers.",
                "symptoms": "Skeletonized leaves.",
                "control": "Dusting with insecticide."
            },
            "thrips": {
                "description": "Damages flowers and young fruits.",
                "symptoms": "Poor fruit set.",
                "control": "Spray recommended insecticide."
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "powdery_mildew": {
                "description": "White powdery fungal growth on leaves.",
                "symptoms": "Reduced photosynthesis and yield.",
                "control": "Sulfur-based fungicide spray."
            },
            "downy_mildew": {
                "description": "Fungal disease under humid conditions.",
                "symptoms": "Yellow spots on upper leaf surface.",
                "control": "Copper-based fungicide."
            },
            "fusarium_wilt": {
                "description": "Soil-borne fungal infection.",
                "symptoms": "Wilting and plant death.",
                "control": "Crop rotation and resistant varieties."
            },
            "anthracnose": {
                "description": "Fungal disease causing dark lesions.",
                "symptoms": "Spots on leaves and fruits.",
                "control": "Fungicide spray and sanitation."
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "80–110 days after sowing",
            "maturity_indicators": [
                "Dried tendril near fruit",
                "Dull hollow sound on tapping",
                "Ground spot turns creamy yellow"
            ],
            "method": "Harvest manually using sharp knife"
        },

        "average_yield_per_acre": "80–120 quintals",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Handle fruits carefully to avoid cracking",
            "Store at 10–15°C temperature",
            "Avoid stacking too high",
            "Transport in cushioned crates"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "30 kcal",
            "protein": "0.6 g",
            "carbohydrates": "8 g",
            "fiber": "0.4 g",
            "vitamin_c": "8 mg",
            "water_content": "91%"
        },

        "nutrition_explanation": [
            "Extremely hydrating fruit",
            "Rich in antioxidants like lycopene",
            "Low calorie and fat-free",
            "Good source of Vitamin C"
        ],

        "health_benefits": [
            "Prevents dehydration",
            "Supports heart health",
            "Improves skin health",
            "Aids digestion",
            "Helps regulate blood pressure"
        ],

        "economic_importance": [
            "High summer market demand",
            "Export potential",
            "Short duration with high returns",
            "Suitable for intercropping"
        ],

        "risk_factors": [
            "Highly sensitive to waterlogging",
            "Fruit cracking due to irregular irrigation",
            "Pollination failure reduces fruit set"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/watermelon.jpg",
            "pests": [
                "static/images/pests/fruit_fly.jpg",
                "static/images/pests/aphids.jpg",
                "static/images/pests/red_pumpkin_beetle.jpg",
                "static/images/pests/thrips.jpg"
            ],
            "diseases": [
                "static/images/diseases/powdery_mildew.jpg",
                "static/images/diseases/downy_mildew.jpg",
                "static/images/diseases/fusarium_wilt.jpg",
                "static/images/diseases/anthracnose.jpg"
            ],
            "weeds": [
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/amaranthus.jpg"
            ]
        }
    }
}