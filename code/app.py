import streamlit as st
import pandas as pd

# load data
data = pd.read_csv('data/trained_data.csv')
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

# get user height
feet = st.number_input("Feet", min_value=4, max_value=7, step=1, value=5)
inches = st.number_input("Inches", min_value=0, max_value=11, step=1, value=8)

size = None
if st.button("Find my size"):
    size = height_to_size(feet, inches)
    st.success(f"Your frame size is likely: **{size}**")

if size is None:
    pass

# get user discipline type and riding style
disciplines = sorted(df['Discipline'].dropna().unique().tolist())
styles = sorted(df['Riding Style'].dropna().unique().tolist())

discipline = st.selectbox("Select discipline", disciplines if disciplines else ["Trail"])
style = st.selectbox("Select riding style", styles if styles else ["Balanced", "Aggressive", "Playful"])

# recommend bikes based on user input
if st.button("Find bikes"):
    # if size wasn't computed yet, compute it now
    if size is None:
        size = height_to_size(feet, inches)

    st.write(f"Looking for **{discipline}** bikes, size **{size}**, style **{style}**…")
    results = find_bikes(df, discipline, size, style)

    if results.empty:
        st.warning("No exact matches found. Try another style or discipline, or broaden size.")
        alt = df[(df['Discipline'] == discipline) & (df['Frame Size'] == size)]
        if not alt.empty:
            st.info("Closest matches (same size + discipline, any style):")
            st.dataframe(alt.head(50))
    else:
        st.success(f"Found {len(results)} bikes:")
        st.dataframe(results.head(50))  # show first 50 for speed
