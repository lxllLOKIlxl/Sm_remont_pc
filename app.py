import streamlit as st

# --- Логотип ---
st.image("assets/logo.png", use_column_width=True)

st.markdown("<h1 style='text-align:center;color:#eeb96b;'>Sm_remont_pc – Наші послуги</h1>", unsafe_allow_html=True)

# --- Банери (3 в ряд) ---
cols = st.columns(3)
banners = ["assets/banner1.png", "assets/banner2.png", "assets/banner3.png"]
titles = ["Послуга 1", "Послуга 2", "Послуга 3"]

for i, col in enumerate(cols):
    with col:
        st.image(banners[i], use_column_width=True)
        st.caption(titles[i])

# --- Банери (2 в ряд) ---
cols2 = st.columns(2)
banners2 = ["assets/banner4.png", "assets/banner5.png"]
titles2 = ["Послуга 4", "Послуга 5"]

for i, col in enumerate(cols2):
    with col:
        st.image(banners2[i], use_column_width=True)
        st.caption(titles2[i])

# --- Відео ---
st.markdown("<h2 style='text-align:center;color:#ffb700;'>Демонстраційне відео</h2>", unsafe_allow_html=True)
st.video("assets/video.mp4")

# --- Footer ---
st.markdown("---")
st.caption("© Sm_remont_pc | Автор: Шаблінський, 2 курс")
