crop_data = {
    "coffee": {
        "name": "Coffee",
        "scientific_name": "Coffea arabica / Coffea canephora",
        "family": "Rubiaceae",
        "category": "Commercial Crop",
        "crop_type": "Plantation Crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Planting: Monsoon (Jun-Jul)",
        "duration_days": "180-240 days (for first harvest)",
        "climate": "Tropical to subtropical highland climate",
        "ideal_temperature": "15°C – 25°C",
        "germination_temperature": "20°C – 25°C",
        "rainfall_requirement_mm": "1500 – 2500 mm",
        "water_requirement_level": "High",
        "sunlight_requirement": "Partial shade preferred",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained deep loamy soil",
        "soil_ph_range": "5.5 – 6.5",
        "soil_depth_requirement": "Deep soil (1.5m+)",
        "salinity_tolerance": "Low",
        "drainage_requirement": "Excellent drainage essential",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Andhra Pradesh",
            "Karnataka",
            "Kerala",
            "Odisha",
            "Tamil Nadu",

        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "Clear forest vegetation",
            "Terracing on slopes",
            "Pit digging (45cm x 45cm x 45cm)",
            "Shade trees planting"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Seedlings or clones",
            "seed_rate_per_hectare": "2500-3000 plants/ha",
            "varieties": "Arabica (Typica, Catimor), Robusta"
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Pit planting seedlings",
        "row_spacing": "2-3 m",
        "plant_spacing": "2-3 m",
        "sowing_depth": "At root collar level",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "seedling_stage": {
                "duration": "0-180 days",
                "details": "Nursery raising and seedling growth."
            },
            "vegetative_stage": {
                "duration": "180-365 days",
                "details": "Bush development."
            },
            "flowering_stage": {
                "duration": "Spring (Feb-Apr)",
                "details": "Flowering after monsoon."
            },
            "fruit_development": {
                "duration": "6-9 months",
                "details": "Bean development and ripening."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_planting": "First irrigation",
            "critical_stages": [
                "Flowering",
                "Fruit development"
            ],
            "frequency": " supplementary irrigation in dry season",
            "avoid": "Water stagnation"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "10-15 kg FYM per plant",
            "nitrogen": "200-250 g N per plant",
            "phosphorus": "150-200 g P per plant",
            "potassium": "150-200 g K per plant"
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "coffee_borer": {
                "description": "Stem borer",
                "symptoms": "Wilting, bore holes",
                "control": "Insecticides, sanitation"
            },
            "aphids": {
                "description": "Sap-sucking insects",
                "symptoms": "Leaf curling",
                "control": "Neem oil, insecticides"
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "coffee_rust": {
                "description": "Fungal disease",
                "symptoms": "Orange rust spots on leaves",
                "control": "Resistant varieties, fungicides"
            },
            "leaf_spot": {
                "description": "Fungal disease",
                "symptoms": "Brown lesions on leaves",
                "control": "Fungicides"
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "October-March",
            "maturity_indicators": [
                "Cherries turn red",
                "Flesh becomes soft",
                "Seeds harden"
            ],
            "method": "Hand picking of ripe cherries"
        },

        "average_yield_per_hectare": "800-1500 kg/ha (green beans)",

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "2 kcal",
            "carbohydrates": "0.5 g",
            "protein": "0.1 g",
            "caffeine": "40-80 mg",
            "antioxidants": "High"
        },

        "nutrition_explanation": [
            "Contains caffeine",
            "Rich in antioxidants",
            "Low calorie beverage",
            "Contains essential oils"
        ],

        "health_benefits": [
            "Boosts energy",
            "Improves focus",
            "Antioxidant properties",
            "May boost metabolism"
        ],

        "economic_importance": [
            "Major export commodity",
            "Employment generation",
            "Processing industry",
            "Foreign exchange earner"
        ],

        "risk_factors": [
            "Price fluctuation",
            "Climate sensitivity",
            "Pest and disease",
            "Market volatility"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
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
            "crop": "static/images/crops/coffee.jpg",
            "pests": [
                "static/images/pests/coffee_borer.jpg",
                "static/images/pests/aphids.jpg"
            ],
            "diseases": [
                "static/images/diseases/coffee_rust.jpg",
                "static/images/diseases/leaf_spot.jpg"
            ],
            "weeds": [
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/trianthema.jpg"
            ]
        }
    }
}
