import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")
st.balloons()

colom1, colom2 = st.columns(2)

with colom1:
    st.image("images/12.png")

with colom2:
    st.title("Lorem Ipsum")
    content = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Nulla non arcu lacinia neque faucibus fringilla. Vestibulum fermentum
    tortor id mi. Ut enim ad minim veniam, quis nostrud exercitation ullamco
    laboris nisi ut aliquip ex ea commodo consequat. Aliquam erat volutpat.
    Nullam feugiat, turpis at pulvinar vulputate, erat libero tristique tellus,
    nec bibendum odio risus sit amet ante. Lorem ipsum dolor sit amet, consectetuer 
    adipiscing elit. Aliquam in lorem sit amet leo accumsan lacinia. Fusce aliquam 
    vestibulum ipsum."""
    st.info(content)

content2 = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit."""

st.write(content2)


colom3, empty_colom, colom4 = st.columns([1.5, 0.5, 1.5])

dataframe = pd.read_csv("data.csv", sep = ";")

for index, row, in dataframe.iterrows():
    if index % 2 == 0: 
        with colom3:
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/"+row["image"])
            url = row["url"]
            st.write("[Source Code](%s)" % url)
    else:
        with colom4:
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/"+row["image"])
            st.write("[Source Code](https://www.google.cz/?hl=cs)")