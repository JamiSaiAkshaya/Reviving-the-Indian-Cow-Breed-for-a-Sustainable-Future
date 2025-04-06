import pickle

def predict_compatible_breeds(input_breed, data, model_path):
    """
    Predict compatible breeds based on the input breed.
    Returns a list of (breed, compatibility_score, notes) tuples sorted by score.
    Now includes notes from the original dataset.
    """
    try:
        # Load the model
        with open(model_path, 'rb') as f:
            breed_compatibility = pickle.load(f)
        
        # Check if the breed exists in our model
        if input_breed in breed_compatibility:
            # Get compatible breeds and sort by compatibility score in descending order
            compatible_breeds = breed_compatibility[input_breed]
            compatible_breeds.sort(key=lambda x: x[1], reverse=True)
            return compatible_breeds
        else:
            return []
            
    except Exception as e:
        print(f"Error in prediction: {e}")
        return []