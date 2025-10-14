import streamlit as st

st.title("🌈 3D Teddy Bear Viewer")

html_code = """
<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
<model-viewer src="Teddy.glb" alt="Teddy Bear"
              auto-rotate camera-controls
              background-color="#70BCD1"
              style="width: 100%; height: 600px;">
</model-viewer>
"""

st.components.v1.html(html_code, height=650)
