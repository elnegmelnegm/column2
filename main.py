import plotly.express as px

data = [
    ('Hydrosphere C18', [1.5, 1.3, 4.4, 1.9, 1.9]),
    ('TSKgel ODS-100V 3m', [1.9, 1, 6, 1.4, 1.8]),
    ('TSKgel ODS-80TM', [2.1, 2.9, 11.1, 4.7, 2.1]),
    ('Xterra RP18', [1, 1.2, 1.7, 1.1, 2.3]),
    ('TSKgel Super-Phenyl', [0.2, 1.9, 1.9, 3.6, 3.9]),
    ('SiliaChrom dt C18', [2.57, 1.01, 1.19, 6.81, 2.03]),
    ('Purospher RP-18 endcapped', [2.4, 1.1, 7.1, 1, 1.7]),
    ('Prevail C18', [2, 1, 23, 2, 2.6]),
    ('SiliaChrom XDB2 C18', [2.8, 1.03, 1.29, 7.3, 2.19]),
    ('Atlantis dC18', [1.7, 1.1, 5.1, 2.4, 1.6]),
    ('ProntoSil 200-5-C18-AQ', [1, 2.2, 3.1, 2.4, 2.1]),
    ('Capcell C18 AQ', [1.8, 1.8, 5.5, 2.1, 1.6]),
    ('Cosmosil 5C18-PAQ', [1.2, 2.2, 2.5, 1.5, 2]),
]

# Extract labels and values
labels, values = zip(*data)

# Create a polar line plot
fig = px.line_polar(
    r=values[0],  # Use the values from the first row
    theta=labels,
    line_close=True,
    range_r=[min(values[0]), max(values[0])],  # Adjust the range based on your data
    title="Your Radar Plot Title"
)

fig.show()
