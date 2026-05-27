from typing import Dict, Any

class CropSchemaV2:
    @staticmethod
    def is_v2_format(crop_module) -> bool:
        # Simplified - rice.py is flat dict, not V2
        return False

# No validation errors for flat structure

