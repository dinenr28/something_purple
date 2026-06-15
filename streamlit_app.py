import streamlit as st
from datetime import datetime, date

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Nadine's Cute Student Hub ✨",
    page_icon="🔮",
    layout="wide"
)

# --- INJEKSI CSS KUSTOM UNTUK TEMA UNGU PASTEL AESTHETIC ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@300..700&family=Quicksand:wght@300..700&display=swap');

    /* Background Utama & Font Global */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #FAF5FF !important; /* Warna ungu pastel super lembut */
        font-family: 'Quicksand', sans-serif !important;
        color: #4A3E56 !important;
    }

    /* Sidebar Kustom */
    [data-testid="stSidebar"] {
        background-color: #EBE0FF !important; /* Lilac pastel lembut */
        border-right: 3px solid #D6C2FF !important;
    }
    [data-testid="stSidebar"] * {
        font-family: 'Fredoka', sans-serif !important;
        color: #4A2E80 !important;
    }

    /* Judul-judul */
    h1, h2, h3, h4, h5, h6, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        font-family: 'Fredoka', sans-serif !important;
        color: #6C429C !important; /* Ungu medium */
        text-shadow: 1px 1px 2px rgba(108, 66, 156, 0.1);
    }

    /* Tombol Kustom Berwarna Ungu Imut */
    div.stButton > button {
        background-color: #D6C2FF !important; 
        color: #4A2E80 !important;
        border: 2px solid #BCA1FF !important;
        border-radius: 20px !important;
        font-family: 'Fredoka', sans-serif !important;
        font-size: 16px !important;
        padding: 8px 24px !important;
        box-shadow: 0 4px 10px rgba(188, 161, 255, 0.3) !important;
        transition: all 0.3s ease-in-out !important;
    }
    div.stButton > button:hover {
        background-color: #BCA1FF !important;
        color: #FFFFFF !important;
        transform: scale(1.05) !important;
        box-shadow: 0 6px 15px rgba(188, 161, 255, 0.5) !important;
    }

    /* Input, Text Area, Select Box, dan Date Input */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>div, .stDateInput>div>div>input {
        border-radius: 15px !important;
        border: 2px solid #E1D5F5 !important;
        background-color: #FFFFFF !important;
        color: #4A3E56 !important;
    }
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: #BCA1FF !important;
        box-shadow: 0 0 8px rgba(188, 161, 255, 0.4) !important;
    }

    /* Desain Kartu Timeline / Jadwal Kuliah */
    .timeline-card {
        background-color: #FFFFFF !important;
        border: 2px solid #E8DAFF !important;
        border-radius: 20px !important;
        padding: 20px !important;
        margin-bottom: 15px !important;
        box-shadow: 0 8px 20px rgba(188, 161, 255, 0.15) !important;
        border-left: 8px solid #BCA1FF !important;
    }
    .timeline-time {
        font-family: 'Fredoka', sans-serif !important;
        color: #8C52FF !important;
        font-size: 16px;
        font-weight: bold;
    }
    .timeline-title {
        font-family: 'Fredoka', sans-serif !important;
        color: #4A2E80 !important;
        margin: 5px 0 !important;
        font-size: 20px;
    }

    /* Tabs Kustom */
    button[data-baseweb="tab"] {
        font-family: 'Fredoka', sans-serif !important;
        color: #8C52FF !important;
    }
    button[aria-selected="true"] {
        background-color: #F0E6FF !important;
        border-radius: 10px 10px 0 0 !important;
        color: #4A2E80 !important;
    }

    /* Kelompok 4 Container */
    .g4-card {
        background: linear-gradient(135deg, #F0E6FF 0%, #E2D1FC 100%) !important;
        border: 2px dashed #BCA1FF !important;
        border-radius: 25px !important;
        padding: 30px !important;
        box-shadow: 0 10px 25px rgba(188, 161, 255, 0.2) !important;
        text-align: center;
        max-width: 500px;
        margin: 0 auto;
    }
    .g4-item {
        font-family: 'Fredoka', sans-serif !important;
        font-size: 20px !important;
        color: #4A2E80 !important;
        background: #FFFFFF !important;
        margin: 10px auto !important;
        padding: 10px 20px !important;
        border-radius: 15px !important;
        width: 80% !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05) !important;
        border: 1px solid #E8DAFF !important;
        transition: transform 0.2s;
    }
    .g4-item:hover {
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

# --- INISIALISASI STORAGE (SESSION STATE) ---
if "jadwal_kuliah" not in st.session_state:
    st.session_state.jadwal_kuliah = [
        {"hari": "Senin", "jam": "08:00 - 10:00", "matkul": "Pemrograman Web 🖥️", "ruang": "Lab ICT"},
        {"hari": "Selasa", "jam": "10:30 - 13:00", "matkul": "Basis Data 💾", "ruang": "Ruang 302"}
    ]

if "diary_notes" not in st.session_state:
    st.session_state.diary_notes = [
        {"tanggal": "2026-06-15", "judul": "Hari Pertama Project ✨", "isi": "Hari ini kelompok 4 mulai bagi-bagi tugas coding bareng."}
    ]

# --- SIDEBAR NAVIGASI ---
st.sidebar.markdown("<h1 style='text-align: center; font-size: 28px;'>🔮 Student Hub</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center;'>Have a magical day! 🌸</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")
menu = st.sidebar.radio("Pilih Halaman:", ["📅 My Timeline", "📝 Dreamy Diary", "🦄 Kelompok 4"])

# =========================================================
# MENU 1: TIMELINE & JADWAL KULIAH
# =========================================================
if menu == "📅 My Timeline":
    st.markdown("<h1>📅 Timeline & Jadwal Kuliah ☁️</h1>", unsafe_allow_html=True)
    st.write("Catat dan rapikan jadwal kuliah atau deadline tugas harianmu di sini!")
    
    # Form Tambah Jadwal
    with st.expander("✨ Tambah Kegiatan Baru"):
        form_hari = st.selectbox("Pilih Hari", ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"])
        form_jam = st.text_input("Jam Kegiatan", placeholder="Contoh: 08:00 - 09:40")
        form_matkul = st.text_input("Nama Mata Kuliah / Agenda")
        form_ruang = st.text_input("Ruangan / Media Zoom")
        
        if st.button("Simpan Jadwal 🎀"):
            if form_jam and form_matkul:
                baru = {"hari": form_hari, "jam": form_jam, "matkul": form_matkul, "ruang": form_ruang}
                st.session_state.jadwal_kuliah.append(baru)
                st.success("Yay! Jadwal berhasil disimpan 🌟")
                st.rerun()
            else:
                st.error("Jam dan Nama Kegiatan harus diisi ya!")

    # Menampilkan Timeline berdasarkan Hari
    st.markdown("<h3 style='margin-top: 30px;'>📌 Timeline Kegiatan Mingguan</h3>", unsafe_allow_html=True)
    hari_pilihan = st.tabs(["Senin 🌸", "Selasa 🔮", "Rabu ☁️", "Kamis 🦄", "Jumat ✨", "Sabtu 🎈", "Minggu 🎀"])
    
    daftar_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    
    for i, hari in enumerate(daftar_hari):
        with hari_pilihan[i]:
            jadwal_hari_ini = [j for j in st.session_state.jadwal_kuliah if j["hari"] == hari]
            
            if not jadwal_hari_ini:
                st.info(f"Tidak ada kegiatan di hari {hari}. Waktunya istirahat dan me-time! 🛌")
            else:
                for j in jadwal_hari_ini:
                    st.markdown(f"""
                    <div class="timeline-card">
                        <div class="timeline-time">⏰ {j['jam']}</div>
                        <div class="timeline-title">{j['matkul']}</div>
                        <div style="color: #6C5B7B;">📍 Ruang: {j['ruang'] if j['ruang'] else '-'}</div>
                    </div>
                    """, unsafe_allow_html=True)

# =========================================================
# MENU 2: DIARY & CATATAN
# =========================================================
elif menu == "📝 Dreamy Diary":
    st.markdown("<h1>📝 Dreamy Diary & Notes 🌸</h1>", unsafe_allow_html=True)
    st.write("Tuangkan curahan hati, impian, atau rangkuman kuliah berhargamu hari ini.")
    
    # Input Diary Baru
    with st.form("form_diary", clear_on_submit=True):
        st.subheader("Tulis Cerita Baru ✨")
        judul_diary = st.text_input("Judul Cerita / Catatan")
        isi_diary = st.st.text_area("Bagikan ceritamu di sini...")
        tanggal_diary = st.date_input("Pilih Tanggal", date.today())
        
        submit_diary = st.form_submit_button("Simpan Diary 💜")
        if submit_diary:
            if judul_diary and isi_diary:
                catatan_baru = {
                    "tanggal": str(tanggal_diary),
                    "judul": judul_diary,
                    "isi": isi_diary
                }
                st.session_state.diary_notes.insert(0, catatan_baru)
                st.success("Ceritamu aman tersimpan di dalam buku harian digital! 📖✨")
                st.rerun()
            else:
                st.error("Isi judul dan ceritamu terlebih dahulu ya!")

    # Menampilkan History Diary
    st.markdown("<h3 style='margin-top: 30px;'>📜 Lembaran Diary</h3>", unsafe_allow_html=True)
    if not st.session_state.diary_notes:
        st.info("Lembar diary-mu masih kosong bersih. Yuk mulai tulis cerita pertamamu!")
    else:
        for note in st.session_state.diary_notes:
            with st.container():
                st.markdown(f"##### 💜 {note['tanggal']} — **{note['judul']}**")
                st.write(note['isi'])
                st.markdown("<hr style='border: 1px dashed #D6C2FF;' />", unsafe_allow_html=True)

# =========================================================
# MENU 3: ANGGOTA KELOMPOK 4
# =========================================================
elif menu == "🦄 Kelompok 4":
    st.markdown("<h1 style='text-align: center;'>🦄 Meet Kelompok 4 🦄</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Tim solid nan super menggemaskan:</p>", unsafe_allow_html=True)
    
    # Menampilkan list 5 nama dengan style card yang imut
    st.markdown("""
    <div class="g4-card">
        <div class="g4-item">👑 1. Fay</div>
        <div class="g4-item">✨ 2. Nadine</div>
        <div class="g4-item">🌸 3. Ajeng</div>
        <div class="g4-item">☁️ 4. Naura</div>
        <div class="g4-item">🔮 5. Chessa</div>
    </div>
    """, unsafe_allow_html=True)
