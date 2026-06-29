import streamlit as st
import base64

st.set_page_config(page_title="Attenu Suite", layout="centered")

# --- HELPER: ENCODE LOCAL SVG TO BASE64 IMAGE DATA ---
def get_svg_html_img(file_path):
    try:
        with open(file_path, "rb") as f:
            svg_bytes = f.read()
        b64 = base64.b64encode(svg_bytes).decode("utf-8")
        return f'<img src="data:image/svg+xml;base64,{b64}" style="width: 100%; height: auto; display: block;" />'
    except FileNotFoundError:
        return None

# --- CUSTOM CSS FOR CLEAN HOVER EFFECTS ---
st.markdown("""
    <style>
    .brand-button {
        display: block;
        background-color: #111827;
        border: 2px solid #1f2937;
        border-radius: 12px;
        padding: 12px;
        transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
        text-decoration: none !important;
        margin-bottom: 20px;
    }
    .brand-button:hover {
        transform: translateY(-5px);
        border-color: #374151;
        box-shadow: 0 10px 25px -5px rgba(0, 243, 255, 0.15);
    }
    </style>
""", unsafe_allow_html=True)

# --- HUB HEADER ---
suite_banner = get_svg_html_img("Attenu_Suite_Banner.svg")

if suite_banner:
    # Render full width clean layout banner frame
    st.markdown(f'<div style="max-width: 800px; margin: 0 auto;">{suite_banner}</div>', unsafe_allow_html=True)
else:
    st.title("🔬 Attenu Suite")
    st.caption("RADIATION & PARTICLE INTERACTION SIMULATION SYSTEM")

st.markdown("<hr style='border-color: #1f2937;'>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# --- CONFIGURATION: DEPLOYED URLS ---
ATTENUX_URL = "https://attenux.streamlit.app"
ATTENUE_URL = "https://attenue.streamlit.app"

# --- SYSTEM ROUTER GRID ---
col_x, col_e = st.columns(2)

with col_x:
    attenux_img = get_svg_html_img("AttenuX_Logo.svg")
    if attenux_img:
        st.markdown(f'''
            <a href="{ATTENUX_URL}" target="_blank" class="brand-button">
                {attenux_img}
                <br>
                <p style='text-align: center; color: #ffffff;'>X-Ray Cross-Section and Attenuation</p>
            </a>
        ''', unsafe_allow_html=True)
    else:
        st.warning("AttenuX_Logo.svg not found.")
        st.link_button("Launch AttenuX 🔬", ATTENUX_URL, use_container_width=True)

with col_e:
    attenue_img = get_svg_html_img("AttenuE_Logo.svg")
    if attenue_img:
        st.markdown(f'''
            <a href="{ATTENUE_URL}" target="_blank" class="brand-button">
                {attenue_img}
                <br>
                <p style='text-align: center; color: #ffffff;'>Electron Trajactory and Attenuation</p>
            </a>
        ''', unsafe_allow_html=True)
    else:
        st.warning("AttenuE_Logo.svg not found.")
        st.link_button("Launch AttenuE ⚡", ATTENUE_URL, use_container_width=True)

# --- FOOTER ---
st.markdown("<hr style='border-color: #1f2937;'>", unsafe_allow_html=True)
st.caption("<p style='text-align: center; color: #334155;'>Created By: Declan Hughes (2026)</p>", unsafe_allow_html=True)