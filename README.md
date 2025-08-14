# BikeFinder  

BikeFinder is a small end-to-end project I built to recommend mountain bikes based on a rider’s height, discipline, and riding style. I started with a dataset of bicycle frame geometry (from https://github.com/dorianprill/dataset-bicycle-geometry). After some eda in pandas, I cleaned and standardized the data. This included handling missing values, mapping frame sizes to standard XS-XXL labels, and classifying bike disciplines based on suspension travel.

To make sizing recommendations more data-driven, I used a K-Means clustering algorithm from scikit-learn to group bikes by geometry and validate the frame size categories. With that logic in place, I built a simple but functional Streamlit app where users enter their height, choose their riding discipline and style from dropdowns, and instantly see matching bikes from the dataset.

This project highlights skills in Python, pandas, scikit-learn, and Streamlit, as well as the full workflow of data cleaning, basic machine learning, and building an interactive UI. It was a fun exercise in taking raw, messy data and turning it into something useful that anyone can interact with in their browser.

