crop_data = {
    "pigeon_pea": {
        "name": "Pigeon Pea",
        "scientific_name": "Cajanus cajan",
        "family": "Fabaceae",
        "category": "Pulse Crop",
        "crop_type": "Leguminous long-duration pulse crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Kharif (June–July); perennial types in tropical regions",
        "duration_days": "120–180 days (variety dependent)",
        "climate": "Tropical and subtropical semi-arid climate",
        "ideal_temperature": "26°C – 35°C",
        "germination_temperature": "20°C – 30°C",
        "rainfall_requirement_mm": "600 – 1000 mm",
        "water_requirement_level": "Moderate",
        "sunlight_requirement": "Requires full sunlight for optimum flowering and pod development",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Well-drained loamy, sandy loam, and black cotton soil",
        "soil_ph_range": "6.5 – 7.5",
        "soil_depth_requirement": "Deep soil preferred for extensive root system",
        "salinity_tolerance": "Low to Moderate",
        "drainage_requirement": "Good drainage essential; sensitive to prolonged waterlogging",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Assam",
            "Bihar",
            "Chhattisgarh",
            "Gujarat",
            "Jharkhand",
            "Karnataka",
            "Madhya Pradesh",
            "Maharashtra",
            "Telangana",
            "Tripura",
            "Uttar Pradesh",

        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "Deep ploughing during summer to destroy pests and weeds",
            "2–3 harrowings to obtain fine tilth",
            "Incorporate 8–10 tons FYM per acre",
            "Level field to ensure uniform irrigation",
            "Prepare ridges and furrows in heavy soils"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Certified high-yielding, wilt-resistant varieties",
            "seed_rate_per_acre": "6–8 kg (variety dependent)",
            "seed_selection": "Bold, uniform, disease-free seeds with high germination",
            "seed_treatment": [
                "Treat seeds with Carbendazim or Thiram before sowing",
                "Rhizobium inoculation for nitrogen fixation",
                "PSB (Phosphate Solubilizing Bacteria) treatment recommended",
                "Trichoderma for protection against soil-borne diseases"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Line sowing using seed drill or dibbling method",
        "row_spacing": "60–90 cm (depending on duration variety)",
        "plant_spacing": "20–30 cm between plants",
        "sowing_depth": "4–6 cm depth",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "germination_stage": {
                "duration": "0–10 days",
                "details": "Seed absorbs moisture and radical emerges; root system begins establishment."
            },
            "seedling_stage": {
                "duration": "10–25 days",
                "details": "Development of primary leaves; nodulation begins."
            },
            "vegetative_stage": {
                "duration": "25–60 days",
                "details": "Rapid stem elongation and branching; nitrogen fixation increases significantly."
            },
            "flowering_stage": {
                "duration": "60–100 days",
                "details": "Yellow to reddish flowers appear; cross-pollination may occur."
            },
            "pod_development_stage": {
                "duration": "90–140 days",
                "details": "Green pods develop containing 3–5 seeds per pod."
            },
            "maturity_stage": {
                "duration": "120–180 days",
                "details": "Pods turn brown and dry; leaves shed naturally."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_sowing": "Light irrigation if rainfall insufficient",
            "critical_stages": [
                "Flowering stage",
                "Pod development stage"
            ],
            "frequency": "Every 15–20 days in dry conditions",
            "avoid": "Water stagnation during flowering and maturity"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "8–10 tons FYM per acre",
            "nitrogen": "20 kg/ha as starter dose",
            "phosphorus": "40–60 kg/ha at sowing",
            "potassium": "20–40 kg/ha if soil deficient",
            "biofertilizers": "Rhizobium and PSB cultures recommended"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {
            "parthenium": {
                "description": "Invasive broadleaf weed commonly found in pulse fields.",
                "damage": "Competes for nutrients and reduces crop growth.",
                "control": "Manual uprooting before flowering."
            },
            "cyperus": {
                "description": "Nut grass spreading through underground rhizomes.",
                "damage": "Competes for moisture and nutrients.",
                "control": "Deep ploughing and mechanical removal."
            },
            "trianthema": {
                "description": "Fast-growing rainy-season weed.",
                "damage": "Reduces crop vigor during early stages.",
                "control": "Hand weeding at 25–30 DAS."
            },
            "amaranthus": {
                "description": "Common broadleaf weed in Kharif crops.",
                "damage": "Heavy nutrient competition.",
                "control": "Mechanical weeding and herbicide if necessary."
            }
        },

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {
            "pod_borer": {
                "description": "Larvae feed inside developing pods.",
                "symptoms": "Holes in pods and damaged seeds.",
                "control": "Pheromone traps and recommended insecticide spray."
            },
            "aphids": {
                "description": "Sap-sucking insects attacking tender shoots.",
                "symptoms": "Leaf curling and sticky honeydew.",
                "control": "Neem oil or systemic insecticide."
            },
            "jassids": {
                "description": "Suck plant sap causing leaf discoloration.",
                "symptoms": "Yellowing and curling of leaf margins.",
                "control": "Spray appropriate insecticide."
            },
            "hairy_caterpillar": {
                "description": "Leaf-eating caterpillar active during vegetative stage.",
                "symptoms": "Severe defoliation.",
                "control": "Manual removal and spraying."
            },
            "thrips": {
                "description": "Small insects damaging flowers.",
                "symptoms": "Poor pod setting and flower drop.",
                "control": "Insecticide spray during flowering."
            }
        },

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {
            "fusarium_wilt": {
                "description": "Soil-borne fungal disease causing plant wilting.",
                "symptoms": "Yellowing, wilting, and plant death.",
                "control": "Use resistant varieties and seed treatment."
            },
            "sterility_mosaic_disease": {
                "description": "Viral disease transmitted by mites.",
                "symptoms": "Bushy appearance and absence of flowering.",
                "control": "Control mite population and use resistant varieties."
            },
            "phytophthora_blight": {
                "description": "Fungal disease occurring in waterlogged fields.",
                "symptoms": "Stem lesions and plant collapse.",
                "control": "Improve drainage and fungicide application."
            },
            "powdery_mildew": {
                "description": "White powdery fungal growth on leaves.",
                "symptoms": "Reduced photosynthesis and yield.",
                "control": "Spray fungicide at early stage."
            }
        },

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "120–180 days after sowing",
            "maturity_indicators": [
                "Pods turn brown and dry",
                "Leaves shed naturally",
                "Seeds become hard and fully developed"
            ],
            "method": "Cut plants and dry in field before threshing"
        },

        "average_yield_per_acre": "6–10 quintals",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Dry seeds to 10–12% moisture",
            "Thresh and clean properly",
            "Store in dry, airtight containers",
            "Protect from storage pests like bruchids"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {
            "calories": "343 kcal",
            "protein": "21 g",
            "carbohydrates": "63 g",
            "fiber": "15 g",
            "iron": "5 mg",
            "magnesium": "183 mg"
        },

        "nutrition_explanation": [
            "Good source of plant-based protein",
            "High dietary fiber improves digestion",
            "Contains essential minerals like iron and magnesium",
            "Low fat and cholesterol-free"
        ],

        "health_benefits": [
            "Improves digestive health",
            "Supports muscle growth",
            "Helps regulate blood sugar levels",
            "Boosts immunity",
            "Supports heart health"
        ],

        "economic_importance": [
            "Major pulse crop in India",
            "Improves soil fertility through nitrogen fixation",
            "Used in dal and processed food industry",
            "Important export commodity"
        ],

        "risk_factors": [
            "Highly susceptible to wilt disease",
            "Heavy rainfall affects flowering",
            "Pod shattering if harvest delayed"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/pigeon_pea.jpg",
            "pests": [
                "static/images/pests/pod_borer.jpg",
                "static/images/pests/aphids.jpg",
                "static/images/pests/jassids.jpg",
                "static/images/pests/hairy_caterpillar.jpg",
                "static/images/pests/thrips.jpg"
            ],
            "diseases": [
                "static/images/diseases/fusarium_wilt.jpg",
                "static/images/diseases/sterility_mosaic_disease.jpg",
                "static/images/diseases/phytophthora_blight.jpg",
                "static/images/diseases/powdery_mildew.jpg"
            ],
            "weeds": [
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/trianthema.jpg",
                "static/images/weeds/amaranthus.jpg"
            ]
        }
    }
}