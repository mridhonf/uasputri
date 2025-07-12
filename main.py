import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ===== Judul Aplikasi =====
st.title("🧀 EOQ untuk Produk Keju Potong")

st.markdown("""
Aplikasi ini membantu menentukan **jumlah optimal produksi/pembelian keju potong** agar biaya pemesanan dan penyimpanan menjadi minimum.

Metode yang digunakan adalah **EOQ (Economic Order Quantity)**.
""")

# ===== Sidebar Input =====
st.sidebar.header("📋 Masukkan Data Produksi Keju Potong")

D = st.sidebar.number_input("Permintaan Keju Potong per Tahun (pack)", min_value=1, value=12000)
S = st.sidebar.number_input("Biaya Pemesanan Bahan Baku per Transaksi (Rp)", min_value=1, value=100000)
H = st.sidebar.number_input("Biaya Penyimpanan Keju Potong per Pack per Tahun (Rp)", min_value=1, value=2000)

# ===== Info Awal =====
st.info("Masukkan data permintaan keju potong, biaya pemesanan bahan baku, dan biaya penyimpanan untuk melanjutkan.")

# ===== Perhitungan EOQ =====
if D > 0 and S > 0 and H > 0:
    EOQ = np.sqrt((2 * D * S) / H)
    pemesanan_per_tahun = D / EOQ
    total_ordering_cost = pemesanan_per_tahun * S
    total_holding_cost = (EOQ / 2) * H
    total_inventory_cost = total_ordering_cost + total_holding_cost

    # ===== Output =====
    st.success("✅ Hasil Perhitungan EOQ untuk Keju Potong:")
    st.write(f"🔢 **EOQ (Jumlah Optimal Produksi): {EOQ:.2f} pack**")
    st.write(f"📦 **Frekuensi Produksi per Tahun:** {pemesanan_per_tahun:.2f} kali")
    st.write(f"💰 **Total Biaya Pemesanan:** Rp {total_ordering_cost:,.0f}")
    st.write(f"💼 **Total Biaya Penyimpanan:** Rp {total_holding_cost:,.0f}")
    st.write(f"📊 **Total Biaya Persediaan Tahunan:** Rp {total_inventory_cost:,.0f}")

    # ===== Grafik =====
    st.markdown("### 📉 Grafik Total Biaya Persediaan")
    Q = np.linspace(1, D * 2, 200)
    TC = (D / Q) * S + (Q / 2) * H

    fig, ax = plt.subplots()
    ax.plot(Q, TC, label='Total Biaya Persediaan', color='green')
    ax.axvline(EOQ, color='red', linestyle='--', label=f'EOQ = {EOQ:.2f}')
    ax.set_xlabel("Jumlah Produksi Keju Potong (pack)")
    ax.set_ylabel("Total Biaya (Rp)")
    ax.set_title("Kurva Total Biaya EOQ untuk Keju Potong")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
else:
    st.warning("Masukkan semua input dengan benar.")
