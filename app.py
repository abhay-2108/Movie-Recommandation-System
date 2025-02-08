from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import difflib

app = Flask(__name__)

# --- Load Data ---
try:
    # Load movies and similarity matrix (ensure these files are in the same directory)
    movies = pickle.load(open("movies.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))
    
    # Convert to DataFrame if necessary
    if not isinstance(movies, pd.DataFrame):
        movies = pd.DataFrame(movies)
    
    # Check for the required column
    if "title" not in movies.columns:
        raise KeyError("The 'title' column is missing in movies.pkl")
    
    # Create a lowercase column for case-insensitive matching
    movies["title_lower"] = movies["title"].str.lower().str.strip()
    print("Movies loaded successfully. Sample titles:", movies["title"].head().tolist())
except Exception as e:
    print(f"Error loading data: {e}")
    movies = pd.DataFrame()
    similarity = None

# --- Recommendation Function ---
def recommend(movie):
    if similarity is None or movies.empty:
        return []
    movie_query = movie.lower().strip()
    # Use difflib to find the closest match in our movie titles
    movie_titles = movies["title_lower"].tolist()
    matches = difflib.get_close_matches(movie_query, movie_titles, n=1, cutoff=0.6)
    
    if not matches:
        print(f"No close match found for '{movie_query}'")
        return []
    
    best_match = matches[0]
    print(f"Input '{movie_query}' matched with '{best_match}'")
    
    try:
        idx = movies[movies["title_lower"] == best_match].index[0]
        # Get (index, similarity) pairs for the matched movie
        distances = sorted(list(enumerate(similarity[idx])), key=lambda x: x[1], reverse=True)
        # Skip the first one (itself) and take the next five recommendations
        recommended_movie_names = [movies.iloc[i[0]].title for i in distances[1:6]]
        print(f"Recommendations for '{movie}': {recommended_movie_names}")
        return recommended_movie_names
    except Exception as e:
        print(f"Error in recommend(): {e}")
        return []

# --- Routes ---
@app.route("/", methods=["GET", "POST"])
def home():
    recommended_movies = []
    movie_name = ""
    if request.method == "POST":
        movie_name = request.form.get("movie")
        if movie_name:
            recommended_movies = recommend(movie_name)
    return render_template("index.html", movie_name=movie_name, recommended_movies=recommended_movies)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    movie_name = data.get("movie", "")
    recommended_movies = recommend(movie_name)
    if not recommended_movies:
        return jsonify({"message": f"No recommendations found for '{movie_name}'"}), 404
    return jsonify({"recommended_movies": recommended_movies})

if __name__ == "__main__":
    app.run(debug=True)
