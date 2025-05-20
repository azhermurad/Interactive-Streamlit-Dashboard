import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import altair as alt

df = pd.read_csv("dataset/palmerpenguins_extended.csv")
df.dropna(inplace=True) 
st.title("Map-Based Visualization")

# filters
selected_species = st.multiselect("Select Species", df['species'].unique(), default=df['species'].unique())
selected_sex = st.multiselect("Select Sex", df['sex'].unique(), default=df['sex'].unique())
filtered_df = df[(df['species'].isin(selected_species)) & (df['sex'].isin(selected_sex))]

# assign coordinates
species_colors = {"Adelie": "#e41a1c", "Chinstrap": "#377eb8", "Gentoo": "#4daf4a"}
island_coords = {
    "Biscoe": {"lat": -65.5, "lon": -65.5},
    "Dream": {"lat": -64.7, "lon": -64.1},
    "Torgensen": {"lat": -64.8, "lon": -64.2}
}
island_colors = {"Biscoe": [255, 99, 71], "Dream": [30, 144, 255], "Torgensen": [34, 139, 34]}

# simulate coordinates for penguins
def jitter(lat, lon, scale=0.03):
    return lat + np.random.uniform(-scale, scale), lon + np.random.uniform(-scale, scale)

penguins = []
for _, row in filtered_df.iterrows():
    base_lat, base_lon = island_coords[row['island']]['lat'], island_coords[row['island']]['lon']
    lat, lon = jitter(base_lat, base_lon)
    penguins.append({
        "lat": lat, "lon": lon, "species": row['species'], "color": species_colors[row['species']]
    })
penguin_df = pd.DataFrame(penguins)

# island summary
summary = filtered_df.groupby('island').agg(
    total=('species', 'count'),
    Adelie=('species', lambda x: (x == 'Adelie').sum()),
    Chinstrap=('species', lambda x: (x == 'Chinstrap').sum()),
    Gentoo=('species', lambda x: (x == 'Gentoo').sum())
).reset_index()
summary['lat'] = summary['island'].map(lambda x: island_coords[x]['lat'])
summary['lon'] = summary['island'].map(lambda x: island_coords[x]['lon'])
summary['color'] = summary['island'].map(island_colors)

# display individual penguin points on the map
penguin_layer = pdk.Layer(
    "ScatterplotLayer",
    data=penguin_df,
    get_position='[lon, lat]',
    get_fill_color='color',
    get_radius=5000,
    pickable=True
)

# display cluster markers centered on each island
island_layer = pdk.Layer(
    "ScatterplotLayer",
    data=summary,
    get_position='[lon, lat]',
    get_fill_color='color',
    get_radius='total * 1000',
    opacity=0.3,
    pickable=True
)

tooltip = {
    "html": """
        <b>{island}</b><br>
        Total: {total}<br>
        Adelie: {Adelie}<br>
        Chinstrap: {Chinstrap}<br>
        Gentoo: {Gentoo}
    """,
    "style": {"backgroundColor": "black", "color": "white", "fontSize": "13px"}
}

view_state = pdk.ViewState(latitude=-65.0, longitude=-64.8, zoom=3)

st.markdown("<br><br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/dark-v10",
        initial_view_state=view_state,
        layers=[penguin_layer, island_layer],
        tooltip=tooltip
    ))

with col2:
    if filtered_df.empty:
        st.warning("No data matches the selected filters.")
    else:
        bar = alt.Chart(filtered_df).mark_bar().encode(
            x=alt.X("count()", title="Penguin Count"),
            y=alt.Y("island:N", title="Island"),
            color=alt.Color("species:N", scale=alt.Scale(domain=list(species_colors.keys()), range=list(species_colors.values()))),
            tooltip=["species", "island", "count()"]
        ).properties(height=350).interactive()

        st.altair_chart(bar, use_container_width=True)