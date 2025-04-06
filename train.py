import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

def train_model(data, model_path):
    """
    Train a simple model based on compatibility scores.
    This is not actually machine learning but a data processing step 
    that converts the data into a usable format for our predictions.
    Now includes notes for each breed combination.
    """
    # Create a dictionary to store all breed relationships
    breed_compatibility = {}
    
    # Process each row of data
    for _, row in data.iterrows():
        breed_a = row['breed_a']
        breed_b = row['breed_b']
        score = row['compatibility_score']
        recommended = row['recommended']
        notes = row['notes']
        
        # Only include recommended combinations
        if recommended.lower() == 'yes':
            # Add bidirectional relationships with notes
            if breed_a not in breed_compatibility:
                breed_compatibility[breed_a] = []
            breed_compatibility[breed_a].append((breed_b, score, notes))
            
            if breed_b not in breed_compatibility:
                breed_compatibility[breed_b] = []
            breed_compatibility[breed_b].append((breed_a, score, notes))
    
    # Save the model (dictionary) to a file
    with open(model_path, 'wb') as f:
        pickle.dump(breed_compatibility, f)
    
    print(f"Model trained and saved to {model_path}")
    return breed_compatibility