from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PDFWix Learning Hub", page_icon="📄", layout="wide")

html_path = Path(__file__).with_name("index.html")
html_content = html_path.read_text(encoding="utf-8")

st.title("📄 PDFWix Learning Hub")
st.caption("This page is now powered by the previously created HTML design and is ready to publish.")

components.v1.html(html_content, height=6200, scrolling=True)
