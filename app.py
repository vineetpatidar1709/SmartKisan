import streamlit as st

from utils.ui_components import apply_custom_theme
from utils.constants import PAGE_CONFIGS

st.set_page_config(
    page_title="SMART KISAN",
    page_icon="🌾",
    layout="wide",
)
apply_custom_theme()

def apply_custom_styles():
    st.markdown("""
    <style>
    .section-header {
        font-size: 20px;
        font-weight: bold;
        color: #1B5E20;
        margin: 20px 0 15px 0;
        padding-bottom: 10px;
        border-bottom: 2px solid #4CAF50;
    }
    .card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 16px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border-left: 5px solid #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)


def main():
    """Front/Landing page with navigation to all pages"""
    apply_custom_styles()
    
    # Hero Section
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 25px;
        text-align: center;
    ">
            <h1 style="color: white; margin: 0; font-size: 36px;">🌾 SMART KISAN</h1>
        <p style="color: rgba(255,255,255,0.9); margin: 10px 0 0 0; font-size: 16px;">
            AI-powered farming solutions for Indian agriculture
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Features Overview
    st.markdown('<p class="section-header">🚀 Features</p>', unsafe_allow_html=True)
    
    # Create columns for feature cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🌾 Crop Recommendation
        Get AI-powered crop recommendations based on soil, weather, and location data.
        """)
        if st.button("Go to Crop Recommendation", key="nav_crop_recommendation"):
            st.switch_page("pages/crop_recommendation.py")
    
    with col2:
        st.markdown("""
        ### 📘 Crop Advisory
        Access detailed information about various crops including best practices, 
        pest management, and market information.
        """)
        if st.button("Go to Crop Advisory", key="nav_crop_advisory"):
            st.switch_page("pages/1_Crop_Advisory.py")
    
    with col3:
        st.markdown("""
        ### 📈 Yield Estimator
        Predict crop yields based on historical data and current farming conditions.
        """)
        if st.button("Go to Yield Estimator", key="nav_yield_estimator"):
            st.switch_page("pages/2_Yield_Estimator.py")
    
    st.markdown("---")
    
    # Additional Features
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.markdown("""
        ### 💰 Profit Calculator
        Calculate expected profits based on costs, yields, and market prices.
        """)
        if st.button("Go to Profit Calculator", key="nav_profit_calculator"):
            st.switch_page("pages/3_Profit_Calculator.py")
    
    with col5:
        st.markdown("""
        ### 📊 Market Prices
        Check current market prices for various crops across different states.
        """)
        if st.button("Go to Market Prices", key="nav_market_prices"):
            st.switch_page("pages/4_Market_Prices.py")
    
    with col6:
        st.markdown("""
        ### 🌍 State Data
        Explore agricultural data specific to different Indian states.
        """)
        # Placeholder for future state data page
    
    st.markdown("---")
    
    # Quick Stats Section
    st.markdown('<p class="section-header">📊 Quick Stats</p>', unsafe_allow_html=True)
    stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)
    
    with stats_col1:
        st.metric("Crops Supported", "20+")
    with stats_col2:
        st.metric("States Covered", "10+")
    with stats_col3:
        st.metric("ML Models", "3")
    with stats_col4:
        st.metric("Features", "5")
    
    # Footer
    st.markdown("---")
    st.caption("💡 Use the navigation buttons above or the sidebar to access different features.")
    st.caption("Built with Streamlit and Machine Learning")


if __name__ == "__main__":
    main()
