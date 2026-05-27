crop_data = {
    "cucumber": {
        "name": "Cucumber",
        "scientific_name": "Cucumis sativus",
        "family": "Cucurbitaceae",
        "category": "Vegetable Crop",
        "crop_type": "Summer season vine vegetable crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Summer (January–March in North India; Year-round in protected cultivation)",
        "duration_days": "50–75 days (variety dependent)",
        "climate": "Warm and humid climate with high sunlight",
        "ideal_temperature": "22°C – 32°C",
        "germination_temperature": "20°C – 30°C",
        "rainfall_requirement_mm": "400 – 600 mm",
        "water_requirement_level": "Moderate to High",
        "sunlight_requirement": "Requires full sunlight for proper vine growth and fruit development",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained sandy loam to loamy soils rich in organic matter",
        "soil_ph_range": "6.0 – 7.0",
        "soil_depth_requirement": "Medium depth soil preferred",
        "salinity_tolerance": "Low",
        "drainage_requirement": "Highly sensitive to waterlogging; raised beds recommended",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Uttar Pradesh",
            "Karnataka",
            "Andhra Pradesh",
            "Telangana",
            "Madhya Pradesh",
            "Tamil Nadu",
            "Haryana"
        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "Deep ploughing followed by 2–3 harrowings",
            "Remove weeds and crop residues",
            "Incorporate 10–12 tons FYM per acre",
            "Prepare raised beds or ridges for drainage",
            "Install drip irrigation system before sowing"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Hybrid or open-pollinated high-yielding varieties",
            "seed_rate_per_acre": "1–1.5 kg",
            "seed_selection": "Uniform, bold seeds with high germination percentage",
            "seed_treatment": [
                "Treat with Thiram or Carbendazim before sowing",
                "Trichoderma treatment to prevent damping-off",
                "Soaking seeds for 4–6 hours improves germination"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Dibbling method on raised beds or pits",
        "row_spacing": "1.5 – 2.0 meters",
        "plant_spacing": "45 – 60 cm",
        "sowing_depth": "2–3 cm",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "germination_stage": {
                "duration": "0–6 days",
                "details": "Seed absorbs moisture and cotyledons emerge above soil."
            },
            "seedling_stage": {
                "duration": "6–15 days",
                "details": "True leaves develop; root establishment begins."
            },
            "vegetative_stage": {
                "duration": "15–30 days",
                "details": "Rapid vine elongation and branching."
            },
            "flowering_stage": {
                "duration": "25–40 days",
                "details": "Male and female flowers appear; pollination mainly by bees."
            },
            "fruit_development_stage": {
                "duration": "35–55 days",
                "details": "Fruits enlarge rapidly; harvesting begins early."
            },
            "maturity_stage": {
                "duration": "50–75 days",
                "details": "Fruits reach marketable size; regular harvesting required."
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
            "frequency": "Every 4–6 days in summer (drip recommended)",
            "avoid": "Water stagnation to prevent root rot"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "10–12 tons FYM per acre",
            "nitrogen": "40–50 kg/acre split doses",
            "phosphorus": "25–30 kg/acre at sowing",
            "potassium": "25–35 kg/acre during fruiting",
            "micronutrients": "Boron and Zinc improve fruit quality and yield"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "parthenium": {
                "description": "Invasive broadleaf weed.",
                "damage": "Competes for nutrients and moisture.",
                "control": "Manual removal and mulching."
            },
            "cyperus": {
                "description": "Nut grass spreading via underground rhizomes.",
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
                "symptoms": "Fruit rotting and maggot infestation.",
                "control": "Use pheromone traps and cover fruits."
            },
            "aphids": {
                "description": "Sap-sucking insects on tender shoots.",
                "symptoms": "Leaf curling and virus transmission.",
                "control": "Neem oil or systemic insecticide."
            },
            "red_pumpkin_beetle": {
                "description": "Feeds on leaves and flowers.",
                "symptoms": "Skeletonized leaves.",
                "control": "Dusting with recommended insecticide."
            },
            "thrips": {
                "description": "Damages flowers and young fruits.",
                "symptoms": "Poor fruit set.",
                "control": "Spray appropriate insecticide."
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
                "description": "Fungal disease in humid conditions.",
                "symptoms": "Yellow spots on leaves.",
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
            "harvest_time": "50–75 days after sowing",
            "maturity_indicators": [
                "Fruits reach desired market size",
                "Bright green color",
                "Tender and firm texture"
            ],
            "method": "Harvest manually every 2–3 days"
        },

        "average_yield_per_acre": "60–100 quintals",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Handle fruits carefully to avoid bruising",
            "Store at 10–12°C temperature",
            "Avoid excessive stacking",
            "Transport in ventilated crates"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "16 kcal",
            "protein": "0.7 g",
            "carbohydrates": "3.6 g",
            "fiber": "0.5 g",
            "vitamin_c": "3 mg",
            "water_content": "95%"
        },

        "nutrition_explanation": [
            "Extremely hydrating vegetable",
            "Low calorie and ideal for weight management",
            "Contains antioxidants",
            "Good for digestion"
        ],

        "health_benefits": [
            "Prevents dehydration",
            "Supports skin health",
            "Aids digestion",
            "Helps regulate blood pressure",
            "Supports weight management"
        ],

        "economic_importance": [
            "High market demand in summer",
            "Suitable for greenhouse cultivation",
            "Short duration with quick returns",
            "Used in salad and processing industry"
        ],

        "risk_factors": [
            "Highly sensitive to waterlogging",
            "Poor pollination reduces yield",
            "Fruit deformation due to nutrient deficiency"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/cucumber.jpg",
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