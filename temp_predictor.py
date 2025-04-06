import joblib
import numpy as np

# Load the trained model
model = joblib.load("animal_temp_model.pkl")

# Animal label encoding (must match training data!)
animal_map = {
    "Dog": 0,
    "Cat": 1,
    "Horse": 2,
    "Cow": 3,
    "Rabbit": 4,
    "Goat": 5
}

print("🐾 Welcome to Animal Temperature Predictor!")
print("Available animals:", ", ".join(animal_map.keys()))

animal_name = input("Enter animal name: ").strip().title()

if animal_name not in animal_map:
    print("❌ Invalid animal! Please choose from:", ", ".join(animal_map.keys()))
    exit()

# Get numeric code for animal
animal_code = animal_map[animal_name]

try:
    heart_rate = float(input("Enter heart rate (e.g., 90): "))
    resp_rate = float(input("Enter respiration rate (e.g., 20): "))
    ambient_temp = float(input("Enter ambient temperature (e.g., 22): "))
except ValueError:
    print("❌ Please enter valid numeric values!")
    exit()

# Create input feature vector
features = np.array([[animal_code, heart_rate, resp_rate, ambient_temp]])

# Make prediction
predicted_temp = model.predict(features)[0]

print(f"\n✅ Predicted Body Temperature for {animal_name}: {predicted_temp:.2f} °C")
