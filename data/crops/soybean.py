crop_data = {
    "soybean": {
        "name": "Soybean",
        "scientific_name": "Glycine max",
        "family": "Fabaceae",
        "category": "Oilseed Crop",
        "crop_type": "Leguminous Oilseed and Protein Crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Kharif (June–July)",
        "duration_days": "90–120 days (variety dependent)",
        "climate": "Warm tropical to subtropical climate",
        "ideal_temperature": "20°C – 30°C",
        "germination_temperature": "18°C – 32°C",
        "rainfall_requirement_mm": "500 – 900 mm",
        "water_requirement_level": "Moderate",
        "sunlight_requirement": "Full sunlight required for flowering and pod development",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained loam to clay loam soil",
        "soil_ph_range": "6.0 – 7.5",
        "soil_depth_requirement": "Deep fertile soil for strong root development",
        "salinity_tolerance": "Low",
        "drainage_requirement": "Good drainage essential to prevent root rot",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Arunachal Pradesh",
            "Chhattisgarh",
            "Jharkhand",
            "Karnataka",
            "Madhya Pradesh",
            "Maharashtra",
            "Nagaland",
            "Rajasthan",
            "Sikkim",
            "Telangana",
            "Uttar Pradesh",
            "Uttarakhand",

        ],


        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "2–3 deep ploughings for fine tilth",
            "Remove weeds and crop residues",
            "Incorporate 8–10 tons FYM per acre",
            "Level field properly",
            "Ensure proper drainage channels"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Certified high-yielding varieties",
            "seed_rate_per_acre": "25–30 kg (variety dependent)",
            "seed_selection": "Healthy, bold and disease-free seeds",
            "seed_treatment": [
                "Treat with fungicide before sowing",
                "Rhizobium inoculation for nitrogen fixation",
                "Trichoderma treatment for soil disease protection"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Line sowing using seed drill",
        "row_spacing": "30–45 cm",
        "plant_spacing": "5–10 cm between plants",
        "sowing_depth": "3–5 cm depth",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "germination_stage": {
                "duration": "0–7 days",
                "details": "Seed germinates and seedling emerges."
            },
            "vegetative_stage": {
                "duration": "7–35 days",
                "details": "Rapid leaf growth and branching."
            },
            "flowering_stage": {
                "duration": "35–55 days",
                "details": "Purple or white flowers appear; self-pollination occurs."
            },
            "pod_formation_stage": {
                "duration": "55–75 days",
                "details": "Pods begin to develop after fertilization."
            },
            "pod_filling_stage": {
                "duration": "75–100 days",
                "details": "Seeds enlarge and accumulate protein and oil."
            },
            "maturity_stage": {
                "duration": "100–120 days",
                "details": "Leaves yellow and pods turn brown."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_sowing": "Light irrigation if rainfall insufficient",
            "critical_stages": [
                "Flowering stage",
                "Pod formation stage",
                "Pod filling stage"
            ],
            "frequency": "Every 12–15 days if rainfall inadequate",
            "avoid": "Waterlogging during flowering"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "8–10 tons FYM per acre",
            "nitrogen": "20 kg/ha starter dose",
            "phosphorus": "60 kg/ha basal dose",
            "potassium": "40 kg/ha",
            "sulphur": "20 kg/ha",
            "biofertilizers": "Rhizobium and PSB recommended"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "trianthema": {
                "description": "Fast-growing broadleaf weed.",
                "damage": "Competes during early growth stage.",
                "control": "Hand weeding and pre-emergence herbicide."
            },
            "cyperus": {
                "description": "Nut grass spreading through tubers.",
                "damage": "Reduces nutrient availability.",
                "control": "Deep ploughing and herbicide."
            },
            "parthenium": {
                "description": "Invasive weed common in Kharif season.",
                "damage": "Reduces yield significantly.",
                "control": "Manual removal before flowering."
            },
            "digera_arvensis": {
                "description": "Common rainy-season weed.",
                "damage": "Aggressive competition.",
                "control": "Timely mechanical weeding."
            }
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "stem_fly": {
                "description": "Larvae bore into stem.",
                "symptoms": "Wilting and plant death.",
                "control": "Seed treatment and insecticide spray."
            },
            "girdle_beetle": {
                "description": "Cuts stem at mid height.",
                "symptoms": "Top portion dries.",
                "control": "Field sanitation and insecticide."
            },
            "leaf_miner": {
                "description": "Larvae mine inside leaves.",
                "symptoms": "Brown zig-zag tunnels.",
                "control": "Insecticide spray."
            },
            "spodoptera": {
                "description": "Leaf eating caterpillar.",
                "symptoms": "Defoliation.",
                "control": "Pheromone traps and spray."
            },
            "whitefly": {
                "description": "Sap sucking insect transmitting viral diseases.",
                "symptoms": "Yellowing and curling of leaves.",
                "control": "Neem oil and systemic insecticide."
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "rust": {
                "description": "Fungal disease forming reddish pustules.",
                "symptoms": "Leaf drying and defoliation.",
                "control": "Resistant varieties and fungicide."
            },
            "yellow_mosaic": {
                "description": "Viral disease transmitted by whitefly.",
                "symptoms": "Yellow patches on leaves.",
                "control": "Control vector and resistant varieties."
            },
            "charcoal_rot": {
                "description": "Soil borne fungal disease.",
                "symptoms": "Root rot and plant drying.",
                "control": "Crop rotation and seed treatment."
            },
            "anthracnose": {
                "description": "Fungal infection affecting pods and stems.",
                "symptoms": "Dark lesions on pods.",
                "control": "Fungicide spray."
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "100–120 days after sowing",
            "maturity_indicators": [
                "Leaves turn yellow and drop",
                "Pods turn brown",
                "Seeds harden"
            ],
            "method": "Cut plants and thresh after drying"
        },

        "average_yield_per_acre": "8–12 quintals",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Dry seeds to 10–12% moisture",
            "Store in dry ventilated area",
            "Avoid fungal contamination"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "446 kcal",
            "protein": "36 g",
            "fat": "20 g",
            "fiber": "9 g",
            "iron": "15 mg",
            "calcium": "277 mg"
        },

        "nutrition_explanation": [
            "Very high protein content",
            "Rich in healthy fats",
            "Excellent plant-based protein source",
            "Contains essential amino acids"
        ],

        "health_benefits": [
            "Supports muscle growth",
            "Improves heart health",
            "Helps regulate cholesterol",
            "Supports bone strength",
            "Used in tofu and soy products"
        ],

        "economic_importance": [
            "Major oilseed crop",
            "Used for edible oil production",
            "Soy meal used as animal feed",
            "Export commodity"
        ],

        "risk_factors": [
            "Waterlogging reduces yield",
            "High pest incidence during flowering",
            "Price fluctuation",
            "Viral disease outbreak risk"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/soybean.jpg",
            "pests": [
                "static/images/pests/stem_fly.jpg",
                "static/images/pests/girdle_beetle.jpg",
                "static/images/pests/leaf_miner.jpg",
                "static/images/pests/spodoptera.jpg",
                "static/images/pests/whitefly.jpg"
            ],
            "diseases": [
                "static/images/diseases/rust.jpg",
                "static/images/diseases/yellow_mosaic.jpg",
                "static/images/diseases/charcoal_rot.jpg",
                "static/images/diseases/anthracnose.jpg"
            ],
            "weeds": [
                "static/images/weeds/trianthema.jpg",
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/digera_arvensis.jpg"
            ]
        }
    }
}