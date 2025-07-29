import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
n_samples = 10000
data = {
    'ad_id': np.random.randint(1000, 1100, n_samples),
    'user_id': np.random.randint(2000, 2100, n_samples),
    'device_type': np.random.choice(['mobile', 'desktop', 'tablet'], n_samples),
    'browser': np.random.choice(['chrome', 'firefox', 'safari', 'edge'], n_samples),
    'hour': np.random.randint(0, 24, n_samples),
    'clicked': np.random.choice([0, 1], n_samples, p=[0.85, 0.15])  # 15% CTR
}

df = pd.DataFrame(data)
df.to_csv('data/ctr_data.csv', index=False)
print("✅ Synthetic CTR dataset saved to data/ctr_data.csv")
