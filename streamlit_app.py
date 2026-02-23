import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.title("正弦波アニメーション（右方向に移動）")

# セッション状態の初期化
if "running" not in st.session_state:
    st.session_state.running = False
if "phase" not in st.session_state:
    st.session_state.phase = 0.0

# ボタン
col1, col2 = st.columns(2)
with col1:
    if st.button("▶️ スタート"):
        st.session_state.running = True
with col2:
    if st.button("⏸ ストップ"):
        st.session_state.running = False

# 描画領域
plot_area = st.empty()

# 1フレームだけ描画する関数
def draw_frame():
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x - st.session_state.phase)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("正弦波アニメーション")

    plot_area.pyplot(fig)

# 実行
draw_frame()

# アニメーション処理
if st.session_state.running:
    st.session_state.phase += 0.1
    time.sleep(0.05)
    st.experimental_rerun()
