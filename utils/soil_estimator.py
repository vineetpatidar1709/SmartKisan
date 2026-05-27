"""
Soil Estimator Module
This is an alias for backward compatibility.
Use utils.enhanced_soil_estimator for the full version.
"""

from utils.enhanced_soil_estimator import estimate_npk, estimate_npk_simple

__all__ = ['estimate_npk', 'estimate_npk_simple']
