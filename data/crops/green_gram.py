crop_data = {
    "green_gram": {
        "name": "Green Gram",
        "scientific_name": "Vigna radiata",
        "family": "Fabaceae",
        "category": "Pulse Crop",
        "crop_type": "Leguminous protein-rich pulse crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Kharif (June–July), Summer (March–April), Rabi (in South India)",
        "duration_days": "60–75 days",
        "climate": "Warm tropical and subtropical climate",
        "ideal_temperature": "25°C – 35°C",
        "germination_temperature": "20°C – 30°C",
        "rainfall_requirement_mm": "400 – 600 mm",
        "water_requirement_level": "Low to Moderate",
        "sunlight_requirement": "Full sunlight required for optimum flowering and pod formation",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained sandy loam to loamy soil",
        "soil_ph_range": "6.2 – 7.8",
        "soil_depth_requirement": "Moderately deep soil for proper root development",
        "salinity_tolerance": "Low to Moderate",
        "drainage_requirement": "Good drainage required; sensitive to waterlogging",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Andhra Pradesh",
            "Arunachal Pradesh",
            "Assam",
            "Chhattisgarh",
            "Haryana",
            "Jharkhand",
            "Karnataka",
            "Madhya Pradesh",
            "Maharashtra",
            "Rajasthan",
            "Tamil Nadu",
            "Tripura",
            "Uttar Pradesh",

        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "1–2 ploughings to create fine tilth",
            "Remove weeds and crop residues",
            "Incorporate 5–8 tons FYM per acre",
            "Level field properly to avoid water stagnation",
            "Prepare raised beds in heavy soil areas"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Certified high-yielding and disease-resistant varieties",
            "seed_rate_per_acre": "8–12 kg (depending on season and variety)",
            "seed_selection": "Bold, healthy, disease-free seeds with high germination rate",
            "seed_treatment": [
                "Treat seeds with Carbendazim or Thiram before sowing",
                "Rhizobium inoculation for enhanced nitrogen fixation",
                "PSB (Phosphate Solubilizing Bacteria) treatment recommended",
                "Trichoderma for soil-borne disease protection"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Line sowing using seed drill or manual dibbling",
        "row_spacing": "25–30 cm",
        "plant_spacing": "8–10 cm between plants",
        "sowing_depth": "3–5 cm depth",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "germination_stage": {
                "duration": "0–7 days",
                "details": "Seeds absorb moisture and sprout; primary roots establish."
            },
            "seedling_stage": {
                "duration": "7–15 days",
                "details": "Development of first true leaves; root nodules begin formation."
            },
            "vegetative_stage": {
                "duration": "15–30 days",
                "details": "Rapid stem elongation and branching; nitrogen fixation increases."
            },
            "flowering_stage": {
                "duration": "30–45 days",
                "details": "Yellow flowers appear; mostly self-pollinated."
            },
            "pod_formation_stage": {
                "duration": "40–60 days",
                "details": "Green slender pods develop containing multiple seeds."
            },
            "maturity_stage": {
                "duration": "60–75 days",
                "details": "Pods turn brown/black; leaves dry and fall."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_sowing": "Light irrigation if soil moisture insufficient",
            "critical_stages": [
                "Flowering stage",
                "Pod formation stage"
            ],
            "frequency": "Every 12–15 days during dry season",
            "avoid": "Waterlogging as it causes root rot and poor nodulation"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "5–8 tons FYM per acre",
            "nitrogen": "10–15 kg/ha as starter dose",
            "phosphorus": "40 kg/ha at sowing",
            "potassium": "20 kg/ha if soil deficient",
            "biofertilizers": "Rhizobium and PSB culture highly recommended"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "trianthema": {
                "description": "Broadleaf weed common during Kharif season.",
                "damage": "Competes for nutrients and moisture in early growth.",
                "control": "Manual weeding at 20–25 days after sowing."
            },
            "cyperus": {
                "description": "Nut grass spreading through underground rhizomes.",
                "damage": "Reduces crop vigor and yield.",
                "control": "Deep ploughing and repeated removal."
            },
            "parthenium": {
                "description": "Invasive weed affecting pulse crops.",
                "damage": "Reduces yield and causes field contamination.",
                "control": "Manual uprooting before flowering."
            },
            "digera_arvensis": {
                "description": "Common rainy-season weed.",
                "damage": "Competes heavily during vegetative stage.",
                "control": "Mechanical weeding or recommended herbicide."
            }
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "whitefly": {
                "description": "Sap-sucking pest transmitting viral diseases.",
                "symptoms": "Yellowing and curling of leaves.",
                "control": "Neem oil spray and systemic insecticide."
            },
            "aphids": {
                "description": "Cluster on tender shoots and flowers.",
                "symptoms": "Sticky honeydew and leaf curling.",
                "control": "Spray recommended insecticide."
            },
            "pod_borer": {
                "description": "Larvae feed inside developing pods.",
                "symptoms": "Holes in pods and damaged seeds.",
                "control": "Pheromone traps and timely spraying."
            },
            "thrips": {
                "description": "Tiny insects damaging flowers.",
                "symptoms": "Poor pod set and silvering of leaves.",
                "control": "Spray insecticide during flowering."
            },
            "hairy_caterpillar": {
                "description": "Leaf-eating caterpillar active during vegetative stage.",
                "symptoms": "Defoliation and skeletonized leaves.",
                "control": "Manual collection and insecticide spray."
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "yellow_mosaic_virus": {
                "description": "Viral disease transmitted by whitefly.",
                "symptoms": "Yellow patches on leaves and stunted growth.",
                "control": "Use resistant varieties and control whiteflies."
            },
            "powdery_mildew": {
                "description": "Fungal disease appearing as white powder on leaves.",
                "symptoms": "Reduced photosynthesis and yield loss.",
                "control": "Fungicide spray at early stage."
            },
            "cercospora_leaf_spot": {
                "description": "Fungal infection causing brown spots.",
                "symptoms": "Leaf drop and reduced pod formation.",
                "control": "Use fungicide and crop rotation."
            },
            "root_rot": {
                "description": "Soil-borne fungal disease.",
                "symptoms": "Wilting and plant death.",
                "control": "Seed treatment and proper drainage."
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "60–75 days after sowing",
            "maturity_indicators": [
                "Pods turn brown or black",
                "Leaves dry and fall",
                "Seeds become hard and shiny"
            ],
            "method": "Cut plants and dry in field before threshing"
        },

        "average_yield_per_acre": "4–6 quintals",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Dry seeds to 10–12% moisture",
            "Clean and grade properly",
            "Store in moisture-free airtight containers",
            "Protect from bruchid infestation"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "347 kcal",
            "protein": "24 g",
            "carbohydrates": "63 g",
            "fiber": "16 g",
            "iron": "6.7 mg",
            "magnesium": "189 mg"
        },

        "nutrition_explanation": [
            "Excellent plant-based protein source",
            "High dietary fiber content",
            "Rich in iron and magnesium",
            "Low fat and cholesterol-free"
        ],

        "health_benefits": [
            "Improves digestion",
            "Supports muscle growth",
            "Helps control blood sugar",
            "Boosts immunity",
            "Supports heart health"
        ],

        "economic_importance": [
            "Major pulse crop in India",
            "Improves soil fertility through nitrogen fixation",
            "Export potential commodity",
            "Used in dal, sprouts, and flour production"
        ],

        "risk_factors": [
            "Susceptible to yellow mosaic virus",
            "Heavy rainfall reduces yield",
            "Pod shattering if harvest delayed"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/green_gram.jpg",
            "pests": [
                "static/images/pests/whitefly.jpg",
                "static/images/pests/aphids.jpg",
                "static/images/pests/pod_borer.jpg",
                "static/images/pests/thrips.jpg",
                "static/images/pests/hairy_caterpillar.jpg"
            ],
            "diseases": [
                "static/images/diseases/yellow_mosaic_virus.jpg",
                "static/images/diseases/powdery_mildew.jpg",
                "static/images/diseases/cercospora_leaf_spot.jpg",
                "static/images/diseases/root_rot.jpg"
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