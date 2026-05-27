# SMART KISAN

## Project Title and Brief Description

**SMART KISAN** is an AI-powered smart agriculture assistant built as a multi-page Streamlit web application for Indian farming use cases. The project helps users make better agricultural decisions through crop recommendation, crop advisory, yield prediction, profit estimation, and market price tracking. It combines machine learning models, curated crop knowledge, and mandi price data in a single interface.

## Technology Stack and Tools Used

- **Programming Language:** Python
- **Frontend / App Framework:** Streamlit
- **Machine Learning:** scikit-learn, XGBoost, joblib
- **Data Processing:** pandas, numpy
- **Data Visualization:** Plotly, Matplotlib, Seaborn
- **Image Handling:** Pillow
- **API Integration:** requests
- **Report Generation:** reportlab
- **Data Sources:** local crop database, CSV datasets, Data.gov.in / AGMARKNET-linked mandi price data
- **Project Assets:** static crop, pest, disease, and weed images

## Features and Functionalities Implemented

- **Crop Recommendation**
  Predicts suitable crops using machine learning based on state, soil type, month, irrigation, rainfall, pH, temperature, and NPK values.

- **Crop Advisory**
  Provides detailed crop-wise guidance including season, soil needs, seed information, fertilizer management, irrigation, growth stages, harvesting, post-harvest handling, and economics.

- **Pest, Disease, and Weed Support**
  Displays common pests, diseases, and weeds along with supporting images for better field-level awareness.

- **Yield Estimator**
  Estimates crop yield using trained ML models and farming input conditions.

- **Profit Calculator**
  Calculates expected profit using crop yield, land size, input cost, and mandi or custom selling price.

- **Live / Fallback Market Prices**
  Fetches mandi prices using Data.gov.in API when available and falls back to static sample market data when live data is unavailable.

- **PDF Export**
  Generates downloadable crop advisory reports for selected crops.

- **Multi-Page User Interface**
  Organizes the system into separate pages for crop recommendation, advisory, yield estimation, profit calculation, and market price tracking.

- **Agriculture-Focused Coverage**
  Includes around **54 crop profiles** and supports **26 Indian states** in the ML/data flow.

## Installation / Execution Steps to Run the Project

### Prerequisites

- Python 3.8 or above
- `pip`

### Steps

1. **Clone the repository**

```bash
git clone <repository-url>
cd smart_agriculture_ai
```

2. **Create and activate a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Optional: configure live market price API**

For live mandi prices, set your Data.gov.in API key as an environment variable:

```bash
# Windows PowerShell
$env:DATA_GOV_IN_API_KEY="your_api_key"

# macOS / Linux
export DATA_GOV_IN_API_KEY="your_api_key"
```

5. **Run the application**

```bash
streamlit run app.py
```

6. **Open in browser**

Streamlit usually starts the app at:

```text
http://localhost:8501
```

## Project Structure

```text
smart_agriculture_ai/
|-- app.py
|-- requirements.txt
|-- pages/
|   |-- crop_recommendation.py
|   |-- 1_Crop_Advisory.py
|   |-- 2_Yield_Estimator.py
|   |-- 3_Profit_Calculator.py
|   |-- 4_Market_Prices.py
|-- data/
|   |-- crop_loader.py
|   |-- crop_database.py
|   |-- market_price.py
|   |-- state_data.py
|   |-- crops/
|-- ml/
|   |-- models/
|   |-- train_crop.py
|   |-- train_yield.py
|-- utils/
|   |-- ui_components.py
|   |-- enhanced_soil_estimator.py
|   |-- water_classifier.py
|-- static/
|   |-- images/
```

## Team Members

1. Vineet Patidar (EN23CS3011132)
2. Devansh Mishra (EN24CS3T10010)

## Project Screenshots / Output

1. Home Page: "\static\images\page images\Home Page.png"
2. Crop Recommendation Page: "\static\images\page images\Crop_recommendation.png"
3. Crop Advisory Page: "\static/images/page images/Crop Advisory.png"
4. Yield Estimator Page: "\static/images/page images/Yield Estimator.png"
5. Profit Calculator Page: "\static/images/page images/Profit calculator.png"
6. Market Prices Page: "\static/images/page images/Market_Price.png


## Data Sources

- Local crop data stored in `data/crops/`
- Machine learning models stored in `ml/models/`
- Market price integration through Data.gov.in agricultural market price API
- Static fallback mandi price records inside the project


