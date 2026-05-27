crop_data = {
    "mustard": {
        "name": "Mustard",
        "scientific_name": "Brassica juncea",
        "family": "Brassicaceae",
        "category": "Oilseed Crop",
        "crop_type": "Rabi oilseed cash crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Rabi (October–November sowing)",
        "duration_days": "110–140 days (variety dependent)",
        "climate": "Cool and dry climate during growth, warm at maturity",
        "ideal_temperature": "10°C – 25°C",
        "germination_temperature": "8°C – 15°C",
        "rainfall_requirement_mm": "350 – 500 mm",
        "water_requirement_level": "Low to Moderate",
        "sunlight_requirement": "Requires full sunlight for better seed formation",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained loamy to clay loam soil",
        "soil_ph_range": "6.0 – 8.5",
        "soil_depth_requirement": "Medium to deep soil preferred",
        "salinity_tolerance": "Moderate",
        "drainage_requirement": "Avoid waterlogging to prevent root diseases",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Arunachal Pradesh",
            "Assam",
            "Bihar",
            "Chhattisgarh",
            "Gujarat",
            "Haryana",
            "Jharkhand",
            "Madhya Pradesh",
            "Meghalaya",
            "Nagaland",
            "Odisha",
            "Punjab",
            "Rajasthan",
            "Sikkim",
            "Uttar Pradesh",
            "West Bengal",

        ],


        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "1–2 deep ploughings to loosen soil",
            "Harrowing to achieve fine tilth",
            "Remove weeds and crop residues",
            "Apply 6–8 tons FYM per acre",
            "Level the field for uniform irrigation"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Certified high-yielding varieties",
            "seed_rate_per_acre": "1.5–2 kg",
            "seed_selection": "Bold, uniform and disease-free seeds",
            "seed_treatment": [
                "Treat with fungicide to prevent seed-borne diseases",
                "Biofertilizer treatment for root enhancement",
                "Ensure proper drying before sowing"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Line sowing using seed drill",
        "row_spacing": "30–45 cm",
        "plant_spacing": "10–15 cm between plants",
        "sowing_depth": "2–3 cm depth",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "germination_stage": {
                "duration": "0–7 days",
                "details": "Seeds sprout and primary roots develop."
            },
            "vegetative_stage": {
                "duration": "7–35 days",
                "details": "Rapid leaf and stem development."
            },
            "flowering_stage": {
                "duration": "35–60 days",
                "details": "Yellow flowers bloom and pollination occurs."
            },
            "pod_formation_stage": {
                "duration": "60–90 days",
                "details": "Pods develop and seeds begin formation."
            },
            "seed_filling_stage": {
                "duration": "90–120 days",
                "details": "Seeds accumulate oil and nutrients."
            },
            "maturity_stage": {
                "duration": "110–140 days",
                "details": "Plants turn yellow and pods dry."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "first_irrigation": "At 20–25 days after sowing",
            "critical_stages": [
                "Flowering stage",
                "Pod formation stage"
            ],
            "frequency": "2–3 irrigations depending on rainfall",
            "avoid": "Excess irrigation during maturity stage"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "6–8 tons FYM per acre",
            "nitrogen": "60–80 kg/ha (split application)",
            "phosphorus": "40–50 kg/ha",
            "potassium": "20–30 kg/ha",
            "sulphur": "20–40 kg/ha for better oil content",
            "biofertilizers": "Azotobacter recommended"
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
                "description": "Grass weed in Rabi season.",
                "damage": "Reduces plant growth and yield.",
                "control": "Pre-emergence herbicide."
            },
            "wild_mustard": {
                "description": "Closely related weed species.",
                "damage": "Competes heavily for nutrients.",
                "control": "Mechanical removal before flowering."
            },
            "melilotus": {
                "description": "Winter weed common in mustard fields.",
                "damage": "Suppresses crop growth.",
                "control": "Timely hand weeding."
            }
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "aphids": {
                "description": "Most destructive pest in mustard.",
                "symptoms": "Sticky honeydew and curling leaves.",
                "control": "Neem oil or insecticide spray."
            },
            "painted_bug": {
                "description": "Sucks sap from young plants.",
                "symptoms": "Stunted growth and shriveled seeds.",
                "control": "Early insecticide application."
            },
            "sawfly": {
                "description": "Larvae feed on leaves.",
                "symptoms": "Irregular holes on foliage.",
                "control": "Manual collection and spraying."
            },
            "diamondback_moth": {
                "description": "Caterpillar pest attacking leaves.",
                "symptoms": "Skeletonized leaves.",
                "control": "Pheromone traps and spray."
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "alternaria_blight": {
                "description": "Fungal disease causing dark spots.",
                "symptoms": "Circular lesions on leaves and pods.",
                "control": "Fungicide spray."
            },
            "white_rust": {
                "description": "Fungal disease common in cool weather.",
                "symptoms": "White pustules on leaves.",
                "control": "Use resistant varieties."
            },
            "downy_mildew": {
                "description": "Disease under humid conditions.",
                "symptoms": "Yellow patches on leaves.",
                "control": "Fungicide application."
            },
            "powdery_mildew": {
                "description": "White powdery growth on foliage.",
                "symptoms": "Reduced seed filling.",
                "control": "Timely fungicide spray."
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "110–140 days after sowing",
            "maturity_indicators": [
                "Plants turn yellow",
                "Pods become brown and dry",
                "Seeds hard and black/brown"
            ],
            "method": "Cut plants and dry before threshing"
        },

        "average_yield_per_acre": "6–10 quintals",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Dry seeds to 8–10% moisture",
            "Clean and grade properly",
            "Store in cool and dry place",
            "Protect from storage pests"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "508 kcal",
            "protein": "26 g",
            "fat": "36 g",
            "fiber": "12 g",
            "calcium": "266 mg",
            "iron": "9 mg"
        },

        "nutrition_explanation": [
            "Rich in healthy oils",
            "High protein content",
            "Contains essential minerals",
            "Used for edible oil extraction"
        ],

        "health_benefits": [
            "Supports heart health",
            "Improves digestion",
            "Anti-inflammatory properties",
            "Boosts metabolism"
        ],

        "economic_importance": [
            "Major oilseed crop in India",
            "Mustard oil production",
            "Used in pickles and condiments",
            "Oil cake used as animal feed"
        ],

        "risk_factors": [
            "Aphid outbreaks reduce yield",
            "Fungal diseases in humid weather",
            "Excess rainfall at maturity reduces seed quality"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/mustard.jpg",
            "pests": [
                "static/images/pests/aphids.jpg",
                "static/images/pests/painted_bug.jpg",
                "static/images/pests/sawfly.jpg",
                "static/images/pests/diamondback_moth.jpg"
            ],
            "diseases": [
                "static/images/diseases/alternaria_blight.jpg",
                "static/images/diseases/white_rust.jpg",
                "static/images/diseases/downy_mildew.jpg",
                "static/images/diseases/powdery_mildew.jpg"
            ],
            "weeds": [
                "static/images/weeds/chenopodium_album.jpg",
                "static/images/weeds/phalaris_minor.jpg",
                "static/images/weeds/wild_mustard.jpg",
                "static/images/weeds/melilotus.jpg"
            ]
        }
    }
}