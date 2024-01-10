import streamlit as st
import plotly.express as px

def main():
    st.title("Streamlit Radar Plot")

    data = [
        [0.5, 0.3, 0.4, 0.9, 0.9],
        [0.9, 0.1, 0.7, 0.4, 0.8],
    ]

    labels = ['Hy', 'CTF', 'CFA', 'TFA', 'BD']

    # Add a multiselect widget for choosing lines
    selected_lines = st.multiselect('Select lines to display:', ['Line A', 'Line B'])

    if not selected_lines:
        st.warning("Please select at least one line.")
        return

    # Filter data based on user selection
    filtered_data = []
    for i, label in enumerate(['Line A', 'Line B']):
        if label in selected_lines:
            filtered_data.extend(data[i])

    if not filtered_data:
        st.warning("No data available for the selected lines.")
        return

    try:
        # Repeat labels for each selected line
        theta_values = labels * len(selected_lines)

        fig = px.line_polar(
            r=filtered_data,
            theta=theta_values,
            line_close=True,
            range_r=[0, 1.0],
            title=f"Selected Lines: {', '.join(selected_lines)}"
        )

        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
