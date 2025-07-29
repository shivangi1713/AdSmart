import streamlit as st
import pandas as pd

# -------------------------------------------
# Set page configuration
# -------------------------------------------
st.set_page_config(
    page_title="AdSmart - Smart Ad Recommender",
    page_icon="📈",
    layout="centered"
)

# -------------------------------------------
# Custom Header
# -------------------------------------------
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>📊 AdSmart</h1>
    <p style='text-align: center; font-size: 18px;'>An AI-based system to recommend the best ads based on CTR and other performance metrics.</p>
    <hr style='border: 1px solid #ccc;'/>
""", unsafe_allow_html=True)

# -------------------------------------------
# Define recommendation function
# -------------------------------------------
def recommend_ads(df):
    if 'CTR' in df.columns:
        df_sorted = df.sort_values(by='CTR', ascending=False)
        return df_sorted
    elif 'ad_id' in df.columns and 'clicked' in df.columns:
        # CTR calculate karo: total clicks per ad / total impressions per ad
        ctr_df = df.groupby('ad_id')['clicked'].agg(['sum', 'count']).reset_index()
        ctr_df['CTR'] = ctr_df['sum'] / ctr_df['count']
        df = df.merge(ctr_df[['ad_id', 'CTR']], on='ad_id', how='left')
        df_sorted = df.sort_values(by='CTR', ascending=False)
        return df_sorted
    else:
        raise ValueError("Missing 'CTR' or necessary columns ('ad_id' and 'clicked') to calculate CTR.")

    
    df_sorted = df.sort_values(by='CTR', ascending=False)
    return df_sorted

# -------------------------------------------
# Create Tabs
# -------------------------------------------
tab1, tab2 = st.tabs(["📤 Upload Data", "📈 View Recommendations"])

# -------------- Tab 1 -----------------------
with tab1:
    st.subheader("Upload Your Ad Data")
    uploaded_file = st.file_uploader("📎 Choose a CSV file", type="csv")

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("✅ File uploaded successfully!")
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"❌ Error reading file: {e}")

# -------------- Tab 2 -----------------------
with tab2:
    st.subheader("Ad Recommendations")

    if uploaded_file is not None:
        try:
            recommendations = recommend_ads(df)
            st.success("🎯 Top 5 Recommended Ads:")
            st.dataframe(recommendations.head(5))
        except Exception as e:
            st.error(f"❌ Error generating recommendations: {e}")
    else:
        st.warning("⚠️ Please upload a file first in the 'Upload Data' tab.")

# -------------------------------------------
# Footer
# -------------------------------------------
st.markdown("""
    <hr/>
    <div style='text-align: center; color: gray; font-size: 14px;'>
        Made with ❤️ by Shivangi | Powered by Streamlit
    </div>
""", unsafe_allow_html=True)
