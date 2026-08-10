"""
Test standalone du look "Terminal de trading" pour Dashboard BW.

Lance avec :  streamlit run terminal_theme_test.py

Ce fichier ne touche pas à tes vraies données (CSV / API de prix) — c'est
juste une démo du thème avec des valeurs d'exemple, pour que tu puisses
voir le rendu avant de l'appliquer sur le vrai dashboard.
"""

import streamlit as st

# ---------------------------
# Thème "Terminal de trading"
# ---------------------------
TERMINAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&display=swap');

:root {
  --term-bg: #000000;
  --term-bg-2: #080a08;
  --term-border: #1a2e22;
  --term-border-soft: #10190f;
  --term-text: #e8e8e8;
  --term-muted: #5a6f62;
  --term-green: #39ff8f;
  --term-red: #ff4d4d;
  --term-amber: #e8c547;
}

html, body, [class*="css"] {
  font-family: 'JetBrains Mono', 'Courier New', monospace !important;
}

.stApp {
  background: var(--term-bg);
  color: var(--term-text);
}

h1, h2, h3 {
  letter-spacing: 0.04em;
  font-weight: 600 !important;
  color: var(--term-text);
}

.block-container {
  padding-top: 1.5rem;
  max-width: 1200px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
  background: var(--term-bg-2);
  border-right: 1px solid var(--term-border);
}

/* Buttons */
.stButton > button {
  border-radius: 2px !important;
  border: 1px solid var(--term-border) !important;
  background: var(--term-bg-2) !important;
  color: var(--term-green) !important;
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 12px !important;
}
.stButton > button:hover {
  border-color: var(--term-green) !important;
  background: rgba(57,255,143,0.08) !important;
}

/* Tabs */
button[data-baseweb="tab"] {
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 11px !important;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--term-muted) !important;
  border-radius: 0 !important;
}
button[data-baseweb="tab"][aria-selected="true"] {
  color: var(--term-green) !important;
}
div[data-baseweb="tab-highlight"] {
  background: var(--term-green) !important;
  height: 2px !important;
  border-radius: 0 !important;
}
div[data-baseweb="tab-list"] {
  border-bottom: 1px solid var(--term-border);
}

/* Metric cards */
div[data-testid="stMetric"] {
  background: var(--term-bg);
  border: 1px solid var(--term-border);
  border-radius: 0;
  padding: 10px 12px;
}

/* HTML tables */
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 11px;
}
thead tr { border-bottom: 1px solid var(--term-border); }
thead th {
  text-align: left !important;
  font-weight: 400 !important;
  color: var(--term-muted) !important;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  padding: 6px 8px !important;
}
tbody td {
  text-align: left !important;
  padding: 6px 8px !important;
  border-bottom: 1px solid var(--term-border-soft);
  color: var(--term-text);
}

/* Tuiles */
.term-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1px;
  background: var(--term-border);
  margin-bottom: 4px;
}
.term-tile {
  background: var(--term-bg);
  padding: 10px 12px;
  border-left: 2px solid var(--term-border);
}
.term-tile-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 6px;
}
.term-tile-title {
  font-size: 12px;
  color: var(--term-text);
}
.term-tile-badge {
  font-size: 11px;
  font-weight: 600;
}
.term-tile-sub {
  font-size: 9.5px;
  color: var(--term-muted);
}

/* Barre cash / positions */
.term-gauge-track {
  height: 4px;
  background: var(--term-border);
  margin: 6px 0 4px 0;
}
.term-gauge-fill {
  height: 4px;
  background: var(--term-green);
}
</style>
"""

st.set_page_config(page_title="Dashboard BW — Terminal", page_icon="📈", layout="wide")
st.markdown(TERMINAL_CSS, unsafe_allow_html=True)

with st.sidebar:
    st.header("PARAMETRES")
    st.selectbox("DEVISE", options=["USD", "EUR"], index=0)
    st.toggle("AUTO-REFRESH", value=True)
    st.button("RAFRAICHIR")
    st.caption("ACTUALISE 13:41:32")

st.markdown(
    '<div style="display:flex; justify-content:space-between; align-items:baseline; '
    'margin-bottom:14px; padding-bottom:10px; border-bottom:1px solid var(--term-border);">'
    '<div style="font-size:15px; color:var(--term-green); letter-spacing:0.06em;">DASHBOARD_BW</div>'
    '<div style="font-size:10px; color:var(--term-muted);">ACTUALISE 13:41:32</div>'
    '</div>',
    unsafe_allow_html=True,
)

# ---------------------------
# Cartes metriques
# ---------------------------
cards = [
    ("PROFIT_NET_TOTAL", "+$61,068", "var(--term-green)"),
    ("VALEUR_CRYPTO", "$63,992", "var(--term-text)"),
    ("CASH_DISPO", "$69,788", "var(--term-text)"),
]
cols = st.columns(3)
for col, (label, value, color) in zip(cols, cards):
    with col:
        st.markdown(
            f'<div style="background:var(--term-bg); border:1px solid var(--term-border); padding:12px 14px;">'
            f'<div style="font-size:9.5px; color:var(--term-muted); text-transform:uppercase; margin-bottom:6px;">{label}</div>'
            f'<div style="font-size:20px; font-weight:700; color:{color};">{value}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

# ---------------------------
# Total + mode
# ---------------------------
st.markdown(
    '<div style="background:var(--term-bg-2); border:1px solid var(--term-border); padding:12px 14px; margin-top:1px; margin-bottom:16px;">'
    '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">'
    '<span style="font-size:9.5px; color:var(--term-muted);">TOTAL: <span style="color:var(--term-text); font-size:14px;">$133,780</span></span>'
    '<span style="font-size:11px; color:var(--term-amber);">MODE_EQUILIBRE</span>'
    '</div>'
    '<div class="term-gauge-track"><div class="term-gauge-fill" style="width:52%;"></div></div>'
    '<div style="display:flex; justify-content:space-between; font-size:9px; color:var(--term-muted); margin-top:3px;">'
    '<span>CASH 52%</span><span>POS 48%</span>'
    '</div>'
    '</div>',
    unsafe_allow_html=True,
)

# ---------------------------
# Tabs
# ---------------------------
tab1, tab2 = st.tabs(["PORTEFEUILLE", "VENTES_REALISEES"])

with tab1:
    st.markdown('<div style="font-size:11px; color:var(--term-muted); margin-bottom:8px;">// POSITIONS</div>', unsafe_allow_html=True)

    positions = [
        {"token": "NOCK", "roi": "-68.6%", "color": "var(--term-red)", "sub": "QTY 3467886 · VAL $33,000"},
        {"token": "FWA", "roi": "-12.8%", "color": "var(--term-red)", "sub": "QTY 1203305 · VAL $28,627"},
    ]
    tiles_html = '<div class="term-grid">'
    for p in positions:
        tiles_html += (
            f'<div class="term-tile" style="border-left-color:{p["color"]};">'
            f'<div class="term-tile-head">'
            f'<span class="term-tile-title">{p["token"]}</span>'
            f'<span class="term-tile-badge" style="color:{p["color"]};">{p["roi"]}</span>'
            f'</div>'
            f'<div class="term-tile-sub">{p["sub"]}</div>'
            f'</div>'
        )
    tiles_html += '</div>'
    st.markdown(tiles_html, unsafe_allow_html=True)

    st.markdown(
        '<div style="font-size:9.5px; color:var(--term-muted); margin-top:6px; margin-bottom:16px;">'
        'PETITES_POS: TAO +4.37 · ZEC +3.18 · HYPE +0.29 · SOL +0.91'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div style="font-size:11px; color:var(--term-muted); margin-bottom:6px;">// JOURNAL</div>', unsafe_allow_html=True)
    st.markdown(
        '<table>'
        '<tr><td>DATE</td><td>TOKEN</td><td>TYPE</td><td style="text-align:right;">MONTANT</td></tr>'
        '<tr><td>2026-08-09</td><td>NOCK</td><td style="color:var(--term-red);">SELL</td><td style="text-align:right;">$142.50</td></tr>'
        '<tr><td>2026-08-07</td><td>FWA</td><td style="color:var(--term-green);">BUY</td><td style="text-align:right;">$310.00</td></tr>'
        '</table>',
        unsafe_allow_html=True,
    )

with tab2:
    st.markdown(
        '<div style="font-size:11px; color:var(--term-muted);">// VENTES_REALISEES (exemple)</div>',
        unsafe_allow_html=True,
    )
