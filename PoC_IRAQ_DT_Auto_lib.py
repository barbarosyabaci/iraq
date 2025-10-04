import pandas as pd, streamlit as st, PoC_IRAQ_DT_Auto_lib_2 as pidal2

def dashboard():
    import streamlit as st
    st.markdown("---")

    col1, col2, col3,col4,col5 = st.columns(5)
    col3.metric("Project Area", "GR / Dusseldorf")
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
    import pydeck as pdk

    duesseldorf_lat = 51.2277
    duesseldorf_lon = 6.7735

    view_state = pdk.ViewState(latitude=duesseldorf_lat, longitude=duesseldorf_lon, zoom=12,  # adjust zoom level as needed
        pitch=0)
    # ---- Render ----

    r = pdk.Deck(layers=[],initial_view_state=view_state,map_style=map_style, tooltip={"text": "{site} | {cell} | Azimuth {azimuth}"})
    import streamlit as st
    st.pydeck_chart(r, height=700)


def tooltip_1():
    tooltip_1 = {"text": "MR-DC Cell 1 SINR (dB): {MR-DC Cell 1 SINR (dB)}\n"
                       "NR Serving Cell SS RSRP Top #1: {NR Serving Cell SS RSRP Top #1}\n"
                       "NR Serving Cell SS RSRQ Top #1: {NR Serving Cell SS RSRQ Top #1}\n"
                       "NR Serving Beam 1 NRARFCN DL: {NR Serving Beam 1 NRARFCN DL}\n"
                       "NR Serving Beam 1 Cell Identity: {NR Serving Beam 1 Cell Identity}\n"
                       "NR Serving Beam 1 Band: {NR Serving Beam 1 Band}\n"
                       "NR Serving Beam 1 Bandwidth DL: {NR Serving Beam 1 Bandwidth DL}"},
    return tooltip_1
def parameter_plot_single(df_pre,parameter,chart_type,uploaded_files_name,lat,lon,zoom_level,color_func,height_pydeck):
    import streamlit as st
    import pydeck as pdk
    i=0

    sel_columns = ["Date Time", "Latitude", "Longitude", parameter, "NR Serving Beam 1 NRARFCN DL", "NR Serving Beam 1 Cell Identity", "NR Serving Beam 1 Band", "NR Serving Beam 1 Bandwidth DL", ]
    data_list = [
    "NR Serving Cell SS RSRQ Top #1",
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

    layer = pdk.Layer('ScatterplotLayer', data=df, get_position='[Longitude, Latitude]', get_color="color", radius_min_pixels=3,  # Fixed point size in pixels
        radius_max_pixels=3, pickable=True, tooltip=True)
    view = pdk.ViewState(latitude= lat, longitude= lon, zoom=zoom_level, pitch=0)
    deck = pdk.Deck(map_style='road', initial_view_state=view, layers=[layer], height=height_pydeck , tooltip=tooltip_1()[0])
    # mapbox://styles/mapbox/streets-v11 , mapbox://styles/mapbox/light-v9

    st.subheader(chart_type)
    st.write(uploaded_files_name)
    st.pydeck_chart(deck)
def LTE_coverage():
    import PoC_IRAQ_DT_Auto_lib_2 as pidal2
    import CDR_EDA_Tools_Functions as cetf

    plot_text_1 = ""
    st.subheader("Coverage Plots and Statistics")
    st.markdown(plot_text_1)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        date_iteration_dict = {"20250101": "20250101", "20250120": "20250120", "20250208": "20250208", "20250226": "20250226", "20250316": "20250316", "20250403": "20250403", "20250421": "20250421", "20250509": "20250509", "20250527": "20250527", "20250614": "20250614", "20250702": "20250702", "20250720": "20250720", "20250807": "20250807", "20250825": "20250825", "20250912": "20250912"}
        selected_iteration = st.selectbox("Select Iteration", options=list(date_iteration_dict.keys()),key = "lteselect", index=0)  # Default to 'Road'

    with col2:
        sector_length = st.slider("Sector length", 1, 30, 5, step=1, key="rsrp_lte")

    with col3:
        # grid_size = st.slider("Grid Size", 10, 500, 200, step=10,key="rsrp_mes_2")
        zoom = st.slider("Zoom Level", min_value=1, max_value=20, value=12,key = "lteselect2",)

        pitch = 0  # st.slider("Pitch Angle", min_value=0, max_value=90, value=0)
    with col4:
        # Create coordinate input field
        coords_input = st.text_input("Longitude,Latitude", value="", key = "lteselect3",help="Enter coordinates as: latitude,longitude (e.g., 89.5239,22.6530)")
        coords = [coord.strip() for coord in coords_input.split(",")]

    # parameters = ["NR RSRQ", "NR RSRP", "NR SINR", "NR Throughput", "LTE RSRQ", "LTE RSRP", "LTE SINR", "LTE Throughput", "Tech Details"]
    # selected_parameters = st.multiselect("Select Parameters:", options=parameters, default=None),

    selected_parameters = ["LTE RSRQ", "LTE RSRP", "LTE SINR", "LTE Throughput"]

    if st.button("Show LTE Plots and Statistics in comparison view"):
        st.title("Modulation Types vs Througput Charts")
        # uploaded_file = st.file_uploader("Choose input CSV files to process", type="csv", accept_multiple_files=True, key="u15")


        dataframes = []
        uploaded_files_names = []
        path = r"C:\Users\barba\Documents\01_Job\2024_CDR\CSV Dusseldorf"
        uploaded_files_names.append("20240715_Dusseldorf_CDRData_1N1.csv")
        uploaded_files_names.append("20240715_Dusseldorf_CDRData_O2.csv")
        dataframes.append(pd.read_csv(r"20240715_Dusseldorf_CDRData_1N1_filtered.csv", low_memory=False))
        dataframes.append(pd.read_csv(r"20240715_Dusseldorf_CDRData_O2_filtered.csv", low_memory=False))

        df_combined = pd.concat(dataframes, ignore_index=False)

        col1, col2, col3 = st.columns(3)

        with col1:
            df_selected = df_combined[df_combined["LTE PDSCH Modulation"].notna()]
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'LTE PDSCH Phy Throughput (kbps)')
            cetf.plot_stacked_bar_2(df_selected, "Local Operator", "LTE PDSCH Modulation")
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'LTE Serving Cell RSRP (dBm)')

        with col2:
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'NR PDSCH Phy Throughput Total (Kbps)')
            cetf.plot_stacked_bar_2(df_combined, "Local Operator", "Multi RAT Connectivity Mode")
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'MR-DC Cell 1 SINR (dB)')

        with col3:
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'Multi_RAT_Phy_Throughput_DL_kbps')
            cetf.plot_stacked_bar_2(df_selected, "Local Operator", "LTE Serving Cell Frequency Band")
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'LTE Serving Cell RS SINR (dB)')

        # Plots part

        col1, col2 = st.columns(2)
        # uploaded_files_names, dataframes = process_uploaded_files(upload_all)

        # st.write(type(dataframes[0]))
        height_pydeck = 700
        zoom_level, lat, lon = pidal2.calculate_boundaries(dataframes[0])

        for selected_parameter in selected_parameters:
            # st.write(selected_parameter)

            parameter = pidal2.get_parameter_details(selected_parameter)["Parameter_Name"]
            # st.subheader(pidal2.get_parameter_details(selected_parameter)["Subheader"])
            chart_type =pidal2.get_parameter_details(selected_parameter)["Chart Type"]
            color_patches = pidal2.get_parameter_details(selected_parameter)["Color_path_Function"]
            color_function =  pidal2.get_parameter_details(selected_parameter)["Color function"]

            with col1:
                pidal2.plot_color_patches(color_patches)
                parameter_plot_single(dataframes[0], parameter, chart_type, uploaded_files_names[0], lat, lon, zoom_level, color_function, height_pydeck)
                # dataframes[0].to_csv(r"C:\Users\barba\Downloads\20240715_Dusseldorf_CDRData_1N1_short.csv")
            with col2:
                pidal2.plot_color_patches(color_patches)
                parameter_plot_single(dataframes[1], parameter, chart_type, uploaded_files_names[1], lat, lon, zoom_level, color_function, height_pydeck)
                # dataframes[1].to_csv(r"C:\Users\barba\Downloads\20240715_Dusseldorf_CDRData_O2_short.csv")
def NR_coverage():
    import PoC_IRAQ_DT_Auto_lib_2 as pidal2
    import CDR_EDA_Tools_Functions as cetf
    plot_text_old = """
    - Select the raw data CDR files than press the process files, example format: 20240507_Dortmund_CDRData_VDF.csv 
    - Each file will be plotted seperately and file name will be on top of the plot.  
     """
    plot_text_1 = ""

    st.subheader("Coverage Plots and Statistics")
    st.markdown(plot_text_1)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        date_iteration_dict = {"20250101": "20250101", "20250120": "20250120", "20250208": "20250208", "20250226": "20250226", "20250316": "20250316", "20250403": "20250403", "20250421": "20250421", "20250509": "20250509", "20250527": "20250527", "20250614": "20250614", "20250702": "20250702", "20250720": "20250720", "20250807": "20250807", "20250825": "20250825", "20250912": "20250912"}
        selected_iteration = st.selectbox("Select Iteration", options=list(date_iteration_dict.keys()), index=0, key = "nr")  # Default to 'Road'

    with col2:
        sector_length = st.slider("Sector length", 1, 30, 5, step=1, key="nr_mes")

    with col3:
        # grid_size = st.slider("Grid Size", 10, 500, 200, step=10,key="rsrp_mes_2")
        zoom = st.slider("Zoom Level", min_value=1, max_value=20, value=12,key = "nr_sl")

        pitch = 0  # st.slider("Pitch Angle", min_value=0, max_value=90, value=0)
    with col4:
        # Create coordinate input field
        coords_input = st.text_input("Longitude,Latitude", value="", help="Enter coordinates as: latitude,longitude (e.g., 89.5239,22.6530)",key = "nr_txt")
        coords = [coord.strip() for coord in coords_input.split(",")]


    parameters = ["NR RSRQ", "NR RSRP", "NR SINR", "NR Throughput", "LTE RSRQ", "LTE RSRP", "LTE SINR", "LTE Throughput", "Tech Details"]

    # selected_parameters = st.multiselect("Select Parameters:", options=parameters, default=None),

    selected_parameters = ["NR RSRQ", "NR RSRP", "NR SINR", "NR Throughput"]

    if st.button("Show NR Plots and Statistics in comparison view", key = "2"):
        dataframes = []
        uploaded_files_names = []
        path = r"C:\Users\barba\Documents\01_Job\2024_CDR\CSV Dusseldorf"
        uploaded_files_names.append("20240715_Dusseldorf_CDRData_1N1.csv")
        uploaded_files_names.append("20240715_Dusseldorf_CDRData_O2.csv")
        dataframes.append(pd.read_csv(r"20240715_Dusseldorf_CDRData_1N1_filtered.csv", low_memory=False))
        dataframes.append(pd.read_csv(r"20240715_Dusseldorf_CDRData_O2_filtered.csv", low_memory=False))

        df_combined = pd.concat(dataframes, ignore_index=False)

        col1, col2, col3 = st.columns(3)

        with col1:
            df_selected = df_combined[df_combined["LTE PDSCH Modulation"].notna()]
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'LTE PDSCH Phy Throughput (kbps)')
            cetf.plot_stacked_bar_2(df_selected, "Local Operator", "LTE PDSCH Modulation")
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'LTE Serving Cell RSRP (dBm)')

        with col2:
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'NR PDSCH Phy Throughput Total (Kbps)')
            cetf.plot_stacked_bar_2(df_combined, "Local Operator", "Multi RAT Connectivity Mode")
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'MR-DC Cell 1 SINR (dB)')

        with col3:
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'Multi_RAT_Phy_Throughput_DL_kbps')
            cetf.plot_stacked_bar_2(df_selected, "Local Operator", "LTE Serving Cell Frequency Band")
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'LTE Serving Cell RS SINR (dB)')

        # Plots Part
        col1, col2 = st.columns(2)
        height_pydeck = 700
        zoom_level, lat, lon = pidal2.calculate_boundaries(dataframes[0])

        for selected_parameter in selected_parameters:
            # st.write(selected_parameter)

            parameter = pidal2.get_parameter_details(selected_parameter)["Parameter_Name"]
            # st.subheader(pidal2.get_parameter_details(selected_parameter)["Subheader"])
            chart_type = pidal2.get_parameter_details(selected_parameter)["Chart Type"]
            color_patches = pidal2.get_parameter_details(selected_parameter)["Color_path_Function"]
            color_function =  pidal2.get_parameter_details(selected_parameter)["Color function"]

            with col1:
                pidal2.plot_color_patches(color_patches)
                parameter_plot_single(dataframes[0], parameter, chart_type, uploaded_files_names[0], lat, lon, zoom_level, color_function, height_pydeck)
                # dataframes[0].to_csv(r"C:\Users\barba\Downloads\20240715_Dusseldorf_CDRData_1N1_short.csv")
            with col2:
                pidal2.plot_color_patches(color_patches)
                parameter_plot_single(dataframes[1], parameter, chart_type, uploaded_files_names[1], lat, lon, zoom_level, color_function, height_pydeck)
                # dataframes[1].to_csv(r"C:\Users\barba\Downloads\20240715_Dusseldorf_CDRData_O2_short.csv")
def GSM_coverage():
    import PoC_IRAQ_DT_Auto_lib_2 as pidal2
    import CDR_EDA_Tools_Functions as cetf

    plot_text_1 = ""
    st.subheader("Coverage Plots and Statistics")
    st.markdown(plot_text_1)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        date_iteration_dict = {"20250101": "20250101", "20250120": "20250120", "20250208": "20250208", "20250226": "20250226", "20250316": "20250316", "20250403": "20250403", "20250421": "20250421", "20250509": "20250509", "20250527": "20250527", "20250614": "20250614", "20250702": "20250702", "20250720": "20250720", "20250807": "20250807", "20250825": "20250825", "20250912": "20250912"}
        selected_iteration = st.selectbox("Select Iteration", options=list(date_iteration_dict.keys()), index=0)  # Default to 'Road'

    with col2:
        sector_length = st.slider("Sector length", 1, 30, 5, step=1, key="gsm_mes")

    with col3:
        # grid_size = st.slider("Grid Size", 10, 500, 200, step=10,key="rsrp_mes_2")
        zoom = st.slider("Zoom Level", min_value=1, max_value=20, value=12)

        pitch = 0  # st.slider("Pitch Angle", min_value=0, max_value=90, value=0)
    with col4:
        # Create coordinate input field
        coords_input = st.text_input("Longitude,Latitude", value="", help="Enter coordinates as: latitude,longitude (e.g., 89.5239,22.6530)")
        coords = [coord.strip() for coord in coords_input.split(",")]

    # parameters = ["NR RSRQ", "NR RSRP", "NR SINR", "NR Throughput", "LTE RSRQ", "LTE RSRP", "LTE SINR", "LTE Throughput", "Tech Details"]
    # selected_parameters = st.multiselect("Select Parameters:", options=parameters, default=None),

    selected_parameters = ["LTE RSRQ", "LTE RSRP", "LTE SINR", "LTE Throughput"]

    if st.button("Show GSM Plots and Statistics in comparison view", key = "3gplots"):
        st.title("Modulation Types vs Througput Charts")
        # uploaded_file = st.file_uploader("Choose input CSV files to process", type="csv", accept_multiple_files=True, key="u15")


        dataframes = []
        uploaded_files_names = []
        path = r"C:\Users\barba\Documents\01_Job\2024_CDR\CSV Dusseldorf"
        uploaded_files_names.append("20240715_Dusseldorf_CDRData_1N1.csv")
        uploaded_files_names.append("20240715_Dusseldorf_CDRData_O2.csv")
        dataframes.append(pd.read_csv(r"20240715_Dusseldorf_CDRData_1N1_filtered.csv", low_memory=False))
        dataframes.append(pd.read_csv(r"20240715_Dusseldorf_CDRData_O2_filtered.csv", low_memory=False))

        df_combined = pd.concat(dataframes, ignore_index=False)

        col1, col2, col3 = st.columns(3)

        with col1:
            df_selected = df_combined[df_combined["LTE PDSCH Modulation"].notna()]
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'LTE PDSCH Phy Throughput (kbps)')
            cetf.plot_stacked_bar_2(df_selected, "Local Operator", "LTE PDSCH Modulation")
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'LTE Serving Cell RSRP (dBm)')

        with col2:
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'NR PDSCH Phy Throughput Total (Kbps)')
            cetf.plot_stacked_bar_2(df_combined, "Local Operator", "Multi RAT Connectivity Mode")
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'MR-DC Cell 1 SINR (dB)')

        with col3:
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'Multi_RAT_Phy_Throughput_DL_kbps')
            cetf.plot_stacked_bar_2(df_selected, "Local Operator", "LTE Serving Cell Frequency Band")
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'LTE Serving Cell RS SINR (dB)')

        # Plots part

        col1, col2 = st.columns(2)
        # uploaded_files_names, dataframes = process_uploaded_files(upload_all)

        # st.write(type(dataframes[0]))
        height_pydeck = 700
        zoom_level, lat, lon = pidal2.calculate_boundaries(dataframes[0])

        for selected_parameter in selected_parameters:
            # st.write(selected_parameter)

            parameter = pidal2.get_parameter_details(selected_parameter)["Parameter_Name"]
            # st.subheader(pidal2.get_parameter_details(selected_parameter)["Subheader"])
            chart_type =pidal2.get_parameter_details(selected_parameter)["Chart Type"]
            color_patches = pidal2.get_parameter_details(selected_parameter)["Color_path_Function"]
            color_function =  pidal2.get_parameter_details(selected_parameter)["Color function"]

            with col1:
                pidal2.plot_color_patches(color_patches)
                parameter_plot_single(dataframes[0], parameter, chart_type, uploaded_files_names[0], lat, lon, zoom_level, color_function, height_pydeck)
                # dataframes[0].to_csv(r"C:\Users\barba\Downloads\20240715_Dusseldorf_CDRData_1N1_short.csv")
            with col2:
                pidal2.plot_color_patches(color_patches)
                parameter_plot_single(dataframes[1], parameter, chart_type, uploaded_files_names[1], lat, lon, zoom_level, color_function, height_pydeck)
                # dataframes[1].to_csv(r"C:\Users\barba\Downloads\20240715_Dusseldorf_CDRData_O2_short.csv")
def WCDMA3G_coverage():
    import PoC_IRAQ_DT_Auto_lib_2 as pidal2
    import CDR_EDA_Tools_Functions as cetf

    plot_text_1 = ""
    st.subheader("Coverage Plots and Statistics")
    st.markdown(plot_text_1)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        date_iteration_dict = {"20250101": "20250101", "20250120": "20250120", "20250208": "20250208", "20250226": "20250226", "20250316": "20250316", "20250403": "20250403", "20250421": "20250421", "20250509": "20250509", "20250527": "20250527", "20250614": "20250614", "20250702": "20250702", "20250720": "20250720", "20250807": "20250807", "20250825": "20250825", "20250912": "20250912"}
        selected_iteration = st.selectbox("Select Iteration", options=list(date_iteration_dict.keys()), index=0, key="3gselect")  # Default to 'Road'

    with col2:
        sector_length = st.slider("Sector length", 1, 30, 5, step=1, key="rsrp_mes")

    with col3:
        # grid_size = st.slider("Grid Size", 10, 500, 200, step=10,key="rsrp_mes_2")
        zoom = st.slider("Zoom Level", min_value=1, max_value=20, value=12, key ="3gslider")

        pitch = 0  # st.slider("Pitch Angle", min_value=0, max_value=90, value=0)
    with col4:
        # Create coordinate input field
        coords_input = st.text_input("Longitude,Latitude", value="",key="3ginput", help="Enter coordinates as: latitude,longitude (e.g., 89.5239,22.6530)")
        coords = [coord.strip() for coord in coords_input.split(",")]

    # parameters = ["NR RSRQ", "NR RSRP", "NR SINR", "NR Throughput", "LTE RSRQ", "LTE RSRP", "LTE SINR", "LTE Throughput", "Tech Details"]
    # selected_parameters = st.multiselect("Select Parameters:", options=parameters, default=None),

    selected_parameters = ["LTE RSRQ", "LTE RSRP", "LTE SINR", "LTE Throughput"]

    if st.button("Show 3G Plots and Statistics in comparison view", key ="3gplots2"):
        st.title("Modulation Types vs Througput Charts")
        # uploaded_file = st.file_uploader("Choose input CSV files to process", type="csv", accept_multiple_files=True, key="u15")

        dataframes = []
        uploaded_files_names = []
        path = r"C:\Users\barba\Documents\01_Job\2024_CDR\CSV Dusseldorf"
        uploaded_files_names.append("20240715_Dusseldorf_CDRData_1N1.csv")
        uploaded_files_names.append("20240715_Dusseldorf_CDRData_O2.csv")
        dataframes.append(pd.read_csv(path + r"\20240715_Dusseldorf_CDRData_1N1_filtered.csv", low_memory=False))
        dataframes.append(pd.read_csv(path + r"\20240715_Dusseldorf_CDRData_O2_filtered.csv", low_memory=False))

        df_combined = pd.concat(dataframes, ignore_index=False)

        col1, col2, col3 = st.columns(3)

        with col1:
            df_selected = df_combined[df_combined["LTE PDSCH Modulation"].notna()]
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'LTE PDSCH Phy Throughput (kbps)')
            cetf.plot_stacked_bar_2(df_selected, "Local Operator", "LTE PDSCH Modulation")
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'LTE Serving Cell RSRP (dBm)')

        with col2:
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'NR PDSCH Phy Throughput Total (Kbps)')
            cetf.plot_stacked_bar_2(df_combined, "Local Operator", "Multi RAT Connectivity Mode")
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'MR-DC Cell 1 SINR (dB)')

        with col3:
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'Multi_RAT_Phy_Throughput_DL_kbps')
            cetf.plot_stacked_bar_2(df_selected, "Local Operator", "LTE Serving Cell Frequency Band")
            cetf.plot_average_throughput_by_operator(df_selected, "LTE PDSCH Modulation", 'LTE Serving Cell RS SINR (dB)')

        # Plots part

        col1, col2 = st.columns(2)
        # uploaded_files_names, dataframes = process_uploaded_files(upload_all)

        # st.write(type(dataframes[0]))
        height_pydeck = 700
        zoom_level, lat, lon = pidal2.calculate_boundaries(dataframes[0])

        for selected_parameter in selected_parameters:
            # st.write(selected_parameter)

            parameter = pidal2.get_parameter_details(selected_parameter)["Parameter_Name"]
            # st.subheader(pidal2.get_parameter_details(selected_parameter)["Subheader"])
            chart_type = pidal2.get_parameter_details(selected_parameter)["Chart Type"]
            color_patches = pidal2.get_parameter_details(selected_parameter)["Color_path_Function"]
            color_function = pidal2.get_parameter_details(selected_parameter)["Color function"]

            with col1:
                pidal2.plot_color_patches(color_patches)
                parameter_plot_single(dataframes[0], parameter, chart_type, uploaded_files_names[0], lat, lon, zoom_level, color_function, height_pydeck)  # dataframes[0].to_csv(r"C:\Users\barba\Downloads\20240715_Dusseldorf_CDRData_1N1_short.csv")
            with col2:
                pidal2.plot_color_patches(color_patches)
                parameter_plot_single(dataframes[1], parameter, chart_type, uploaded_files_names[1], lat, lon, zoom_level, color_function, height_pydeck)  # dataframes[1].to_csv(r"C:\Users\barba\Downloads\20240715_Dusseldorf_CDRData_O2_short.csv")
def data_kpi_general():
    import streamlit as st
    import pandas as pd

    date_iteration_dict = {"20250101": "20250101", "20250120": "20250120", "20250208": "20250208", "20250226": "20250226", "20250316": "20250316", "20250403": "20250403", "20250421": "20250421", "20250509": "20250509", "20250527": "20250527", "20250614": "20250614", "20250702": "20250702", "20250720": "20250720", "20250807": "20250807", "20250825": "20250825", "20250912": "20250912"}

    # Data
    data = {"TECHNOLOGY": ["Tests Executed only in LTE", "Tests Executed in EN-DC/LTE", "Tests Executed only in EN-DC", "Tests Total", "GSM/WCDMA", "GSM/WCDMA Ratio", "Only LTE Ratio", "EN-DC Ratio", "EN-DC/LTE Ratio", "Overall Test Time Sum [s]", "EN-DC Overall Time Sum [s]", "EN-DC Overall Time Share Ratio"], "Telefonica": [4, 38, 135, 177, 0, "0.00%", "2.26%", "76.27%", "21.47%", 2029.119, 1288.236, "63.49%"],
        "1 & 1": [7, 25, 139, 164, 0, "0.00%", "4.27%", "84.76%", "15.24%", 2032.324, 1335.584, "65.72%"] }

    df = pd.DataFrame(data)

    # Style only the column headers
    styled_df = df.style.set_table_styles([{'selector': 'th', 'props': [('background-color', '#d9ead3'), ('font-weight', 'bold'), ('color', 'black')]}])

    col1, col2 = st.columns(2)
    with col1:
        selected_iteration = st.selectbox("Select test date", options=list(date_iteration_dict.keys()), key="data1", index=0)  # Default to 'Road'

        st.write("### Network Test Summary")
        st.table(styled_df)

    col1, col2,col3,col4 = st.columns(4)
    with col1:
        import streamlit as st
        import pandas as pd
        import matplotlib.pyplot as plt
        import numpy as np

        # Data
        data = {"TECHNOLOGY": ["Only LTE Ratio"], "Telefonica": [2.26], "1 & 1": [4.27]}

        df = pd.DataFrame(data)

        # Plot
        fig, ax = plt.subplots(figsize=(5, 4))
        bars = ax.bar(["Telefonica", "1 & 1"], df.loc[0, ["Telefonica", "1 & 1"]])

        # Customize
        ax.set_title(df.loc[0, "TECHNOLOGY"], fontsize=14, weight='bold')
        ax.set_ylabel("Ratio (%)")
        ax.set_ylim(0, 100)  # fix max at 100%
        ax.set_yticks(np.arange(0, 101, 20))  # guideline every 20%

        # Color only the x-axis labels (not bars)
        ax.tick_params(axis='x', colors='dodgerblue', labelsize=12)
        ax.tick_params(axis='y', labelsize=10)

        # Add gridlines for better visual reference
        ax.grid(axis='y', linestyle='--', alpha=0.7)

        # Show value labels on bars
        for bar in bars:
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f"{bar.get_height():.2f}%", ha='center', va='bottom')

        # Display in Streamlit
        st.pyplot(fig)
    with col2:
        import streamlit as st
        import pandas as pd
        import matplotlib.pyplot as plt
        import numpy as np

        # Data
        data = {"TECHNOLOGY": ["EN-DC Ratio"], "Telefonica": [76.27], "1 & 1": [84.76]}

        df = pd.DataFrame(data)

        # Plot
        fig, ax = plt.subplots(figsize=(5, 4))
        bars = ax.bar(["Telefonica", "1 & 1"], df.loc[0, ["Telefonica", "1 & 1"]])

        # Customize
        ax.set_title(df.loc[0, "TECHNOLOGY"], fontsize=14, weight='bold')
        ax.set_ylabel("Ratio (%)")
        ax.set_ylim(0, 100)  # fix max at 100%
        ax.set_yticks(np.arange(0, 101, 20))  # guideline every 20%

        # Color only the x-axis labels (not bars)
        ax.tick_params(axis='x', colors='dodgerblue', labelsize=12)
        ax.tick_params(axis='y', labelsize=10)

        # Add gridlines for better visual reference
        ax.grid(axis='y', linestyle='--', alpha=0.7)

        # Show value labels on bars
        for bar in bars:
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f"{bar.get_height():.2f}%", ha='center', va='bottom')

        # Display in Streamlit
        st.pyplot(fig)
    with col3:
        import streamlit as st
        import pandas as pd
        import matplotlib.pyplot as plt
        import numpy as np

        # Data
        data = {"TECHNOLOGY": ["EN-DC/LTE Ratio"], "Telefonica": [21.47], "1 & 1": [15.24]}

        df = pd.DataFrame(data)

        # Plot
        fig, ax = plt.subplots(figsize=(5, 4))
        bars = ax.bar(["Telefonica", "1 & 1"], df.loc[0, ["Telefonica", "1 & 1"]])

        # Customize
        ax.set_title(df.loc[0, "TECHNOLOGY"], fontsize=14, weight='bold')
        ax.set_ylabel("Ratio (%)")
        ax.set_ylim(0, 100)  # fix max at 100%
        ax.set_yticks(np.arange(0, 101, 20))  # guideline every 20%

        # Color only the x-axis labels (not bars)
        ax.tick_params(axis='x', colors='dodgerblue', labelsize=12)
        ax.tick_params(axis='y', labelsize=10)

        # Add gridlines for better visual reference
        ax.grid(axis='y', linestyle='--', alpha=0.7)

        # Show value labels on bars
        for bar in bars:
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f"{bar.get_height():.2f}%", ha='center', va='bottom')

        # Display in Streamlit
        st.pyplot(fig)
def data_kpi_http_dl():
    import streamlit as st
    import pandas as pd
    date_iteration_dict = {"20250101": "20250101", "20250120": "20250120", "20250208": "20250208", "20250226": "20250226", "20250316": "20250316", "20250403": "20250403", "20250421": "20250421", "20250509": "20250509", "20250527": "20250527", "20250614": "20250614", "20250702": "20250702", "20250720": "20250720", "20250807": "20250807", "20250825": "20250825", "20250912": "20250912"}


    # ---- DATA ----
    data = [["FDFS DL Attempts", 13, 12], ["FDFS DL Transfer Cutoff", 0, 0], ["FDFS DL Success", 13, 12], ["FDFS DL Failure", 0, 0], ["FDFS DL Access Failure", 0, 0], ["FDFS DL Access Success", 13, 12], ["FDFS DL Access Failure Ratio", "0.00%", "0.00%"], ["FDFS DL Transfer Cutoff Ratio", "0.00%", "0.00%"], ["FDFS DL Success Ratio", "100.00%", "100.00%"],

        ["FDFS UL Attempts", 13, 12], ["FDFS UL Transfer Cutoff", 0, 0], ["FDFS UL Success", 0, 0], ["FDFS UL Failure", 0, 0], ["FDFS UL Access Failure", 13, 12], ["FDFS UL Access Success", 13, 12], ["FDFS UL Access Failure Ratio", "100.00%", "100.00%"], ["FDFS UL Transfer Cutoff Ratio", "0.00%", "0.00%"], ["FDFS UL Success Ratio", "100.00%", "100.00%"],

        ["FDTT DL Attempts", 14, 13], ["FDTT DL Cutoff", 0, 0], ["FDTT DL Success", 14, 13], ["FDTT DL Failure", 0, 0], ["FDTT DL Access Failure", 0, 0], ["FDTT DL Access Successful", 14, 13], ["FDTT DL Min Data Rate [Mbit/s]", 1.54, 0], ["FDTT DL 5 PCTL Data Rate [Mbit/s]", 6.88, 3.62], ["FDTT DL Average Data Rate [Mbit/s]", 4.66, 2.48], ["FDTT DL Median Data Rate [Mbit/s]", 4.59, 2.67], ["FDTT DL 95 PCTL Data Rate [Mbit/s]", 6.88, 3.62], ["FDTT DL Max Data Rate [Mbit/s]", 7.39, 3.63],
        ["FDTT DL > 100 Mbps", 14, 12], ["FDTT DL > 20 Mbps", 14, 13],

        ["FDTT UL Attempts", 14, 13], ["FDTT UL Cutoff", 0, 0], ["FDTT UL Successful", 0, 0], ["FDTT UL Access Failure", 14, 13], ["FDTT UL Access Success", 0, 0], ["FDTT UL Min Data Rate [Mbit/s]", 0.00, 0], ["FDTT UL 5 PCTL Data Rate [Mbit/s]", 0.16, 0.11], ["FDTT UL Average Data Rate [Mbit/s]", 0.42, 0.25], ["FDTT UL Median Data Rate [Mbit/s]", 0.54, 0.29], ["FDTT UL 95 PCTL Data Rate [Mbit/s]", 0.56, 0.38], ["FDTT UL Max Data Rate [Mbit/s]", 0.56, 0.40], ["FDTT UL > 5 Mbps", 14, 13],
        ["FDTT UL > 2 Mbps", 14, 13], ]

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=["HTTP TRANSFER KPIs", "Telefonica", "1 & 1"])

    # ---- SPLIT INTO DL and UL ----
    df_dl = df[df["HTTP TRANSFER KPIs"].str.contains("DL")]
    df_ul = df[df["HTTP TRANSFER KPIs"].str.contains("UL")]
    st.write("## HTTP TRANSFER KPIs")

    # ---- STYLE ----
    header_style = [{'selector': 'th', 'props': [('background-color', '#d9ead3'), ('font-weight', 'bold'), ('color', 'black')]}]

    col1, col2 = st.columns(2)
    with col1:
        selected_iteration = st.selectbox("Select test date", options=list(date_iteration_dict.keys()), key="data2", index=0)  # Default to 'Road'

        styled_dl = df_dl.style.set_table_styles(header_style)

        # ---- DISPLAY ----

        st.write("### 📥 Downlink (DL) KPIs")
        st.table(styled_dl)
def data_kpi_ping():
    import streamlit as st
    import pandas as pd

    date_iteration_dict = {"20250101": "20250101", "20250120": "20250120", "20250208": "20250208", "20250226": "20250226", "20250316": "20250316", "20250403": "20250403", "20250421": "20250421", "20250509": "20250509", "20250527": "20250527", "20250614": "20250614", "20250702": "20250702", "20250720": "20250720", "20250807": "20250807", "20250825": "20250825", "20250912": "20250912"}


    # Data

    data_ping = [["Ping Attempt", 13, 12], ["Ping Success", 13, 9], ["Ping Failures", 0, 0], ["Ping Success rate", "100.00%", "75.00%"], ["Ping RTT_ms", 2.96, 3.58], ["Ping Trace Loss [%]", "0.00%", "2.50%"]]

    df_ping = pd.DataFrame(data_ping, columns=["PING KPIs", "Telefonica", "1 & 1"])

    # Style only the column headers
    styled_df_ping = df_ping.style.set_table_styles([{'selector': 'th', 'props': [('background-color', '#d9ead3'), ('font-weight', 'bold'), ('color', 'black')]}])

    col1, col2 = st.columns(2)
    with col1:
        selected_iteration = st.selectbox("Select test date", options=list(date_iteration_dict.keys()), key="data3", index=0)  # Default to 'Road'

        st.write("### PING KPIs")
        st.table(styled_df_ping)
def data_kpi_brw():
    import streamlit as st
    import pandas as pd
    date_iteration_dict = {"20250101": "20250101", "20250120": "20250120", "20250208": "20250208", "20250226": "20250226", "20250316": "20250316", "20250403": "20250403", "20250421": "20250421", "20250509": "20250509", "20250527": "20250527", "20250614": "20250614", "20250702": "20250702", "20250720": "20250720", "20250807": "20250807", "20250825": "20250825", "20250912": "20250912"}


    data = [["HTTP Browsing Attempts", 96, 89], ["HTTP Browsing Transfer Cutoff", 0, 0], ["HTTP Browsing Success", 96, 89], ["HTTP Browsing Access Failure", 0, 0], ["HTTP Browsing Access Success", 96, 89], ["HTTP Browsing Access Failure Ratio", 0, 0], ["HTTP Browsing Transfer Cutoff Ratio", 0, 0], ["HTTP Browsing Success Ratio", "100%", "100%"], ["HTTP Browsing Min Transfer Time [s]", 3.68, 3.82], ["HTTP Browsing 10 PCTL Transfer Time [s]", 4.07, 0.00],
        ["HTTP Browsing Average Transfer Time [s]", 5.05, 5.89], ["HTTP Browsing Median Transfer Time [s]", 4.83, 0.00], ["HTTP Browsing 90 PCTL Transfer Time [s]", 5.79, 0.00], ["HTTP Browsing Max Transfer Time [s]", 18.78, 0.00]]

    df = pd.DataFrame(data, columns=["HTTP Browsing KPIs", "Telefonica", "1 & 1"])

    # Style only the column headers
    styled_df = df.style.set_table_styles([{'selector': 'th', 'props': [('background-color', '#d9ead3'), ('font-weight', 'bold'), ('color', 'black')]}])

    col1, col2 = st.columns(2)
    with col1:
        selected_iteration = st.selectbox("Select test date", options=list(date_iteration_dict.keys()), key="data4", index=0)  # Default to 'Road'

        st.write("### HTTP Browsing KPIs")
        st.table(styled_df)
def data_kpi_http_ul():
    import streamlit as st
    import pandas as pd
    date_iteration_dict = {"20250101": "20250101", "20250120": "20250120", "20250208": "20250208", "20250226": "20250226", "20250316": "20250316", "20250403": "20250403", "20250421": "20250421", "20250509": "20250509", "20250527": "20250527", "20250614": "20250614", "20250702": "20250702", "20250720": "20250720", "20250807": "20250807", "20250825": "20250825", "20250912": "20250912"}


    # ---- DATA ----
    data = [["FDFS DL Attempts", 13, 12], ["FDFS DL Transfer Cutoff", 0, 0], ["FDFS DL Success", 13, 12], ["FDFS DL Failure", 0, 0], ["FDFS DL Access Failure", 0, 0], ["FDFS DL Access Success", 13, 12], ["FDFS DL Access Failure Ratio", "0.00%", "0.00%"], ["FDFS DL Transfer Cutoff Ratio", "0.00%", "0.00%"], ["FDFS DL Success Ratio", "100.00%", "100.00%"],

        ["FDFS UL Attempts", 13, 12], ["FDFS UL Transfer Cutoff", 0, 0], ["FDFS UL Success", 0, 0], ["FDFS UL Failure", 0, 0], ["FDFS UL Access Failure", 13, 12], ["FDFS UL Access Success", 13, 12], ["FDFS UL Access Failure Ratio", "100.00%", "100.00%"], ["FDFS UL Transfer Cutoff Ratio", "0.00%", "0.00%"], ["FDFS UL Success Ratio", "100.00%", "100.00%"],

        ["FDTT DL Attempts", 14, 13], ["FDTT DL Cutoff", 0, 0], ["FDTT DL Success", 14, 13], ["FDTT DL Failure", 0, 0], ["FDTT DL Access Failure", 0, 0], ["FDTT DL Access Successful", 14, 13], ["FDTT DL Min Data Rate [Mbit/s]", 1.54, 0], ["FDTT DL 5 PCTL Data Rate [Mbit/s]", 6.88, 3.62], ["FDTT DL Average Data Rate [Mbit/s]", 4.66, 2.48], ["FDTT DL Median Data Rate [Mbit/s]", 4.59, 2.67], ["FDTT DL 95 PCTL Data Rate [Mbit/s]", 6.88, 3.62], ["FDTT DL Max Data Rate [Mbit/s]", 7.39, 3.63],
        ["FDTT DL > 100 Mbps", 14, 12], ["FDTT DL > 20 Mbps", 14, 13],

        ["FDTT UL Attempts", 14, 13], ["FDTT UL Cutoff", 0, 0], ["FDTT UL Successful", 0, 0], ["FDTT UL Access Failure", 14, 13], ["FDTT UL Access Success", 0, 0], ["FDTT UL Min Data Rate [Mbit/s]", 0.00, 0], ["FDTT UL 5 PCTL Data Rate [Mbit/s]", 0.16, 0.11], ["FDTT UL Average Data Rate [Mbit/s]", 0.42, 0.25], ["FDTT UL Median Data Rate [Mbit/s]", 0.54, 0.29], ["FDTT UL 95 PCTL Data Rate [Mbit/s]", 0.56, 0.38], ["FDTT UL Max Data Rate [Mbit/s]", 0.56, 0.40], ["FDTT UL > 5 Mbps", 14, 13],
        ["FDTT UL > 2 Mbps", 14, 13], ]

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=["HTTP TRANSFER KPIs", "Telefonica", "1 & 1"])

    # ---- SPLIT INTO DL and UL ----
    df_dl = df[df["HTTP TRANSFER KPIs"].str.contains("DL")]
    df_ul = df[df["HTTP TRANSFER KPIs"].str.contains("UL")]
    st.write("## HTTP TRANSFER KPIs")

    # ---- STYLE ----
    header_style = [{'selector': 'th', 'props': [('background-color', '#d9ead3'), ('font-weight', 'bold'), ('color', 'black')]}]

    col1, col2 = st.columns(2)

    with col1:
        selected_iteration = st.selectbox("Select test date", options=list(date_iteration_dict.keys()), key="data5", index=0)  # Default to 'Road'

        styled_ul = df_ul.style.set_table_styles(header_style)
        st.write("### 📤 Uplink (UL) KPIs")
        st.table(styled_ul)

