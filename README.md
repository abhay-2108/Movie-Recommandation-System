# 🎬 Movie Recommendation System 🎥

A **Content-Based Movie Recommendation System** built using **Python, Flask, Scikit-learn, and NLP techniques**. It provides personalized movie recommendations based on user input.

---

## 🚀 **Project Overview**
This project helps users **find movies similar to their favorite movies** using **Natural Language Processing (NLP) & Machine Learning (ML)** techniques. It processes movie metadata such as **genres, keywords, cast, and crew** to generate recommendations.

🔹 **Technology Stack:**  
- **Frontend:** HTML, CSS 
- **Backend:** Flask (Python)  
- **Machine Learning:** Scikit-learn, NLP (TF-IDF Vectorization & Cosine Similarity)  
- **Dataset:** TMDB 5000 Movies Dataset  

---

## 📌 **Algorithms & Techniques Used**
### ✅ **1. Data Preprocessing**
- Combined **movies** and **credits** datasets.
- Extracted **genres, keywords, cast, and director** from JSON format.
- Tokenized the **overview** text to improve feature representation.
- Removed **duplicates and missing values**.

### ✅ **2. Feature Engineering**
- Created a **‘tags’** column combining overview, genres, keywords, cast, and crew.
- Applied **Text Normalization**: Lowercased text and removed spaces in words.
- Applied **Stemming** (PorterStemmer) to group similar words.

### ✅ **3. Machine Learning Model**
- **TF-IDF Vectorization** (Max Features: 6000) to convert movie metadata into numerical vectors.
- **Cosine Similarity** to compute the similarity between movies.
- **Difflib Matching** for improved search accuracy.

### ✅ **4. Recommendation Mechanism**
1. **User enters a movie name.**  
2. Finds the **most similar movie title** using **Difflib**.  
3. Uses **Cosine Similarity** to get the top 5 recommended movies.  
4. Displays results with an intuitive **web interface** using Flask.  

---

## 📊 **Model Efficiency**
- **Dataset Size:** 5000 Movies  
- **Vectorization:** TF-IDF (6000 features)  
- **Similarity Score:** Cosine Similarity  
- **Search Accuracy Improvement:** **Difflib Approximate Matching**  
- **Performance:** Works in **real-time** for instant recommendations  

---

## 🛠 **Installation & Setup**
Follow these steps to run the project locally.

### **🔹 1. Clone the Repository**
```sh
git clone https://github.com/abhay-2108/Movie-Recommendation-System.git
cd Movie-Recommendation-System
