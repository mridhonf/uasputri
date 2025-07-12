import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# ===== Header Aplikasi EOQ =====
# ===============================
st.set_page_config(page_title="EOQ Keju Potong", layout="wide")
st.title("🧀 Economic Order Quantity (EOQ) untuk Produk Keju Potong")
st.markdown("""
Aplikasi ini membantu menentukan jumlah **produksi atau pembelian keju potong** yang optimal  
dengan **meminimalkan biaya persediaan** berdasarkan model EOQ.
""")
st.divider()

# ========================
# ===== Input Section =====
# ========================
with st.sidebar:
    st.header("📋 Input Parameter")
    D = st.number_input("📦 Permintaan Tahunan (pack)", min_value=1, value=12000, step=100)
    S = st.number_input("💰 Biaya Pemesanan / Transaksi (Rp)", min_value=1, value=100000, step=1000)
    H = st.number_input("🏪 Biaya Penyimpanan per Pack per Tahun (Rp)", min_value=1, value=2000, step=100)

    st.info("Isi parameter sesuai kondisi produksi keju potong Anda.")

# ========================================
# ===== Perhitungan EOQ & Output UI =====
# ========================================
if D > 0 and S > 0 and H > 0:
    EOQ = np.sqrt((2 * D * S) / H)
    freq_order = D / EOQ
    total_ordering_cost = freq_order * S
    total_holding_cost = (EOQ / 2) * H
    total_inventory_cost = total_ordering_cost + total_holding_cost

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🔢 Hasil Perhitungan EOQ")
        st.success(f"Jumlah Optimal Produksi (EOQ): **{EOQ:.2f} pack**")
        st.write(f"Frekuensi Produksi per Tahun: **{freq_order:.2f} kali**")
    
    with col2:
        st.subheader("💼 Rincian Biaya Tahunan")
        st.metric("Total Biaya Pemesanan", f"Rp {total_ordering_cost:,.0f}")
        st.metric("Total Biaya Penyimpanan", f"Rp {total_holding_cost:,.0f}")
        st.metric("Total Biaya Persediaan", f"Rp {total_inventory_cost:,.0f}")

    st.divider()

    # ========================
    # ===== Grafik Output =====
    # ========================
    st.subheader("📈 Grafik Kurva Total Biaya Persediaan")

    Q = np.linspace(1, D * 2, 200)
    TC = (D / Q) * S + (Q / 2) * H

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(Q, TC, label='Total Biaya Persediaan', color='green', linewidth=2)
    ax.axvline(EOQ, color='red', linestyle='--', linewidth=2, label=f'EOQ = {EOQ:.2f}')
    ax.set_xlabel("Jumlah Produksi (Q)")
    ax.set_ylabel("Total Biaya (Rp)")
    ax.set_title("Kurva EOQ: Total Biaya vs Jumlah Produksi")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
else:
    st.warning("Masukkan semua input terlebih dahulu.")
