crop_data = {
    "bajra": {
        "name": "Bajra (Pearl Millet)",
        "scientific_name": "Pennisetum glaucum",
        "family": "Poaceae",
        "category": "Cereal Crop",
        "crop_type": "Drought-resistant coarse grain",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Kharif (Jun-Jul)",
        "duration_days": "70–90 days (variety dependent)",
        "climate": "Arid tropical climate",
        "ideal_temperature": "25°C – 35°C",
        "germination_temperature": "25°C – 30°C",
        "rainfall_requirement_mm": "200 – 400 mm",
        "water_requirement_level": "Low",
        "sunlight_requirement": "Full sunlight required",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Light sandy to loamy soil",
        "soil_ph_range": "5.5 – 8.0",
        "soil_depth_requirement": "Shallow to medium deep",
        "salinity_tolerance": "High",
        "drainage_requirement": "Well-drained",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Arunachal Pradesh",
            "Bihar",
            "Gujarat",
            "Himachal Pradesh",
            "Jammu and Kashmir",
            "Haryana",
            "Karnataka",
            "Madhya Pradesh",
            "Maharashtra",
            "Nagaland",
            "Rajasthan",
            "Uttar Pradesh",
            "Uttarakhand",

        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "1-2 ploughings",
            "Add FYM 8-10 t/ha",
            "Light harrowing",
            "Prepare field for sowing"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Improved varieties",
            "seed_rate_per_hectare": "4-5 kg/ha",
            "varieties": "HHB 67, ICMH 356, RCB 311"
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Line sowing or broadcasting",
        "row_spacing": "45-60 cm",
        "plant_spacing": "10-15 cm",
        "sowing_depth": "2-3 cm",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "seedling_stage": {
                "duration": "0-10 days",
                "details": "Germination and seedling establishment."
            },
            "vegetative_stage": {
                "duration": "10-35 days",
                "details": "Tillering and stem growth."
            },
            "flowering_stage": {
                "duration": "35-55 days",
                "details": "Ear head emergence and flowering."
            },
            "grain_development_stage": {
                "duration": "55-90 days",
                "details": "Grain filling and maturity."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_sowing": "First irrigation if needed",
            "critical_stages": [
                "Flowering",
                "Grain filling"
            ],
            "frequency": "2-3 light irrigations",
            "avoid": "Excess water"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "8-10 t/ha FYM",
            "nitrogen": "40-60 kg/ha N",
            "phosphorus": "30-40 kg/ha P",
            "potassium": "20-25 kg/ha K"
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "stem_borer": {
                "description": "Stem boring larvae",
                "symptoms": "Dead heart",
                "control": "Insecticides"
            },
            "grasshopper": {
                "description": "Leaf-feeding insect",
                "symptoms": "Defoliation",
                "control": "Insecticides"
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "downy_mildew": {
                "description": "Fungal disease",
                "symptoms": "White growth on leaves",
                "control": "Resistant varieties"
            },
            "rust": {
                "description": "Fungal disease",
                "symptoms": "Brown pustules on leaves",
                "control": "Fungicides"
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "70-90 days after sowing",
            "maturity_indicators": [
                "Grain hardens",
                "Ear head turns golden",
                "Leaves dry"
            ],
            "method": "Hand cutting or threshing"
        },

        "average_yield_per_hectare": "10-15 quintals/ha",

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "363 kcal",
            "protein": "12 g",
            "carbohydrates": "67 g",
            "fiber": "11 g",
            "iron": "6.8 mg"
        },

        "nutrition_explanation": [
            "High energy grain",
            "Rich in fiber",
            "Good iron source",
            "Gluten-free",
            "More nutritious than wheat/rice"
        ],

        "health_benefits": [
            "Sustained energy release",
            "Improves digestion",
            "Heart health",
            "Blood sugar management",
            "Iron for anemia prevention"
        ],

        "economic_importance": [
            "Food security crop",
            "Drought-resistant",
            "Animal feed",
            "Fodder crop",
            "Low input cost"
        ],

        "risk_factors": [
            "Drought resistance",
            "Bird attacks",
            "Price fluctuation",
            "Limited market"
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
            "parthenium": {
                "description": "Invasive weed common in open fields",
                "damage": "Reduces yield and may cause allergies",
                "control": "Manual uprooting before flowering"
            },
            "trianthema": {
                "description": "Fast-growing broadleaf weed",
                "damage": "Competes during early growth stage",
                "control": "Mechanical weeding"
            }
        },

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/bajra.jpg",
            "pests": [
                "static/images/pests/stem_borer.jpg",
                "static/images/pests/grasshopper.jpg"
            ],
            "diseases": [
                "static/images/diseases/downy_mildew.jpg",
                "static/images/diseases/rust.jpg"
            ],
            "weeds": [
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/trianthema.jpg"
            ]
        }
    }
}
