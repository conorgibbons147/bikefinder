import streamlit as st
import pandas as pd

# load data
data = pd.read_csv('../data/trained_data.csv')
df = pd.DataFrame(data)

# create a function to find bikes based on discipline, frame size, and riding style
def find_bikes(df, discipline, frame_size, style):
    return df[(df['Discipline'] == discipline) &
              (df['Frame Size'] == frame_size) &
              (df['Riding Style'] == style)]

# since the user input will take height in feet and inches, this function will convert it to a bike size based on general height guidelines
def height_to_size(feet, inches):
    height = (feet * 12) + inches
    if height <= 62:
      return 'XS'
    elif height <=66:
      return 'S'
    elif height <=70:
      return 'M'
    elif height <=73:
      return 'L'
    elif height <=76:
      return 'XL'
    else:
      return 'XXL'

st.title('BikeFinder')

# Example: let user input height
feet = st.number_input("Feet", min_value=4, max_value=7, step=1)
inches = st.number_input("Inches", min_value=0, max_value=11, step=1)

if st.button("Find my size"):
    size = height_to_size(feet, inches)
    st.write(f"Your frame size is likely: **{size}**")

    # Filter dataset
    results = df[df['Frame Size'] == size]
    st.dataframe(results)
