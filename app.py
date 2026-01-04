import streamlit as st
import streamlit.components.v1 as components
import json
import os

# Page configuration
st.set_page_config(
    page_title="Smart Farming System",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# File paths for persistence
USERS_FILE = "users_data.json"
SESSION_FILE = "session_data.json"

def load_users():
    """Load users from JSON file"""
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_users(users):
    """Save users to JSON file"""
    try:
        with open(USERS_FILE, 'w') as f:
            json.dump(users, f)
    except:
        pass

def load_session():
    """Load session data from JSON file"""
    if os.path.exists(SESSION_FILE):
        try:
            with open(SESSION_FILE, 'r') as f:
                return json.load(f)
        except:
            return {"logged_in": False, "current_user": ""}
    return {"logged_in": False, "current_user": ""}

def save_session(logged_in, current_user):
    """Save session data to JSON file"""
    try:
        session_data = {
            "logged_in": logged_in,
            "current_user": current_user
        }
        with open(SESSION_FILE, 'w') as f:
            json.dump(session_data, f)
    except:
        pass

# Custom CSS for modern design
st.markdown("""
<style>
    /* Farming-themed background with beautiful gradient - Full page coverage */
    .stApp {
        background: 
            linear-gradient(135deg, 
                rgba(135, 206, 235, 0.95) 0%,    /* Sky blue */
                rgba(152, 216, 200, 0.95) 30%,   /* Light green transition */
                rgba(144, 238, 144, 0.95) 60%,   /* Green fields */
                rgba(247, 220, 111, 0.95) 100%   /* Golden wheat */
            ),
            url('https://images.unsplash.com/photo-1500937386664-56d1dfef3854?w=1920&q=80') center/cover fixed !important;
        background-blend-mode: overlay;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        min-height: 100vh !important;
        width: 100% !important;
    }
    
    .main {
        background: transparent !important;
        padding: 2rem;
        width: 100% !important;
        max-width: 100% !important;
    }
    
    section[data-testid="stMain"] {
        background: transparent !important;
        width: 100% !important;
    }
    
    /* Full width layout */
    .block-container {
        max-width: 100% !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    
    /* Add a subtle pattern overlay */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 0
            repeating-linear-gradient(
                0deg,
                transparent,
                transparent 2px,
                rgba(255,255,255,.03) 2px,
                rgba(255,255,255,.03) 4px
            );
        pointer-events: none;
        z-index: 1;
    }
    
    .stApp > div {
        position: relative;
        z-index: 2;
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.9) 0%, rgba(118, 75, 162, 0.9) 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        backdrop-filter: blur(10px);
    }
    
    .header-title {
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .header-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    /* Card styling */
    .feature-card {
        background: rgba(255, 255, 255, 0.7);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border-left: 5px solid #667eea;
        height: 100%;
        cursor: pointer;
        text-decoration: none;
        display: block;
        color: inherit;
        backdrop-filter: blur(10px);
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        text-decoration: none;
        color: inherit;
        background: rgba(255, 255, 255, 0.85);
    }
    
    .feature-card-link {
        text-decoration: none;
        color: inherit;
    }
    
    .metric-card-link {
        text-decoration: none;
        color: inherit;
        display: block;
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #333;
        margin-bottom: 0.5rem;
    }
    
    .feature-description {
        color: #666;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    
    /* Login/Signup form styling */
    .login-container {
        max-width: 500px;
        margin: 2rem auto;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.8);
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        backdrop-filter: blur(10px);
        color: #1f1f1f !important;
    }
    
    .login-container h3,
    .login-container p,
    .login-container label,
    .login-container div {
        color: #1f1f1f !important;
    }
    
    .login-container .stMarkdown h3 {
        color: #1f1f1f !important;
    }
    
    .login-container .stMarkdown p {
        color: #333333 !important;
    }
    
    .login-container .stTextInput label {
        color: #1f1f1f !important;
        font-weight: 600;
    }
    
    .login-container input {
        color: #1f1f1f !important;
    }
    
    /* Style tabs content - dark text */
    div[data-testid="stTabs"] [data-testid="stMarkdownContainer"] {
        color: #1f1f1f !important;
    }
    
    div[data-testid="stTabs"] [data-testid="stMarkdownContainer"] h3,
    div[data-testid="stTabs"] [data-testid="stMarkdownContainer"] p {
        color: #1f1f1f !important;
    }
    
    /* Style all markdown in middle column (login area) */
    div[data-testid="column"]:nth-of-type(2) [data-testid="stMarkdownContainer"] h3 {
        color: #1f1f1f !important;
    }
    
    div[data-testid="column"]:nth-of-type(2) [data-testid="stMarkdownContainer"] p {
        color: #333333 !important;
    }
    
    /* Style input labels in login area */
    div[data-testid="column"]:nth-of-type(2) label {
        color: #1f1f1f !important;
        font-weight: 600;
    }
    
    /* Style text inputs */
    div[data-testid="column"]:nth-of-type(2) input {
        color: #1f1f1f !important;
    }
    
    /* Style all text in tabs */
    div[data-testid="stTabs"] * {
        color: #1f1f1f !important;
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem;
        border-radius: 10px;
        font-weight: bold;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* Metrics styling */
    .metric-container {
        background: linear-gradient(135deg, rgba(240, 147, 251, 0.8) 0%, rgba(245, 87, 108, 0.8) 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        backdrop-filter: blur(10px);
    }
    
    /* Hide Sidebar completely */
    [data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* Make main content full width when sidebar is hidden */
    .main .block-container {
        max-width: 100% !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    
    /* Hide sidebar button */
    [data-testid="collapsedControl"] {
        display: none !important;
    }
    
    button[title="View sidebar"] {
        display: none !important;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Hide pages navigation menu in sidebar */
    [data-testid="stSidebar"] [data-testid="stSidebarNav"] {
        display: none !important;
    }
    
    [data-testid="stSidebar"] ul[data-testid="stSidebarNav"] {
        display: none !important;
    }
    
    /* Hide any navigation elements in sidebar */
    [data-testid="stSidebar"] nav {
        display: none !important;
    }
    
    /* Hide pages menu specifically */
    [data-testid="stSidebar"] [data-testid="stSidebarNavItems"] {
        display: none !important;
    }
    
    /* Hide Streamlit pages navigation - target the specific navigation container */
    [data-testid="stSidebar"] > div > div > nav {
        display: none !important;
    }
    
    [data-testid="stSidebar"] > div > div > ul {
        display: none !important;
    }
    
    /* Hide pages navigation links */
    [data-testid="stSidebar"] a[href*="pages/"] {
        display: none !important;
    }
    
    /* Make all Streamlit containers transparent */
    .block-container {
        background: transparent !important;
    }
    
    div[data-baseweb="modal"] {
        background: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(10px);
    }
    
    /* Streamlit default backgrounds */
    .element-container {
        background: transparent !important;
    }
    
    /* Instructions box background */
    div[style*="background: #f0f2f6"] {
        background: rgba(240, 242, 246, 0.7) !important;
        backdrop-filter: blur(10px);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state - load from files if they exist
if "users" not in st.session_state:
    st.session_state["users"] = load_users()
if "logged_in" not in st.session_state:
    session_data = load_session()
    st.session_state["logged_in"] = session_data.get("logged_in", False)
    st.session_state["current_user"] = session_data.get("current_user", "")

# Sidebar with user info and logout
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <h1 style="color: white; font-size: 2rem;">🌾</h1>
        <h2 style="color: white; margin-top: 1rem;">Smart Farming</h2>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state["logged_in"]:
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
            <p style="color: white; margin: 0; font-size: 1.1rem;">
                👤 <strong>{st.session_state['current_user']}</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("🔓 Logout"):
        st.session_state["logged_in"] = False
        st.session_state["current_user"] = ""
        save_session(False, "")
        st.rerun()
    
    st.markdown("---")
    st.markdown("""
    <div style="color: white; padding: 1rem 0;">
        <p style="font-size: 0.9rem; opacity: 0.8;">
            Use the buttons on the main page to access different features.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Login/Signup Page
if not st.session_state["logged_in"]:
    st.markdown("""
    <div class="header-container">
        <div class="header-title">🌾 Smart Farming System</div>
        <div class="header-subtitle">Empowering Farmers with AI-Driven Agricultural Solutions</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Center the login form on full page
    col1, col2, col3 = st.columns([2, 3, 2])
    
    with col2:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["🔐 Login", "📝 Sign Up"])
        
        with tab1:
            st.markdown('<h3 style="color: #1f1f1f; font-weight: bold;">Welcome Back!</h3>', unsafe_allow_html=True)
            st.markdown('<p style="color: #333333;">Please login to access the Smart Farming System</p>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
            username = st.text_input("Username", key="login_user")
            password = st.text_input("Password", type="password", key="login_pass")
            
            if st.button("Login", key="login_btn"):
                if username in st.session_state["users"] and st.session_state["users"][username] == password:
                    st.session_state["logged_in"] = True
                    st.session_state["current_user"] = username
                    save_session(True, username)
                    st.success(f"✅ Welcome back, {username}!")
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password")
        
        with tab2:
            st.markdown('<h3 style="color: #1f1f1f; font-weight: bold;">Create Account</h3>', unsafe_allow_html=True)
            st.markdown('<p style="color: #333333;">Join the Smart Farming community today</p>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
            new_user = st.text_input("Username", key="signup_user")
            new_pass = st.text_input("Password", type="password", key="signup_pass")
            
            if st.button("Sign Up", key="signup_btn"):
                if new_user in st.session_state["users"]:
                    st.error("❌ Username already exists")
                elif new_user == "" or new_pass == "":
                    st.warning("⚠️ Please enter both username and password")
                else:
                    st.session_state["users"][new_user] = new_pass
                    save_users(st.session_state["users"])
                    st.success(f"✅ Account created successfully! Please login now.")
        
        st.markdown('</div>', unsafe_allow_html=True)

# Dashboard (Main Page after login)
else:
    # Header with Logout button
    col_header1, col_header2 = st.columns([4, 1])
    
    with col_header1:
        st.markdown(f"""
        <div class="header-container">
            <div class="header-title">🌾 Welcome, {st.session_state['current_user']}!</div>
            <div class="header-subtitle">Your Smart Farming Dashboard - All tools at your fingertips</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_header2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔓 Logout", key="header_logout", use_container_width=True):
            st.session_state["logged_in"] = False
            st.session_state["current_user"] = ""
            save_session(False, "")
            st.rerun()
    
    # Quick Stats (Clickable)
    st.markdown("### 📊 Quick Overview")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-container" style="cursor: pointer;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🌾</div>
            <div style="font-size: 1.5rem; font-weight: bold;">Crop</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Recommendation</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View →", key="quick_crop", use_container_width=True):
            st.switch_page("pages/Crop_Recommendation.py")
    
    with col2:
        st.markdown("""
        <div class="metric-container" style="cursor: pointer;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🦠</div>
            <div style="font-size: 1.5rem; font-weight: bold;">Disease</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Detection</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View →", key="quick_disease", use_container_width=True):
            st.switch_page("pages/Disease_Detection.py")
    
    with col3:
        st.markdown("""
        <div class="metric-container" style="cursor: pointer;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">💧</div>
            <div style="font-size: 1.5rem; font-weight: bold;">Smart</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Irrigation</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View →", key="quick_irrigation", use_container_width=True):
            st.switch_page("pages/Smart_Irrigation.py")
    
    with col4:
        st.markdown("""
        <div class="metric-container" style="cursor: pointer;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">💰</div>
            <div style="font-size: 1.5rem; font-weight: bold;">Market</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Advice</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View →", key="quick_market", use_container_width=True):
            st.switch_page("pages/Market_advice.py")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Features Grid
    st.markdown("### 🚀 Available Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Crop Recommendation Card
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🌾</div>
            <div class="feature-title">Crop Recommendation</div>
            <div class="feature-description">
                Get AI-powered crop recommendations based on soil nutrients (N, P, K), 
                temperature, humidity, pH, and rainfall data. Optimize your farming 
                decisions with machine learning insights.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Crop Recommendation →", key="btn_crop", use_container_width=True):
            st.switch_page("pages/Crop_Recommendation.py")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Fertilizer Recommendation Card
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💊</div>
            <div class="feature-title">Fertilizer Recommendation</div>
            <div class="feature-description">
                Receive intelligent fertilizer suggestions based on your soil's nitrogen, 
                phosphorus, and potassium levels. Ensure optimal nutrient balance for 
                healthy crop growth.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Fertilizer Recommendation →", key="btn_fertilizer", use_container_width=True):
            st.switch_page("pages/Fertilizer_Recommendation.py")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Weather Alerts Card
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🌤</div>
            <div class="feature-title">Weather Alerts</div>
            <div class="feature-description">
                Stay informed about weather conditions and receive timely alerts to 
                protect your crops. Plan your farming activities based on weather forecasts.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Weather Alerts →", key="btn_weather", use_container_width=True):
            st.switch_page("pages/Weather_Alerts.py")
    
    with col2:
        # Disease Detection Card
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🦠</div>
            <div class="feature-title">Disease Detection</div>
            <div class="feature-description">
                Upload images of your crops to detect diseases early. Our AI-powered 
                system helps identify plant diseases and provides recommendations for 
                treatment.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Disease Detection →", key="btn_disease", use_container_width=True):
            st.switch_page("pages/Disease_Detection.py")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Smart Irrigation Card
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💧</div>
            <div class="feature-title">Smart Irrigation</div>
            <div class="feature-description">
                Get intelligent irrigation recommendations based on soil moisture, 
                temperature, and weather forecasts. Optimize water usage and ensure 
                your crops receive the right amount of water.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Smart Irrigation →", key="btn_irrigation", use_container_width=True):
            st.switch_page("pages/Smart_Irrigation.py")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Market Advice Card
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💰</div>
            <div class="feature-title">Market Advice</div>
            <div class="feature-description">
                Access market trends and pricing information to make informed decisions 
                about when to sell your crops. Maximize your profits with strategic 
                market insights.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Market Advice →", key="btn_market", use_container_width=True):
            st.switch_page("pages/Market_advice.py")
    
    # Instructions
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
        <div style="background: rgba(240, 242, 246, 0.7); padding: 2rem; border-radius: 15px; margin-top: 2rem; backdrop-filter: blur(10px);">
        <h3 style="color: #333; margin-bottom: 1rem;">📌 How to Use</h3>
        <ol style="color: #666; line-height: 2; font-size: 1rem;">
            <li>Click on the feature cards or buttons on the main page to access different modules</li>
            <li>Enter the required information in each module</li>
            <li>Get AI-powered recommendations and insights</li>
            <li>Apply the suggestions to improve your farming practices</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
