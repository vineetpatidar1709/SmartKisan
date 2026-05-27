crop_data = {
    "large_cardamom": {
        "name": "Large Cardamom",
        "scientific_name": "Amomum subulatum",
        "family": "Zingiberaceae",
        "category": "Spice Crop",
        "crop_type": "Perennial spice crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Annual",
        "duration_days": "Perennial (bearing from 3rd year)",
        "climate": "Cool humid mountain climate",
        "ideal_temperature": "10 C - 25 C",
        "germination_temperature": "18 C - 24 C",
        "rainfall_requirement_mm": "1500 - 3000 mm",
        "water_requirement_level": "Moderate to high",
        "sunlight_requirement": "Partial shade",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Humus-rich forest loam",
        "soil_ph_range": "5.0 - 6.5",
        "soil_depth_requirement": "Deep organic-rich soils",
        "salinity_tolerance": "Low",
        "drainage_requirement": "Excellent drainage on slopes",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Arunachal Pradesh",
            "Nagaland",
            "Sikkim",
            "West Bengal (Darjeeling)",
        ],

        # -------------------------------------------------
        # LAND PREPARATION
        # -------------------------------------------------
        "land_preparation": [
            "Deep ploughing followed by 2 harrowings",
            "Incorporate well-decomposed FYM/compost",
            "Remove weeds and crop residues",
            "Prepare raised beds or ridges where needed",
            "Ensure drainage channels before sowing/planting"
        ],

        # -------------------------------------------------
        # SEED INFORMATION
        # -------------------------------------------------
        "seed_information": {
            "seed_type": "Certified planting material/seed",
            "seed_rate_per_acre": "Varies by variety and spacing",
            "seed_selection": "Healthy, disease-free, true-to-type material",
            "seed_treatment": [
                "Biological seed treatment where applicable",
                "Fungicidal treatment in disease-prone fields",
                "Use recommended nursery/propagation practices"
            ]
        },

        # -------------------------------------------------
        # SOWING METHOD & SPACING
        # -------------------------------------------------
        "sowing_method": "Line sowing or transplanting based on crop and region",
        "row_spacing": "As per variety recommendation",
        "plant_spacing": "As per crop architecture",
        "sowing_depth": "Shallow to medium depth based on seed size",

        # -------------------------------------------------
        # GROWTH STAGES
        # -------------------------------------------------
        "growth_stages": {
            "establishment_stage": {
                "duration": "Initial 2-4 weeks",
                "details": "Germination/root establishment and early canopy formation."
            },
            "vegetative_stage": {
                "duration": "Next 4-10 weeks",
                "details": "Rapid biomass build-up and branching/tillering."
            },
            "reproductive_stage": {
                "duration": "Variety-specific",
                "details": "Flowering/fruit or economic part initiation."
            },
            "maturity_stage": {
                "duration": "Final phase",
                "details": "Quality development and harvest readiness."
            }
        },

        # -------------------------------------------------
        # IRRIGATION SCHEDULE
        # -------------------------------------------------
        "irrigation_schedule": {
            "immediately_after_sowing": "Light irrigation for uniform establishment",
            "critical_stages": [
                "Early vegetative stage",
                "Flowering/initiation stage",
                "Economic part development stage"
            ],
            "frequency": "Based on soil moisture, season, and rainfall",
            "avoid": "Waterlogging and prolonged moisture stress"
        },

        # -------------------------------------------------
        # FERTILIZER MANAGEMENT
        # -------------------------------------------------
        "fertilizer_management": {
            "organic_manure": "Apply well-decomposed FYM/compost before planting",
            "nitrogen": "Split dose as per soil test recommendation",
            "phosphorus": "Basal dose as per soil test recommendation",
            "potassium": "Basal/top-dress based on crop need",
            "micronutrients": "Apply as per deficiency symptoms/soil report",
            "biofertilizers": "Recommended where compatible with crop"
        },

        # -------------------------------------------------
        # MAJOR WEEDS
        # -------------------------------------------------
        "major_weeds": {'cyperus': {'description': 'A persistent sedge weed that competes for nutrients and moisture.', 'damage': 'Reduces growth and nutrient availability.', 'control': 'Mulching, manual weeding, and timely herbicide use.'}, 'parthenium': {'description': 'Aggressive broadleaf weed in open fields.', 'damage': 'Competes for light, water, and nutrients.', 'control': 'Uproot before flowering and maintain field sanitation.'}, 'amaranthus': {'description': 'Fast-growing broadleaf weed in warm conditions.', 'damage': 'Suppresses crop seedlings and lowers yield.', 'control': 'Early weeding and shallow intercultivation.'}},

        # -------------------------------------------------
        # MAJOR PESTS
        # -------------------------------------------------
        "major_pests": {'thrips': {'description': 'Feed on leaves and economic parts.',
            'symptoms': 'Scarring and poor quality.',
            'control': 'Need-based sprays and monitoring.'},
 'shoot_borer': {'description': 'Larvae bore into shoots/pseudostems.',
                 'symptoms': 'Dead hearts and drying.',
                 'control': 'Remove affected shoots and spray.'},
 'aphids': {'description': 'Sap-sucking pest on young tissues.',
            'symptoms': 'Curling and stunting.',
            'control': 'Botanicals and selective sprays.'}},

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {'rhizome_rot': {'description': 'Common fungal rot in humid soils.',
                 'symptoms': 'Yellowing and clump collapse.',
                 'control': 'Drainage and fungicidal drench.'},
 'leaf_blight': {'description': 'Blight on foliage in humid weather.',
                 'symptoms': 'Necrotic streaks and drying.',
                 'control': 'Sanitation and fungicide.'},
 'wilt_complex': {'description': 'Complex decline due to pathogens/stress.',
                  'symptoms': 'Progressive wilting and poor yield.',
                  'control': 'Clean planting material and IPM.'}},

        # -------------------------------------------------
        # HARVESTING
        # -------------------------------------------------
        "harvesting_details": {
            "harvest_time": "At physiological maturity / marketable stage",
            "maturity_indicators": [
                "Crop-specific color and size development",
                "Target moisture level for storage",
                "Best market quality achieved"
            ],
            "method": "Manual or mechanical harvesting depending on crop"
        },

        "average_yield_per_acre": "1.5-3 quintals (dry capsules)",

        # -------------------------------------------------
        # POST HARVEST
        # -------------------------------------------------
        "post_harvest": [
            "Clean and grade produce",
            "Dry/cure to safe moisture if needed",
            "Store in clean, ventilated conditions",
            "Use crop-specific packaging to reduce losses"
        ],

        # -------------------------------------------------
        # NUTRITION PROFILE
        # -------------------------------------------------
        "nutrition_per_100g": {'calories': '311 kcal', 'carbohydrates': '68 g', 'fiber': '28 g', 'protein': '11 g', 'iron': '14 mg'},

        "nutrition_explanation": ['Provides useful macro and micronutrients',
 'Supports dietary diversity',
 'Nutrient profile depends on variety and processing'],

        "health_benefits": ['Contributes to balanced nutrition',
 'Supports energy and overall wellbeing',
 'Contains crop-specific functional compounds'],

        "economic_importance": [
            "Provides farm income and livelihood support",
            "Supports regional value chains and markets",
            "Important for food/industrial uses depending on crop"
        ],

        "risk_factors": [
            "Weather variability",
            "Pest and disease outbreaks",
            "Market price fluctuations"
        ],

        # -------------------------------------------------
        # IMAGES
        # -------------------------------------------------
        "images": {
            "crop": "static/images/crops/large_cardamom.jpg",
            "pests": [
                "static/images/pests/thrips.jpg",
                "static/images/pests/shoot_borer.jpg",
                "static/images/pests/aphids.jpg"
            ],
            "diseases": [
                "static/images/diseases/rhizome_rot.jpg",
                "static/images/diseases/leaf_blight.jpg",
                "static/images/diseases/wilt_complex.jpg"
            ],
            "weeds": [
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/amaranthus.jpg"
            ]
        }
    }
}
