import pandas as pd, streamlit as st, PoC_IRAQ_DT_Auto_lib_2 as pidal2

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
        dataframes.append(pd.read_csv(r"\20240715_Dusseldorf_CDRData_1N1_filtered.csv", low_memory=False))
        dataframes.append(pd.read_csv(r"\20240715_Dusseldorf_CDRData_O2_filtered.csv", low_memory=False))

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

    if st.button("Show LTE Plots and Statistics in comparison view", key = "3gplots"):
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




