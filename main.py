import plotly.express as px

data = [0.5, 0.3, 0.4, 0.9, 0.9]

# Create labels for the radar plot
labels = ['Hy', 'CTF', 'CFA', 'TFA', 'BD']

# Repeat the labels for each set of values
theta = labels * len(data)

# Create a polar line plot
fig = px.line_polar(
    r=data * len(labels),  # Repeat the data for each label
    theta=theta,
    line_close=True,
    range_r=[0, 1.0],  # Adjust the range based on your data
    title="Your Radar Plot Title"
)

fig.show()
