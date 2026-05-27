crop_data = {
    "onion": {
        "name": "Onion",
        "scientific_name": "Allium cepa",
        "family": "Amaryllidaceae",
        "category": "Vegetable Crop",
        "crop_type": "Bulb Vegetable Crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Kharif (June–July), Rabi (Oct–Nov), Late Kharif (Aug–Sept)",
        "duration_days": "90–150 days (variety dependent)",
        "climate": "Mild cool climate for vegetative growth and warm dry climate for bulb maturity",
        "ideal_temperature": "13°C – 24°C",
        "germination_temperature": "18°C – 30°C",
        "rainfall_requirement_mm": "350 – 550 mm",
        "water_requirement_level": "Moderate",
        "sunlight_requirement": "Full sunlight required for proper bulb formation",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained sandy loam to loamy soil",
        "soil_ph_range": "6.0 – 7.5",
        "soil_depth_requirement": "Loose soil for proper bulb enlargement",
        "salinity_tolerance": "Low to moderate",
        "drainage_requirement": "Good drainage essential to prevent bulb rot",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Bihar",
            "Gujarat",
            "Haryana",
            "Karnataka",
            "Madhya Pradesh",
            "Maharashtra",
            "Rajasthan",
            "Uttar Pradesh",

        ],
        # -------------------------------------------------
        "land_preparation": [
            "2–3 deep ploughings for fine tilth",
            "Remove stones and previous crop residues",
            "Incorporate 10–15 tons FYM per acre",
            "Prepare raised beds for better drainage",
            "Level field properly for uniform irrigation"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Certified high-yielding varieties or hybrids",
            "seed_rate_per_acre": "4–5 kg (for transplanting)",
            "seed_selection": "Healthy, bold and disease-free seeds",
            "seed_treatment": [
                "Treat seeds with fungicide before sowing",
                "Trichoderma treatment for fungal protection",
                "Biofertilizer treatment for better root growth"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Nursery raising and transplanting",
        "row_spacing": "15 cm",
        "plant_spacing": "8–10 cm between plants",
        "sowing_depth": "1–1.5 cm depth",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "germination_stage": {
                "duration": "0–10 days",
                "details": "Seeds sprout and initial roots develop."
            },
            "nursery_stage": {
                "duration": "0–45 days",
                "details": "Seedlings grow in nursery before transplanting."
            },
            "vegetative_stage": {
                "duration": "30–70 days",
                "details": "Rapid leaf growth and establishment."
            },
            "bulb_initiation_stage": {
                "duration": "60–90 days",
                "details": "Bulb formation starts depending on day length."
            },
            "bulb_development_stage": {
                "duration": "90–120 days",
                "details": "Bulbs enlarge and gain weight."
            },
            "maturity_stage": {
                "duration": "120–150 days",
                "details": "Leaves bend and neck fall indicates maturity."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_transplanting": "Light irrigation for establishment",
            "critical_stages": [
                "Bulb initiation stage",
                "Bulb development stage"
            ],
            "frequency": "Every 7–10 days depending on soil",
            "avoid": "Waterlogging and excess irrigation near harvest"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "10–15 tons FYM per acre",
            "nitrogen": "100 kg/ha split doses",
            "phosphorus": "50 kg/ha basal dose",
            "potassium": "50 kg/ha",
            "sulphur": "20–25 kg/ha for better bulb pungency",
            "biofertilizers": "Azospirillum recommended"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "cyperus_rotundus": {
                "description": "Nut grass spreading through underground tubers.",
                "damage": "Competes heavily for nutrients and water.",
                "control": "Deep ploughing and manual removal."
            },
            "parthenium": {
                "description": "Invasive broadleaf weed.",
                "damage": "Reduces crop growth and yield.",
                "control": "Manual uprooting before flowering."
            },
            "chenopodium": {
                "description": "Common winter weed in vegetable fields.",
                "damage": "Competes during early stages.",
                "control": "Timely hand weeding."
            },
            "amaranthus": {
                "description": "Fast growing broadleaf weed.",
                "damage": "Shades onion seedlings.",
                "control": "Mechanical weeding."
            }
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "thrips": {
                "description": "Tiny insects sucking sap from leaves.",
                "symptoms": "Silvering and curling of leaves.",
                "control": "Neem oil spray or recommended insecticide."
            },
            "onion_maggot": {
                "description": "Larvae feed on bulbs underground.",
                "symptoms": "Rotting and wilting plants.",
                "control": "Soil treatment before planting."
            },
            "cutworm": {
                "description": "Caterpillars cutting young seedlings at base.",
                "symptoms": "Seedlings fall down overnight.",
                "control": "Soil insecticide and field sanitation."
            },
            "aphids": {
                "description": "Sap sucking insects on tender leaves.",
                "symptoms": "Yellowing and virus transmission.",
                "control": "Systemic insecticide spray."
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "purple_blight": {
                "description": "Fungal disease causing purple lesions on leaves.",
                "symptoms": "Leaf drying and reduced bulb size.",
                "control": "Fungicide spray and crop rotation."
            },
            "downy_mildew": {
                "description": "Fungal infection under humid conditions.",
                "symptoms": "Grayish mold and leaf collapse.",
                "control": "Avoid excess moisture and spray fungicide."
            },
            "basal_rot": {
                "description": "Soil borne fungal disease.",
                "symptoms": "Bulb rot from bottom.",
                "control": "Good drainage and seed treatment."
            },
            "neck_rot": {
                "description": "Post-harvest fungal disease.",
                "symptoms": "Soft rot at neck region.",
                "control": "Proper curing before storage."
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "90–150 days after transplanting",
            "maturity_indicators": [
                "50–70% neck fall",
                "Bulbs firm and well developed",
                "Outer skin dry"
            ],
            "method": "Uproot bulbs and cure in field for 3–5 days"
        },

        "average_yield_per_acre": "100–140 quintals",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Cure bulbs properly before storage",
            "Store in well ventilated dry place",
            "Avoid high humidity to prevent rot"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "40 kcal",
            "carbohydrates": "9 g",
            "fiber": "1.7 g",
            "vitamin_C": "7 mg",
            "folate": "19 mcg",
            "potassium": "146 mg"
        },

        "nutrition_explanation": [
            "Low calorie vegetable",
            "Rich in antioxidants",
            "Contains sulfur compounds",
            "Supports digestion"
        ],

        "health_benefits": [
            "Improves immunity",
            "Supports heart health",
            "Helps control blood sugar",
            "Anti-inflammatory properties",
            "Improves digestion"
        ],

        "economic_importance": [
            "High market demand vegetable",
            "Used in almost all cuisines",
            "Export commodity",
            "Processed into flakes and powder"
        ],

        "risk_factors": [
            "Price fluctuation in market",
            "Storage losses due to rot",
            "High pest attack during dry season"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/onion.jpg",
            "pests": [
                "static/images/pests/thrips.jpg",
                "static/images/pests/onion_maggot.jpg",
                "static/images/pests/cutworm.jpg",
                "static/images/pests/aphids.jpg"
            ],
            "diseases": [
                "static/images/diseases/purple_blight.jpg",
                "static/images/diseases/downy_mildew.jpg",
                "static/images/diseases/basal_rot.jpg",
                "static/images/diseases/neck_rot.jpg"
            ],
            "weeds": [
                "static/images/weeds/cyperus_rotundus.jpg",
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/chenopodium.jpg",
                "static/images/weeds/amaranthus.jpg"
            ]
        }
    }
}