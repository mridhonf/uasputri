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
    D = st.number_input("📦 (D) Permintaan Tahunan (pack)", min_value=1, value=12000, step=100)
    S = st.number_input("💰 (S) Biaya Pemesanan / Transaksi (Rp)", min_value=1, value=100000, step=1000)
    H = st.number_input("🏪 (H) Biaya Penyimpanan per Pack per Tahun (Rp)", min_value=1, value=2000, step=100)

    st.info("Isi parameter sesuai kondisi produksi keju potong Anda.")

# ========================================
# ===== Perhitungan EOQ & Output UI =====
# ========================================
EOQ = np.sqrt((2 * D * S) / H)
freq_order = D / EOQ
total_ordering_cost = freq_order * S
total_holding_cost = (EOQ / 2) * H
total_inventory_cost = total_ordering_cost + total_holding_cost

col1, col2 = st.columns(2)
with col1:
    st.subheader("🔢 Hasil Perhitungan EOQ")
    st.success(f"Jumlah Optimal Produksi (EOQ): **{EOQ:.2f} pack**")
    st.write(f"Total Produksi dalam 1 Tahun: **{freq_order:.2f} kali**")
    
with col2:
    st.subheader("💼 Rincian Biaya Tahunan")
    st.metric("Total Biaya Pemesanan Dalam 1 Tahun", f"Rp {total_ordering_cost:,.0f}")
    st.metric("Total Biaya Penyimpanan Dalam 1 Tahun", f"Rp {total_holding_cost:,.0f}")
    st.metric("Total Biaya Persediaan Dalam 1 Tahun", f"Rp {total_inventory_cost:,.0f}")

st.divider()

    # ========================
    # ===== Grafik Output =====
    # ========================
st.subheader("📈 Grafik EOQ: Pemesanan, Penyimpanan & Total Biaya")

    # Rentang jumlah produksi di sekitar EOQ
Q_min = max(1, EOQ * 0.1)
Q_max = EOQ * 3
Q = np.linspace(Q_min, Q_max, 200)

ordering_cost = (D / Q) * S
holding_cost = (Q / 2) * H
total_cost = ordering_cost + holding_cost

EOQ_cost = (D / EOQ) * S + (EOQ / 2) * H

    # Buat grafik
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(Q, ordering_cost, label="Biaya Pemesanan", color='blue', linestyle='--')
ax.plot(Q, holding_cost, label="Biaya Penyimpanan", color='orange', linestyle='-.')
ax.plot(Q, total_cost, label="Total Biaya Persediaan", color='green', linewidth=2)

    # Tambahkan titik EOQ
ax.plot(EOQ, EOQ_cost, 'ro', label="Titik EOQ")
ax.axvline(EOQ, color='red', linestyle='--', linewidth=1)

    # Tambahkan label EOQ
ax.annotate(
    f"EOQ = {EOQ:.2f}\nTotal = Rp {EOQ_cost:,.0f}",
    xy=(EOQ, EOQ_cost),
    xytext=(EOQ * 1.1, EOQ_cost * 1.05),
    arrowprops=dict(arrowstyle="->", color='black'),
    fontsize=10,
    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray")
)

ax.set_xlabel("Jumlah Produksi Keju Potong (pack)")
ax.set_ylabel("Biaya (Rp)")
ax.set_title("Kurva EOQ: Biaya Pemesanan, Penyimpanan, dan Total")
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend()
st.pyplot(fig)
