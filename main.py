import plotly.express as px

data = [
    [0.5, 0.3, 0.4, 0.9, 0.9],
    [0.9, 0.1, 0.7, 0.4, 0.8],
]

# Create labels for the radar plot
labels = ['Hy', 'CTF', 'CFA', 'TFA', 'BD']

# Flatten the data for plotting
flat_data = [value for sublist in data for value in sublist]

# Repeat the labels for each set of values
labels *= len(data)

# Repeat the labels for each set of values
fig = px.line_polar(
    r=flat_data,
    theta=labels,
    line_close=True,
    range_r=[0, 1.0],
    title="Your Radar Plot Title"
)

fig.show()
