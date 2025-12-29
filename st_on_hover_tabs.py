import streamlit as st
from typing import List, Dict, Any

# Sử dụng emoji hoặc Unicode cho icon chuyên nghiệp hơn
ICON_MAP = {
    "home": "🏠",
    "map": "🗺️",
    "info": "ℹ️",
    "settings": "⚙️",
    "chart": "📊",
    "search": "🔍",
    # Thêm các icon khác nếu cần
}

def on_hover_tabs(tab_names: List[str], icon_names: List[str], styles: Dict[str, Any] = None, default_choice: int = 0):
    # Style chuyên nghiệp cho radio
    st.markdown("""
        <style>
        div[data-testid="stRadio"] > label {
            font-size: 18px;
            font-weight: bold;
            color: #238b45;
            font-family: 'Space Grotesk', sans-serif;
        }
        div[data-testid="stRadio"] div[role="radiogroup"] > label {
            background: #232323;
            color: #A9A9A9;
            border-radius: 8px;
            margin-right: 8px;
            padding: 8px 20px;
            font-size: 17px;
            font-family: 'Space Grotesk', sans-serif;
            transition: background 0.2s, color 0.2s;
        }
        div[data-testid="stRadio"] div[role="radiogroup"] > label[data-selected="true"] {
            background: #238b45;
            color: #fff;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)
    def format_tab(idx):
        icon = ICON_MAP.get(icon_names[idx], icon_names[idx])
        return f"{icon} {tab_names[idx]}"
    selected = st.radio(
        label="",
        options=list(range(len(tab_names))),
        index=default_choice,
        format_func=format_tab,
        horizontal=True
    )
    return tab_names[selected]
