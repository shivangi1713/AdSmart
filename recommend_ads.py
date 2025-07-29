import pandas as pd
import joblib

# Load trained model
model = joblib.load("ctr_model.pkl")

# Load new ad-user features for prediction (sample data for testing)
new_data = pd.read_csv("new_ads.csv")  # you’ll create this next

# Predict CTR probabilities
ctr_probs = model.predict_proba(new_data)[:, 1]  # Get probability for class '1'

# Attach CTR score to data
new_data["Predicted_CTR"] = ctr_probs

# Sort ads by highest predicted CTR
recommended_ads = new_data.sort_values(by="Predicted_CTR", ascending=False)

# Display top 5 ads
print("🎯 Top 5 Recommended Ads based on CTR:\n")
print(recommended_ads.head(5))
