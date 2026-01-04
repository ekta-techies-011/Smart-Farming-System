# 🌾 Smart Farming System

A comprehensive AI-powered farming management system built with Streamlit.

## Features

- 🌾 **Crop Recommendation** - AI-powered crop selection based on soil and weather data
- 🦠 **Disease Detection** - Upload images to detect plant diseases (Coming Soon)
- 💊 **Fertilizer Recommendation** - Optimize soil nutrients for better yield
- 💧 **Smart Irrigation** - Intelligent water management recommendations
- 💰 **Market Advice** - Real-time crop prices and market analysis
- 🌤 **Weather Alerts** - Live weather data and forecasts

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Live Data Integration

### Weather Data
The app uses free weather APIs for live data. For production use:
- Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
- Add your API key to the `utils/weather_api.py` file

### Market Data
Market data is currently using realistic mock data. For production:
- Integrate with agricultural market APIs
- Connect to commodity exchange APIs
- Use government agricultural price databases

## Project Structure

```
Smart farming system/
├── app.py                      # Main application
├── pages/                      # Feature pages
│   ├── Crop_Recommendation.py
│   ├── Disease_Detection.py
│   ├── Fertilizer_Recommendation.py
│   ├── Market_advice.py
│   ├── Smart_Irrigation.py
│   └── Weather_Alerts.py
├── utils/                      # Utility modules
│   ├── weather_api.py         # Weather data integration
│   └── market_data.py         # Market data utilities
├── models/                     # ML models
│   ├── crop_model.pkl
│   └── scaler.pkl
├── data/                       # Data files
│   └── crop_recommendation.csv
└── requirements.txt            # Python dependencies
```

## Usage

1. **Login/Signup**: Create an account or login
2. **Dashboard**: Access all features from the main dashboard
3. **Live Data**: Use the "Fetch Live Weather" option in Crop Recommendation and Smart Irrigation
4. **Market Analysis**: Select crops to get real-time price information and market insights
5. **Weather Alerts**: Enter your city to get current weather and forecasts

## Technologies

- Streamlit - Web application framework
- Scikit-learn - Machine learning
- NumPy & Pandas - Data processing
- Requests - API integration

## License

This project is open source and available for educational purposes.

