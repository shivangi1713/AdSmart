import pandas as pd
import random

# Sample categories and genders
categories = ["Tech", "Fashion", "Gaming", "Health", "Travel", "Education", "Finance", "Food", "Sports", "Entertainment"]
genders = ["Male", "Female"]

# Generate sample data
data = {
    "ad_id": [100 + i for i in range(1, 51)],
    "user_id": [i for i in range(1, 51)],
    "age": [random.randint(18, 50) for _ in range(50)],
    "gender": [random.choice(genders) for _ in range(50)],
    "ad_category": [random.choice(categories) for _ in range(50)],
    "clicked": [random.randint(0, 1) for _ in range(50)]
}

# Create DataFrame and save to CSV
df_50 = pd.DataFrame(data)
csv_path_50 = "/mnt/data/sample_ads_50.csv"
df_50.to_csv(csv_path_50, index=False)

csv_path_50
