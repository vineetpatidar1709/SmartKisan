crop_data = {
    "tomato": {
        "name": "Tomato",
        "scientific_name": "Solanum lycopersicum",
        "family": "Solanaceae",
        "category": "Vegetable Crop",
        "crop_type": "Fruit Vegetable Crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
"season": "Tomato can be grown throughout the year in different seasons. Kharif season sowing in June-July, Rabi sowing in October-November, and Summer crop in January-February. Multiple harvests possible with proper management.",
        "duration_days": "Tomato varieties take 90-120 days from transplanting to first harvest. Indeterminate varieties continue production for 3-4 months while determinate varieties complete production in 90-100 days. Total duration depends on variety and season.",
        "climate": "Tomato requires warm and moderately cool climate for good growth. It is sensitive to frost and extreme heat. Optimum conditions allow continuous flowering and fruit setting without physiological disorders.",
        "ideal_temperature": "Ideal temperature range for tomato is 18-30°C. Day temperature of 23-27°C and night temperature of 15-20°C is optimal. Temperatures above 32°C cause flower drop and fruit crack while below 12°C causes poor fruit set.",
        "germination_temperature": "20°C – 25°C",
        "rainfall_requirement_mm": "600 – 800 mm",
        "water_requirement_level": "Moderate",
        "sunlight_requirement": "Full sunlight required for flowering and fruit setting",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained sandy loam to loamy soil",
        "soil_ph_range": "6.0 – 7.0",
        "soil_depth_requirement": "Deep fertile soil rich in organic matter",
        "salinity_tolerance": "Low to moderate",
        "drainage_requirement": "Excellent drainage to prevent root diseases",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Andhra Pradesh",
            "Gujarat",
            "Haryana",
            "Karnataka",
            "Madhya Pradesh",
            "Maharashtra",
            "Punjab",
            "Tamil Nadu",
            "Uttar Pradesh",
            "West Bengal"
        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "2–3 deep ploughings to obtain fine tilth",
            "Remove previous crop residues and weeds",
            "Incorporate 10–15 tons FYM per acre",
            "Prepare raised beds for better drainage",
            "Ensure proper irrigation channels"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Certified hybrid or high-yielding varieties",
            "seed_rate_per_acre": "60–80 grams (for transplanting)",
            "seed_selection": "Healthy, bold and disease-free seeds",
            "seed_treatment": [
                "Treat with fungicide to prevent damping-off",
                "Trichoderma treatment for soil-borne disease protection",
                "Soak seeds in bio-stimulant solution for better germination"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Nursery raising and transplanting",
        "row_spacing": "60–75 cm",
        "plant_spacing": "45–60 cm between plants",
        "sowing_depth": "0.5–1 cm in nursery beds",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "germination_stage": {
                "duration": "0–7 days",
                "details": "Seeds germinate and seedlings emerge."
            },
            "seedling_stage": {
                "duration": "7–25 days",
                "details": "Seedlings develop true leaves in nursery."
            },
            "vegetative_stage": {
                "duration": "25–45 days",
                "details": "Rapid stem and leaf development."
            },
            "flowering_stage": {
                "duration": "45–65 days",
                "details": "Yellow flowers appear; pollination occurs."
            },
            "fruit_set_stage": {
                "duration": "60–80 days",
                "details": "Small green fruits develop."
            },
            "fruit_development_stage": {
                "duration": "80–110 days",
                "details": "Fruits enlarge and change color."
            },
            "maturity_stage": {
                "duration": "90–120 days",
                "details": "Fruits turn red and reach harvest stage."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_transplanting": "Light irrigation for establishment",
            "critical_stages": [
                "Flowering stage",
                "Fruit setting stage",
                "Fruit development stage"
            ],
            "frequency": "Every 5–7 days depending on soil type",
            "avoid": "Waterlogging to prevent root rot and blossom end rot"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "10–15 tons FYM per acre",
            "nitrogen": "100–120 kg/ha split doses",
            "phosphorus": "60 kg/ha basal dose",
            "potassium": "60–80 kg/ha",
            "calcium": "Essential to prevent blossom end rot",
            "biofertilizers": "Azospirillum and PSB recommended"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "cyperus_rotundus": {
                "description": "Nut grass spreading through underground tubers.",
                "damage": "Competes for nutrients and moisture.",
                "control": "Deep ploughing and herbicide application."
            },
            "amaranthus": {
                "description": "Fast-growing broadleaf weed.",
                "damage": "Reduces crop growth in early stage.",
                "control": "Mechanical weeding."
            },
            "parthenium": {
                "description": "Invasive weed in open fields.",
                "damage": "Heavy competition for nutrients.",
                "control": "Manual uprooting."
            },
            "chenopodium": {
                "description": "Common seasonal weed.",
                "damage": "Shades young plants.",
                "control": "Timely hand weeding."
            }
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "fruit_borer": {
                "description": "Larvae bore into fruits.",
                "symptoms": "Holes in fruits with internal damage.",
                "control": "Pheromone traps and insecticide spray."
            },
            "whitefly": {
                "description": "Sap sucking insect transmitting viral diseases.",
                "symptoms": "Yellowing and curling of leaves.",
                "control": "Neem oil and systemic insecticide."
            },
            "aphids": {
                "description": "Sap sucking pest on tender shoots.",
                "symptoms": "Leaf curling and stunted growth.",
                "control": "Insecticidal spray."
            },
            "thrips": {
                "description": "Tiny insects damaging flowers.",
                "symptoms": "Poor fruit setting.",
                "control": "Recommended insecticide."
            },
            "cutworm": {
                "description": "Caterpillar cutting seedlings at soil surface.",
                "symptoms": "Sudden plant collapse.",
                "control": "Soil treatment before transplanting."
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "early_blight": {
                "description": "Fungal disease causing concentric leaf spots.",
                "symptoms": "Leaf drying and defoliation.",
                "control": "Fungicide spray and crop rotation."
            },
            "late_blight": {
                "description": "Serious fungal disease in cool humid conditions.",
                "symptoms": "Brown patches on leaves and fruits.",
                "control": "Preventive fungicide spray."
            },
            "bacterial_wilt": {
                "description": "Soil-borne bacterial disease.",
                "symptoms": "Sudden wilting of plants.",
                "control": "Resistant varieties and crop rotation."
            },
            "leaf_curl": {
                "description": "Viral disease transmitted by whitefly.",
                "symptoms": "Upward curling and yellowing of leaves.",
                "control": "Control vector and remove infected plants."
            },
            "damping_off": {
                "description": "Fungal disease affecting seedlings.",
                "symptoms": "Seedling collapse in nursery.",
                "control": "Seed treatment and proper drainage."
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "90–120 days after sowing",
            "maturity_indicators": [
                "Fruits turn red or pink depending on market requirement",
                "Firm texture",
                "Full size development"
            ],
            "method": "Hand picking at breaker or fully ripe stage"
        },

        "average_yield_per_acre": "150–250 quintals",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Grade fruits based on size and quality",
            "Store at cool temperature",
            "Avoid bruising during transport",
            "Pack in ventilated crates"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "18 kcal",
            "carbohydrates": "3.9 g",
            "protein": "0.9 g",
            "fiber": "1.2 g",
            "vitamin_C": "13 mg",
            "lycopene": "8–10 mg"
        },

        "nutrition_explanation": [
            "Rich in antioxidants like lycopene",
            "Low calorie vegetable",
            "Good source of vitamin C",
            "Contains potassium and folate"
        ],

        "health_benefits": [
            "Supports heart health",
            "Boosts immunity",
            "Improves skin health",
            "Reduces risk of certain cancers",
            "Supports digestive health"
        ],

        "economic_importance": [
            "High market demand vegetable",
            "Used in processing industry (ketchup, sauce, puree)",
            "Export potential crop",
            "Provides good income to farmers"
        ],

        "risk_factors": [
            "Viral disease outbreaks",
            "Fruit borer infestation",
            "Price fluctuation",
            "Sensitive to extreme weather"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/tomato.jpg",
            "pests": [
                "static/images/pests/fruit_borer.jpg",
                "static/images/pests/whitefly.jpg",
                "static/images/pests/aphids.jpg",
                "static/images/pests/thrips.jpg",
                "static/images/pests/cutworm.jpg"
            ],
            "diseases": [
                "static/images/diseases/early_blight.jpg",
                "static/images/diseases/late_blight.jpg",
                "static/images/diseases/bacterial_wilt.jpg",
                "static/images/diseases/leaf_curl.jpg",
                "static/images/diseases/damping_off.jpg"
            ],
            "weeds": [
                "static/images/weeds/cyperus_rotundus.jpg",
                "static/images/weeds/amaranthus.jpg",
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/chenopodium.jpg"
            ]
        }
    }
}