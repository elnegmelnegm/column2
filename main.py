import streamlit as st
import plotly.express as px

def main():
    st.title("Streamlit Radar Plot")

    data = [
        [0.5, 0.3, 0.4, 0.9, 0.9],
        [0.9, 0.1, 0.7, 0.4, 0.8],
    ]

    labels = ['Hy', 'CTF', 'CFA', 'TFA', 'BD']
    flat_data = [value for sublist in data for value in sublist]
    labels *= len(data)

    fig = px.line_polar(
        r=flat_data,
        theta=labels,
        line_close=True,
        range_r=[0, 1.0],
        title="Your Radar Plot Title"
    )

    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
