# Categorizers
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
def categorize_Technology_Detail(value):
    match value:
        case value if value >= "LTE":
            return [0, 0, 255]  # Blue
        case value if value >= "EN-DC":
            return [255, 69, 0] # OrangeRed
        case _:
            return [128, 0, 0]  # Maroon
def categorize_rxlev(value):
    match value:
        case value if value >= -60:
            return [0, 0, 255]    # Excellent (Blue)
        case value if value >= -70:
            return [0, 176, 240]  # Very Good (Light Blue)
        case value if value >= -80:
            return [0, 255, 255]  # Good (Cyan)
        case value if value >= -90:
            return [0, 176, 80]   # Fair (Green)
        case value if value >= -100:
            return [146, 208, 80] # Poor (Light Green)
        case value if value >= -105:
            return [255, 255, 0]  # Very Poor (Yellow)
        case value if value >= -110:
            return [237, 125, 49] # Bad (Orange)
        case value if value < -110:
            return [255, 0, 0]    # No Coverage (Red)
        case _:
            return [0, 0, 0]      # Invalid (Black)
def categorize_rxqual(value):
    match value:
        case value if value <= 0:
            return [0, 0, 255]    # Excellent (Blue)
        case value if value <= 1:
            return [0, 176, 240]  # Very Good (Light Blue)
        case value if value <= 2:
            return [0, 255, 255]  # Good (Cyan)
        case value if value <= 3:
            return [0, 176, 80]   # Fair (Green)
        case value if value <= 4:
            return [146, 208, 80] # Poor (Light Green)
        case value if value <= 5:
            return [255, 255, 0]  # Very Poor (Yellow)
        case value if value <= 6:
            return [237, 125, 49] # Bad (Orange)
        case value if value >= 7:
            return [255, 0, 0]    # Unusable (Red)
        case _:
            return [0, 0, 0]      # Invalid (Black)

def categorize_wcdma_rsrp(value):
    match value:
        case value if value >= -70:
            return [0, 0, 255]    # Blue
        case value if value >= -80:
            return [0, 176, 240]  # Light Blue
        case value if value >= -90:
            return [0, 255, 255]  # Cyan
        case value if value >= -100:
            return [0, 176, 80]   # Green
        case value if value >= -105:
            return [146, 208, 80] # Light Green
        case value if value >= -110:
            return [255, 255, 0]  # Yellow
        case value if value >= -115:
            return [237, 125, 49] # Orange
        case value if value < -115:
            return [255, 0, 0]    # Red
        case _:
            return [0, 0, 0]
def categorize_wcdma_rsrq(value):
    match value:
        case value if value >= -6:
            return [0, 0, 255]    # Blue
        case value if value >= -9:
            return [0, 176, 240]  # Light Blue
        case value if value >= -11:
            return [0, 255, 255]  # Cyan
        case value if value >= -13:
            return [0, 176, 80]   # Green
        case value if value >= -15:
            return [146, 208, 80] # Light Green
        case value if value >= -17:
            return [255, 255, 0]  # Yellow
        case value if value >= -19:
            return [237, 125, 49] # Orange
        case value if value < -19:
            return [255, 0, 0]    # Red
        case _:
            return [0, 0, 0]
def categorize_wcdma_rssi(value):
    match value:
        case value if value >= -60:
            return [0, 0, 255]    # Blue
        case value if value >= -70:
            return [0, 176, 240]  # Light Blue
        case value if value >= -80:
            return [0, 255, 255]  # Cyan
        case value if value >= -90:
            return [0, 176, 80]   # Green
        case value if value >= -100:
            return [146, 208, 80] # Light Green
        case value if value >= -105:
            return [255, 255, 0]  # Yellow
        case value if value >= -110:
            return [237, 125, 49] # Orange
        case value if value < -110:
            return [255, 0, 0]    # Red
        case _:
            return [0, 0, 0]


# Color Patches
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
def get_rxlev_color_patches():
    import matplotlib.patches as mpatches
    color_patches_rxlev = [
        mpatches.Patch(color='#0000FF', label='>= -60 (Blue)'),        # Excellent
        mpatches.Patch(color='#00B0F0', label='-60 to -70 (Light Blue)'),  # Very Good
        mpatches.Patch(color='#00FFFF', label='-70 to -80 (Cyan)'),        # Good
        mpatches.Patch(color='#00B050', label='-80 to -90 (Green)'),       # Fair
        mpatches.Patch(color='#92D050', label='-90 to -100 (Light Green)'),# Poor
        mpatches.Patch(color='#FFFF00', label='-100 to -105 (Yellow)'),    # Very Poor
        mpatches.Patch(color='#ED7D31', label='-105 to -110 (Orange)'),    # Bad
        mpatches.Patch(color='#FF0000', label='< -110 (Red)')              # No Coverage
    ]
    return color_patches_rxlev
def get_rxqual_color_patches():
    import matplotlib.patches as mpatches
    color_patches_rxqual = [
        mpatches.Patch(color='#0000FF', label='0 (Excellent, Blue)'),
        mpatches.Patch(color='#00B0F0', label='1 (Very Good, Light Blue)'),
        mpatches.Patch(color='#00FFFF', label='2 (Good, Cyan)'),
        mpatches.Patch(color='#00B050', label='3 (Fair, Green)'),
        mpatches.Patch(color='#92D050', label='4 (Poor, Light Green)'),
        mpatches.Patch(color='#FFFF00', label='5 (Very Poor, Yellow)'),
        mpatches.Patch(color='#ED7D31', label='6 (Bad, Orange)'),
        mpatches.Patch(color='#FF0000', label='7 (Unusable, Red)')
    ]
    return color_patches_rxqual

def get_wcdma_rsrp_color_patches():
    import matplotlib.patches as mpatches
    color_patches = [
        mpatches.Patch(color='#0000FF', label='>= -70 (Blue)'),
        mpatches.Patch(color='#00B0F0', label='-70 to -80 (Light Blue)'),
        mpatches.Patch(color='#00FFFF', label='-80 to -90 (Cyan)'),
        mpatches.Patch(color='#00B050', label='-90 to -100 (Green)'),
        mpatches.Patch(color='#92D050', label='-100 to -105 (Light Green)'),
        mpatches.Patch(color='#FFFF00', label='-105 to -110 (Yellow)'),
        mpatches.Patch(color='#ED7D31', label='-110 to -115 (Orange)'),
        mpatches.Patch(color='#FF0000', label='< -115 (Red)')
    ]
    return color_patches
def get_wcdma_rsrq_color_patches():
    import matplotlib.patches as mpatches
    color_patches = [
        mpatches.Patch(color='#0000FF', label='>= -6 (Blue)'),
        mpatches.Patch(color='#00B0F0', label='-6 to -9 (Light Blue)'),
        mpatches.Patch(color='#00FFFF', label='-9 to -11 (Cyan)'),
        mpatches.Patch(color='#00B050', label='-11 to -13 (Green)'),
        mpatches.Patch(color='#92D050', label='-13 to -15 (Light Green)'),
        mpatches.Patch(color='#FFFF00', label='-15 to -17 (Yellow)'),
        mpatches.Patch(color='#ED7D31', label='-17 to -19 (Orange)'),
        mpatches.Patch(color='#FF0000', label='< -19 (Red)')
    ]
    return color_patches
def get_wcdma_rssi_color_patches():
    import matplotlib.patches as mpatches
    color_patches = [
        mpatches.Patch(color='#0000FF', label='>= -60 (Blue)'),
        mpatches.Patch(color='#00B0F0', label='-60 to -70 (Light Blue)'),
        mpatches.Patch(color='#00FFFF', label='-70 to -80 (Cyan)'),
        mpatches.Patch(color='#00B050', label='-80 to -90 (Green)'),
        mpatches.Patch(color='#92D050', label='-90 to -100 (Light Green)'),
        mpatches.Patch(color='#FFFF00', label='-100 to -105 (Yellow)'),
        mpatches.Patch(color='#ED7D31', label='-105 to -110 (Orange)'),
        mpatches.Patch(color='#FF0000', label='< -110 (Red)')
    ]
    return color_patches


# Other functions

def calculate_zoom_level(lat_diff, lon_diff):
    max_dim = max(lat_diff, lon_diff)
    if max_dim < 0.0001:
        return 21  # Maximum zoom level for very close points
    return min(15, max(1, 11 - (max_dim * 2)))
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
        "NR RSRQ": {"Parameter_Name": "NR Serving Cell SS RSRQ Top #1", "Subheader": "RSRQ Color Schema", "Chart Type": "NR Serving Cell SS RSRQ", "Color_path_Function": get_rsrq_color_patches(), "Color function": categorize_rsrq},
        "NR RSRP": {"Parameter_Name": "NR Serving Cell SS RSRP Top #1", "Subheader": "RSRP Color Schema", "Chart Type": "NR Serving Cell SS RSRP", "Color_path_Function": get_rsrp_color_patches(), "Color function": categorize_rsrp},
        "NR SINR": {"Parameter_Name": "MR-DC Cell 1 SINR (dB)", "Subheader": "SINR Color Schema", "Chart Type": "MR-DC Cell 1 SINR (dB)", "Color_path_Function": get_sinr_color_patches(), "Color function": categorize_sinr},
        "NR Throughput": {"Parameter_Name": "NR MAC DL Throughput Total (kbps)", "Subheader": "NR MAC DL Color Schema", "Chart Type": "NR MAC DL Throughput Total (kbps)", "Color_path_Function": get_throughput_color_patches(), "Color function": categorize_throughput},
        "LTE RSRQ": {"Parameter_Name": "LTE Serving Cell RSRQ (dB)", "Subheader": "RSRQ Color Schema", "Chart Type": "LTE Serving Cell RSRQ (dB)", "Color_path_Function": get_rsrq_color_patches(), "Color function": categorize_rsrq},
        "LTE RSRP": {"Parameter_Name": "LTE Serving Cell RSRP (dBm)", "Subheader": "RSRP Color Schema", "Chart Type": "LTE Serving Cell RSRP (dBm)", "Color_path_Function": get_rsrp_color_patches(), "Color function": categorize_rsrp},
        "LTE SINR": {"Parameter_Name": "LTE Serving Cell RS SINR (dB)", "Subheader": "SINR Color Schema", "Chart Type": "LTE Serving Cell RS SINR (dB)", "Color_path_Function": get_sinr_color_patches(), "Color function": categorize_sinr},
        "LTE Throughput": {"Parameter_Name": "LTE MAC DL Throughput (kbps)", "Subheader": "LTE MAC DL Color Schema", "Chart Type": "LTE MAC DL Throughput (kbps)", "Color_path_Function": get_throughput_color_patches(), "Color function": categorize_throughput},
        "Tech Details": {"Parameter_Name": "Technology_Detail", "Subheader": "Technology Detail Color Schema", "Chart Type": "Technology_Detail", "Color_path_Function": get_tech_detail_color_patches(), "Color function": categorize_Technology_Detail}}

    parameter_mapping = {"NR RSRQ": {"Parameter_Name": "NR Serving Cell SS RSRQ Top #1", "Subheader": "RSRQ Color Schema", "Chart Type": "NR Serving Cell SS RSRQ", "Color_path_Function": get_rsrq_color_patches(), "Color function": categorize_rsrq}, "NR RSRP": {"Parameter_Name": "NR Serving Cell SS RSRP Top #1", "Subheader": "RSRP Color Schema", "Chart Type": "NR Serving Cell SS RSRP", "Color_path_Function": get_rsrp_color_patches(), "Color function": categorize_rsrp},
        "NR SINR": {"Parameter_Name": "MR-DC Cell 1 SINR (dB)", "Subheader": "SINR Color Schema", "Chart Type": "MR-DC Cell 1 SINR (dB)", "Color_path_Function": get_sinr_color_patches(), "Color function": categorize_sinr}, "NR Throughput": {"Parameter_Name": "NR MAC DL Throughput Total (kbps)", "Subheader": "NR MAC DL Color Schema", "Chart Type": "NR MAC DL Throughput Total (kbps)", "Color_path_Function": get_throughput_color_patches(), "Color function": categorize_throughput},
        "LTE RSRQ": {"Parameter_Name": "LTE Serving Cell RSRQ (dB)", "Subheader": "RSRQ Color Schema", "Chart Type": "LTE Serving Cell RSRQ (dB)", "Color_path_Function": get_rsrq_color_patches(), "Color function": categorize_rsrq}, "LTE RSRP": {"Parameter_Name": "LTE Serving Cell RSRP (dBm)", "Subheader": "RSRP Color Schema", "Chart Type": "LTE Serving Cell RSRP (dBm)", "Color_path_Function": get_rsrp_color_patches(), "Color function": categorize_rsrp},
        "LTE SINR": {"Parameter_Name": "LTE Serving Cell RS SINR (dB)", "Subheader": "SINR Color Schema", "Chart Type": "LTE Serving Cell RS SINR (dB)", "Color_path_Function": get_sinr_color_patches(), "Color function": categorize_sinr}, "LTE Throughput": {"Parameter_Name": "LTE MAC DL Throughput (kbps)", "Subheader": "LTE MAC DL Color Schema", "Chart Type": "LTE MAC DL Throughput (kbps)", "Color_path_Function": get_throughput_color_patches(), "Color function": categorize_throughput},
        "Tech Details": {"Parameter_Name": "Technology_Detail", "Subheader": "Technology Detail Color Schema", "Chart Type": "Technology_Detail", "Color_path_Function": get_tech_detail_color_patches(), "Color function": categorize_Technology_Detail},

        # --- Newly added GSM parameters ---
        "GSM RxLev Full": {"Parameter_Name": "RxLevFull (dBm) - .Server", "Subheader": "RxLev Full Color Schema", "Chart Type": "RxLevFull (dBm) - .Server", "Color_path_Function": get_rxlev_color_patches(), "Color function": categorize_rxlev},
        "GSM RxLev Sub": {"Parameter_Name": "RxLevSub (dBm) - .Server", "Subheader": "RxLev Sub Color Schema", "Chart Type": "RxLevSub (dBm) - .Server", "Color_path_Function": get_rxlev_color_patches(), "Color function": categorize_rxlev},
        "GSM RxQual Full": {"Parameter_Name": "RxQual Full", "Subheader": "RxQual Full Color Schema", "Chart Type": "RxQual Full", "Color_path_Function": get_rxqual_color_patches(), "Color function": categorize_rxqual},
        "GSM RxQual Sub": {"Parameter_Name": "RxQual Sub", "Subheader": "RxQual Sub Color Schema", "Chart Type": "RxQual Sub", "Color_path_Function": get_rxqual_color_patches(), "Color function": categorize_rxqual},
        "WCDMA RSRP": {
        "Parameter_Name": "Serving Cell RSRP (dBm)",
        "Subheader": "RSRP Color Schema",
        "Chart Type": "Serving Cell RSRP (dBm)",
        "Color_path_Function": get_wcdma_rsrp_color_patches(),
        "Color function": categorize_wcdma_rsrp
    },
        "WCDMA RSRQ": {
        "Parameter_Name": "Serving Cell RSRQ (dB)",
        "Subheader": "RSRQ Color Schema",
        "Chart Type": "Serving Cell RSRQ (dB)",
        "Color_path_Function": get_wcdma_rsrq_color_patches(),
        "Color function": categorize_wcdma_rsrq
    },
        "WCDMA RSSI": {
        "Parameter_Name": "Serving RSSI (dBm)",
        "Subheader": "RSSI Color Schema",
        "Chart Type": "Serving RSSI (dBm)",
        "Color_path_Function": get_wcdma_rssi_color_patches(),
        "Color function": categorize_wcdma_rssi
    }
    }

    return parameter_mapping.get(parameter, "Invalid parameter")
def plot_color_patches(legend_handles):
    import matplotlib.pyplot as plt
    import streamlit as st
    fig, ax = plt.subplots(figsize=(10, 1))
    ax.legend(handles=legend_handles, loc='upper left')
    ax.axis('off')
    st.pyplot(fig)

