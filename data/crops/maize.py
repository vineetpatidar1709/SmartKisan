crop_data = {
    "maize": {
        "name": "Maize",
        "scientific_name": "Zea mays",
        "family": "Poaceae",
        "category": "Cereal Crop",
        "crop_type": "Food, feed and industrial grain crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Kharif (June–July), Rabi (Oct–Nov in some regions), Summer (Jan–Feb)",
        "duration_days": "90–120 days (variety dependent)",
        "climate": "Warm tropical and subtropical climate",
        "ideal_temperature": "21°C – 30°C",
        "germination_temperature": "18°C – 25°C",
        "rainfall_requirement_mm": "500 – 800 mm",
        "water_requirement_level": "Moderate",
        "sunlight_requirement": "Requires full sunlight for proper cob development",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained loamy to sandy loam soil",
        "soil_ph_range": "5.5 – 7.5",
        "soil_depth_requirement": "Deep fertile soil for strong root system",
        "salinity_tolerance": "Low to Moderate",
        "drainage_requirement": "Good drainage required to prevent root diseases",

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
            "Himachal Pradesh",
            "Jammu and Kashmir",
            "Jharkhand",
            "Karnataka",
            "Madhya Pradesh",
            "Maharashtra",
            "Meghalaya",
            "Nagaland",
            "Odisha",
            "Punjab",
            "Rajasthan",
            "Sikkim",
            "Telangana",
            "Tripura",
            "Uttar Pradesh",
            "West Bengal",

        ],


        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "1–2 deep ploughings to loosen soil",
            "2 harrowings to obtain fine tilth",
            "Remove weeds and previous crop residues",
            "Apply 8–10 tons FYM per acre",
            "Level the field properly for uniform irrigation"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Certified hybrid or composite varieties",
            "seed_rate_per_acre": "8–10 kg (grain maize), 12–15 kg (sweet corn)",
            "seed_selection": "Bold, uniform and disease-free seeds",
            "seed_treatment": [
                "Treat with fungicide to prevent seed rot",
                "Insecticide treatment against soil pests",
                "Biofertilizer treatment for improved root growth"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Line sowing using seed drill or dibbling",
        "row_spacing": "60–75 cm",
        "plant_spacing": "20–25 cm between plants",
        "sowing_depth": "4–6 cm depth",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "germination_stage": {
                "duration": "0–7 days",
                "details": "Seeds sprout and primary roots establish."
            },
            "seedling_stage": {
                "duration": "7–20 days",
                "details": "Early leaf formation and rapid root growth."
            },
            "vegetative_stage": {
                "duration": "20–45 days",
                "details": "Rapid stem elongation and leaf expansion."
            },
            "tasseling_stage": {
                "duration": "45–60 days",
                "details": "Male flowers (tassels) emerge at top."
            },
            "silking_stage": {
                "duration": "55–70 days",
                "details": "Silks emerge from ears for pollination."
            },
            "grain_filling_stage": {
                "duration": "70–100 days",
                "details": "Kernels develop and accumulate starch."
            },
            "maturity_stage": {
                "duration": "90–120 days",
                "details": "Leaves dry and kernels harden."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "first_irrigation": "Immediately after sowing if soil dry",
            "critical_stages": [
                "Knee-high stage",
                "Tasseling stage",
                "Silking stage",
                "Grain filling stage"
            ],
            "frequency": "Every 10–12 days depending on rainfall",
            "avoid": "Water stress during tasseling and silking"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "8–10 tons FYM per acre",
            "nitrogen": "100–150 kg/ha (split application)",
            "phosphorus": "50–60 kg/ha",
            "potassium": "40–50 kg/ha",
            "micronutrients": "Zinc recommended in deficient soils",
            "biofertilizers": "Azospirillum for root growth"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "echinochloa": {
                "description": "Common grassy weed in maize fields.",
                "damage": "Competes for nutrients and sunlight.",
                "control": "Pre-emergence herbicide and early hand weeding."
            },
            "cyperus": {
                "description": "Nut grass spreading through tubers.",
                "damage": "Reduces moisture availability.",
                "control": "Deep ploughing and mechanical removal."
            },
            "amaranthus": {
                "description": "Fast-growing broadleaf weed.",
                "damage": "Suppresses early maize growth.",
                "control": "Manual weeding at early stage."
            },
            "parthenium": {
                "description": "Invasive weed in many regions.",
                "damage": "Reduces yield and competes heavily.",
                "control": "Uprooting before flowering."
            }
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "stem_borer": {
                "description": "Larvae bore into stem and feed internally.",
                "symptoms": "Dead heart in young plants.",
                "control": "Apply recommended insecticide."
            },
            "fall_armyworm": {
                "description": "Highly destructive caterpillar pest.",
                "symptoms": "Irregular holes and window panes on leaves.",
                "control": "Pheromone traps and insecticide spray."
            },
            "cutworm": {
                "description": "Soil pest cutting seedlings at base.",
                "symptoms": "Plants fall suddenly.",
                "control": "Soil treatment before sowing."
            },
            "aphids": {
                "description": "Sap sucking insects on leaves and cobs.",
                "symptoms": "Yellowing and sticky leaves.",
                "control": "Neem oil or systemic insecticide."
            },
            "cob_borer": {
                "description": "Larvae feed on developing kernels.",
                "symptoms": "Damaged grains and holes in cobs.",
                "control": "Timely insecticide spray."
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "leaf_blight": {
                "description": "Fungal disease causing elongated brown lesions.",
                "symptoms": "Reduced photosynthesis and yield.",
                "control": "Fungicide spray."
            },
            "downy_mildew": {
                "description": "Fungal disease affecting young plants.",
                "symptoms": "Yellow streaks on leaves.",
                "control": "Use resistant varieties."
            },
            "rust": {
                "description": "Reddish pustules on leaf surface.",
                "symptoms": "Premature drying of leaves.",
                "control": "Fungicide application."
            },
            "smut": {
                "description": "Fungal disease forming tumor-like growths.",
                "symptoms": "Swollen black masses on cobs.",
                "control": "Field sanitation and resistant varieties."
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "90–120 days after sowing",
            "maturity_indicators": [
                "Husks turn brown and dry",
                "Kernels hard and shiny",
                "Black layer forms at base of kernel"
            ],
            "method": "Manual harvesting or combine harvester"
        },

        "average_yield_per_acre": "18–30 quintals (grain maize)",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Dry cobs to 12–14% moisture",
            "Shell kernels properly",
            "Store in dry and ventilated place",
            "Protect from storage pests"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "365 kcal",
            "protein": "9 g",
            "carbohydrates": "74 g",
            "fiber": "7 g",
            "magnesium": "127 mg",
            "vitamin_B6": "0.6 mg"
        },

        "nutrition_explanation": [
            "Rich in carbohydrates for energy",
            "Contains dietary fiber",
            "Good source of vitamins and minerals",
            "Provides plant-based protein"
        ],

        "health_benefits": [
            "Supports digestive health",
            "Provides sustained energy",
            "Supports heart health",
            "Rich in antioxidants",
            "Gluten-free grain option"
        ],

        "economic_importance": [
            "Staple food crop in many regions",
            "Used as animal feed",
            "Raw material for starch and ethanol industries",
            "Export commodity"
        ],

        "risk_factors": [
            "Fall armyworm infestation risk",
            "Water stress during silking reduces yield",
            "Storage pest infestation"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/maize.jpg",
            "pests": [
                "static/images/pests/stem_borer.jpg",
                "static/images/pests/fall_armyworm.jpg",
                "static/images/pests/cutworm.jpg",
                "static/images/pests/aphids.jpg",
                "static/images/pests/cob_borer.jpg"
            ],
            "diseases": [
                "static/images/diseases/leaf_blight.jpg",
                "static/images/diseases/downy_mildew.jpg",
                "static/images/diseases/rust.jpg",
                "static/images/diseases/smut.jpg"
            ],
            "weeds": [
                "static/images/weeds/echinochloa.jpg",
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/amaranthus.jpg",
                "static/images/weeds/parthenium.jpg"
            ]
        }
    }
}