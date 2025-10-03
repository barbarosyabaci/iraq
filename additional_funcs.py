def create_sectors(sector_length,sites_df):
    import math
    import pandas as pd
    import pydeck as pdk


    line_length_deg = 0.001 * sector_length  # length of sector line in degrees
    arrow_size = 0.0002 * sector_length  # size of triangle arrowhead

    sector_lines = []
    arrowheads = []
    site_points = []
    line_length_deg = 0.001 * sector_length  # length of sector line in degrees
    arrow_size = 0.0002 * sector_length  # size of triangle arrowhead

    # Unique site points
    site_points = sites_df.groupby("Site ID").first().reset_index()
    site_points = site_points.rename(columns={"Longitude": "lon", "Latitude": "lat","Site ID": "Site_ID"})

    for _, site in sites_df.iterrows():
        lon0, lat0 = site["Longitude"], site["Latitude"]
        azimuth = site["Azimuth"]

        # Line endpoint
        dx = math.sin(math.radians(azimuth)) * line_length_deg
        dy = math.cos(math.radians(azimuth)) * line_length_deg
        lon1, lat1 = lon0 + dx, lat0 + dy

        # Add line
        sector_lines.append({"path": [[lon0, lat0], [lon1, lat1]], "site": site["Site ID"], "cell": site["Cell"], "azimuth": azimuth})

        # Arrowhead as small triangle
        # direction vector
        dx_a = math.sin(math.radians(azimuth))
        dy_a = math.cos(math.radians(azimuth))

        # perpendicular vector (left/right)
        dx_p = math.sin(math.radians(azimuth + 90))
        dy_p = math.cos(math.radians(azimuth + 90))

        # Triangle points
        tip = [lon1, lat1]
        left = [lon1 - dx_a * arrow_size + dx_p * arrow_size / 2, lat1 - dy_a * arrow_size + dy_p * arrow_size / 2]
        right = [lon1 - dx_a * arrow_size - dx_p * arrow_size / 2, lat1 - dy_a * arrow_size - dy_p * arrow_size / 2]

        arrowheads.append({"polygon": [tip, left, right], "site": site["Site ID"], "cell": site["Cell"]})

    sector_df = pd.DataFrame(sector_lines)
    arrow_df = pd.DataFrame(arrowheads)
    sector_layer = pdk.Layer("PathLayer", sector_df, get_path="path", get_color=[200, 0, 0], width_scale=1, width_min_pixels=2, width_units="pixels", pickable=True, )
    arrow_layer = pdk.Layer("PolygonLayer", arrow_df, get_polygon="polygon", get_fill_color=[0, 0, 0], stroked=False, pickable=False)
    site_layer = pdk.Layer("ScatterplotLayer", site_points, get_position=["lon", "lat"], get_color=[255, 0, 0], get_radius=5, radius_units = "pixels", pickable=True)
    label_layer = pdk.Layer("TextLayer", site_points, get_position=["lon", "lat"], get_text="Site_ID", get_size=12, get_color=[0, 0, 0], get_alignment_baseline="'top'")

    return site_layer,sector_layer,arrow_layer,label_layer
def shapely_to_coords(geom):
    # Convert shapely geometry into list of [lon, lat] coordinates
    if geom is None:
        return None
    if geom.geom_type == "Polygon":
        return [list(coord) for coord in geom.exterior.coords]
    elif geom.geom_type == "MultiPolygon":
        # Flatten all polygons (outer rings only)
        polygons = []
        for poly in geom.geoms:
            polygons.append([list(coord) for coord in poly.exterior.coords])
        return polygons
    else:
        return None
def border_read(file):
    import pydeck as pdk
    import geopandas as gpd

    gdf = gpd.read_file(file)
    if gdf.crs and gdf.crs.to_epsg() != 4326:
        gdf = gdf.to_crs(epsg=4326)
    gdf["polygon"] = gdf.geometry.apply(shapely_to_coords)
    data = gdf.drop(columns="geometry")
    # Pydeck layer for district boundary
    gdf_layer = pdk.Layer("PolygonLayer",data, get_polygon="polygon", get_fill_color=[200, 200, 200, 0],  # light transparent fill
        get_line_color=[0, 0, 0],  # black outline
        line_width_min_pixels=1, stroked=True, filled=True, pickable=False)
    return gdf_layer
def get_ind_color_mapping(cell_ids):
    import random
    """Generate a consistent color mapping for all cell IDs"""
    unique_ids = sorted(list(set(cell_ids)))
    color_map = {}

    for cell_id in unique_ids:
        # Generate a random but consistent color for each cell_id
        random.seed(hash(cell_id) % 1000)  # For consistent colors
        color_map[cell_id] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 150  # Alpha channel (transparency)
        ]
    return color_map
def classify_color_RSRP(value):
    if value <= -140:  # Below display limit
        return [0, 0, 0, 0]  # Transparent (effectively not displayed)
    elif value <= -114:  # Very weak signal (-140 dBm to -114 dBm)
        return [0, 0, 0, 180]  # Black
    elif value <= -110:  # Weak signal (-114 dBm to -110 dBm)
        return [255, 0, 0, 180]  # Red
    elif value <= -100:  # Moderate signal (-110 dBm to -100 dBm)
        return [255, 105, 180, 180]  # Pink
    elif value <= -90:  # Good signal (-100 dBm to -90 dBm)
        return [255, 255, 0, 180]  # Yellow
    else:  # Excellent signal (-90 dBm to 0 dBm)
        return [0, 0, 255, 180]  # Blue
def classify_color_traffic_old(value):
    if value < 0.25:
        return [0, 0, 255, 180]  # Blue
    elif value < 0.50:
        return [255, 255, 0, 180]  # Yellow
    elif value < 0.75:
        return [255, 0, 0, 180]  # Red
    else:
        return [0, 0, 0, 180]  # Black
def classify_color_traffic(value):
    if value < 100:
        return [0, 0, 255, 180]  # Blue
    elif value < 500:
        return [255, 255, 0, 180]  # Yellow
    elif value < 5000:
        return [255, 165, 0, 180]  # Orange (RGB: 255,165,0)
    elif value < 40000:
        return [255, 0, 0, 180]  # Red
    else:
        return [0, 0, 0, 180]  # Black
def create_color_legend_traffic():
    def classify(value):
        if value < 100:
            return "#0000FF"  # Blue
        elif value < 500:
            return "#FFFF00"  # Yellow
        elif value < 5000:
            return "#FFA500"  # Orange
        elif value < 40000:
            return "#FF0000"  # Red
        else:
            return "#000000"  # Black

    import streamlit as st
    ranges = [("0 - 100", classify(50)),  # Blue
        ("100 - 500", classify(250)),  # Yellow
        ("500 - 5000", classify(2500)),  # Orange
        ("5000 - 40000", classify(20000)),  # Red
        ("40000 - 400000", classify(100000))  # Black
    ]

    st.write("Value Ranges for Traffic Threshold")
    for label, color_code in ranges:
        st.markdown(f"""
            <div style="display: flex; align-items: center; margin-bottom: 8px;">
                <div style="width: 25px; height: 25px; background-color: {color_code}; 
                           margin-right: 10px; border: 1px solid #ddd; border-radius: 3px;"></div>
                <span style="font-size: 0.95em;">{label}</span>
            </div>
            """, unsafe_allow_html=True)
def grid_read(file,color_opt):
    import geopandas as gpd
    import pydeck as pdk

    # grid_gdf = gpd.read_file(file)
    grid_gdf = gpd.read_file(file, engine='pyogrio', use_arrow=True)
    # Convert CRS to WGS84 for pydeck
    if grid_gdf.crs != "EPSG:4326":
        grid_gdf = grid_gdf.to_crs("EPSG:4326")

    if color_opt == 1:
        color_map = get_ind_color_mapping(grid_gdf["Cell_ID"])
        grid_gdf["color"] = grid_gdf["Cell_ID"].map(color_map)
    elif color_opt == 2:
        grid_gdf["color"] = grid_gdf["RSRP_dBm_num___mean"].apply(classify_color_RSRP)
    elif color_opt == 3:
        grid_gdf["color"] = grid_gdf["_mean"].apply(classify_color_RSRP)
    elif color_opt == 4:
        grid_gdf["color"] = grid_gdf["_mean"].apply(classify_color_traffic_old)
    elif color_opt == 5:
        grid_gdf["color"] = grid_gdf["RSRP_pred"].apply(classify_color_RSRP)
    elif color_opt == 6:
        grid_gdf["color"] = grid_gdf["RSRP_dBm_mean"].apply(classify_color_RSRP)
    elif color_opt == 7:
        grid_gdf["color"] = grid_gdf["_mean"].apply(classify_color_traffic)
    else:
        grid_gdf["color"] = 0

    grid_gdf["coords"] = grid_gdf["geometry"].apply(lambda geom: list(geom.exterior.coords))
    grid_layer = pdk.Layer("PolygonLayer", grid_gdf, get_polygon="coords", get_fill_color="color", pickable=True, filled=True, stroked=False,opacity=0.5, get_line_color=[0,0, 0], line_width_min_pixels=1)
    return grid_layer
def create_signal_strength_legend():
    import streamlit as st

    def classify_color(value):
        if value <= -140:  # Below display limit
            return [0, 0, 0, 0]  # Transparent
        elif value <= -114:  # Very weak signal (-140 dBm to -114 dBm)
            return [0, 0, 0, 180]  # Black
        elif value <= -110:  # Weak signal (-114 dBm to -110 dBm)
            return [255, 0, 0, 180]  # Red
        elif value <= -100:  # Moderate signal (-110 dBm to -100 dBm)
            return [255, 105, 180, 180]  # Pink
        elif value <= -90:  # Good signal (-100 dBm to -90 dBm)
            return [255, 255, 0, 180]  # Yellow
        else:  # Excellent signal (-90 dBm to 0 dBm)
            return [0, 0, 255, 180]  # Blue

    # Convert RGBA list to hex color
    def rgba_to_hex(rgba):
        r, g, b, a = rgba
        return f"#{r:02x}{g:02x}{b:02x}"

    # Define signal strength ranges with representative values
    ranges = [("Below -140 dBm (No signal)", classify_color(-150)), ("-140 to -114 dBm (Very weak)", classify_color(-120)), ("-114 to -110 dBm (Weak)", classify_color(-112)), ("-110 to -100 dBm (Moderate)", classify_color(-105)), ("-100 to -90 dBm (Good)", classify_color(-95)), ("-90 to 0 dBm (Excellent)", classify_color(-45))]

    st.write("Signal Strength Legend (dBm)")
    for label, color_rgba in ranges:
        # Skip transparent entries (alpha = 0)
        if color_rgba[3] == 0:
            continue

        color_hex = rgba_to_hex(color_rgba)

        st.markdown(f"""
            <div style="display: flex; align-items: center; margin-bottom: 8px;">
                <div style="width: 25px; height: 25px; background-color: {color_hex}; 
                           margin-right: 10px; border: 1px solid #ddd; border-radius: 3px; 
                           opacity: {color_rgba[3] / 255};"></div>
                <span style="font-size: 0.95em;">{label}</span>
            </div>
            """, unsafe_allow_html=True)
def filter_centroids_kdtree(centroids_df, site_db, distance_km=1):
    from scipy.spatial import KDTree
    import numpy as np
    """
    Faster version using KDTree for large datasets
    """
    # Convert degrees to radians for accurate distance calculation
    centroids_rad = np.radians(centroids_df[['lat', 'lon']].values)
    sites_rad = np.radians(site_db[['Latitude', 'Longitude']].values)

    # Build KDTree with sites
    tree = KDTree(sites_rad)

    # Query all centroids against sites
    # Earth radius in km
    earth_radius_km = 6371
    distances, _ = tree.query(centroids_rad, k=1, distance_upper_bound=distance_km / earth_radius_km)

    # Keep centroids where the minimum distance is greater than threshold
    # (distances will be infinity if no site is within the threshold)
    mask = distances > (distance_km / earth_radius_km)

    return centroids_df[mask]
def add_nearest_sites_traffic(centroids_df, site_db, traffic_column="Average of Total_Traffic_GB(Daily)"):
    import numpy as np
    from scipy.spatial import KDTree
    """
    Add average traffic from nearest 3 sites to each centroid point

    Parameters:
    centroids_df: DataFrame with columns 'lon' and 'lat'
    site_db: DataFrame with columns 'Longitude', 'Latitude', and traffic_column
    traffic_column: Name of the traffic column in site_db

    Returns:
    centroids_df with new column containing average traffic from nearest 3 sites
    """
    # Convert coordinates to numpy arrays
    centroids_coords = np.radians(centroids_df[['lat', 'lon']].values)
    sites_coords = np.radians(site_db[['Latitude', 'Longitude']].values)

    # Build KDTree with sites
    tree = KDTree(sites_coords)

    # Find nearest 9 cells for each centroid
    distances, indices = tree.query(centroids_coords, k=min(9, len(site_db)))

    # Calculate average traffic for nearest sites
    avg_traffic_list = []

    for i in range(len(centroids_df)):
        # Get indices of nearest sites
        nearest_indices = indices[i]

        # Handle case where there are fewer than 3 sites
        valid_indices = nearest_indices[nearest_indices < len(site_db)]

        if len(valid_indices) > 0:
            # Get traffic values from nearest sites
            traffic_values = site_db.iloc[valid_indices][traffic_column].values
            # Calculate average
            avg_traffic = np.mean(traffic_values*3)
        else:
            avg_traffic = 0  # or np.nan if you prefer

        avg_traffic_list.append(avg_traffic)

    # Add the new column to centroids_df
    centroids_df[traffic_column] = avg_traffic_list

    return centroids_df
def remove_points_near_existing_sites(candidates_df, existing_sites_df, min_distance_km=1):
    import numpy as np
    from sklearn.neighbors import BallTree
    import pandas as pd
    """
    Remove candidate points that are too close to existing sites

    Parameters:
    candidates_df: DataFrame with candidate site data (must have 'lon', 'lat' columns)
    existing_sites_df: DataFrame with existing site data (must have 'lon', 'lat' columns)
    min_distance_km: Minimum required distance from existing sites (default: 2km)

    Returns:
    Filtered candidates_df with points too close to existing sites removed
    """
    existing_sites_df = existing_sites_df.rename(columns={"Longitude": "lon", "Latitude": "lat", "Site ID": "Site_ID"})

    if len(candidates_df) == 0 or len(existing_sites_df) == 0:
        return candidates_df

    # Convert to radians for haversine distance calculation
    candidates_coords = np.radians(candidates_df[['lat', 'lon']].values)
    existing_coords = np.radians(existing_sites_df[['lat', 'lon']].values)

    # Create BallTree for efficient distance calculations
    tree = BallTree(existing_coords, metric='haversine')

    # Find distance to nearest existing site for each candidate
    distances, indices = tree.query(candidates_coords, k=1)

    # Convert radians to kilometers (earth radius = 6371 km)
    distances_km = distances * 6371

    # Filter candidates that are at least min_distance_km away from any existing site
    valid_mask = distances_km.flatten() >= min_distance_km

    # Add distance information to the dataframe (optional)
    candidates_df = candidates_df.copy()
    candidates_df['distance_to_nearest_site_km'] = distances_km.flatten()
    candidates_df['nearest_site_id'] = existing_sites_df.iloc[indices.flatten()].index.values

    print(f"Removed {len(candidates_df) - valid_mask.sum()} candidates within {min_distance_km}km of existing sites")
    print(f"Remaining candidates: {valid_mask.sum()}")

    return candidates_df[valid_mask]
def move_centroids_to_hotspots_closest_selection(centroids_df, hotspots_df, max_distance_km=1.5,lon_col='lon', lat_col='lat'):
    import numpy as np
    import pandas as pd

    def haversine_distance(lat1, lon1, lat2, lon2):
        # Convert decimal degrees to radians
        lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
        c = 2 * np.arcsin(np.sqrt(a))
        r = 6371  # Earth radius in km
        return c * r

    moved_centroids = centroids_df.copy()
    moved_centroids["priority"] = 2  # default = not moved

    # Iterate through centroids
    for i, row in moved_centroids.iterrows():
        lat_c, lon_c = row[lat_col], row[lon_col]

        # Compute distances to all hotspots
        dists = hotspots_df.apply(
            lambda h: haversine_distance(lat_c, lon_c, h[lat_col], h[lon_col]), axis=1
        )

        min_dist = dists.min()
        if min_dist <= max_distance_km:
            # Snap centroid to closest hotspot
            closest_idx = dists.idxmin()
            moved_centroids.at[i, lat_col] = hotspots_df.at[closest_idx, lat_col]
            moved_centroids.at[i, lon_col] = hotspots_df.at[closest_idx, lon_col]
            moved_centroids.at[i, "priority"] = 1  # mark as moved

    return moved_centroids
def haversine_distance(lat1, lon1, lat2, lon2):
    import numpy as np
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6371  # Radius of earth in kilometers
    return c * r
def remove_close_points(filtered_centroids_all, min_distance_km=1.5, lon_col='lon', lat_col='lat', priority_col='priority'):
    import pandas as pd
    import numpy as np

    df = filtered_centroids_all.copy().reset_index(drop=True)

    # Sort by priority ascending so low priority survives (high gets deleted)
    df = df.sort_values(by=priority_col, ascending=True).reset_index(drop=True)

    to_keep = []
    removed = set()

    for i in range(len(df)):
        if i in removed:
            continue
        to_keep.append(i)
        lat1, lon1 = df.loc[i, [lat_col, lon_col]]
        # Compare with remaining points
        for j in range(i+1, len(df)):
            if j in removed:
                continue
            lat2, lon2 = df.loc[j, [lat_col, lon_col]]
            dist = haversine_distance(lat1, lon1, lat2, lon2)
            if dist < min_distance_km:
                removed.add(j)  # remove higher priority (because list is sorted ascending)

    return df.loc[to_keep].reset_index(drop=True)

