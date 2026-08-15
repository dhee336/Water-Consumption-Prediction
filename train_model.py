import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

# Set seed for same results every time
np.random.seed(42)

# Create dataset
print("Creating dataset...")
rows = []

# Generate 300 data samples
for i in range(300):
    # Random values for each household
    family_members = np.random.randint(1, 8)  # 1 to 7 members
    bathrooms = np.random.randint(1, 4)       # 1 to 3 bathrooms
    washing_machine = np.random.randint(0, 2) # 0 or 1
    garden = np.random.randint(0, 2)          # 0 or 1
    
    # Calculate water usage
    water = (120 * family_members) + (25 * bathrooms) + (50 * washing_machine) + (80 * garden) + np.random.randint(-20, 21)
    
    # Store in list
    row = {
        "Family_Members": family_members,
        "Bathrooms": bathrooms,
        "Washing_Machine": washing_machine,
        "Garden": garden,
        "Daily_Water_Usage": water
    }
    rows.append(row)

# Convert to dataframe and save
data = pd.DataFrame(rows)
data.to_csv("water_dataset.csv", index=False)

print("Dataset created!")
print(f"Total rows: {len(data)}")

# Split data into training (80%) and testing (20%)
print("\nSplitting data...")
features = data[["Family_Members", "Bathrooms", "Washing_Machine", "Garden"]]
target = data["Daily_Water_Usage"]

x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

print(f"Training samples: {len(x_train)}")
print(f"Testing samples: {len(x_test)}")

# Train the model
print("\nTraining model...")
model = LinearRegression()
model.fit(x_train, y_train)

# Test the model
print("Testing model...")
predictions = model.predict(x_test)
accuracy = r2_score(y_test, predictions)
error = mean_absolute_error(y_test, predictions)

# Show results
print("\n" + "="*40)
print("MODEL PERFORMANCE")
print("="*40)
print(f"Accuracy: {accuracy:.4f}")
print(f"Average Error: {error:.2f} litres")
print("\nWhat the model learned:")
print(f"  Family Members: {model.coef_[0]:.2f} litres per member")
print(f"  Bathrooms: {model.coef_[1]:.2f} litres per bathroom")
print(f"  Washing Machine: {model.coef_[2]:.2f} litres")
print(f"  Garden: {model.coef_[3]:.2f} litres")
print("="*40)

# Save the model
print("\nSaving model...")
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Done! Model saved as 'model.pkl'")
