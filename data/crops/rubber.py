crop_data = {
    "rubber": {
        "name": "Rubber",
        "scientific_name": "Hevea brasiliensis",
        "family": "Euphorbiaceae",
        "category": "Plantation Crop",
        "crop_type": "Perennial industrial crop",

        # -------------------------------------------------
        # BASIC CULTIVATION DETAILS
        # -------------------------------------------------
        "season": "Annual",
        "duration_days": "Perennial (tapping starts after 6-7 years)",
        "climate": "Hot humid tropical",
        "ideal_temperature": "25 C - 35 C",
        "germination_temperature": "25 C - 32 C",
        "rainfall_requirement_mm": "2000 - 3000 mm",
        "water_requirement_level": "High",
        "sunlight_requirement": "Bright sunlight",

        # -------------------------------------------------
        # SOIL REQUIREMENTS
        # -------------------------------------------------
        "soil_type": "Deep lateritic/alluvial, well-drained",
        "soil_ph_range": "4.5 - 6.5",
        "soil_depth_requirement": "Very deep soil preferred",
        "salinity_tolerance": "Low",
        "drainage_requirement": "Excellent drainage with contour channels",

        # -------------------------------------------------
        # MAJOR GROWING STATES IN INDIA
        # -------------------------------------------------
        "major_states": [
            "Arunachal Pradesh",
            "Kerala",
            "Meghalaya",
            "Tripura",
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
        "major_pests": {'aphids': {'description': 'Sap-sucking insects on young tissues.',
            'symptoms': 'Leaf curling and yellowing.',
            'control': 'Biological control and selective spray.'},
 'mealybug': {'description': 'Colonizes stems and leaves.',
              'symptoms': 'Honeydew and sooty mold.',
              'control': 'Pruning and need-based treatment.'},
 'termites': {'description': 'Damage roots/stems in dry soils.',
              'symptoms': 'Weak growth and plant decline.',
              'control': 'Soil treatment and sanitation.'}},

        # -------------------------------------------------
        # MAJOR DISEASES
        # -------------------------------------------------
        "major_diseases": {'leaf_spot': {'description': 'Common leaf fungal infection.',
               'symptoms': 'Necrotic spots and drying.',
               'control': 'Fungicidal protection and sanitation.'},
 'root_rot': {'description': 'Root/collar rot in poor drainage.',
              'symptoms': 'Wilting and yellowing.',
              'control': 'Drainage management and soil treatment.'},
 'blight': {'description': 'Blight under humid stress.',
            'symptoms': 'Rapid tissue drying.',
            'control': 'Preventive sprays and IPM.'}},

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

        "average_yield_per_acre": "600-1000 kg dry rubber",

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
        "nutrition_per_100g": {'calories': 'Not applicable',
 'carbohydrates': 'Not applicable',
 'protein': 'Not applicable',
 'fiber': 'Not applicable',
 'key_minerals': 'Not applicable'},

        "nutrition_explanation": ['Commercial non-food/industrial crop',
 'Nutritional profile is not typically for consumption',
 'Economic value is based on industrial use'],

        "health_benefits": ['Primary benefit is livelihood support', 'Supports industrial value chains', 'Provides regional employment'],

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
            "crop": "static/images/crops/rubber.jpg",
            "pests": [
                "static/images/pests/aphids.jpg",
                "static/images/pests/mealybug.jpg",
                "static/images/pests/termites.jpg"
            ],
            "diseases": [
                "static/images/diseases/leaf_spot.jpg",
                "static/images/diseases/root_rot.jpg",
                "static/images/diseases/blight.jpg"
            ],
            "weeds": [
                "static/images/weeds/cyperus.jpg",
                "static/images/weeds/parthenium.jpg",
                "static/images/weeds/amaranthus.jpg"
            ]
        }
    }
}
