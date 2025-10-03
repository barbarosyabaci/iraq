def calculate_zoom_level(lat_diff, lon_diff):
    max_dim = max(lat_diff, lon_diff)
    if max_dim < 0.0001:
        return 21  # Maximum zoom level for very close points
    return min(15, max(1, 11 - (max_dim * 2)))
def interpolate_dataframe(df, group_size=20):
    import pandas as pd
    interpolated_points = {'Latitude': [], 'Longitude': []}

    for i in range(0, len(df), group_size):
        group = df.iloc[i:i + group_size]
        if not group.empty:
            avg_lat = group['Latitude'].mean()
            avg_lng = group['Longitude'].mean()
            interpolated_points['Latitude'].append(avg_lat)
            interpolated_points['Longitude'].append(avg_lng)

    return pd.DataFrame(interpolated_points)
def get_color(value):
    if value < 3:
        return [255, 0, 0]  # Red for low values
    elif value < 5:
        return [255, 165, 0]  # Orange for medium values
    else:
        return [0, 128, 0]  # Green for high values
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
def get_rsrp_color_patches():
    import matplotlib.patches as mpatches
    color_patches_rsrp = [mpatches.Patch(color='#0000FF', label='>= -70 (Blue)'),  # Blue
        mpatches.Patch(color='#00B0F0', label='-70 to -80 (Light Blue)'),  # Light Blue
        mpatches.Patch(color='#00FFFF', label='-80 to -90 (Cyan)'),  # Cyan
        mpatches.Patch(color='#00B050', label='-90 to -100 (Green)'),  # Green
        mpatches.Patch(color='#92D050', label='-100 to -110 (Light Green)'),  # Light Green
        mpatches.Patch(color='#FFFF00', label='-110 to -115 (Yellow)'),  # Yellow
        mpatches.Patch(color='#ED7D31', label='-115 to -120 (Orange)'),  # Orange
        mpatches.Patch(color='#FF0000', label='< -120 (Red)')  # Red
    ]
    return color_patches_rsrp
def get_rsrq_color_patches():
    import matplotlib.patches as mpatches
    color_patches_rsrq = [mpatches.Patch(color='#0000FF', label='>= -6 (Blue)'),  # Blue
        mpatches.Patch(color='#00B0F0', label='-6 to -9 (Light Blue)'),  # Light Blue
        mpatches.Patch(color='#00FFFF', label='-9 to -11 (Cyan)'),  # Cyan
        mpatches.Patch(color='#00B050', label='-11 to -13 (Green)'),  # Green
        mpatches.Patch(color='#92D050', label='-13 to -15 (Light Green)'),  # Light Green
        mpatches.Patch(color='#FFFF00', label='-15 to -17 (Yellow)'),  # Yellow
        mpatches.Patch(color='#ED7D31', label='-17 to -20 (Orange)'),  # Orange
        mpatches.Patch(color='#FF0000', label='< -20 (Red)')  # Red
    ]
    return color_patches_rsrq
def get_sinr_color_patches():
    import matplotlib.patches as mpatches
    color_patches_sinr = [
        mpatches.Patch(color='#0000FF', label='>= 25 (Blue)'),           # Blue
        mpatches.Patch(color='#00B0F0', label='20 to 25 (Light Blue)'),  # Light Blue
        mpatches.Patch(color='#00FFFF', label='15 to 20 (Cyan)'),        # Cyan
        mpatches.Patch(color='#00B050', label='10 to 15 (Green)'),       # Green
        mpatches.Patch(color='#92D050', label='5 to 10 (Light Green)'),  # Light Green
        mpatches.Patch(color='#FFFF00', label='0 to 5 (Yellow)'),        # Yellow
        mpatches.Patch(color='#ED7D31', label='-2 to 0 (Orange)'),       # Orange
        mpatches.Patch(color='#FF0000', label='< -2 (Red)')              # Red
    ]
    return color_patches_sinr
def get_cqi_color_patches():
    import matplotlib.patches as mpatches
    color_patches_cqi = [
        mpatches.Patch(color='#0000FF', label='> 12 (Blue)'),            # Blue
        mpatches.Patch(color='#00B0F0', label='9 to 12 (Light Blue)'),   # Light Blue
        mpatches.Patch(color='#92D050', label='6 to 9 (Light Green)'),   # Light Green
        mpatches.Patch(color='#FFFF00', label='3 to 6 (Yellow)'),        # Yellow
        mpatches.Patch(color='#ED7D31', label='< 3 (Orange)')            # Orange
    ]
    return color_patches_cqi
def get_modulation_color_patches():
    import matplotlib.patches as mpatches
    color_patches_modulation = [
        mpatches.Patch(color='#0000FF', label='256QAM (Blue)'),       # Blue
        mpatches.Patch(color='#00FFFF', label='64QAM (Cyan)'),        # Cyan
        mpatches.Patch(color='#92D050', label='16QAM (Light Green)'), # Light Green
        mpatches.Patch(color='#FFFF00', label='QPSK (Yellow)')        # Yellow
    ]
    return color_patches_modulation
def get_throughput_color_patches():
    import matplotlib.patches as mpatches
    color_patches_throughput = [
        mpatches.Patch(color='#0000FF', label='>500 Mbps (Blue)'),
        mpatches.Patch(color='#00B0F0', label='300 to 500 Mbps (Light Blue)'),
        mpatches.Patch(color='#00FFFF', label='200 to 300 Mbps (Cyan)'),
        mpatches.Patch(color='#00B050', label='100 to 200 Mbps (Green)'),
        mpatches.Patch(color='#92D050', label='50 to 100 Mbps (Light Green)'),
        mpatches.Patch(color='#FFFF00', label='30 to 50 Mbps (Yellow)'),
        mpatches.Patch(color='#ED7D31', label='10 to 30 Mbps (Orange)'),
        mpatches.Patch(color='#FF0000', label='<10 Mbps (Red)')
    ]
    return color_patches_throughput
def get_tech_detail_color_patches():
    import matplotlib.patches as mpatches
    color_patches = [mpatches.Patch(color='#0000FF', label='LTE'),  # Blue
        mpatches.Patch(color='#FF4500', label='EN-DC'),  # OrangeRed
        mpatches.Patch(color='#800000', label='Other')  # Maroon
    ]
    return color_patches
def get_ri_color_patches():
    import matplotlib.patches as mpatches
    color_patches_ri = [
        mpatches.Patch(color='#0000FF', label='Rank 4 (Blue)'),       # Blue
        mpatches.Patch(color='#00FFFF', label='Rank 3 (Cyan)'),       # Cyan
        mpatches.Patch(color='#92D050', label='Rank 2 (Light Green)'),# Light Green
        mpatches.Patch(color='#FFFF00', label='Rank 1 (Yellow)')      # Yellow
    ]
    return color_patches_ri
def categorize_rsrq(value):
    match value:
        case value if value >= -6:
            return [0, 0, 255]    # #0000FF (Blue)
        case value if value >= -9:
            return [0, 176, 240]  # #00B0F0 (Light Blue)
        case value if value >= -11:
            return [0, 255, 255]  # #00FFFF (Cyan)
        case value if value >= -13:
            return [0, 176, 80]   # #00B050 (Green)
        case value if value >= -15:
            return [146, 208, 80] # #92D050 (Light Green)
        case value if value >= -17:
            return [255, 255, 0]  # #FFFF00 (Yellow)
        case value if value >= -20:
            return [237, 125, 49] # #ED7D31 (Orange)
        case value if value < -20:
            return [255, 0, 0]    # #FF0000 (Red)
        case _:
            return [0, 0, 0]      # #000000 (Black)
def categorize_rsrp(value):
    match value:
        case value if value >= -70:
            return [0, 0, 255]    # #0000FF (Blue)
        case value if value >= -80:
            return [0, 176, 240]  # #00B0F0 (Light Blue)
        case value if value >= -90:
            return [0, 255, 255]  # #00FFFF (Cyan)
        case value if value >= -100:
            return [0, 176, 80]   # #00B050 (Green)
        case value if value >= -110:
            return [146, 208, 80] # #92D050 (Light Green)
        case value if value >= -115:
            return [255, 255, 0]  # #FFFF00 (Yellow)
        case value if value >= -120:
            return [237, 125, 49] # #ED7D31 (Orange)
        case value if value < -120:
            return [255, 0, 0]    # #FF0000 (Red)
        case _:
            return [0, 0, 0]      # #000000 (Black)
def categorize_sinr(value):
    match value:
        case value if value >= 25:
            return [0, 0, 255]    # #0000FF (Blue)
        case value if value >= 20:
            return [0, 176, 240]  # #00B0F0 (Light Blue)
        case value if value >= 15:
            return [0, 255, 255]  # #00FFFF (Cyan)
        case value if value >= 10:
            return [0, 176, 80]   # #00B050 (Green)
        case value if value >= 5:
            return [146, 208, 80] # #92D050 (Light Green)
        case value if value >= 0:
            return [255, 255, 0]  # #FFFF00 (Yellow)
        case value if value >= -2:
            return [237, 125, 49] # #ED7D31 (Orange)
        case value if value < -2:
            return [255, 0, 0]    # #FF0000 (Red)
        case _:
            return [0, 0, 0]      # #000000 (Black)
def categorize_cqi(value):
    match value:
        case value if value > 12:
            return [0, 0, 255]    # #0000FF (Blue)
        case value if value >= 9:
            return [0, 176, 240]  # #00B0F0 (Light Blue)
        case value if value >= 6:
            return [146, 208, 80] # #92D050 (Light Green)
        case value if value >= 3:
            return [255, 255, 0]  # #FFFF00 (Yellow)
        case value if value < 3:
            return [237, 125, 49] # #ED7D31 (Orange)
        case _:
            return [0, 0, 0]      # #000000 (Black)
def categorize_modulation(value):
    match value:
        case '256QAM':
            return [0, 0, 255]    # #0000FF (Blue)
        case '64QAM':
            return [0, 255, 255]  # #00FFFF (Cyan)
        case '16QAM':
            return [146, 208, 80] # #92D050 (Light Green)
        case 'QPSK':
            return [255, 255, 0]  # #FFFF00 (Yellow)
        case _:
            return [0, 0, 0]      # #000000 (Black)
def categorize_Technology_Detail(value):
    match value:
        case value if value >= "LTE":
            return [0, 0, 255]  # Blue
        case value if value >= "EN-DC":
            return [255, 69, 0] # OrangeRed
        case _:
            return [128, 0, 0]  # Maroon
def categorize_ri(value):
    match value:
        case 'Rank 4':
            return [0, 0, 255]    # #0000FF (Blue)
        case 'Rank 3':
            return [0, 255, 255]  # #00FFFF (Cyan)
        case 'Rank 2':
            return [146, 208, 80] # #92D050 (Light Green)
        case 'Rank 1':
            return [255, 255, 0]  # #FFFF00 (Yellow)
        case _:
            return [0, 0, 0]      # #000000 (Black)
def plot_color_patches(legend_handles):
    import matplotlib.pyplot as plt
    import streamlit as st
    fig, ax = plt.subplots(figsize=(10, 1))
    ax.legend(handles=legend_handles, loc='upper left')
    ax.axis('off')
    st.pyplot(fig)
def categorize_throughput(value):
    match value:
        case value if value > 500:
            return [0, 0, 255]    # #0000FF (Blue)
        case value if value >= 300:
            return [0, 176, 240]  # #00B0F0 (Light Blue)
        case value if value >= 200:
            return [0, 255, 255]  # #00FFFF (Cyan)
        case value if value >= 100:
            return [0, 176, 80]   # #00B050 (Green)
        case value if value >= 50:
            return [146, 208, 80] # #92D050 (Light Green)
        case value if value >= 30:
            return [255, 255, 0]  # #FFFF00 (Yellow)
        case value if value >= 10:
            return [237, 125, 49] # #ED7D31 (Orange)
        case value if value < 10:
            return [255, 0, 0]    # #FF0000 (Red)
        case _:
            return [0, 0, 0]      # #000000 (Black) for values that do not fit the defined ranges
def process_uploaded_files(uploaded_files):
    import pandas as pd
    dataframes = []
    uploaded_files_names = []

    for uploaded_file in uploaded_files:
        # Read the uploaded file into a DataFrame
        df = pd.read_csv(uploaded_file, low_memory=False)
        # Append the file name to the list
        uploaded_files_names.append(uploaded_file.name)
        # Append the DataFrame to the list
        dataframes.append(df)

    return uploaded_files_names, dataframes
def filter_dataframe_by_ranges(df, col1_range, col2_range, col3_range, col1_name, col2_name, col3_name):
    """
    Filters the dataframe based on the provided ranges for three columns.

    Parameters:
    - df: The dataframe to filter.
    - col1_range: A tuple indicating the (min, max) range for the first column.
    - col2_range: A tuple indicating the (min, max) range for the second column.
    - col3_range: A tuple indicating the (min, max) range for the third column.
    - col1_name: Name of the first column.
    - col2_name: Name of the second column.
    - col3_name: Name of the third column.

    Returns:
    - Filtered dataframe with rows that fall within the specified ranges.
    """
    filtered_df = df[
        (df[col1_name].between(col1_range[0], col1_range[1])) &
        (df[col2_name].between(col2_range[0], col2_range[1])) &
        (df[col3_name].between(col3_range[0], col3_range[1]))
    ]
    return filtered_df
def tooltip_1():
    tooltip_1 = {"text": "MR-DC Cell 1 SINR (dB): {MR-DC Cell 1 SINR (dB)}\n"
                       "NR Serving Cell SS RSRP Top #1: {NR Serving Cell SS RSRP Top #1}\n"
                       "NR Serving Cell SS RSRQ Top #1: {NR Serving Cell SS RSRQ Top #1}\n"
                       "NR Serving Beam 1 NRARFCN DL: {NR Serving Beam 1 NRARFCN DL}\n"
                       "NR Serving Beam 1 Cell Identity: {NR Serving Beam 1 Cell Identity}\n"
                       "NR Serving Beam 1 Band: {NR Serving Beam 1 Band}\n"
                       "NR Serving Beam 1 Bandwidth DL: {NR Serving Beam 1 Bandwidth DL}"},
    return tooltip_1
def parameter_plot(dataframes,parameter,chart_type,uploaded_files_names,lat,lon,zoom_level,color_func,height_pydeck):
    import streamlit as st
    import pydeck as pdk
    i=0
    for df_pre in dataframes:
        sel_columns = ["Date Time", "Latitude", "Longitude", parameter, "NR Serving Beam 1 NRARFCN DL", "NR Serving Beam 1 Cell Identity", "NR Serving Beam 1 Band", "NR Serving Beam 1 Bandwidth DL", ]
        data_list = ["NR Serving Cell SS RSRQ Top #1",
        "NR Serving Cell SS RSRP Top #1",
        "MR-DC Cell 1 SINR (dB)",
        "NR MAC DL Throughput Total (kbps)",
        "LTE Serving Cell RSRQ (dB)",
        "LTE Serving Cell RSRP (dBm)",
        "LTE Serving Cell RS SINR (dB)",
        "LTE MAC DL Throughput (kbps)",
        "Technology_Detail"]
        data_list.remove(parameter)
        df_1 = df_pre[sel_columns+data_list]  # ["Date Time", "Latitude", "Longitude",parameter]]  # .head(30000)
        df = df_1[df_1[parameter].notna()]
        df['color'] = df[parameter].apply(color_func)
        # df.to_csv("C:/Users/barba/PycharmProjects/pythonProject/2024_works/output.csv")

        layer = pdk.Layer('ScatterplotLayer', data=df, get_position='[Longitude, Latitude]', get_color="color", radius_min_pixels=3,  # Fixed point size in pixels
            radius_max_pixels=3, pickable=True, tooltip=True)
        view = pdk.ViewState(latitude= lat, longitude= lon, zoom=zoom_level, pitch=0)
        deck = pdk.Deck(map_style='mapbox://styles/mapbox/light-v9', initial_view_state=view, layers=[layer], height=height_pydeck , tooltip=tooltip_1()[0])
        # mapbox://styles/mapbox/streets-v11 , mapbox://styles/mapbox/light-v9

        st.subheader(chart_type)
        st.write(uploaded_files_names[i])
        i = i + 1
        st.pydeck_chart(deck)
def calculate_boundaries(df):
    min_latitude = df['Latitude'].min()
    max_latitude = df['Latitude'].max()
    min_longitude = df['Longitude'].min()
    max_longitude = df['Longitude'].max()
    zoom_level = calculate_zoom_level((max_latitude - min_latitude), (max_longitude - min_longitude)) * 1
    lat = (max_latitude + min_latitude) / 2
    lon = (max_longitude + min_longitude) / 2
    return zoom_level,lat,lon
def get_parameter_details(parameter):
    parameter_mapping_old = {
        "NR RSRQ": {"Parameter_Name": "NR Serving Cell SS RSRQ Top #1",
            "Subheader": "RSRQ Color Schema",
            "Chart Type": "NR Serving Cell SS RSRQ",
            "Color_path_Function": get_rsrq_color_patches(),
            "Color function": categorize_rsrq },
        "NR RSRP": {"Parameter_Name": "NR Serving Cell SS RSRP Top #1", "Subheader": "RSRP Color Schema", "Chart Type": "NR Serving Cell SS RSRP", "Color_path_Function": "cetf.get_rsrp_color_patches()", "Color function": "cetf.categorize_rsrp"},
        "NR SINR": {"Parameter_Name": "MR-DC Cell 1 SINR (dB)", "Subheader": "SINR Color Schema", "Chart Type": "MR-DC Cell 1 SINR (dB)", "Color_path_Function": "cetf.get_sinr_color_patches()", "Color function": "cetf.categorize_sinr"},
        "NR Throughput": {"Parameter_Name": "NR MAC DL Throughput Total (kbps)", "Subheader": "NR MAC DL Color Schema", "Chart Type": "NR MAC DL Throughput Total (kbps)", "Color_path_Function": "get_throughput_color_patches()", "Color function": "cetf.categorize_throughput"},
        "LTE RSRQ": {"Parameter_Name": "LTE Serving Cell RSRQ (dB)", "Subheader": "RSRQ Color Schema", "Chart Type": "LTE Serving Cell RSRQ (dB)", "Color_path_Function": "cetf.get_rsrq_color_patches()", "Color function": "cetf.categorize_rsrq"}, "LTE RSRP": {"Parameter_Name": "LTE Serving Cell RSRP (dBm)", "Subheader": "RSRP Color Schema", "Chart Type": "LTE Serving Cell RSRP (dBm)", "Color_path_Function": "cetf.get_rsrp_color_patches()", "Color function": "cetf.categorize_rsrp"},
        "LTE SINR": {"Parameter_Name": "LTE Serving Cell RS SINR (dB)", "Subheader": "SINR Color Schema", "Chart Type": "LTE Serving Cell RS SINR (dB)", "Color_path_Function": "cetf.get_sinr_color_patches()", "Color function": "cetf.categorize_sinr"},
        "LTE Throughput": {"Parameter_Name": "LTE MAC DL Throughput (kbps)", "Subheader": "LTE MAC DL Color Schema", "Chart Type": "LTE MAC DL Throughput (kbps)", "Color_path_Function": "get_throughput_color_patches()", "Color function": "cetf.categorize_throughput"},
        "Tech Details": {"Parameter_Name": "Technology_Detail", "Subheader": "Technology Detail Color Schema", "Chart Type": "Technology_Detail", "Color_path_Function": "get_tech_detail_color_patches()", "Color function": "categorize_Technology_Detail"}}

    parameter_mapping = {"NR RSRQ": {"Parameter_Name": "NR Serving Cell SS RSRQ Top #1", "Subheader": "RSRQ Color Schema", "Chart Type": "NR Serving Cell SS RSRQ", "Color_path_Function": get_rsrq_color_patches(), "Color function": categorize_rsrq}, "NR RSRP": {"Parameter_Name": "NR Serving Cell SS RSRP Top #1", "Subheader": "RSRP Color Schema", "Chart Type": "NR Serving Cell SS RSRP", "Color_path_Function": get_rsrp_color_patches(), "Color function": categorize_rsrp},
        "NR SINR": {"Parameter_Name": "MR-DC Cell 1 SINR (dB)", "Subheader": "SINR Color Schema", "Chart Type": "MR-DC Cell 1 SINR (dB)", "Color_path_Function": get_sinr_color_patches(), "Color function": categorize_sinr}, "NR Throughput": {"Parameter_Name": "NR MAC DL Throughput Total (kbps)", "Subheader": "NR MAC DL Color Schema", "Chart Type": "NR MAC DL Throughput Total (kbps)", "Color_path_Function": get_throughput_color_patches(), "Color function": categorize_throughput},
        "LTE RSRQ": {"Parameter_Name": "LTE Serving Cell RSRQ (dB)", "Subheader": "RSRQ Color Schema", "Chart Type": "LTE Serving Cell RSRQ (dB)", "Color_path_Function": get_rsrq_color_patches(), "Color function": categorize_rsrq}, "LTE RSRP": {"Parameter_Name": "LTE Serving Cell RSRP (dBm)", "Subheader": "RSRP Color Schema", "Chart Type": "LTE Serving Cell RSRP (dBm)", "Color_path_Function": get_rsrp_color_patches(), "Color function": categorize_rsrp},
        "LTE SINR": {"Parameter_Name": "LTE Serving Cell RS SINR (dB)", "Subheader": "SINR Color Schema", "Chart Type": "LTE Serving Cell RS SINR (dB)", "Color_path_Function": get_sinr_color_patches(), "Color function": categorize_sinr}, "LTE Throughput": {"Parameter_Name": "LTE MAC DL Throughput (kbps)", "Subheader": "LTE MAC DL Color Schema", "Chart Type": "LTE MAC DL Throughput (kbps)", "Color_path_Function": get_throughput_color_patches(), "Color function": categorize_throughput},
        "Tech Details": {"Parameter_Name": "Technology_Detail", "Subheader": "Technology Detail Color Schema", "Chart Type": "Technology_Detail", "Color_path_Function": get_tech_detail_color_patches(), "Color function": categorize_Technology_Detail}}

    return parameter_mapping.get(parameter, "Invalid parameter")
def plot_bins(df, parameter, parameter_bin, bin_size,min,max,file_name):
    import pandas as pd
    import streamlit as st
    import plotly.express as px

    # Define bin edges from 0 to 100
    bin_edges = list(range(min, max, bin_size))

    # Create bins with the defined edges
    bins = pd.IntervalIndex.from_breaks(bin_edges)
    df['Bin'] = pd.cut(df[parameter_bin], bins=bins, right=False)

    # Add missing bins to the dataframe
    df['Bin'] = df['Bin'].cat.set_categories(bins)

    df['Bin_str'] = df['Bin'].astype(str)
    df['Bin_Lower'] = df['Bin'].apply(lambda x: x.left)
    df['Bin_Lower_Numeric'] = df['Bin_Lower'].astype(float)

    # Compute the average throughput per bin
    average_throughput = df.groupby(['Bin_str', 'Bin_Lower_Numeric'])[parameter].mean().reset_index()

    # Create a dataframe with all bins
    all_bins = pd.DataFrame({'Bin_str': [str(b) for b in bins], 'Bin_Lower_Numeric': [b.left for b in bins]})

    # Merge with the average throughput to ensure all bins are included
    average_throughput = pd.merge(all_bins, average_throughput, on=['Bin_str', 'Bin_Lower_Numeric'], how='left')
    average_throughput[parameter].fillna(0, inplace=True)  # Replace NaN values with 0 for bins with no data

    # Sort values
    average_throughput = average_throughput.sort_values('Bin_Lower_Numeric')

    # Plot the bar chart
    fig = px.bar(average_throughput, x='Bin_str', y=parameter, labels={'Bin_str': parameter_bin + " Bins", parameter: parameter + " Average"}, title= parameter+" vs "+ parameter_bin, hover_data={'Bin_str': True, parameter: True})  # Enable tooltips
    st.plotly_chart(fig)

    # export_format = 'jpeg'
    # path = "C:/Users/barba/Downloads/img_exports/bin_plots/"

    # Automatically export the plot in the specified format
    # file_name = path + file_name[:-4] + f'{parameter}_vs_{parameter_bin}.{export_format}'
    # if export_format == 'jpeg':
    #     fig.write_image(file_name, engine='kaleido')
    # elif export_format == 'html':
    #     fig.write_html(file_name)
    # st.write(f"Plot exported as {file_name}.")
def plot_bins_multi(df_list, parameter, parameter_bin, bin_size, min, max, file_names):
    import pandas as pd
    import streamlit as st
    import plotly.graph_objects as go  # Import Plotly graph objects for more control over the plot

    # Define bin edges from min to max
    bin_edges = list(range(min, max, bin_size))

    # Initialize the figure
    fig = go.Figure()
    i = 0
    # Loop through each dataframe in the list
    for df_index, df in enumerate(df_list):
        # Create bins with the defined edges
        bins = pd.IntervalIndex.from_breaks(bin_edges)
        df['Bin'] = pd.cut(df[parameter_bin], bins=bins, right=False)

        # Add missing bins to the dataframe
        df['Bin'] = df['Bin'].cat.set_categories(bins)

        df['Bin_str'] = df['Bin'].astype(str)
        df['Bin_Lower'] = df['Bin'].apply(lambda x: x.left)
        df['Bin_Lower_Numeric'] = df['Bin_Lower'].astype(float)

        # Compute the average throughput per bin
        average_throughput = df.groupby(['Bin_str', 'Bin_Lower_Numeric'])[parameter].mean().reset_index()

        # Create a dataframe with all bins
        all_bins = pd.DataFrame({'Bin_str': [str(b) for b in bins], 'Bin_Lower_Numeric': [b.left for b in bins]})

        # Merge with the average throughput to ensure all bins are included
        average_throughput = pd.merge(all_bins, average_throughput, on=['Bin_str', 'Bin_Lower_Numeric'], how='left')
        average_throughput[parameter].fillna(0, inplace=True)  # Replace NaN values with 0 for bins with no data

        # Sort values
        average_throughput = average_throughput.sort_values('Bin_Lower_Numeric')

        # Add line to the figure for each dataframe
        fig.add_trace(go.Scatter(
            x=average_throughput['Bin_Lower_Numeric'],
            y=average_throughput[parameter],
            # mode='lines+markers',
            mode='lines',
            #name=f"DataFrame {df_index + 1}"  # Name each line uniquely
            name = f'{file_names[i]}'
        ))
        i = i + 1

    # Customize layout
    fig.update_layout(
        title=parameter + " vs " + parameter_bin,
        xaxis_title=parameter_bin + " Bins",
        yaxis_title=parameter + " Average",
        hovermode='x unified'  # Unified hover label to show all traces on hover
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig)
def plot_running_sum_percentage(df, bin_column, target_column, bin_size,min,max):
    import pandas as pd
    import streamlit as st
    import plotly.express as px
    # Exclude NaN values in the RSRP column
    df = df.dropna(subset=[bin_column])

    # Define the minimum and maximum values for the bins

    bins = pd.interval_range(start=min, end=max, freq=bin_size, closed='left')

    # Bin the values and convert to string
    df['Binned'] = pd.cut(df[bin_column], bins=bins).astype(str)

    # Count the occurrences of "MR-DC Cell 1 SINR (dB)" in each bin
    count_per_bin = df.groupby('Binned')[target_column].count().reset_index()
    count_per_bin.columns = ['Binned', 'Count']

    # Create a DataFrame with all bins to ensure they are displayed
    all_bins = pd.DataFrame({'Binned': [str(bin) for bin in bins]})
    count_per_bin = pd.merge(all_bins, count_per_bin, on='Binned', how='left').fillna(0)

    # Calculate the running sum and total count
    count_per_bin['Running_Sum'] = count_per_bin['Count'].cumsum()
    total_count = count_per_bin['Count'].sum()
    count_per_bin['Running_Percentage'] = count_per_bin['Running_Sum'] / total_count * 100

    # Plotting using Plotly
    fig = px.line(count_per_bin, x='Binned', y='Running_Percentage', title=f"{bin_column} vs % of Total Running Sum of Count of {target_column}", labels={'Binned': f"{bin_column} (bin)", 'Running_Percentage': '% of Total Running Sum'}, line_shape='spline',markers=False)


    st.plotly_chart(fig)
def plot_running_sum_percentage_all(dfs, bin_column, target_column, bin_size, min_val, max_val,file_names):
    import pandas as pd
    import streamlit as st
    import plotly.graph_objects as go

    # Create a Plotly figure
    fig = go.Figure()

    # Loop through each dataframe in the list
    for i, df in enumerate(dfs):
        # Exclude NaN values in the bin column
        df = df.dropna(subset=[bin_column])

        # Define the bins
        bins = pd.interval_range(start=min_val, end=max_val, freq=bin_size, closed='left')

        # Bin the values and convert to string
        df['Binned'] = pd.cut(df[bin_column], bins=bins).astype(str)

        # Count occurrences of the target column in each bin
        count_per_bin = df.groupby('Binned')[target_column].count().reset_index()
        count_per_bin.columns = ['Binned', 'Count']

        # Create a DataFrame with all bins to ensure they are displayed
        all_bins = pd.DataFrame({'Binned': [str(bin) for bin in bins]})
        count_per_bin = pd.merge(all_bins, count_per_bin, on='Binned', how='left').fillna(0)

        # Calculate the running sum and percentage
        count_per_bin['Running_Sum'] = count_per_bin['Count'].cumsum()
        total_count = count_per_bin['Count'].sum()
        count_per_bin['Running_Percentage'] = count_per_bin['Running_Sum'] / total_count * 100

        # Add a line for each dataframe to the plot
        fig.add_trace(go.Scatter(
            x=count_per_bin['Binned'],
            y=count_per_bin['Running_Percentage'],
            mode='lines',  # Smooth lines
            line_shape='spline',
            # name=f'file_names {file_names[i]}{i+1}'
            name=f'{file_names[i]}'
        ))

    # Update the layout of the figure
    fig.update_layout(
        title=f"{bin_column} vs % of Total Running Sum of Count of {target_column}",
        xaxis_title=f"{bin_column} (bin)",
        yaxis_title='% of Total Running Sum',
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig)
def display_all_operators_test_results_tables(df):
    import streamlit as st
    import pandas as pd

    # Get unique operators
    operators = df['Operator'].unique()

    for operator_name in operators:
        # Filtering data for the current operator
        operator_data = df[df['Operator'] == operator_name]
        # Grouping data by 'Type_of_Test' and 'Type_of_Test_Result', and calculating the count
        counts = operator_data.groupby(['Type_of_Test', 'Type_of_Test_Result']).size().reset_index(name='Count')

        # Display the operator's data as a table in Streamlit
        st.subheader(f'Test Results for {operator_name}')
        st.dataframe(counts)

def plot_http_download_success_ratio(df):
    import plotly.graph_objects as go
    import streamlit as st

    # Get the unique operators
    unique_operators = df['Operator'].unique()

    # Loop through each operator and plot the stacked bar chart
    for operator_name in unique_operators:
        # Filter the dataframe for the current Operator and Type_of_Test
        type_of_test = 'HTTP Browsing'
        filtered_df = df[(df['Operator'] == operator_name) & (df['Type_of_Test'] == type_of_test)]

        # Create a column for success/failure based on HTTP_Download_Session_Success_Ratio
        filtered_df['Session_Status'] = filtered_df['HTTP_Download_Session_Success_Ratio'].apply(lambda x: 'Success' if x == 100 else 'Failed')

        # Group by Test_Name and Session_Status and count occurrences
        counts = filtered_df.groupby(['Test_Name', 'Session_Status']).size().unstack(fill_value=0)

        # Calculate percentages for each Test_Name
        percentages = counts.div(counts.sum(axis=1), axis=0) * 100

        # Creating the stacked bar chart using Plotly
        fig = go.Figure()

        # Adding each status as a separate trace for stacked bar chart
        for status in ['Success', 'Failed']:  # Ensure 'Failed' is stacked on top
            if status in percentages.columns:
                fig.add_trace(go.Bar(x=percentages.index,  # Test_Name on x-axis
                    y=percentages[status] / 100,  # Divide by 100 for correct percentage display
                    name=status, text=percentages[status].apply(lambda x: f'{x:.1f}%'), textposition='inside'))

        # Updating layout for stacked bar chart
        fig.update_layout(barmode='stack', title=f'HTTP Download Session Success Ratio for Operator {operator_name}', xaxis=dict(title='Test_Name'), yaxis=dict(title='Percentage', range=[0, 1],  # Set the range from 0 to 1 (0% to 100%)
            tickformat='.0%'  # Format as whole percentages
        ), legend=dict(title='Session Status'), plot_bgcolor='white')

        # Displaying the chart in Streamlit
        st.subheader(f'Operator: {operator_name}')
        st.plotly_chart(fig)
def create_and_display_success_fail_table(df):
    import streamlit as st
    """
    Create a table showing counts of success and fail for each Test_Name and Operator,
    and display it using Streamlit.

    Parameters:
    df (pd.DataFrame): Input DataFrame with columns 'Operator', 'Test_Name', 'HTTP_Download_Session_Success_Ratio'
    """
    # Add success/fail columns
    df['Succ'] = df['HTTP_Download_Session_Success_Ratio'].apply(lambda x: 1 if x == 100 else 0)
    df['Fail'] = df['HTTP_Download_Session_Success_Ratio'].apply(lambda x: 1 if x == 0 else 0)

    # Group by Test_Name and Operator, and aggregate counts
    grouped = df.groupby(['Test_Name', 'Operator']).agg({'Succ': 'sum', 'Fail': 'sum'}).reset_index()

    # Pivot the table to get the desired format
    pivot_table = grouped.pivot(index='Test_Name', columns='Operator', values=['Succ', 'Fail']).fillna(0)

    # Flatten the MultiIndex columns
    pivot_table.columns = [f'{op}_{result}' for result, op in pivot_table.columns]

    # Reset index to have Test_Name as a column
    pivot_table.reset_index(inplace=True)

    # Display the table using Streamlit
    st.subheader("Success and Failure Counts by Test Name and Operator:")

    # Specify the column configuration with custom width for 'Test_Name'
    column_config = {
        'Test_Name': st.column_config.Column(width="medium"),  # Wider width for the first column
        **{col: st.column_config.Column(width=70) for col in pivot_table.columns if col != 'Test_Name'}
    }


    st.dataframe(pivot_table, column_config=column_config)
def plot_stacked_bar_2(df,parameter_x,parameter_y):
    import plotly.graph_objects as go
    import streamlit as st

    # Grouping data by 'operator' and 'technology' and calculating the count
    tech_counts = df.groupby([parameter_x,parameter_y]).size().unstack(fill_value=0)
    # st.write(tech_counts)
    # Calculating percentages for each technology per operator
    tech_percentages = tech_counts.div(tech_counts.sum(axis=1), axis=0) * 100

    # Creating the stacked bar chart using Plotly
    fig = go.Figure()

    # Adding each technology as a separate trace for stacked bar chart
    for tech in tech_counts.columns:
        fig.add_trace(go.Bar(
            x=tech_percentages.index,
            y=tech_percentages[tech] / 100,  # Divide by 100 for correct percentage display
            name=tech,
            text=tech_percentages[tech].apply(lambda x: f'{x:.1f}%'),
            textposition='inside'
        ))

    # Updating layout for stacked bar chart
    fig.update_layout(
        barmode='stack',
        title= parameter_y + ' Percentages',
        xaxis=dict(title=parameter_x),
        yaxis=dict(
            title='Percentage',
            range=[0, 1],  # Set the range from 0 to 1 (0% to 100%)
            tickformat='.0%'  # Format as whole percentages
        ),
        legend=dict(title=parameter_y),
        plot_bgcolor='white'
    )

    # Displaying the chart in Streamlit
    st.plotly_chart(fig)
def plot_average_throughput_by_operator(df,parameter_x,parameter_y):
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    # Calculate the average throughput grouped by local operator and modulation
    avg_throughput = df.groupby(['Local Operator', parameter_x])[parameter_y].mean().reset_index()

    # Create a grouped bar chart using Plotly
    fig = px.bar(avg_throughput, x=parameter_x, y=parameter_y,
                 color='Local Operator', barmode='group',
                 title='Average ' +  parameter_y + ' by ' + parameter_x + ' Local Operator',
                 labels={parameter_x: parameter_x, parameter_y: parameter_y})

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig)
def plot_lte_serving_cell_identity_count(dataframe):
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    # Count the occurrences of each LTE Serving Cell Identity per Local Operator
    identity_counts = dataframe.groupby('Local Operator')['LTE Serving Cell Identity'].nunique().reset_index()
    identity_counts.columns = ['Local Operator', 'LTE Serving Cell Identity Count']

    # Create a bar plot using Plotly with different colors for each operator
    fig = px.bar(identity_counts, x='Local Operator', y='LTE Serving Cell Identity Count',
                 color='Local Operator',  # Different colors for each operator
                 title='Count of LTE Serving Cell Identity per Local Operator',
                 labels={'LTE Serving Cell Identity Count': 'Cell Identity Count', 'Local Operator': 'Local Operator'},
                 text='LTE Serving Cell Identity Count')  # Add count as text labels

    # Customize text labels
    fig.update_traces(texttemplate='%{text}', textposition='outside')

    # Display the plot in Streamlit
    st.plotly_chart(fig)
def plot_lte_serving_cell_dlearfcn_count(dataframe):
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    # Count the occurrences of each LTE Serving Cell Identity per Local Operator
    identity_counts = dataframe.groupby('Local Operator')['LTE Serving Cell DL EARFCN'].nunique().reset_index()
    identity_counts.columns = ['Local Operator', 'LTE Serving Cell DL EARFCN']

    # Create a bar plot using Plotly with different colors for each operator
    fig = px.bar(identity_counts, x='Local Operator', y='LTE Serving Cell DL EARFCN',
                 color='Local Operator',  # Different colors for each operator
                 title='Count of LTE Serving Cell DL EARFCN per Local Operator',
                 labels={'LTE Serving Cell DL EARFCN': 'LTE Serving Cell DL EARFCN', 'Local Operator': 'Local Operator'},
                 text='LTE Serving Cell DL EARFCN')  # Add count as text labels

    # Customize text labels
    fig.update_traces(texttemplate='%{text}', textposition='outside')

    # Display the plot in Streamlit
    st.plotly_chart(fig)
def parameter_plot_single(df_pre,parameter,chart_type,uploaded_files_name,lat,lon,zoom_level,color_func,height_pydeck):
    import streamlit as st
    import pydeck as pdk
    i=0

    sel_columns = ["Date Time", "Latitude", "Longitude", parameter, "NR Serving Beam 1 NRARFCN DL", "NR Serving Beam 1 Cell Identity", "NR Serving Beam 1 Band", "NR Serving Beam 1 Bandwidth DL", ]
    data_list = ["NR Serving Cell SS RSRQ Top #1",
    "NR Serving Cell SS RSRP Top #1",
    "MR-DC Cell 1 SINR (dB)",
    "NR MAC DL Throughput Total (kbps)",
    "LTE Serving Cell RSRQ (dB)",
    "LTE Serving Cell RSRP (dBm)",
    "LTE Serving Cell RS SINR (dB)",
    "LTE MAC DL Throughput (kbps)",
    "Technology_Detail"]
    data_list.remove(parameter)
    df_1 = df_pre[sel_columns+data_list]  # ["Date Time", "Latitude", "Longitude",parameter]]  # .head(30000)
    df = df_1[df_1[parameter].notna()]
    df['color'] = df[parameter].apply(color_func)
    # df.to_csv("C:/Users/barba/PycharmProjects/pythonProject/2024_works/output.csv")

    layer = pdk.Layer('ScatterplotLayer', data=df, get_position='[Longitude, Latitude]', get_color="color", radius_min_pixels=3,  # Fixed point size in pixels
        radius_max_pixels=3, pickable=True, tooltip=True)
    view = pdk.ViewState(latitude= lat, longitude= lon, zoom=zoom_level, pitch=0)
    deck = pdk.Deck(map_style='road', initial_view_state=view, layers=[layer], height=height_pydeck , tooltip=tooltip_1()[0])
    # mapbox://styles/mapbox/streets-v11 , mapbox://styles/mapbox/light-v9

    st.subheader(chart_type)
    st.write(uploaded_files_name)
    st.pydeck_chart(deck)
def streaming_analysis(df):
    import streamlit as st
    import pandas as pd
    # Find start indices where "Streaming_URL" is not null
    start_indices = df.index[df['Streaming_URL'].notnull()]

    # Find end indices where "Streaming_Completion_Rate" is not null
    end_indices = df.index[df['Streaming_Completion_Rate'].notnull()]

    # Make sure there is a corresponding end index for each start index
    filtered_sessions = []

    for start in start_indices:
        # Find the first end index that comes after the start index
        end = end_indices[end_indices > start].min()

        if pd.notna(end):
            # Filter rows between the start and end index (inclusive)
            session_df = df.loc[start:end]
            filtered_sessions.append(session_df)

    # Combine all filtered sessions into a single DataFrame
    streaming_df = pd.concat(filtered_sessions)

    # Group by 'Local Operator' and count non-null entries in 'Streaming_URL'
    result = streaming_df.groupby('Local Operator')['Streaming_URL'].count().reset_index()

    # Rename the columns for better clarity
    result.columns = ['Local Operator', 'Count of Filled Streaming_URL']

    st.write(result)

    averages = streaming_df[['Streaming_Average_Session_Resolution', 'Streaming_Average_Throughput', 'Streaming_Maximum_Duration_Of_Video_Session_Interruptions']].mean()
    averages = averages.round(2)
    # Convert the result to a DataFrame for better display
    averages_df = averages.to_frame(name='Average').reset_index()
    averages_df.columns = ['Metric', 'Average']
    st.write(averages_df)

    # Define the columns to be processed
    columns = ['Streaming_Completion_Rate', 'Streaming_Impairment_Free_Video_Session_Ratio', 'Streaming_Session_Without_Interruption_Rate']

    # Calculate the number of 100s and total counts for each column
    result = {}
    for col in columns:
        count_100 = (df[col] == 100).sum()  # Count number of 100s
        total_count = df[col].count()  # Total count of non-null values (0s and 100s)
        ratio = count_100 / total_count if total_count > 0 else 0  # Calculate ratio and avoid division by zero
        result[col] = [count_100, total_count, round(ratio, 2)]  # Store the results with ratio rounded to 2 decimals

    # Convert the results to a DataFrame for display
    result_df = pd.DataFrame(result, index=['Number of 100s', 'Total Count', 'Ratio of 100s']).T

    # Reset index to make the current index a new column called "Metric"
    result_df = result_df.reset_index().rename(columns={'index': 'Metric'})

    # Add a new numerical index starting from 1
    result_df.index = range(1, len(result_df) + 1)

    st.write(result_df)
def transform_geojson_epsg27700_to_epsg4326(geojson_data):
    from pyproj import Transformer
    transformer = Transformer.from_crs("epsg:27700", "epsg:4326", always_xy=True)

    for feature in geojson_data['features']:
        if feature['geometry']['type'] == 'Polygon':
            new_coords = []
            for ring in feature['geometry']['coordinates']:
                new_ring = [transformer.transform(x, y) for x, y in ring]
                new_coords.append(new_ring)
            feature['geometry']['coordinates'] = new_coords
        elif feature['geometry']['type'] == 'Point':
            x, y = feature['geometry']['coordinates']
            feature['geometry']['coordinates'] = list(transformer.transform(x, y))

    return geojson_data
def get_geojson_bounds(geojson_data):
    """Calculate the bounding box for all features in the GeoJSON."""
    min_lon, min_lat = float('inf'), float('inf')
    max_lon, max_lat = float('-inf'), float('-inf')

    # Loop through each feature's coordinates
    for feature in geojson_data['features']:
        coordinates = feature['geometry']['coordinates']

        # For Polygon or MultiPolygon, flatten the list of coordinates
        if feature['geometry']['type'] == "Polygon":
            coordinates = [coord for ring in coordinates for coord in ring]
        elif feature['geometry']['type'] == "MultiPolygon":
            coordinates = [coord for polygon in coordinates for ring in polygon for coord in ring]

        # Update the bounds
        for lon, lat in coordinates:
            min_lon = min(min_lon, lon)
            max_lon = max(max_lon, lon)
            min_lat = min(min_lat, lat)
            max_lat = max(max_lat, lat)

    return min_lat, max_lat, min_lon, max_lon
def display_grid_geojson_data(geojson_data):
    import pydeck as pdk
    import streamlit as st
    import json
    geojson_epsg4326 = transform_geojson_epsg27700_to_epsg4326(geojson_data)
    min_lat, max_lat, min_lon, max_lon = get_geojson_bounds(geojson_epsg4326)
    zoom_level = calculate_zoom_level(max_lat - min_lat, max_lon - min_lon)

    geojson_layer = pdk.Layer("GeoJsonLayer",geojson_epsg4326, pickable=True,auto_highlight=True,get_fill_color=[0, 255, 0, 100],get_line_color=[255, 0, 0], line_width_min_pixels=2)

    # Define the tooltip for displaying the "id" field
    tooltip = {
        "html": "<b>ID:</b> {id}",  # Tooltip content: show the "id" from properties
        "style": {
            "backgroundColor": "steelblue",
            "color": "white"
        }
    }

    labels = [
        {
            # Use the first coordinate point of the polygon as a temporary label position
            "coordinates": feature["geometry"]["coordinates"][0][0],  # Ensure this is [lon, lat]
            "text": str(feature["properties"]["id"]),  # Convert ID to string for display
        }
        for feature in geojson_epsg4326['features']
    ]

    text_layer = pdk.Layer("TextLayer", data=labels,get_position="coordinates", get_text="text", get_size=16,get_color=[0, 0, 0, 255], get_alignment_baseline="'bottom'", )

    view_state = pdk.ViewState(latitude=(min_lat + max_lat) / 2,longitude=(min_lon + max_lon) / 2,zoom=zoom_level,pitch=0)
    st.pydeck_chart(pdk.Deck(
        layers=[geojson_layer],  # Include both the GeoJSON layer and text layer
        initial_view_state=view_state,
        height=1000,
        tooltip=tooltip,  # Add the tooltip configuration
        map_style='mapbox://styles/mapbox/streets-v11'
    ))
def plot_average_aggregate_by_operator(df,group_par,parameter_x,parameter_y):
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    # Calculate the average throughput grouped by local operator and modulation
    avg_throughput = df.groupby([group_par, parameter_x])[parameter_y].mean().reset_index()

    # Create a grouped bar chart using Plotly
    fig = px.bar(avg_throughput, x=parameter_x, y=parameter_y,
                 color=group_par, barmode='group',
                 title='Average ' +  parameter_y + ' by ' + parameter_x + ' Local Operator',
                 labels={parameter_x: parameter_x, parameter_y: parameter_y})

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig)






