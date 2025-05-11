
import streamlit as st

st.set_page_config(page_title="IA DJ Jukebox", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""<h1 style='text-align: center; color: white;'>IA DJ Jukebox</h1>""", unsafe_allow_html=True)
st.markdown("""<p style='text-align: center;'>Crée ton ambiance musicale avec intelligence artificielle</p>""", unsafe_allow_html=True)

univers = ["Rock", "Électro", "Rap", "Latino", "Jazz", "Afrika", "Caraïbes", "Underground"]
selected_univers = st.selectbox("Choisis ton univers musical", univers)

ambiances = ["Nostalgique", "Chill", "Luxe", "Festif", "Corporate", "Sensuel"]
selected_ambiance = st.selectbox("Choisis une ambiance", ambiances)

if st.button("Générer ta vibe"):
    st.success(f"Playlist générée pour : {selected_univers} - Ambiance {selected_ambiance}")
    st.write("1. Titre A\n2. Titre B\n3. Titre C")
    st.image("https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4", caption="Ambiance visuelle")
