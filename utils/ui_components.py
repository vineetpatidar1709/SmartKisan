"""
UI Components and Utilities for Streamlit App
"""

import streamlit as st
import base64
import os
from typing import Optional, List, Dict, Any
from utils.constants import ERROR_CROP_NOT_FOUND, ERROR_INVALID_CROP_STRUCTURE


def set_background(image_path: str) -> None:
    """Set background image for the app."""
    if not os.path.exists(image_path):
        return

    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


def apply_custom_theme() -> None:
    """Apply custom CSS theme to the app."""
    st.markdown("""
        <style>
        .block-container {
            padding-top: 2rem;
        }
        .stMetric {
            background-color: rgba(255,255,255,0.8);
            padding: 15px;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)


def display_error_message(message: str, error_type: str = "error") -> None:
    """Display error message with appropriate styling."""
    if error_type == "error":
        st.error(message)
    elif error_type == "warning":
        st.warning(message)
    elif error_type == "info":
        st.info(message)


def create_input_columns(
    inputs: List[Dict[str, Any]],
    columns: int = 2
) -> Dict[str, Any]:
    """
    Create input columns dynamically.

    Args:
        inputs: List of input configurations
        columns: Number of columns to create

    Returns:
        Dict of input values
    """
    values = {}
    cols = st.columns(columns)

    for i, input_config in enumerate(inputs):
        col_idx = i % columns
        with cols[col_idx]:
            input_type = input_config.get("type", "text")
            key = input_config["key"]
            label = input_config["label"]

            if input_type == "selectbox":
                values[key] = st.selectbox(
                    label,
                    input_config["options"],
                    index=input_config.get("index", 0)
                )
            elif input_type == "number_input":
                values[key] = st.number_input(
                    label,
                    min_value=input_config.get("min_value", 0.0),
                    max_value=input_config.get("max_value", 1000.0),
                    value=input_config.get("value", 0.0),
                    step=input_config.get("step", 1.0)
                )
            elif input_type == "checkbox":
                values[key] = st.checkbox(
                    label,
                    value=input_config.get("value", False)
                )

    return values


def display_crop_summary(
    crop_name: str,
    summary_data: Dict[str, Any]
) -> None:
    """Display crop summary in a structured format."""
    st.markdown("### 🌾 Farmer Summary")

    # Display summary using columns
    cols = st.columns(5)
    fields = ["Crop", "Season", "Duration", "Water Requirement", "Average Yield"]

    for i, field in enumerate(fields):
        with cols[i]:
            st.caption(field)
            value = summary_data.get(field, "-")
            if field == "Crop":
                value = value or crop_name
            st.markdown(f"**{value}**")


def display_image(
    image_path: str,
    caption: str = "",
    width: int = 200
) -> None:
    """Display image with fallback to placeholder."""
    if image_path and os.path.exists(image_path):
        st.image(image_path, caption=caption, width=width)
    else:
        # Show placeholder with emoji
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            width: {width}px;
            height: {width}px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 5px;
        ">
            <span style="font-size: 40px;">🌱</span>
        </div>
        """, unsafe_allow_html=True)
        if caption:
            st.caption(caption)


def handle_crop_loading_error(error: Dict[str, str]) -> bool:
    """Handle crop loading errors and return True if should continue."""
    if "error" in error:
        if error["error"] == ERROR_CROP_NOT_FOUND:
            st.error("Crop not found in database.")
        elif error["error"] == ERROR_INVALID_CROP_STRUCTURE:
            st.error("Invalid crop data structure.")
        else:
            st.error(f"Error loading crop: {error['error']}")
        return False
    return True
