import streamlit as st

st.set_page_config(page_title="3D Teddy Bear Viewer")
st.title("🌈 3D Teddy Bear (Interactive)")

# Path to your GLB file
glb_file = "Untitled.glb"  # Put teddy.glb in the same folder as this script

# HTML code using <model-viewer>
html_code = f"""
<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>

<model-viewer src="{glb_file}" 
              alt="Teddy Bear"
              auto-rotate
              camera-controls
              background-color="#70BCD1"
              style="width: 100%; height: 600px;">
</model-viewer>
"""

st.components.v1.html(html_code, height=650)
