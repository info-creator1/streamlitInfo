import streamlit as st
import base64

st.title("🌈 3D Teddy Bear Viewer")

# Load GLB as binary and encode to base64
with open("Teddy.glb", "rb") as f:
    glb_bytes = f.read()
glb_b64 = base64.b64encode(glb_bytes).decode()

# Embed GLB in model-viewer
html_code = f"""
<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
<model-viewer src="data:model/gltf-binary;base64,{glb_b64}"
              alt="Teddy Bear"
              auto-rotate
              camera-controls
              background-color="#70BCD1"
              style="width: 100%; height: 600px;">
</model-viewer>
"""

st.components.v1.html(html_code, height=650)
