crop_data = {
    "peach": {
        "name": "Peach",
        "scientific_name": "Prunus persica",
        "family": "Rosaceae",
        "category": "Fruit Crop",
        "crop_type": "Temperate orchard crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Annual (summer harvest)",
        "duration_days": "Perennial tree crop",
        "climate": "Temperate to subtropical hills",
        "ideal_temperature": "12 C - 28 C",
        "germination_temperature": "18 C - 25 C",
        "rainfall_requirement_mm": "700 - 1200 mm",
        "water_requirement_level": "Moderate",
        "sunlight_requirement": "Full sunlight",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Loam with good organic matter",
        "soil_ph_range": "6.0 - 7.5",
        "soil_depth_requirement": "Deep, well-drained",
        "salinity_tolerance": "Low",
        "drainage_requirement": "Good drainage required",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Himachal Pradesh",
            "Jammu and Kashmir",
            "Uttarakhand",
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
        "major_pests": {'fruit_fly': {'description': 'Infests developing/ripening fruits.',
               'symptoms': 'Maggot damage and fruit drop.',
               'control': 'Sanitation, traps, and need-based sprays.'},
 'aphids': {'description': 'Sap-sucking colonies on tender shoots.',
            'symptoms': 'Leaf curling and sticky honeydew.',
            'control': 'Biological control and selective insecticide.'},
 'scale_insect': {'description': 'Sessile insects on twigs/leaves.',
                  'symptoms': 'Weak growth and sooty mold.',
                  'control': 'Dormant oil and pruning.'}},

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {'anthracnose': {'description': 'Fungal disease on leaves/fruits.',
                 'symptoms': 'Dark lesions and quality loss.',
                 'control': 'Canopy sanitation and fungicide spray.'},
 'powdery_mildew': {'description': 'White fungal growth on tender tissues.',
                    'symptoms': 'Leaf distortion and reduced quality.',
                    'control': 'Sulfur/fungicide and aeration.'},
 'root_rot': {'description': 'Soil-borne root disease under poor drainage.',
              'symptoms': 'Wilting and dieback.',
              'control': 'Improve drainage and soil treatment.'}},

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

        "average_yield_per_acre": "35-70 quintals",

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
        "nutrition_per_100g": {'calories': '39 kcal',
 'carbohydrates': '9.5 g',
 'fiber': '1.5 g',
 'vitamin_C': '6.6 mg',
 'vitamin_A': '16 mcg'},

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
            "crop": "static/images/crops/peach.jpg",
            "pests": [
                "static/images/pests/fruit_fly.jpg",
                "static/images/pests/aphids.jpg",
                "static/images/pests/scale_insect.jpg"
            ],
            "diseases": [
                "static/images/diseases/anthracnose.jpg",
                "static/images/diseases/powdery_mildew.jpg",
                "static/images/diseases/root_rot.jpg"
            ],
            "weeds": [
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/amaranthus.jpg"
            ]
        }
    }
}
