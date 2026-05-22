import streamlit as st

st.title("Project LPK 2026")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:")

st.code(f"""
import streamlit as st

st.markdown('''{md}''')
""")

st.markdown(md)
import streamlit as st

# Judul Aplikasi
st.title("Aplikasi Kalkulator Sederhana")

# Input Angka
angka1 = st.number_input("Masukkan angka pertama", value=0.0)
angka2 = st.number_input("Masukkan angka kedua", value=0.0)

# Pilihan Operasi
operasi = st.selectbox("Pilih operasi:", ["+", "-", "x", "/"])

# Tombol Hitung
if st.button("Hitung"):
    if operasi == "+":
        hasil = angka1 + angka2
    elif operasi == "-":
        hasil = angka1 - angka2
    elif operasi == "x":
        hasil = angka1 * angka2
    elif operasi == "/":
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            hasil = "Error! Tidak bisa membagi dengan nol."
            
    # Menampilkan Hasil
    st.success(f"Hasil: {hasil}")
    
