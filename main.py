import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ===== Judul Aplikasi =====
st.title("📦 Aplikasi Perhitungan EOQ (Economic Order Quantity)")

st.markdown("""
EOQ membantu menentukan jumlah pembelian optimal yang **meminimalkan biaya persediaan**, 
yang terdiri dari **biaya pemesanan** dan **biaya penyimpanan**.
""")

# ===== Sidebar Input =====
st.sidebar.header("📋 Masukkan Data")

D = st.sidebar.number_input("Permintaan Tahunan (unit)", min_value=1, value=1000)
S = st.sidebar.number_input("Biaya Pemesanan per Order (Rp)", min_value=1, value=50000)
H = st.sidebar.number_input("Biaya Penyimpanan per Unit per Tahun (Rp)", min_value=1, value=1000)

# ===== Info Awal =====
st.info("Masukkan ketiga parameter di sidebar untuk menghitung EOQ dan total biaya persediaan.")

# ===== Perhitungan EOQ =====
if D > 0 and S > 0 and H > 0:
    EOQ = np.sqrt((2 * D * S) / H)
    pemesanan_per_tahun = D / EOQ
    total_ordering_cost = pemesanan_per_tahun * S
    total_holding_cost = (EOQ / 2) * H
    total_inventory_cost = total_ordering_cost + total_holding_cost

    # ===== Output =====
    st.success("✅ Hasil Perhitungan EOQ:")
    st.write(f"🔢 **EOQ (Jumlah Optimal Pemesanan): {EOQ:.2f} unit**")
    st.write(f"📦 **Jumlah Pemesanan per Tahun:** {pemesanan_per_tahun:.2f} kali")
    st.write(f"💰 **Total Biaya Pemesanan:** Rp {total_ordering_cost:,.0f}")
    st.write(f"💼 **Total Biaya Penyimpanan:** Rp {total_holding_cost:,.0f}")
    st.write(f"📊 **Total Biaya Persediaan:** Rp {total_inventory_cost:,.0f}")

    # ===== Grafik =====
    st.markdown("### 📉 Grafik Total Biaya vs Jumlah Pemesanan")
    Q = np.linspace(1, D * 2, 200)
    TC = (D / Q) * S + (Q / 2) * H

    fig, ax = plt.subplots()
    ax.plot(Q, TC, label='Total Biaya Persediaan', color='green')
    ax.axvline(EOQ, color='red', linestyle='--', label=f'EOQ = {EOQ:.2f}')
    ax.set_xlabel("Jumlah Pemesanan (Q)")
    ax.set_ylabel("Total Biaya (Rp)")
    ax.set_title("Kurva Total Biaya Persediaan")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
else:
    st.warning("Mohon isi semua input dengan benar.")
