import os
import pandas as pd
from train import train_model
from predict import predict_compatible_breeds

def main():
    # Check if model is already trained
    model_path = 'cow_breed_model.pkl'
    csv_path = 'cow_breeds.csv'
    
    # Load data
    if not os.path.exists(csv_path):
        print(f"Error: Dataset file '{csv_path}' not found.")
        return
    
    data = pd.read_csv(csv_path)
    
    # Train model if not already trained or if we want to retrain
    if not os.path.exists(model_path) or os.path.getmtime(csv_path) > os.path.getmtime(model_path):
        print("Training model...")
        train_model(data, model_path)
    
    # Get user input
    available_breeds = set(data['breed_a'].unique()) | set(data['breed_b'].unique())
    print("\nAvailable cow breeds:", ", ".join(sorted(available_breeds)))
    
    while True:
        breed_input = input("\nEnter a cow breed (or 'q' to quit): ").strip()
        
        if breed_input.lower() == 'q':
            print("Exiting program. Goodbye!")
            break
            
        if breed_input not in available_breeds:
            print(f"Breed '{breed_input}' not found in the dataset. Please choose from the available breeds.")
            continue
        
        # Predict compatible breeds
        compatible_breeds = predict_compatible_breeds(breed_input, data, model_path)
        
        # Filter to ensure uniqueness
        seen_breeds = set()
        unique_compatible_breeds = []
        
        for breed, score, notes in compatible_breeds:
            if breed not in seen_breeds:
                seen_breeds.add(breed)
                unique_compatible_breeds.append((breed, score, notes))
        
        # Display results
        if unique_compatible_breeds:
            print(f"\nRecommended compatible breeds for {breed_input}:")
            for breed, score, notes in unique_compatible_breeds:
                print(f"- {breed} (Compatibility Score: {score:.2f})")
                print(f"  Notes: {notes}")
                print()  # Empty line for better readability
        else:
            print(f"No compatible breeds found for {breed_input}.")

if __name__ == "__main__":
    main()