import math
import pandas as pd
import pydeck as pdk
import streamlit as st
import pyproj
import additional_funcs as adf
import geopandas as gpd
def read_config_file(config_path):
    df = pd.read_csv(config_path) #  sep='\t'
    config_dict = dict(zip(df['Name'], df['File_Name']))

    return config_dict
@st.cache_resource
def get_map_layers(config):
    """Cache the map layers to avoid reloading on every rerun"""

    class CachedLayers:
        def __init__(self, config):
            self.district_layer = adf.border_read(config["District Borders"])
            self.country_layer = adf.border_read(config["Country Borders"])
            self.limits_layer = adf.border_read(config["Analysis borders"])

    return CachedLayers(config)
@st.cache_resource
def get_site_layers(config, sector_length):
    """Cache site layers with sector_length as key"""
    sites_df = pd.read_csv(config["Site Database"])
    return adf.create_sectors(sector_length, sites_df) + (sites_df,)
def agglomerative_cluster(df, lon_col="lon", lat_col="lat", distance_km=1.0):
    from sklearn.cluster import AgglomerativeClustering
    from sklearn.metrics import pairwise_distances
    from haversine import haversine, Unit
    coords = df[[lat_col, lon_col]].values

    # Pairwise haversine distances (km)
    dist_matrix = pairwise_distances(
        coords,
        metric=lambda u, v: haversine(u, v, unit=Unit.KILOMETERS)
    )

    # Agglomerative clustering with complete linkage
    model = AgglomerativeClustering(
        n_clusters=None,
        metric="precomputed",      # ✅ use 'metric' instead of affinity
        linkage="complete",
        distance_threshold=distance_km
    )
    labels = model.fit_predict(dist_matrix)
    df["cluster"] = labels
    return df
def filter_isolated_points(df, lon_col="lon", lat_col="lat", min_dist_m=300):
    import numpy as np
    from sklearn.neighbors import BallTree

    earth_radius = 6371008.8

    # Convert to radians
    coords = np.radians(df[[lat_col, lon_col]].values)

    # BallTree for fast neighbor search (haversine metric)
    tree = BallTree(coords, metric="haversine")

    # Query radius in radians
    radius = min_dist_m / earth_radius

    # Find neighbors
    ind = tree.query_radius(coords, r=radius, count_only=False)

    # Keep only points that have at least 2 entries (itself + ≥1 neighbor)
    mask = [len(neigh) > 1 for neigh in ind]

    return df.loc[mask].reset_index(drop=True)
def dashboard(config):
    import streamlit as st
    st.markdown("---")

    col1, col2, col3,col4,col5 = st.columns(5)
    col3.metric("Planning Area", "Bagerhat")
    col4.metric("Total Area(sqm)", "3,959.11")
    col5.metric("Population", "1.6M")
    col1.metric("Number of Sites", "406")
    col2.metric("Number of Sectors", "1263")

    st.markdown("---")

    col1, col2, col3,col4,col5 = st.columns(5)
    col1.metric("Coverage (%)", "92.3", "+1.2")
    col2.metric("Traffic Load (GB)", "2,345", "-3.5%")
    col3.metric("Population Served", "1.2M", "+4.1%")


    st.markdown("---")

    # --- SUMMARY METRICS ---

    col1, col2, col3,col4 = st.columns(4)

    with col1:
        sector_length = st.slider("Sector length", 1, 30, 5, step=1,key=2)
    with col2:
        map_styles = {'Road': 'road',  # Carto: Emphasizes road networks
            'Light': 'light',  # Carto: Light-themed map
            'Satellite': 'satellite',  # Carto: Free satellite imagery
            'Dark': 'dark',  # Carto: Dark-themed map
            'Light No Labels': 'light_no_labels',  # Carto: Light map without labels
            'Dark No Labels': 'dark_no_labels',  # Carto: Dark map without labels
        }
        selected_style_name = st.selectbox("Select Map Style", options=list(map_styles.keys()), index=0  # Default to 'Road'
        )

        # Get the corresponding map style value
        map_style = map_styles[selected_style_name]
    with col3:
        a = 1
        # quality_threshold = st.slider("Quality threshold", 0.1, 1.0, 0.7, step=0.01)
    with col4:
        a = 1
        # coverage_threshold = st.slider("Coverage threshold", 0.1, 1.0, 0.7, step=0.01)

    layers = get_map_layers(config)

    sites_df = pd.read_csv(config["Site Database"])
    site_layer, sector_layer, arrow_layer, label_layer = adf.create_sectors(sector_length, sites_df)

    # ---- View ----
    view_state = pdk.ViewState(latitude=sites_df["Latitude"].mean(), longitude=sites_df["Longitude"].mean(), zoom=12, pitch=0, )

    # ---- Render ----
    r = pdk.Deck(layers=[sector_layer, arrow_layer, label_layer,layers.district_layer,layers.limits_layer,layers.country_layer],initial_view_state=view_state,map_style=map_style, tooltip={"text": "{site} | {cell} | Azimuth {azimuth}"})
    import streamlit as st
    st.pydeck_chart(r, height=700)
def display_population_map(config):
    import additional_funcs as adf

    col1, col2 = st.columns([5, 1])

    with col2:
        adf.create_color_legend_traffic()

    with col1:
        if st.button('Show traffic raster on map'):

            sector_length = st.slider("Sector length", 1, 30, 5, step=1, key=2)
            import additional_funcs as adf

            sites_df = pd.read_csv(config["Site Database"])

            site_layer, sector_layer, arrow_layer, label_layer = adf.create_sectors(sector_length, sites_df)
            district_layer = adf.border_read(config["District Borders"])
            country_layer = adf.border_read(config["Country Borders"])
            limits_layer = adf.border_read(config["Analysis borders"])
            grid_layer = adf.grid_read(config["Population Raster"], 7)

            view_state = pdk.ViewState(latitude=sites_df["Latitude"].mean(), longitude=sites_df["Longitude"].mean(), zoom=12, pitch=0, )

            # --- Deck ---
            r = pdk.Deck(
                layers=[grid_layer,district_layer,sector_layer,site_layer,arrow_layer],
                initial_view_state=view_state,
                map_style="road",
                tooltip={"text": "{site} | {cell} | Azimuth {azimuth}"}
            )
            st.title("Clutter-Weighted Population Raster Display")
            st.pydeck_chart(r, height=700)
def display_pred(config):
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        sector_length = st.slider("Sector length", 1, 30, 5, step=1)
    with col2:
        grid_size = st.slider("Grid Size", 10, 500, 200, step=10)

    if st.button('RSRP Prediction analysis'):
        # Get border layers (cached)
        layers = get_map_layers(config)
        site_layer, sector_layer, arrow_layer, label_layer, sites_df = get_site_layers(config, sector_length)
        grid_layer = adf.grid_read(config["RSRP Prediction"], 5)
        view_state = pdk.ViewState(latitude=sites_df["Latitude"].mean(), longitude=sites_df["Longitude"].mean(), zoom=12, pitch=0, )

        col1, col2 = st.columns([5, 1])
        with col2:
            adf.create_signal_strength_legend()
        with col1:
            r = pdk.Deck(layers=[arrow_layer, grid_layer,sector_layer,label_layer], initial_view_state=view_state, map_style="road",tooltip={"text": "{site} | {cell} | Azimuth {azimuth}"})
            st.title("RSRP Prediction analysis")
            st.pydeck_chart(r, height=700)
def traffic_load(config):
    import streamlit as st
    st.markdown("---")

    col1,col2,col3,col4 = st.columns(4)
    with col1:
        sector_length = st.slider("Sector length", 1, 30, 5, step=1,key="traffic_load")
    with col2:
        grid_size = st.slider("Grid Size", 10, 500, 200, step=10,key ="traffic load")

    HT_sites_df = pd.read_csv(config["HT sites"])
    HT_sites_df = HT_sites_df.rename(columns={"Site_ID": "Site ID"})
    HT_site_layer = adf.create_sectors(sector_length,HT_sites_df)[0]

    layers = get_map_layers(config)
    site_layer, sector_layer, arrow_layer, label_layer, sites_df = get_site_layers(config, sector_length)
    grid_layer = adf.grid_read(config["HT sites Grid"],1)

    view_state = pdk.ViewState(latitude=sites_df["Latitude"].mean(), longitude=sites_df["Longitude"].mean(), zoom=12, pitch=0, )

    r = pdk.Deck(layers=[layers.country_layer, grid_layer,layers.limits_layer,sector_layer,arrow_layer,label_layer,layers.district_layer,HT_site_layer],initial_view_state=view_state,map_style="road", tooltip={"text": "Cell ID: {Cell_Id}"})
    import streamlit as st
    st.pydeck_chart(r, height=700)
def recommendation_engine_v3(config):
    import ast

    if st.button('Recalculate New Site Recommendations Center Points'):

        # --- Load grid file ---
        path = r"C:\Users\barba\Documents\01_Job\2025_Predictive_Tool\Geodata\Bagerhat_RSRP TAB"
        file = r"\Bagerhat_RSRP_Field_Meas_points_extent_110_10.csv"
        df_FM = pd.read_csv(path+file)
        # transformer = pyproj.Transformer.from_crs("EPSG:32646", "EPSG:4326", always_xy=True)

        # Transform X, Y to lon, lat
        # df_FM[["lon", "lat"]] = df_FM.apply(lambda row: transformer.transform(row["X"], row["Y"]), axis=1, result_type="expand")
        df_FM = df_FM.rename(columns={"X": "lon", "Y": "lat"})

        from datetime import datetime
        print("process started: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        # Select relevant columns (no filter applied)
        # df_FM_points = df_FM[["id", "lon", "lat", "RSRP_dBm_num___mean", "Sampling_Points_num__mean", "KPI_RSRP_dBm_num___mean"]]
        df_FM_points = df_FM

        view_state = pdk.ViewState(latitude=df_FM_points["lat"].mean(), longitude=df_FM_points["lon"].mean(), zoom=10)

        import numpy as np
        # Assuming df is your dataframe with lon/lat
        df_filtered = filter_isolated_points(df_FM, lon_col="lon", lat_col="lat", min_dist_m=300)
        print("agg_cluster started: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        df_clustered = agglomerative_cluster(df_filtered, lon_col="lon", lat_col="lat")
        print("agg_cluster finished: " +datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        df_clustered = df_clustered[df_clustered['cluster'].isin(df_clustered['cluster'].value_counts()[lambda x: x >= 5].index)]
        print("centroids clusters started: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        centroids_df_pre = df_clustered.groupby("cluster").agg(lon=("lon", "mean"), lat=("lat", "mean"), Sampling_Points=("Sampling_Points", "sum"), num_points=("cluster", "count")).reset_index()
        print("centroids finished, agg started: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        centroids_agg_df  = agglomerative_cluster(centroids_df_pre, lon_col="lon", lat_col="lat",distance_km=3)
        print("centroids agg finished, clustering started: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        centroids_df = centroids_agg_df.groupby("cluster").agg(lon=("lon", "mean"), lat=("lat", "mean"), Sampling_Points=("Sampling_Points", "sum"), num_points=("cluster", "count")).reset_index()
        print("centroids agg clustering finished: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print(len(centroids_df))
        # Create a color for each cluster
        print("coloring started: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        unique_clusters = df_clustered["cluster"].unique()
        color_map = {cl: [int(np.random.randint(0, 255)), int(np.random.randint(0, 255)), int(np.random.randint(0, 255))] for cl in unique_clusters}
        print("coloring finished: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        file_sites = r"C:\Users\barba\Documents\01_Job\2025_Predictive_Tool\Site_Data\bagerhat_with_traffic.csv"
        sites_df = pd.read_csv(file_sites)

        centroids_df = adf.add_nearest_sites_traffic(centroids_df, sites_df)
        centroids_df.sort_values("Sampling_Points", ascending=False, inplace=True)

        filtered_centroids_all = adf.filter_centroids_kdtree(centroids_df, sites_df, distance_km=1)
        hotspots_df = pd.read_csv(r"C:\Users\barba\Documents\01_Job\2025_Predictive_Tool\Geodata\bazaar\Hotspots_merged.csv")
        hotspots_df = adf.remove_points_near_existing_sites(hotspots_df,sites_df)
        hotspots_df.to_csv(r"C:\Users\barba\Documents\01_Job\2025_Predictive_Tool\Geodata\bazaar\Hotspots_merged_cleaned.csv")
        filtered_centroids_all = adf.move_centroids_to_hotspots_closest_selection(filtered_centroids_all, hotspots_df, max_distance_km=1.5)

        filtered_centroids_all.insert(0, 'Candidate_ID', ['Rec_' + str(i) for i in range(1, len(filtered_centroids_all) + 1)])

        filtered_centroids_all = adf.remove_close_points(filtered_centroids_all, min_distance_km=1.5, lon_col='lon', lat_col='lat', priority_col='priority')

        # filtered_centroids = filtered_centroids_all.head(50)
        filtered_centroids_all.rename(columns={'Average of Total_Traffic_GB(Daily)': 'Estimated Total Site Traffic GB(Daily)'}, inplace=True)
        # filtered_centroids.insert(0, 'Candidate_ID', ['Rec_' + str(i) for i in range(1, len(filtered_centroids) + 1)])

        filtered_centroids_all = adf.add_nearest_sites_traffic(filtered_centroids_all, sites_df,"Est_cov_pop")

        df_clustered["color"] = df_clustered["cluster"].map(color_map)
        df_clustered.to_csv("C:/Users/barba/Downloads/clustered.csv")
        filtered_centroids_all.to_csv("C:/Users/barba/Downloads/centroids_all.csv")
        # filtered_centroids.to_csv("C:/Users/barba/Downloads/centroids.csv")
        centroids_df_pre.to_csv("C:/Users/barba/Downloads/centroids_pre.csv")
        st.write("Results Generated, ready to display and analysis")

    col1,col2,col3,col4 = st.columns(4)
    with col1:
        iteration = {
            'Last Calculated':config["Last Calculated"],
            '1st': config["1st"],
            '7th': config["7th"]}
        # Create a selection box for map styles
        selected_iteration = st.selectbox("Select Iteration", options=list(iteration.keys()), index=0)  # Default to 'Road'
        file_rec = iteration[selected_iteration]
        filtered_centroids = pd.read_csv(file_rec)
        rec_layer = pdk.Layer("ScatterplotLayer", filtered_centroids, get_position=["lon", "lat"], get_color=[0, 0, 0],  # Red to differentiate
            get_radius=5, radius_units="pixels",  # 30 pixels
            pickable=True)
    with col2:
        sector_length = st.slider("Sector length", 1, 30, 5, step=1,key="rsrp_mes")

    with col3:
        # grid_size = st.slider("Grid Size", 10, 500, 200, step=10,key="rsrp_mes_2")
        zoom = st.slider("Zoom Level", min_value=1, max_value=20, value=12)

        pitch = 0 # st.slider("Pitch Angle", min_value=0, max_value=90, value=0)
    with col4:
        # Create coordinate input field
        sites_df = pd.read_csv(config["Site Database"])
        latitude = sites_df["Latitude"].mean()
        longitude = sites_df["Longitude"].mean()
        default_coords = f"{longitude:.6f},{latitude:.6f}"
        coords_input = st.text_input("Longitude,Latitude", value=default_coords, help="Enter coordinates as: latitude,longitude (e.g., 89.5239,22.6530)")

        coords = [coord.strip() for coord in coords_input.split(",")]

        if len(coords) == 2:
            longitude = float(coords[0])
            latitude= float(coords[1])

    display_layers = {
        "Existing Sites": [ "sector_layer", "label_layer","arrow_layer"],
        "Reference Points": ["ref_layer", "ref_text_layer"],
        "Recommended Sites": ["rec_layer","text_layer"],
        "Hotspot Points": ["hot_layer","hot_points_layer"],
        "Low RSRP Groups": ["group_layer"]}
    selected_categories = st.multiselect(
            "Choose layers to display:",
            options=list(display_layers.keys())
            ,help="Select which visualization layers to display on the map")
    selected_layers = []
    for category in selected_categories:
        selected_layers.extend(display_layers[category])

    if st.button('Display Recommendations Center Points Results'):
        # Load additional data
        hotspots = pd.read_csv(config["Hotspots Database"])
        ref_df = pd.read_csv(config["Reference Sites Database"])
        ref_points = ref_df.rename(columns={"D1 file long": "lon", "D1 file Lat": "lat", "Generic ID": "Site_ID"})
        df_clustered = pd.read_csv(config["Cluster Points Database"])
        df_clustered['color'] = df_clustered['color'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

        layers = get_map_layers(config)
        site_layer, sector_layer, arrow_layer, label_layer, sites_df = get_site_layers(config, sector_length)

        # Define PyDeck layers
        pydeck_layers = {
            "group_layer": pdk.Layer("ScatterplotLayer", df_clustered, get_position=["lon", "lat"], get_color="color", get_radius=30,  # radius_units="pixels",
            pickable=True),
            "hot_layer": pdk.Layer(
                "TextLayer",
                data=hotspots,
                get_position=["lon", "lat"],
                get_text="PLACE_NAME",
                get_size=14,
                get_color=[0, 0, 0],
                get_alignment_baseline="'center'"
            ),
            "hot_points_layer": pdk.Layer(
                "ScatterplotLayer",
                data=hotspots,
                get_position=["lon", "lat"], get_color=[255, 165, 0],  # Orange color to differentiate from other layers
                get_radius=5, radius_units="pixels", pickable=True),
            "district_layer": layers.district_layer, #  adf.border_read(config["District Borders"]),
            "limits_layer": layers.limits_layer, # adf.border_read(config["Analysis borders"]),
            "rec_layer": pdk.Layer(
                "ScatterplotLayer",
                filtered_centroids,
                get_position=["lon", "lat"],
                get_color=[0, 0, 0],
                get_radius=5,
                radius_units="pixels",
                pickable=True
            ),
            "text_layer": pdk.Layer(
                "TextLayer",
                data=filtered_centroids,
                get_position=["lon", "lat"],
                get_text="Candidate_ID",
                get_size=18,
                get_color=[0, 0, 0],
                get_alignment_baseline="'top'"
            ),
            "site_layer": site_layer,
            "sector_layer": sector_layer,
            "arrow_layer": arrow_layer,
            "label_layer": label_layer,
            "ref_layer": pdk.Layer("ScatterplotLayer", ref_points, get_position=["lon", "lat"], get_color=[0, 0, 255], get_radius=7, radius_units="pixels", pickable=True),
            "ref_text_layer": pdk.Layer("TextLayer", data=ref_points, get_position=["lon", "lat"], get_text="Site_ID", get_size=18, get_color=[0, 0, 0], get_alignment_baseline="'top'")
        }

        # Map selected layer names to PyDeck layers
        active_layers = [pydeck_layers[layer_name] for layer_name in selected_layers if layer_name in pydeck_layers]
        # Optionally, add mandatory layers like limits_layer and district_layer
        active_layers += [pydeck_layers.get("limits_layer"), pydeck_layers.get("district_layer")]

        # Set view state
        view_state = pdk.ViewState(
            latitude= latitude, # sites_df["Latitude"].mean(),
            longitude=longitude, # sites_df["Longitude"].mean(),
            zoom=zoom,
            pitch=pitch
        )

        # Create columns for map and legend
        col1, col2 = st.columns([5, 1])
        with col2:
            # adf.create_signal_strength_legend()
            a = 1
        with col1:
            tooltip_1 = {
                "text": (
                    "RSRP: {RSRP_dBm_num___mean} dBm | "
                    "Sampling Points: {Sampling_Points} | "
                    "KPI RSRP: {KPI_RSRP_dBm_num___mean} dBm"
                )
            }
            r = pdk.Deck(
                layers=active_layers,
                initial_view_state=view_state,
                map_style="road",
                tooltip=tooltip_1
            )
            st.title("New Site Recommendations Center Points")
            st.pydeck_chart(r, height=700)
            # st.table(filtered_centroids.sort_values(by='Candidate_ID'))
            filtered_centroids['sort_key'] = filtered_centroids['Candidate_ID'].str.extract('(\d+)').astype(float)

            # Sort by the numeric value
            sorted_centroids = filtered_centroids.sort_values(by='sort_key')

            # Drop the temporary sort key column if you don't want to display it
            sorted_centroids = sorted_centroids.drop('sort_key', axis=1)

            # Display the sorted table
            st.table(sorted_centroids.reset_index(drop=True))
def display_rsrp_data(config):

    col1,col2,col3,col4 = st.columns(4)
    with col1:
        sector_length = st.slider("Sector length", 1, 30, 5, step=1,key="rsrp_mes")
    with col2:
        grid_size = st.slider("Grid Size", 10, 500, 200, step=10,key="rsrp_mes_2")

    if st.button('RSRP Field meas analysis'):

        layers = get_map_layers(config)
        site_layer, sector_layer, arrow_layer, label_layer, sites_df = get_site_layers(config, sector_length)
        grid_layer = adf.grid_read(config["Low RSRP database"], 6)

        view_state = pdk.ViewState(latitude=sites_df["Latitude"].mean(), longitude=sites_df["Longitude"].mean(), zoom=12, pitch=0, )

        col1, col2 = st.columns([5, 1])

        with col2:
            adf.create_signal_strength_legend()
        with col1:
            r = pdk.Deck(layers=[arrow_layer,grid_layer,sector_layer,label_layer,layers.limits_layer,layers.district_layer], initial_view_state=view_state, map_style="road",tooltip={"text": "{site} | {cell} | Azimuth {azimuth}"})
            st.title("RSRP Coverage Analysis")
            st.pydeck_chart(r, height=700)








