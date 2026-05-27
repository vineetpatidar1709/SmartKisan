crop_data = {
    "apple": {
        "name": "Apple",
        "scientific_name": "Malus domestica",
        "family": "Rosaceae",
        "category": "Fruit Crop",
        "crop_type": "Temperate Fruit",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Winter (Dec-Feb planting), Harvest in Summer-Autumn",
        "duration_days": "150–180 days (variety dependent)",
        "climate": "Cool temperate climate with winter chilling",
        "ideal_temperature": "15°C – 25°C (summer), 0°C – 7°C (winter)",
        "germination_temperature": "20°C – 25°C",
        "rainfall_requirement_mm": "1000 – 1500 mm",
        "water_requirement_level": "Moderate to High",
        "sunlight_requirement": "Full sunlight required for fruit development",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Deep, well-drained loamy soil",
        "soil_ph_range": "5.5 – 6.5",
        "soil_depth_requirement": "Deep soil (1-1.5m) for root development",
        "salinity_tolerance": "Low",
        "drainage_requirement": "Excellent drainage essential",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Arunachal Pradesh",
            "Assam",
            "Himachal Pradesh",
            "Jammu and Kashmir",
            "Kerala",
            "Meghalaya",
            "Nagaland",
            "Tripura",
            "Uttarakhand",
            "West Bengal",

        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "Deep pits (1m x 1m x 1m) dug months before planting",
            "Add well-decomposed FYM and soil amendments",
            "Ensure proper drainage channels",
            "Layout according to spacing system"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Grafting on seedling rootstocks",
            "seed_rate_per_hectare": "100-150 plants/ha",
            "varieties": "Red Delicious, Golden Delicious, Royal Gala, Fuji"
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Budding/grafting on rootstock",
        "row_spacing": "5-6 m",
        "plant_spacing": "5-6 m",
        "sowing_depth": "At graft union level",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "dormant_stage": {
                "duration": "Dec-Feb",
                "details": "Winter dormancy period."
            },
            "flowering_stage": {
                "duration": "Mar-Apr",
                "details": "Bloom and fruit set."
            },
            "fruit_development": {
                "duration": "May-Aug",
                "details": "Fruit growth and maturation."
            },
            "harvest_stage": {
                "duration": "Aug-Oct",
                "details": "Fruit ripens and harvested."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_planting": "First irrigation after planting",
            "critical_stages": [
                "Bloom stage",
                "Fruit development stage"
            ],
            "frequency": "7-10 days interval in summer",
            "avoid": "Waterlogging"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "10-15 kg FYM per tree",
            "nitrogen": "200-300 g N per tree",
            "phosphorus": "150-200 g P per tree",
            "potassium": "200-300 g K per tree"
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "codling_moth": {
                "description": "Fruit borer larva",
                "symptoms": "Holes in fruits, frass exudation",
                "control": "Pheromone traps, insecticides"
            },
            "aphids": {
                "description": "Sap-sucking insects",
                "symptoms": "Leaf curling, sticky honeydew",
                "control": "Neem oil, insecticides"
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "apple_scab": {
                "description": "Fungal disease",
                "symptoms": "Dark scab lesions on leaves and fruits",
                "control": " Fungicides, resistant varieties"
            },
            "powdery_mildew": {
                "description": "Fungal disease",
                "symptoms": "White powdery coating on leaves",
                "control": "Sulfur fungicides"
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "150-180 days after planting",
            "maturity_indicators": [
                "Fruit develops characteristic color",
                "Seeds turn brown",
                "Fruit easily separates from spur"
            ],
            "method": "Hand picking carefully"
        },

        "average_yield_per_hectare": "15-25 tonnes/ha",

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "52 kcal",
            "carbohydrates": "14 g",
            "protein": "0.3 g",
            "fiber": "2.4 g",
            "vitamin_C": "4 mg",
            "potassium": "107 mg"
        },

        "nutrition_explanation": [
            "Good source of dietary fiber",
            "Contains vitamin C",
            "Rich in antioxidants",
            "Low calorie fruit"
        ],

        "health_benefits": [
            "Supports heart health",
            "Aids digestion",
            "Boosts immunity",
            "May reduce cancer risk"
        ],

        "economic_importance": [
            "High-value export fruit",
            "Processing industry (juices, canned)",
            "Fresh market demand",
            "Employment generation"
        ],

        "risk_factors": [
            "Chilling hour requirement",
            "Prone to frost damage",
            "Disease susceptibility",
            "High initial investment"
        ],

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "cyperus": {
                "description": "Nut grass, spreads through underground tubers",
                "damage": "Competes for nutrients and moisture",
                "control": "Deep ploughing and repeated removal"
            },
            "chenopodium_album": {
                "description": "Common lambsquarters, broadleaf weed",
                "damage": "Competes for nutrients in early growth",
                "control": "Mechanical weeding"
            },
            "parthenium": {
                "description": "Invasive weed common in open fields",
                "damage": "Reduces yield and may cause allergies",
                "control": "Manual uprooting before flowering"
            }
        },

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/apple.jpg",
            "pests": [
                "static/images/pests/codling_moth.jpg",
                "static/images/pests/aphids.jpg"
            ],
            "diseases": [
                "static/images/diseases/apple_scab.jpg",
                "static/images/diseases/powdery_mildew.jpg"
            ],
            "weeds": [
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/chenopodium_album.jpg",
                "static/images/weeds/parthenium.jpg"
            ]
        }
    }
}
