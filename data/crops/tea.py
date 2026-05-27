crop_data = {
    "tea": {
        "name": "Tea",
        "scientific_name": "Camellia sinensis",
        "family": "Theaceae",
        "category": "Plantation Crop",
        "crop_type": "Perennial evergreen beverage crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Perennial crop (planting usually during monsoon)",
        "duration_days": "Economic lifespan 40–60 years",
        "climate": "Humid tropical and subtropical climate",
        "ideal_temperature": "18°C – 30°C",
        "germination_temperature": "20°C – 25°C",
        "rainfall_requirement_mm": "1200 – 2500 mm annually",
        "water_requirement_level": "High",
        "sunlight_requirement": "Requires diffused sunlight; partial shade beneficial",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained acidic loamy soil rich in organic matter",
        "soil_ph_range": "4.5 – 5.5",
        "soil_depth_requirement": "Deep soil (minimum 1 meter depth)",
        "salinity_tolerance": "Very low",
        "drainage_requirement": "Excellent drainage essential; sensitive to waterlogging",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Arunachal Pradesh",
            "Assam",
            "Himachal Pradesh",
            "Karnataka",
            "Kerala",
            "Nagaland",
            "Sikkim",
            "Tamil Nadu",
            "Tripura",
            "West Bengal (Darjeeling)",

        ],


        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "Clear bushes and previous vegetation",
            "Deep digging and leveling of land",
            "Establish proper drainage channels",
            "Add organic manure before planting",
            "Prepare contour planting in hilly areas"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Vegetatively propagated clones or quality seeds",
            "seed_rate_per_acre": "Approx. 4000–5000 plants per acre",
            "seed_selection": "High-yielding, pest-resistant clones preferred",
            "seed_treatment": [
                "Nursery raising under shade",
                "Root hormone treatment for cuttings",
                "Fungicide treatment before transplanting"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Transplanting nursery-raised seedlings or rooted cuttings",
        "row_spacing": "1.2 – 1.5 meters",
        "plant_spacing": "0.75 – 1.0 meter",
        "sowing_depth": "Planting pit depth 30–45 cm",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "nursery_stage": {
                "duration": "3–6 months",
                "details": "Seedlings raised under shade for strong root development."
            },
            "establishment_stage": {
                "duration": "1–2 years",
                "details": "Young plants develop strong framework; pruning starts."
            },
            "vegetative_growth_stage": {
                "duration": "Continuous",
                "details": "Bush formation through periodic pruning and tipping."
            },
            "plucking_stage": {
                "duration": "Starts after 3 years",
                "details": "Tender leaves (two leaves and a bud) plucked at intervals."
            },
            "maturity_stage": {
                "duration": "3–5 years onwards",
                "details": "Full commercial production achieved."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_planting": "Light irrigation for establishment",
            "critical_stages": [
                "Dry season",
                "Flush development stage"
            ],
            "frequency": "Every 7–10 days during dry period",
            "avoid": "Water stagnation"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "10–15 tons per acre annually",
            "nitrogen": "100–150 kg/ha per year in split doses",
            "phosphorus": "40–60 kg/ha annually",
            "potassium": "60–100 kg/ha annually",
            "micronutrients": "Magnesium and Zinc supplementation improves yield"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "parthenium": {
                "description": "Broadleaf invasive weed.",
                "damage": "Competes for nutrients and sunlight.",
                "control": "Manual removal and mulching."
            },
            "cyperus": {
                "description": "Nut grass spreading through rhizomes.",
                "damage": "Reduces plant growth.",
                "control": "Mechanical removal."
            },
            "imperata": {
                "description": "Perennial grass weed.",
                "damage": "Competes heavily for nutrients.",
                "control": "Herbicide application and deep ploughing."
            }
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "tea_mosquito_bug": {
                "description": "Sap-sucking pest attacking tender leaves.",
                "symptoms": "Brown patches and leaf drop.",
                "control": "Spray recommended insecticide."
            },
            "red_spider_mite": {
                "description": "Feeds on leaf underside.",
                "symptoms": "Bronzing and leaf drying.",
                "control": "Miticide spray and irrigation management."
            },
            "looper_caterpillar": {
                "description": "Leaf-eating caterpillar.",
                "symptoms": "Defoliation.",
                "control": "Manual removal and insecticide."
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "blister_blight": {
                "description": "Fungal disease in humid areas.",
                "symptoms": "Blister-like spots on leaves.",
                "control": "Copper fungicide spray."
            },
            "root_rot": {
                "description": "Soil-borne fungal disease.",
                "symptoms": "Wilting and root decay.",
                "control": "Improve drainage and apply fungicide."
            },
            "red_rust": {
                "description": "Algal disease on older leaves.",
                "symptoms": "Reddish patches on leaves.",
                "control": "Balanced fertilization and fungicide spray."
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "Plucking begins 3 years after planting",
            "maturity_indicators": [
                "Two leaves and a bud stage",
                "Tender and bright green leaves"
            ],
            "method": "Hand plucking at 7–15 day intervals"
        },

        "average_yield_per_acre": "800–1200 kg made tea annually",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Withering of fresh leaves",
            "Rolling and fermentation",
            "Drying and grading",
            "Packaging in moisture-proof containers"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "1 kcal (brewed tea)",
            "protein": "0 g",
            "carbohydrates": "0 g",
            "caffeine": "40–50 mg per cup",
            "antioxidants": "Rich in polyphenols"
        },

        "nutrition_explanation": [
            "Contains powerful antioxidants",
            "Low calorie beverage",
            "Contains moderate caffeine",
            "Rich in flavonoids"
        ],

        "health_benefits": [
            "Improves alertness",
            "Supports heart health",
            "Boosts metabolism",
            "Rich in antioxidants",
            "May reduce stress"
        ],

        "economic_importance": [
            "Major export commodity of India",
            "Employment generation in plantation sector",
            "High global demand beverage",
            "Long-term income crop"
        ],

        "risk_factors": [
            "Sensitive to drought stress",
            "High labor requirement",
            "Pest outbreaks reduce leaf quality",
            "Climate change affects yield"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/tea.jpg",
            "pests": [
                "static/images/pests/tea_mosquito_bug.jpg",
                "static/images/pests/red_spider_mite.jpg",
                "static/images/pests/looper_caterpillar.jpg"
            ],
            "diseases": [
                "static/images/diseases/blister_blight.jpg",
                "static/images/diseases/root_rot.jpg",
                "static/images/diseases/red_rust.jpg"
            ],
            "weeds": [
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/imperata.jpg"
            ]
        }
    }
}