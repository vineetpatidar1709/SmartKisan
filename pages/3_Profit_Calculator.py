import streamlit as st
import pandas as pd
import requests
import re
from datetime import datetime
from data.market_price import market_data, calculate_profit
from data.crop_loader import load_all_crops
from utils.shared_constants import get_data_gov_api_key as _get_data_gov_api_key


st.set_page_config(page_title="Profit Calculator", page_icon="💰", layout="wide")

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


def _commodity_candidates(crop_name: str):
    """Return commodity aliases commonly used by mandi datasets."""
    alias_map = {
        "Rice": ["Rice", "Paddy", "Rice (Basmati)"],
        "Chilli": ["Chilli", "Chili", "Green Chilli", "Red Chilli"],
        "Turmeric": ["Turmeric", "Haldi"],
        "Groundnut": ["Groundnut", "Peanut"],
        "Mustard": ["Mustard", "Mustard Seed"],
        "Tomato": ["Tomato"],
        "Onion": ["Onion"],
        "Potato": ["Potato"],
        "Wheat": ["Wheat"],
        "Maize": ["Maize", "Corn"],
        "Soybean": ["Soybean", "Soyabean"],
        "Cotton": ["Cotton"],
    }
    return alias_map.get(crop_name, [crop_name])


def get_mandi_prices(crop_name: str, state: str = None):
    """
    Fetch mandi prices directly from Data.gov.in API.
    Returns None when data is unavailable so caller can fallback to static prices.
    """
    try:
        api_key = _get_data_gov_api_key()
        if not api_key:
            return None
        response = requests.get(
            "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070",
            params={
                "api-key": api_key,
                "format": "json",
                "limit": 1000,
            },
        timeout=30,
        )

        if response.status_code != 200:
            return None

        data = response.json()
        records = data.get("records", [])
        if not records:
            return None

        all_data = []
        for record in records:
            all_data.append(
                {
                    "State": record.get("state", ""),
                    "Market": record.get("market", ""),
                    "Commodity": record.get("commodity", ""),
                    "Min Price": float(record.get("min_price", 0) or 0),
                    "Max Price": float(record.get("max_price", 0) or 0),
                    "Modal Price": float(record.get("modal_price", 0) or 0),
                    "Unit": record.get("unit", "Quintal"),
                    "Date": record.get("arrival_date", datetime.now().strftime("%Y-%m-%d")),
                }
            )

        df = pd.DataFrame(all_data)
        if df.empty:
            return None

        if state and state != "All":
            df = df[df["State"] == state]

        if crop_name and crop_name != "All":
            candidates = [c.lower() for c in _commodity_candidates(crop_name)]
            commodity_lc = df["Commodity"].astype(str).str.lower()
            df = df[commodity_lc.isin(candidates)]

        if df.empty:
            return None

        return df
    except Exception:
        return None

    return None


def main():
    apply_custom_styles()
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 25px;
        text-align: center;
    ">
        <h1 style="color: white; margin: 0; font-size: 36px;">💰 Profit Calculator</h1>
        <p style="color: rgba(255,255,255,0.9); margin: 10px 0 0 0; font-size: 16px;">
            Calculate expected profit using market prices, yield, and input costs
        </p>
    </div>
    """, unsafe_allow_html=True)

    crops = load_all_crops()
    crop_options = sorted(market_data.keys())

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<p class="section-header">📋 Enter Details</p>', unsafe_allow_html=True)
        
        crop_name = st.selectbox("Select Crop", crop_options, index=0)

        states_list = ["All", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
             "Gujarat", "Haryana", "Himachal Pradesh", "Jammu & Kashmir", "Jharkhand",
             "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Meghalaya",
             "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
             "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
        
        selected_state = st.selectbox("Select State", states_list, index=0)

        mandi_df = get_mandi_prices(crop_name, None if selected_state == "All" else selected_state)
        
        st.markdown("### 💵 Price Source")
        
        price_option = st.radio("Choose price source:",
            ["📍 Select Mandi Price", "✏️ Enter Custom Price"], horizontal=True)
        
        selected_mandi = None
        user_price = None
        price_source_status = "Unknown"
        
        if price_option == "📍 Select Mandi Price":
            if mandi_df is not None and not mandi_df.empty:
                mandi_options = [f"{row['Market']} ({row['State']}) - ₹{row['Modal Price']:,}/q" 
                               for _, row in mandi_df.iterrows()]
                mandi_options.insert(0, "🏆 Best Price (Average of All)")
                
                selected_mandi_option = st.selectbox("Select Mandi", mandi_options, index=0)
                
                if selected_mandi_option == "🏆 Best Price (Average of All)":
                    price_per_quintal = mandi_df["Modal Price"].mean()
                    selected_mandi = "Best Average"
                    price_source_status = "Live Mandi"
                else:
                    market_name = selected_mandi_option.split(" (")[0]
                    selected_row = mandi_df[mandi_df["Market"] == market_name].iloc[0]
                    price_per_quintal = selected_row["Modal Price"]
                    selected_mandi = f"{selected_row['Market']}, {selected_row['State']}"
                    price_source_status = "Live Mandi"
            else:
                st.warning("⚠️ No live mandi prices. Using static data.")
                price_per_quintal = market_data.get(crop_name, {}).get("price_per_ton", 20000) / 10
                selected_mandi = "Static Market Data"
                price_source_status = "Static Fallback"
        else:
            default_price = int(market_data.get(crop_name, {}).get("price_per_ton", 20000) / 10)
            user_price = st.number_input("Enter your selling price (₹/quintal)", min_value=0, value=default_price, step=50)
            price_per_quintal = user_price
            selected_mandi = "Custom Price"
            price_source_status = "Custom Price"

        land_size = st.number_input("Land Size (acres)", min_value=0.5, max_value=100.0, value=1.0, step=0.5)

        default_yield = 25.0
        if crop_name in crops:
            # Try to get yield from crop data
            yield_info = crops[crop_name].get("Yield Information", {})
            avg_yield = yield_info.get("Average Yield", "")
            if avg_yield:
                try:
                    ton_value = float(str(avg_yield).split()[0])
                    default_yield = ton_value * 10
                except:
                    pass
            # Also check for flat structure (new format)
            if not avg_yield:
                avg_yield = crops[crop_name].get("average_yield_per_acre", "")
                if avg_yield:
                    try:
                        # Handle formats like "18-25 quintals" or just numbers
                        match = re.search(r'(\d+(?:\.\d+)?)', str(avg_yield))
                        if match:
                            default_yield = float(match.group(1))
                    except:
                        pass

        yield_per_acre = st.number_input("Expected Yield (quintals/acre)", min_value=1.0, max_value=500.0, value=default_yield, step=1.0)

        use_custom_cost = st.checkbox("Override input cost", value=False)
        
        market_info = market_data.get(crop_name, {"price_per_ton": 20000, "input_cost_per_acre": 25000, "demand": "Medium", "volatility": "Medium"})
        
        if use_custom_cost:
            input_cost = st.number_input("Input Cost per Acre (₹)", min_value=0, value=int(market_info["input_cost_per_acre"]), step=1000)
        else:
            input_cost = market_info["input_cost_per_acre"]

    with col2:
        st.markdown('<p class="section-header">📊 Price Summary</p>', unsafe_allow_html=True)
        st.caption("Data Source Status")
        if price_source_status == "Live Mandi":
            st.success("Live Mandi")
        elif price_source_status == "Static Fallback":
            st.info("Static Fallback")
        elif price_source_status == "Custom Price":
            st.warning("Custom Price")
        else:
            st.info("Unknown")
        
        if selected_mandi == "Best Average":
            st.success(f"📡 **Best Average Price**")
            if mandi_df is not None:
                st.markdown(f"**Avg Price:** ₹{int(price_per_quintal):,}/quintal")
                st.markdown(f"**Markets:** {len(mandi_df)} mandis")
        elif selected_mandi == "Custom Price":
            st.warning(f"✏️ **Custom Price**")
            st.markdown(f"**Your Price:** ₹{int(price_per_quintal):,}/quintal")
        elif selected_mandi and selected_mandi not in ["Static Market Data"]:
            st.success(f"📍 **{selected_mandi}**")
            st.markdown(f"**Modal Price:** ₹{int(price_per_quintal):,}/quintal")
        else:
            st.info(f"📅 **Static Market Data**")
            st.markdown(f"**Price:** ₹{int(price_per_quintal):,}/quintal")
        
        if mandi_df is not None and not mandi_df.empty and selected_mandi not in ["Best Average", "Static Market Data", "Custom Price"]:
            st.markdown("---")
            st.markdown("**Other Mandi Prices:**")
            for _, row in mandi_df.head(5).iterrows():
                st.markdown(f"- {row['Market']}: ₹{row['Modal Price']:,}/q")
        
        st.markdown("---")
        st.info(f"**Demand:** {market_info['demand']}")
        st.warning(f"**Volatility:** {market_info['volatility']}")
        st.markdown("---")
        st.markdown(f"**Default Cost:** ₹{market_info['input_cost_per_acre']:,}/acre")

    st.markdown("---")
    st.markdown('<p class="section-header">💵 Profit Calculation</p>', unsafe_allow_html=True)

    if st.button("Calculate Profit", type="primary"):
        total_yield = yield_per_acre * land_size
        total_revenue = price_per_quintal * total_yield
        total_cost = input_cost * land_size
        profit = total_revenue - total_cost
        roi = (profit / total_cost * 100) if total_cost > 0 else 0

        r1, r2, r3, r4 = st.columns(4)
        r1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
        r2.metric("Total Cost", f"₹{total_cost:,.0f}")
        r3.metric("Net Profit", f"₹{profit:,.0f}", delta="₹{:,.0f}".format(profit) if profit > 0 else None, delta_color="normal" if profit > 0 else "inverse")
        r4.metric("ROI", f"{roi:.1f}%")

        st.markdown("---")
        st.markdown('<p class="section-header">📋 Calculation Breakdown</p>', unsafe_allow_html=True)

        st.markdown(f"""
        | Item | Value |
        |------|-------|
        | Crop | {crop_name} |
        | Price Source | {selected_mandi} |
        | Selling Price | ₹{price_per_quintal:,}/quintal |
        | Yield/Acre | {yield_per_acre} quintals |
        | **Total Yield** | **{total_yield} quintals** |
        | **Revenue** | **₹{total_revenue:,.0f}** |
        | Cost/Acre | ₹{input_cost:,} |
        | **Total Cost** | **₹{total_cost:,.0f}** |
        | **Net Profit** | **₹{profit:,.0f}** |
        | ROI | {roi:.1f}% |
        """)

        if profit > 0:
            st.success(f"✅ Good profit! Expected: ₹{profit:,.0f} for {land_size} acres")
        elif profit == 0:
            st.warning("⚠️ Break-even point.")
        else:
            st.error(f"⚠️ Loss: ₹{abs(profit):,.0f}")

        st.markdown("---")
        st.markdown('<p class="section-header">📈 Compare with Other Crops</p>', unsafe_allow_html=True)

        comparison_data = []
        for crop, info in market_data.items():
            comp_revenue = (info["price_per_ton"] / 10) * yield_per_acre * land_size
            comp_cost = info["input_cost_per_acre"] * land_size
            comp_profit = comp_revenue - comp_cost
            comp_roi = (comp_profit / comp_cost * 100) if comp_cost > 0 else 0
            comparison_data.append({"Crop": crop, "Price (₹/q)": int(info["price_per_ton"]/10), "Revenue": comp_revenue, "Cost": comp_cost, "Profit": comp_profit, "ROI %": comp_roi})

        comparison_df = sorted(comparison_data, key=lambda x: x["Profit"], reverse=True)
        st.table(comparison_df[:5])

    st.markdown("---")
    with st.expander("📊 View All Crops Market Data"):
        st.dataframe(pd.DataFrame(market_data).T, use_container_width=True)


if __name__ == "__main__":
    main()
