"""
Crop Advisory Page - Enhanced UI/UX with better visual design
"""

import streamlit as st
import os
import re
import io
from typing import Dict, Any, List, Optional, Tuple

from data.crop_loader import load_all_crops, load_crop
from utils.ui_components import display_image


# Custom CSS for enhanced UI/UX
def apply_custom_styles():
    st.markdown("""
    <style>
    /* Main container styles */
    .crop-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 16px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-left: 5px solid #4CAF50;
    }
    
    .crop-card-header {
        font-size: 24px;
        font-weight: bold;
        color: #2E7D32;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .info-badge {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: 600;
        display: inline-block;
        margin: 5px;
    }
    
    .info-badge-secondary {
        background: linear-gradient(135deg, #2196F3 0%, #1976D2 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: 600;
        display: inline-block;
        margin: 5px;
    }
    
    .info-badge-warning {
        background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: 600;
        display: inline-block;
        margin: 5px;
    }
    
    .stat-box {
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        margin: 5px;
    }
    
    .stat-box-title {
        font-size: 12px;
        color: #666;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stat-box-value {
        font-size: 20px;
        font-weight: bold;
        color: #2E7D32;
    }
    
    .section-header {
        font-size: 20px;
        font-weight: bold;
        color: #1B5E20;
        margin: 20px 0 15px 0;
        padding-bottom: 10px;
        border-bottom: 2px solid #4CAF50;
    }
    
    .search-box {
        padding: 12px 20px;
        border-radius: 25px;
        border: 2px solid #4CAF50;
        font-size: 16px;
        width: 100%;
        margin-bottom: 20px;
    }
    
    /* Tab styles */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0 20px;
        background: #f0f0f0;
        border-radius: 10px 10px 0px 0px;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background: #4CAF50;
        color: white;
    }
    
    /* Custom expander */
    .streamlit-expanderHeader {
        background: #e8f5e9;
        border-radius: 10px;
        font-weight: 600;
    }
    
    /* Metric card styles */
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #ffffff 0%, #f5f5f5 100%);
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    /* Filter chips */
    .filter-chip {
        background: #e8f5e9;
        color: #2E7D32;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 14px;
        margin: 5px;
        cursor: pointer;
        display: inline-block;
    }
    
    .filter-chip:hover {
        background: #4CAF50;
        color: white;
    }
    
    .filter-chip-active {
        background: #4CAF50;
        color: white;
    }
    
    /* Image gallery */
    .gallery-image {
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s;
    }
    
    .gallery-image:hover {
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)


def get_crop_categories() -> Dict[str, List[str]]:
    """Get crop categories for filtering."""
    return {
        "Cereals": ["Rice", "Wheat", "Maize", "Bajra", "Jowar", "Barley"],
        "Pulses": ["Chickpea", "Pigeon Pea", "Green Gram", "Red Lentil", "Urad"],
        "Vegetables": ["Potato", "Tomato", "Onion", "Brinjal", "Cabbage", "Cucumber"],
        "Fruits": ["Banana", "Mango", "Apple", "Orange", "Guava", "Litchi", "Jackfruit"],
        "Oilseeds": ["Soybean", "Groundnut", "Mustard"],
        "Cash Crops": ["Cotton", "Sugarcane", "Tea", "Coffee", "Jute", "Tobacco"],
    }


def generate_farmer_summary(crop_name: str) -> dict:
    """Simplified farmer-friendly advisory"""
    data = load_crop(crop_name, mode="detailed")
    
    if "name" in data:
        summary = {
            "Crop": data.get("name", crop_name),
            "Season": data.get("season", ""),
            "Duration": data.get("duration_days", ""),
            "Water Requirement": data.get("water_requirement_level", ""),
            "Average Yield": data.get("average_yield_per_acre", "")
        }
    else:
        summary = {
            "Crop": data.get("Basic Information", {}).get("Common Name", ""),
            "Season": data.get("Basic Information", {}).get("Season", ""),
            "Duration": data.get("Basic Information", {}).get("Life Cycle", ""),
            "Water Requirement": data.get("Irrigation Management", {}).get("Total Water Requirement", ""),
            "Average Yield": data.get("Yield Information", {}).get("Average Yield", "")
        }
    return summary


def get_crop_advisory(crop_name: str, mode: str = "brief") -> dict:
    """Returns crop advisory in selected mode."""
    try:
        crop_data = load_crop(crop_name, mode=mode)
        if isinstance(crop_data, dict) and "error" in crop_data:
            return crop_data
        return crop_data
    except Exception as e:
        return {"error": str(e)}


def display_image(image_path: str, caption: str = "", width: int = 200):
    """Display image with fallback to placeholder."""
    if image_path and os.path.exists(image_path):
        st.image(image_path, caption=caption, width=width, use_container_width=False)
    else:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
            border-radius: 12px;
            padding: 30px;
            text-align: center;
            width: {width}px;
            margin: 10px auto;
        ">
            <span style="font-size: 50px;">🌱</span>
            <p style="color: #666; margin-top: 10px;">{caption}</p>
        </div>
        """, unsafe_allow_html=True)


def render_list(items):
    for item in items:
        st.markdown(f"- {item}")


def render_key_value(label: str, value):
    if isinstance(value, list):
        st.markdown(f"**{label}:**")
        render_list(value)
        return
    if isinstance(value, dict):
        st.markdown(f"**{label}:**")
        for k, v in value.items():
            render_key_value(k.replace('_', ' ').title(), v)
        return
    st.markdown(f"**{label}:** {value}")


def parse_quintal_range(value: str) -> Optional[Tuple[float, float]]:
    if not isinstance(value, str):
        return None
    nums = re.findall(r"\d+(?:\.\d+)?", value.replace(",", ""))
    if not nums:
        return None
    vals = [float(n) for n in nums]
    if len(vals) == 1:
        return vals[0], vals[0]
    return vals[0], vals[1]


def format_range(a: float, b: float) -> str:
    if abs(a - b) < 1e-9:
        return f"{a:.1f}"
    return f"{a:.1f}–{b:.1f}"


def _wrap_pdf_text(text: str, max_width: float, font_name: str, font_size: int):
    from reportlab.pdfbase.pdfmetrics import stringWidth
    words = text.split()
    lines = []
    line = []
    for word in words:
        test = (" ".join(line + [word])).strip()
        if stringWidth(test, font_name, font_size) <= max_width:
            line.append(word)
        else:
            if line:
                lines.append(" ".join(line))
            line = [word]
    if line:
        lines.append(" ".join(line))
    return lines


def _section_to_lines(title: str, data) -> List[str]:
    lines = []
    if title:
        lines.append(title)
    if isinstance(data, dict):
        for k, v in data.items():
            key = k.replace("_", " ").title()
            if isinstance(v, list):
                lines.append(f"{key}:")
                for item in v:
                    lines.append(f"- {item}")
            elif isinstance(v, dict):
                lines.append(f"{key}:")
                for kk, vv in v.items():
                    lines.append(f"- {kk.replace('_', ' ').title()}: {vv}")
            else:
                lines.append(f"{key}: {v}")
    elif isinstance(data, list):
        for item in data:
            lines.append(f"- {item}")
    elif data:
        lines.append(str(data))
    return lines


def build_crop_pdf(crop_name: str, summary: dict, advisory: dict) -> bytes:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.lib.utils import ImageReader

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    margin_x = 40
    y = height - 40
    title_font = ("Helvetica-Bold", 16)
    header_font = ("Helvetica-Bold", 12)
    body_font = ("Helvetica", 10)

    def draw_line(text: str, font_name: str, font_size: int, indent: int = 0):
        nonlocal y
        if y < 50:
            c.showPage()
            y = height - 40
        c.setFont(font_name, font_size)
        c.drawString(margin_x + indent, y, text)
        y -= font_size + 4

    def draw_block(lines: List[str], title: Optional[str] = None):
        nonlocal y
        if title:
            draw_line(title, header_font[0], header_font[1])
        max_width = width - 2 * margin_x
        for line in lines:
            for wrapped in _wrap_pdf_text(line, max_width, body_font[0], body_font[1]):
                draw_line(wrapped, body_font[0], body_font[1], indent=10)

    def draw_image(path: str, label: Optional[str] = None, max_w: float = 360, max_h: float = 220):
        nonlocal y
        if not path or not os.path.exists(path):
            return
        if y < max_h + 60:
            c.showPage()
            y = height - 40
        if label:
            draw_line(label, header_font[0], header_font[1])
        try:
            img = ImageReader(path)
            iw, ih = img.getSize()
            scale = min(max_w / iw, max_h / ih, 1.0)
            w = iw * scale
            h = ih * scale
            c.drawImage(img, margin_x, y - h, width=w, height=h, preserveAspectRatio=True, mask='auto')
            y -= h + 12
        except Exception:
            pass

    # Title
    draw_line(f"Crop Advisory Report: {crop_name}", title_font[0], title_font[1])
    draw_line("Generated by Smart Agriculture AI", body_font[0], body_font[1])
    y -= 8

    # Summary
    summary_lines = []
    for k, v in summary.items():
        summary_lines.append(f"{k}: {v}")
    draw_block(summary_lines, title="Summary")
    y -= 6

    # Images (crop + a few examples)
    images = advisory.get("images") or advisory.get("Images") or {}
    if isinstance(images, dict):
        crop_img = images.get("crop")
        if isinstance(crop_img, str):
            draw_image(crop_img, label="Crop Image")
        for label, key in [("Pest Images", "pests"), ("Disease Images", "diseases"), ("Weed Images", "weeds")]:
            vals = images.get(key, [])
            if isinstance(vals, list) and vals:
                draw_line(label, header_font[0], header_font[1])
                # show up to 4 thumbnails per category
                shown = 0
                for img_path in vals:
                    if shown >= 4:
                        break
                    if not isinstance(img_path, str) or not os.path.exists(img_path):
                        continue
                    draw_image(img_path, label=None, max_w=160, max_h=120)
                    shown += 1

    # Sections
    sections = [
        ("Cultivation Basics", {k: advisory.get(k) for k in [
            "name", "scientific_name", "family", "category", "crop_type", "season",
            "duration_days", "climate", "ideal_temperature", "water_requirement_level",
            "average_yield_per_acre", "sunlight_requirement"
        ] if k in advisory}),
        ("Major Growing States", advisory.get("major_states")),
        ("Soil Requirements", {k: advisory.get(k) for k in [
            "soil_type", "soil_ph_range", "soil_depth_requirement", "salinity_tolerance",
            "drainage_requirement"
        ] if k in advisory}),
        ("Fertilizer Management", advisory.get("fertilizer_management")),
        ("Seed Information", advisory.get("seed_information")),
        ("Sowing & Spacing", {k: advisory.get(k) for k in [
            "sowing_method", "row_spacing", "plant_spacing", "sowing_depth"
        ] if k in advisory}),
        ("Land Preparation", advisory.get("land_preparation")),
        ("Growth Stages", advisory.get("growth_stages")),
        ("Irrigation", {k: advisory.get(k) for k in [
            "rainfall_requirement_mm", "water_requirement_level"
        ] if k in advisory}),
        ("Irrigation Schedule", advisory.get("irrigation_schedule")),
        ("Pests", advisory.get("major_pests")),
        ("Diseases", advisory.get("major_diseases")),
        ("Weeds", advisory.get("major_weeds")),
        ("Harvesting", advisory.get("harvesting_details")),
        ("Post-Harvest", advisory.get("post_harvest")),
        ("Nutrition (per 100g)", advisory.get("nutrition_per_100g")),
        ("Nutrition Notes", advisory.get("nutrition_explanation")),
        ("Health Benefits", advisory.get("health_benefits")),
        ("Economics", advisory.get("economic_importance")),
        ("Risk Factors", advisory.get("risk_factors")),
    ]

    for title, data in sections:
        lines = _section_to_lines("", data)
        if lines:
            draw_block(lines, title=title)
            y -= 6

    c.save()
    buffer.seek(0)
    return buffer.read()


def main():
    apply_custom_styles()
    
    # Header
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 25px;
        text-align: center;
    ">
        <h1 style="color: white; margin: 0; font-size: 36px;">🌾 Crop Advisory</h1>
        <p style="color: rgba(255,255,255,0.9); margin: 10px 0 0 0; font-size: 16px;">
            Get comprehensive information and guidance for your crops
        </p>
    </div>
    """, unsafe_allow_html=True)

    crops = load_all_crops()
    crop_names = sorted(crops.keys())

    if not crop_names:
        st.error("No crops found in `data/crops`.")
        return

    # Search and Filter Section
    st.markdown('<p class="section-header">🔍 Find Your Crop</p>', unsafe_allow_html=True)
    
    # Search box
    search_query = st.text_input("🔎 Search crops by name...", placeholder="Type crop name here...", key="crop_search")
    
    # Category filter - all in one line using radio buttons
    st.markdown("**Filter by Category:**")
    category_options = ["All", "Cereals", "Pulses", "Vegetables", "Fruits", "Oilseeds", "Cash Crops"]
    selected_category = st.radio(
        "Select category:",
        category_options,
        index=0,
        horizontal=True,
        label_visibility="collapsed",
        key="category_radio"
    )
    
    # Get categories dictionary for filtering
    categories = get_crop_categories()

    # Filter crops based on search and category
    filtered_crops = crop_names
    
    if search_query:
        filtered_crops = [c for c in filtered_crops if search_query.lower() in c.lower()]
    
    if 'selected_category' in locals() and selected_category != "All":
        category_crops = categories.get(selected_category, [])
        filtered_crops = [c for c in filtered_crops if c in category_crops]
    
    # Display crop count
    st.markdown(f"**Showing {len(filtered_crops)} crops**")
    
    # Crop Selection
    crop_name = st.selectbox(
        "📋 Select a crop to view details:",
        filtered_crops,
        index=0 if filtered_crops else 0,
        key="crop_selector"
    )

    if not crop_name:
        st.info("👆 Please select a crop from the dropdown above to view its advisory.")
        return

    # Generate and display summary
    summary = generate_farmer_summary(crop_name)

    # Hero section with crop name
    st.markdown(f"""
    <div class="crop-card">
        <div class="crop-card-header">
            🌾 {summary.get('Crop', '') or crop_name}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Quick Stats Cards
    st.markdown('<p class="section-header">📈 Quick Overview</p>', unsafe_allow_html=True)
    
    q1, q2, q3, q4, q5 = st.columns(5)
    
    with q1:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-box-title">📅 Season</div>
            <div class="stat-box-value">{summary.get('Season', '-')}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with q2:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-box-title">⏱️ Duration</div>
            <div class="stat-box-value">{summary.get('Duration', '-')}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with q3:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-box-title">💧 Water</div>
            <div class="stat-box-value">{summary.get('Water Requirement', '-')}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with q4:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-box-title">📊 Yield</div>
            <div class="stat-box-value">{summary.get('Average Yield', '-')}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with q5:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-box-title">🏷️ Category</div>
            <div class="stat-box-value">{selected_category if 'selected_category' in locals() else 'General'}</div>
        </div>
        """, unsafe_allow_html=True)

    advisory = {}
    for mode in ["legacy", "detailed", "expert"]:
        data = get_crop_advisory(crop_name, mode=mode)
        if isinstance(data, dict) and "error" in data:
            st.error(data["error"])
            return
        if isinstance(data, dict):
            advisory.update(data)

    # PDF Export
    st.markdown('<p class="section-header">📄 Export</p>', unsafe_allow_html=True)
    try:
        pdf_bytes = build_crop_pdf(crop_name, summary, advisory)
        st.download_button(
            "Download Crop Advisory (PDF)",
            data=pdf_bytes,
            file_name=f"{crop_name.lower().replace(' ', '_')}_advisory.pdf",
            mime="application/pdf",
        )
    except Exception as e:
        st.warning(f"PDF export is unavailable: {e}")

# 7 Detailed Tabs - Clickable sections
    st.markdown('<p class="section-header">📋 Detailed Information</p>', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
        "Cultivation Basics",
        "Soil & Fertility",
        "Seed & Sowing",
        "Growth Stages",
        "Irrigation",
        "Pest & Disease Management",
        "Harvesting & Post‑Harvest",
        "Nutrition & Health Benefits",
        "Yield & Profit",
    ])

    with tab1:
        st.markdown("### Cultivation Basics")
        if isinstance(advisory, dict):
            fields = ["name", "scientific_name", "family", "category", "crop_type", "season", "duration_days", "climate", "ideal_temperature", "water_requirement_level", "average_yield_per_acre", "sunlight_requirement"]
            for field in fields:
                if field in advisory:
                    value = advisory[field]
                    label = field.replace('_', ' ').title()
                    st.markdown(f"**{label}:** {' | '.join(value) if isinstance(value, list) else value}")
            if "major_states" in advisory and isinstance(advisory["major_states"], list):
                st.markdown("### Major Growing States")
                render_list(advisory["major_states"])

    with tab2:
        st.markdown("### Soil & Fertility")
        if isinstance(advisory, dict):
            st.markdown("### Soil Requirements")
            soil_fields = ["soil_type", "soil_ph_range", "soil_depth_requirement", "salinity_tolerance", "drainage_requirement"]
            for field in soil_fields:
                if field in advisory:
                    st.markdown(f"**{field.replace('_', ' ').title()}:** {advisory[field]}")
            if "fertilizer_management" in advisory and isinstance(advisory["fertilizer_management"], dict):
                st.markdown("### Fertilizer Management")
                for key, value in advisory["fertilizer_management"].items():
                    label = key.replace('_', ' ').title()
                    render_key_value(label, value)

    with tab3:
        st.markdown("### Seed & Sowing")
        if isinstance(advisory, dict):
            if "seed_information" in advisory and isinstance(advisory["seed_information"], dict):
                st.markdown("### Seed Information")
                for key, value in advisory["seed_information"].items():
                    label = key.replace('_', ' ').title()
                    render_key_value(label, value)
            sowing_fields = ["sowing_method", "row_spacing", "plant_spacing", "sowing_depth"]
            sowing_present = [f for f in sowing_fields if f in advisory]
            if sowing_present:
                st.markdown("### Sowing & Spacing")
                for field in sowing_present:
                    label = field.replace('_', ' ').title()
                    st.markdown(f"**{label}:** {advisory[field]}")
            if "land_preparation" in advisory and isinstance(advisory["land_preparation"], list):
                st.markdown("### Land Preparation")
                render_list(advisory["land_preparation"])

    with tab4:
        st.markdown("### Growth Stages")
        if isinstance(advisory, dict) and "growth_stages" in advisory and isinstance(advisory["growth_stages"], dict):
            for stage, info in advisory["growth_stages"].items():
                stage_label = stage.replace('_', ' ').title()
                if isinstance(info, dict):
                    duration = info.get("duration")
                    details = info.get("details")
                    if duration:
                        st.markdown(f"**{stage_label} (Duration):** {duration}")
                    if details:
                        st.markdown(f"**{stage_label} (Details):** {details}")

    with tab5:
        st.markdown("### Irrigation")
        if isinstance(advisory, dict):
            irr_fields = ["rainfall_requirement_mm", "irrigation_schedule", "water_requirement_level"]
            for field in irr_fields:
                if field in advisory:
                    value = advisory[field]
                    label = field.replace('_', ' ').title()
                    st.markdown(f"**{label}:** {' | '.join(value) if isinstance(value, list) else value}")
            if "irrigation_schedule" in advisory and isinstance(advisory["irrigation_schedule"], dict):
                for k, v in advisory["irrigation_schedule"].items():
                    render_key_value(k.replace('_', ' ').title(), v)

    with tab6:
        st.markdown("### Pest & Disease Management")
        if isinstance(advisory, dict):
            pest_fields = ["major_pests", "major_diseases", "major_weeds"]
            for field in pest_fields:
                if field in advisory:
                    st.markdown(f"#### {field.replace('_', ' ').title()}")
                    data = advisory[field]
                    if isinstance(data, dict):
                        for pest, info in data.items():
                            st.markdown(f"**{pest.replace('_', ' ').title()}:**")
                            if isinstance(info, dict):
                                for k, v in info.items():
                                    render_key_value(k.replace('_', ' ').title(), v)
                            elif isinstance(info, list):
                                render_list(info)
                            else:
                                st.markdown(str(info))

    with tab7:
        st.markdown("### Harvesting & Post‑Harvest")
        if isinstance(advisory, dict):
            sections = ["harvesting_details", "post_harvest"]
            for section in sections:
                if section in advisory:
                    st.markdown(f"### {section.replace('_', ' ').title()}")
                    data = advisory[section]
                    if isinstance(data, dict):
                        for key, value in data.items():
                            render_key_value(str(key), value)
                    elif isinstance(data, list):
                        render_list(data)

    with tab8:
        st.markdown("### Nutrition & Health Benefits")
        if isinstance(advisory, dict):
            sections = ["nutrition_per_100g", "nutrition_explanation", "health_benefits"]
            for section in sections:
                if section in advisory:
                    st.markdown(f"### {section.replace('_', ' ').title()}")
                    data = advisory[section]
                    if isinstance(data, dict):
                        if section == "nutrition_per_100g":
                            cols = st.columns(2)
                            for i, (key, value) in enumerate(data.items()):
                                with cols[i % 2]:
                                    st.metric(key, value)
                        else:
                            for key, value in data.items():
                                render_key_value(str(key), value)
                    elif isinstance(data, list):
                        render_list(data)

    with tab9:
        st.markdown("### Yield & Profit")
        if isinstance(advisory, dict):
            # Yield in quintal/ha
            yield_value = advisory.get("average_yield_per_acre") or advisory.get("average_yield_per_hectare")
            if isinstance(yield_value, str):
                parsed = parse_quintal_range(yield_value)
                if parsed:
                    per_acre = parsed
                    per_ha = (per_acre[0] * 2.47105, per_acre[1] * 2.47105)
                    st.markdown("#### Yield (Quintal/ha)")
                    st.markdown(f"**Estimated:** {format_range(per_ha[0], per_ha[1])} quintal/ha")
                    st.markdown(f"**Source (per acre):** {yield_value}")
                else:
                    st.markdown("#### Yield (Quintal/ha)")
                    st.markdown(str(yield_value))
            elif yield_value:
                st.markdown("#### Yield (Quintal/ha)")
                st.markdown(str(yield_value))

            # Profit/Economics
            st.markdown("#### Profit & Economics")
            if "profit_per_hectare" in advisory:
                render_key_value("Profit Per Hectare", advisory["profit_per_hectare"])
            elif "profit_per_acre" in advisory:
                parsed = parse_quintal_range(str(advisory["profit_per_acre"]))
                if parsed:
                    per_ha = (parsed[0] * 2.47105, parsed[1] * 2.47105)
                    st.markdown(f"**Profit Per Hectare:** {format_range(per_ha[0], per_ha[1])}")
                    st.markdown(f"**Source (per acre):** {advisory['profit_per_acre']}")
                else:
                    render_key_value("Profit Per Acre", advisory["profit_per_acre"])
            else:
                st.info("Profit varies by input cost and market price. Use the Profit Calculator page for estimates.")

            for section in ["economic_importance", "risk_factors"]:
                if section in advisory:
                    st.markdown(f"#### {section.replace('_', ' ').title()}")
                    data = advisory[section]
                    if isinstance(data, list):
                        render_list(data)
                    elif isinstance(data, dict):
                        for key, value in data.items():
                            render_key_value(str(key), value)
                    else:
                        st.markdown(str(data))
    # Image Gallery Section
    if isinstance(advisory, dict) and ("Images" in advisory or "images" in advisory):
        st.markdown('<p class="section-header">🖼️ Image Gallery</p>', unsafe_allow_html=True)
        
        images = advisory.get("Images") or advisory.get("images")
        
        if "crop" in images:
            st.markdown("**Crop Image:**")
            display_image(images["crop"], f"{crop_name} - Main View", width=400)
        
        # Pest Images
        if "pests" in images and isinstance(images["pests"], list) and images["pests"]:
            st.markdown("**🐛 Common Pests:**")
            pest_cols = st.columns(4)
            for idx, pest_img in enumerate(images["pests"]):
                with pest_cols[idx % 4]:
                    display_image(pest_img, f"Pest {idx+1}", width=180)
        
        # Disease Images
        if "diseases" in images and isinstance(images["diseases"], list) and images["diseases"]:
            st.markdown("**🦠 Common Diseases:**")
            disease_cols = st.columns(4)
            for idx, disease_img in enumerate(images["diseases"]):
                with disease_cols[idx % 4]:
                    display_image(disease_img, f"Disease {idx+1}", width=180)
        
        # Weed Images
        if "weeds" in images and isinstance(images["weeds"], list) and images["weeds"]:
            st.markdown("**🌿 Common Weeds:**")
            weed_cols = st.columns(4)
            for idx, weed_img in enumerate(images["weeds"]):
                with weed_cols[idx % 4]:
                    display_image(weed_img, f"Weed {idx+1}", width=180)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 20px;">
        <p>🌱 Smart Agriculture AI - Crop Advisory System</p>
        <p>For more information, consult local agricultural experts.</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

