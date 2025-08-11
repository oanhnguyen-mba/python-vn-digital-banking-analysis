import pandas as pd
import matplotlib.pyplot as plt
import os

def calculate_cagr(start_value, end_value, periods):
    """
    Calculate the Compound Annual Growth Rate (CAGR).

    Parameters:
    - start_value: initial value (e.g., users in 2019)
    - end_value: final value (e.g., users in 2024)
    - periods: number of years between start and end

    Returns:
    - CAGR as a decimal (e.g., 0.12 for 12%)
    """
    return (end_value / start_value) ** (1 / periods) - 1

# Create the 'deliverables' folder if it doesn't exist
os.makedirs('deliverables', exist_ok=True)

# Load the banking data CSV file
data = pd.read_csv('data/banking_data.csv')

# Calculate CAGR for digital users between 2019 and 2024
data['cagr'] = data.apply(
    lambda row: calculate_cagr(row['digital_users_2019'], row['digital_users_2024'], 5),
    axis=1
)

# Select top 5 banks by number of digital users in 2024
top_banks = data.sort_values(by='digital_users_2024', ascending=False).head(5)

# Plot bar chart of digital users for top 5 banks
plt.figure(figsize=(10, 6))
plt.bar(top_banks['bank_name'], top_banks['digital_users_2024'], color='skyblue')
plt.title('Top 5 Banks by Digital Users in 2024')
plt.xlabel('Bank')
plt.ylabel('Digital Users (Millions)')
plt.tight_layout()
plt.savefig('deliverables/top_banks_bar.png')
plt.close()

# Define a pastel color palette
pastel_colors = ['#AEC6CF', '#FFB347', '#77DD77', '#F49AC2', '#FFD1DC', '#CBAACB', '#FFDAB9', '#B0E0E6', '#D3FFCE', '#FFCCCB']

# Plot pie chart of market share for digital banking users in 2024 with pastel colors
plt.figure(figsize=(8, 8))
plt.pie(
    data['market_share'], 
    labels=data['bank_name'], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=pastel_colors[:len(data)]  # use as many colors as needed
)
plt.title('Market Share of Digital Banking Users in 2024')
plt.tight_layout()
plt.savefig('deliverables/market_share_pie.png')
plt.close()
\newpage
