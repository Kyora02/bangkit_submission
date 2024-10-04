import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title('Bike Sharing Dataset')
st.write('berikut ini merupakan visualisasi data tentang "Bike Sharing"')

hour_df = pd.read_csv('hour.csv')
st.subheader("Bike Hour Data")
st.dataframe(hour_df)

st.subheader('Exploratory Data Analysis')

st.subheader('Permasalahan Bisnis')
st.write("""
Sebagai penyedia layanan penyewaan sepeda, perusahaan perlu memahami faktor-faktor yang mempengaruhi jumlah penyewaan sepeda untuk meningkatkan pelayanan.
Selain itu, kondisi cuaca berperan dalam perubahan jumlah penyewaan sepeda, yang dapat membantu dalam mengoptimalkan operasional di berbagai situasi cuaca.
Penting juga untuk mengevaluasi tren penggunaan sepeda selama hari kerja dan hari non-kerja, guna mengidentifikasi jam-jam sibuk penyewaan.
""")

st.subheader('Pertanyaan Bisnis')
st.write("""
1. Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?
2. Kapan jam sibuk penyewaan sepeda pada hari kerja vs hari non-kerja?
""")

rata2_penyewaan_cuaca = hour_df.groupby('weathersit')['cnt'].mean().reset_index()
rata2_penyewaan_cuaca.columns = ['Situasi Cuaca', 'Rata-rata Penyewaan Sepeda']
rata2_penyewaan_cuaca['Situasi Cuaca'] = rata2_penyewaan_cuaca['Situasi Cuaca'].map({
    1: 'Cerah',
    2: 'Kabut',
    3: 'Hujan/Salju Ringan',
    4: 'Hujan/Salju Lebat'
})

st.subheader('Rata-rata Penyewaan Sepeda Berdasarkan Situasi Cuaca')
st.table(rata2_penyewaan_cuaca)

penyewaan_per_jam = hour_df.groupby(['hr', 'workingday'])['cnt'].mean().reset_index()
penyewaan_per_jam['Hari Kerja'] = penyewaan_per_jam['workingday'].map({
    0: 'Hari Non-Kerja',
    1: 'Hari Kerja'
})
penyewaan_per_jam.drop(columns=['workingday'], inplace=True)
penyewaan_per_jam.columns = ['Jam', 'Rata-rata Penyewaan Sepeda', 'Hari Kerja']

st.subheader('Rata-rata Penyewaan Sepeda per Jam pada Hari Kerja vs Non-Kerja')
st.table(penyewaan_per_jam)

st.subheader('Visualisasi: Rata-rata Penyewaan Sepeda Berdasarkan Situasi Cuaca')

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Situasi Cuaca', y='Rata-rata Penyewaan Sepeda', data=rata2_penyewaan_cuaca, palette='Blues_d', ax=ax)
ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Situasi Cuaca', fontsize=16)
ax.set_xlabel('Situasi Cuaca', fontsize=12)
ax.set_ylabel('Rata-rata Penyewaan Sepeda', fontsize=12)
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

for index, value in enumerate(rata2_penyewaan_cuaca['Rata-rata Penyewaan Sepeda']):
    ax.text(index, value + 5, f'{int(value)}', ha='center', fontsize=10)

st.pyplot(fig)

st.subheader('Visualisasi: Penyewaan Sepeda per Jam pada Hari Kerja vs Non-Kerja')

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='Jam', y='Rata-rata Penyewaan Sepeda', hue='Hari Kerja', data=penyewaan_per_jam, marker='o', ax=ax)
ax.set_title('Rata-rata Penyewaan Sepeda pada Hari Kerja dan Non-Kerja', fontsize=16)
ax.set_xlabel('Jam dalam Sehari', fontsize=12)
ax.set_ylabel('Rata-rata Penyewaan Sepeda', fontsize=12)
ax.grid(True)

st.pyplot(fig)

st.title("Conclution")
st.subheader("Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?")
st.write("Berdasarkan visualisasi data tentang rata-rata penyewaan sepeda pada setiap kondisi cuaca, terlihat bahwa cuaca memiliki pengaruh yang signifikan terhadap jumlah penyewaan sepeda:")
st.write("- Cuaca cerah (Kondisi 1) mendorong jumlah penyewaan sepeda tertinggi.")
st.write("- Kabut (Kondisi 2) sedikit menurunkan penyewaan, tetapi masih cukup tinggi.")
st.write("- Hujan ringan atau salju (Kondisi 3) mengurangi jumlah penyewaan secara signifikan.")
st.write("- Hujan deras atau salju lebat (Kondisi 4) menghasilkan penyewaan terendah.")
st.write("Simpulan : Cuaca cerah meningkatkan penyewaan sepeda, sementara cuaca ekstrem mengurangi minat penyewaan.")

st.subheader("Kapan jam sibuk penyewaan sepeda pada hari kerja vs. hari non-kerja?")
st.write("- Pada hari kerja, puncak penyewaan terjadi saat jam berangkat kerja (08:00) dan pulang kerja (17:00).")
st.write("- Pada hari non-kerja, penyewaan memuncak di tengah hari (12:00-14:00).")
st.write("Simpulan : Jam sibuk pada hari kerja adalah pagi dan sore, sedangkan pada hari non-kerja adalah siang hari.")
st.write("Dengan memanfaatkan pola cuaca dan jam sibuk ini, perusahaan dapat meningkatkan layanan dan alokasi sepeda.")