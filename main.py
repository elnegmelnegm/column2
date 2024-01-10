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

    # Add a selectbox for choosing lines
    selected_lines = st.multiselect('Select lines to display:', ['Line A', 'Line B', 'Both'])

    if 'Line A' in selected_lines and 'Line B' not in selected_lines:
        fig = px.line_polar(
            r=data[0],
            theta=labels,
            line_close=True,
            range_r=[0, 1.0],
            title="Line A"
        )
        st.plotly_chart(fig)
    elif 'Line B' in selected_lines and 'Line A' not in selected_lines:
        fig = px.line_polar(
            r=data[1],
            theta=labels,
            line_close=True,
            range_r=[0, 1.0],
            title="Line B"
        )
        st.plotly_chart(fig)
    elif 'Both' in selected_lines:
        fig = px.line_polar(
            r=data,
            theta=labels,
            line_close=True,
            range_r=[0, 1.0],
            title="Both Lines"
        )
        st.plotly_chart(fig)

if __name__ == '__main__':
    main()
