import streamlit as st
import base64

st.set_page_config(page_title="🎨 3D Character Playground")

st.title("🌈 3D Character Playground")

# --- Step 1: Upload GLB file ---
glb_file = st.file_uploader("Upload your GLB character", type=["glb"])
if glb_file is not None:
    glb_bytes = glb_file.read()
    glb_b64 = base64.b64encode(glb_bytes).decode()

    # --- Step 2: Color pickers for body parts ---
    st.subheader("Pick colors for body parts")
    body_color = st.color_picker("Body", "#ff6600")
    head_color = st.color_picker("Head", "#ffcc99")
    ears_color = st.color_picker("Ears", "#ff9999")

    # --- Step 3: Animation controls ---
    st.subheader("Animations")
    play_animation = st.checkbox("Play animation", value=True)

    # --- Step 4: Generate HTML with model-viewer ---
    html_code = f"""
    <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
    <model-viewer id="character" 
                  src="data:model/gltf-binary;base64,{glb_b64}" 
                  alt="3D Character"
                  camera-controls
                  auto-rotate
                  style="width: 100%; height: 600px;"
                  shadow-intensity="1"
                  exposure="1"
                  animation-name="">
    </model-viewer>

    <script>
        const model = document.querySelector('#character');

        // Play/Pause animation
        const playAnim = {str(play_animation).lower()};
        if(playAnim) {{
            model.play();
        }} else {{
            model.pause();
        }}

        // Change colors dynamically
        function setMaterialColor(materialName, hexColor) {{
            const material = model.model.materials.find(m => m.name === materialName);
            if(material) {{
                const [r,g,b] = hexColor.match(/.{2}/g).map(h => parseInt(h,16)/255);
                material.pbrMetallicRoughness.baseColorFactor = [r,g,b,1];
            }}
        }}

        setMaterialColor("Body", "{body_color[1:]}");
        setMaterialColor("Head", "{head_color[1:]}");
        setMaterialColor("Ears", "{ears_color[1:]}");
    </script>
    """

    st.components.v1.html(html_code, height=650)

else:
    st.info("Please upload a GLB file to see your 3D character!")
