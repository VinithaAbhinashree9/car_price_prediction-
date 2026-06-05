import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Car AI SaaS",
    page_icon="🚗",
    layout="wide"
)

# -----------------------------
# GLASSMORPHISM CSS 🎨
# -----------------------------
st.markdown("""
<style>

/* Animated Gradient Background */
body {
    background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #1c1c1c);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Glass Card */
.glass {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.18);
    margin-bottom: 20px;
}

/* Title Glow */
.title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    color: #00E5FF;
    text-shadow: 0 0 15px #00E5FF;
}

/* Metric Cards */
.metric-box {
    padding: 20px;
    border-radius: 15px;
    background: rgba(255,255,255,0.05);
    text-align: center;
    color: white;
    box-shadow: 0 0 10px rgba(0,255,255,0.2);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(0,0,0,0.3);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD MODEL
# -----------------------------
model = joblib.load("model/car_price_model.pkl")

# -----------------------------
# TITLE
# -----------------------------
st.markdown('<div class="title">🚗 Car Price AI Dashboard</div>', unsafe_allow_html=True)

st.write("")

# -----------------------------
# INPUT SECTION (GLASS CARD)
# -----------------------------
st.markdown('<div class="glass">', unsafe_allow_html=True)

st.subheader("🔧 Enter Car Details")

col1, col2, col3 = st.columns(3)

with col1:
    year = st.slider("Year", 2000, 2025, 2018)
    kms = st.number_input("KMs Driven", 0, 300000, 20000)

with col2:
    present_price = st.number_input("Present Price (Lakhs)", 0.0, 50.0, 5.0)
    owner = st.selectbox("Owner", [0, 1, 2, 3])

with col3:
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# ENCODING
# -----------------------------
fuel_map = {"Petrol": 2, "Diesel": 1, "CNG": 0}
seller_map = {"Dealer": 0, "Individual": 1}
trans_map = {"Manual": 1, "Automatic": 0}

input_data = np.array([[
    year,
    present_price,
    kms,
    fuel_map[fuel_type],
    seller_map[seller_type],
    trans_map[transmission],
    owner
]])

# -----------------------------
# PREDICTION
# -----------------------------
prediction = model.predict(input_data)[0]

# -----------------------------
# RESULT CARD
# -----------------------------
st.markdown('<div class="glass">', unsafe_allow_html=True)

st.subheader("📊 Prediction Result")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🚗 Predicted Price", f"₹ {prediction:.2f} Lakhs")

with col2:
    st.metric("📉 Depreciation", f"{(2025 - year) * 5}%")

with col3:
    st.metric("⚡ Model", "Random Forest AI")

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# FEATURE IMPORTANCE
# -----------------------------
st.markdown('<div class="glass">', unsafe_allow_html=True)

st.subheader("🔥 Feature Importance")

features = ["Year", "Price", "KMs", "Fuel", "Seller", "Transmission", "Owner"]
importance = model.feature_importances_

fig, ax = plt.subplots()
sns.barplot(x=importance, y=features, ax=ax)
st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# PRICE RANGE SIMULATION
# -----------------------------
st.markdown('<div class="glass">', unsafe_allow_html=True)

st.subheader("📈 Price Range Forecast")

values = [prediction * 0.85, prediction, prediction * 1.15]
labels = ["Low", "Expected", "High"]

fig2, ax2 = plt.subplots()
ax2.plot(labels, values, marker='o', linewidth=3)
ax2.set_ylabel("Price (Lakhs)")
ax2.set_title("Prediction Range")
st.pyplot(fig2)

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
<div style="text-align:center; color:grey; padding:20px;">
💎 Built as AI SaaS Project | Streamlit + ML + Glassmorphism UI
</div>
""", unsafe_allow_html=True)