import streamlit as st
from streamlit_option_menu import option_menu
import PoC_IRAQ_DT_Auto_lib as pidtal

# Set page configuration
st.set_page_config(page_title="Drive Test Analytics Automation Suite for Smart RAN", layout="wide", initial_sidebar_state="expanded", page_icon="📶")

# config = pidtal.read_config_file(r'C:\Users\barba\Documents\01_Job\2025_Predictive_Tool\Predran_Configuration.csv')
# Define menu structure

menu_sections = {
    "Dashboard": {
        "title": "🏠 Drive Test Analytics Automation Suite for Smart RAN",
        "subsections": {},
        "icon": "home"
    },
    "Data Upload": {
        "title": "📁 Upload Drive Test & KPI Data",
        "subsections": {
            "Logfiles": "Upload raw logfiles to server",
            "Reference Data": "Optional site list, coverage grids, thresholds"
        },
        "icon": "upload"
    },
    "Coverage Statistics": {
        "title": "📶 Coverage & Call Statistics",
        "subsections": {
            "2G Coverage": "Voice call coverage & quality KPIs",
            "3G Coverage": "CS + PS call stats and KPIs",
            "4G Coverage": "LTE coverage and RSRP/RSRQ metrics",
            "5G Coverage": "NR coverage and RSRP/RSRQ metrics"
        },
        "icon": "signal"
    },
    "Data KPIs": {
        "title": "📊 Data Service KPIs",
        "subsections": {
            "General Data Test": "Network Test Summary",
            "Ping": "Latency & round-trip time measurements",
            "HTTP Browsing": "Page load success and response time",
            "HTTP Download": "Throughput and session stats for DL",
            "HTTP Upload": "Throughput and session stats for UL"
        },
        "icon": "bar-chart"
    },
    "Capacity": {
        "title": "📈 Capacity Testing",
        "subsections": {
            "Capacity Download": "Max achievable DL throughput",
            "Capacity Upload": "Max achievable UL throughput"
        },
        "icon": "activity"
    },
    "Device Stats": {
        "title": "📱 Device Performance",
        "subsections": {
            "Phone Temperature": "Thermal profile during tests"
        },
        "icon": "smartphone"
    },
    "Export & Reports": {
        "title": "📤 Export Processed Reports",
        "subsections": {
            "Auto Reports": "Generate summary PDF reports",
            "Raw Exports": "CSV / Excel exports of KPIs",
            "Map Snapshots": "Coverage heatmaps and KPI overlays"
        },
        "icon": "download"
    },
    "Help": {
        "title": "ℹ️ Help & Documentation",
        "subsections": {
            "About the Tool": "Overview of tool capabilities",
            "Sample Workflow": "Step-by-step usage instructions",
            "Contact & Support": "Reach out for issues or questions"
        },
        "icon": "info"
    }
}


# Create sidebar menu
with st.sidebar:
    st.title("Drive Test Analytics Automation Suite for Smart RAN")
    selected = option_menu(
        menu_title="Main Modules",
        options=list(menu_sections.keys()),
        # options=[menu_sections[x]["title"] for x in menu_sections],
        icons=[menu_sections[x]["icon"] for x in menu_sections],
        menu_icon="wifi", default_index=0,
        styles={}
)

section = menu_sections[selected]

# Display main section title
st.title(section["title"])

# config = raapoc.read_config_file(r'C:\Users\barba\Documents\01_Job\2025_Predictive_Tool\Predran_Configuration.csv')

if selected == "Dashboard":
    pidtal.dashboard()


for subsection, content in section["subsections"].items():
    st.subheader(subsection)
    items = content.split(",")
    for i in items:
        st.write(i)
        with st.expander("Click to expand/Collapse", expanded=False):  # plain text title, not markdown
            if i == "LTE coverage and RSRP/RSRQ metrics":
                st.write("LTE coverage and RSRP/RSRQ metrics")
                pidtal.LTE_coverage()
            if i == "NR coverage and RSRP/RSRQ metrics":
                st.write("NR coverage and RSRP/RSRQ metrics")
                pidtal.NR_coverage()
            if i == "Voice call coverage & quality KPIs":
                st.write("Voice call coverage & quality KPIs")
                pidtal.GSM_coverage()
            if i =="CS + PS call stats and KPIs":
                st.write("CS + PS call stats and KPIs")
                pidtal.WCDMA3G_coverage()
            if i == "Network Test Summary":
                pidtal.data_kpi_general()
            if i == "Throughput and session stats for DL":
                pidtal.data_kpi_http_dl()
            if i == "Latency & round-trip time measurements":
                pidtal.data_kpi_ping()
            if i == "Page load success and response time":
                pidtal.data_kpi_brw()
            if i == "Throughput and session stats for UL":
                pidtal.data_kpi_http_ul()
            else:
                st.write("")