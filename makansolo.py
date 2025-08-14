import streamlit as st
import pandas as pd

# Menentukan judul aplikasi
st.title('Rumah Makan Legendaris di Solo 🍽️')
st.markdown("---")

# DataFrame yang berisi daftar rumah makan
# Data ini bisa diganti dengan data dari file CSV atau sumber lain
data_makan = {
    'Nama': [
        'Sate Kambing Pak Manto', 
        'Timlo Sastro', 
        'Tengkleng Klewer Bu Edi', 
        'Nasi Liwet Wongso Lemu', 
        'Es Dawet Telasih Bu Dermi'
    ],
    'Lokasi': [
        'Jl. Honggowongso No.36, Solo',
        'Jl. Kapten Mulyadi No.85, Solo',
        'Jl. Dr. Wahidin Sudirohusodo, Solo',
        'Keprabon, Solo',
        'Pasar Gede, Solo'
    ],
    'Menu Favorit': [
        'Sate Buntel, Tongseng',
        'Timlo Komplit',
        'Tengkleng',
        'Nasi Liwet',
        'Es Dawet Telasih'
    ],
    'Tahun Berdiri': [
        '1990an', 
        '1950', 
        '1971', 
        '1950',
        '1930an'
    ]
}

df = pd.DataFrame(data_makan)

# Menampilkan informasi di Streamlit
st.header('Daftar Rumah Makan')
st.write(df)

st.markdown("---")

st.header('Pilihan Rekomendasi')
st.markdown("Pilih rumah makan dari daftar di bawah untuk melihat detailnya.")

# Bagian interaktif dengan selectbox
pilihan_makan = st.selectbox(
    'Pilih Rumah Makan:',
    df['Nama']
)

# Menampilkan detail berdasarkan pilihan pengguna
if pilihan_makan:
    detail = df[df['Nama'] == pilihan_makan].iloc[0]
    st.subheader(f'Detail: {detail["Nama"]}')
    st.write(f'**Lokasi:** {detail["Lokasi"]}')
    st.write(f'**Menu Favorit:** {detail["Menu Favorit"]}')
    st.write(f'**Berdiri Sejak:** {detail["Tahun Berdiri"]}')

st.markdown("---")

# Menambahkan gambar untuk visualisasi
st.image('https://i.imgur.com/example.jpg', caption='Suasana di salah satu rumah makan legendaris Solo')


# --- Bagian Tambahan: Menampilkan Created By ---
st.markdown("---")
st.markdown("Created by **Fajar Hidayah**")





