import random
import time

# Daftar pesan romantis
romantic_messages = [
    "Awak selalu bersyukur karena seng ada di hidup awak, .",
    "Sayang adalah alasan mengapa awak tersenyum setiap hari, .",
    "Setiap detik bersama seng adalah momen yang aku hargai, .",
    "awak cintai seng lebih dari kata-kata bisa ungkapkan, .",
    "sayang adalah pelangi di hari-hari awak yang hujan, .",
    "Hati awak selalu milik seng, sekarang dan selamanya, .",
    "Bersama seng, awak menemukan kebahagiaan yang sebenarnya, .",
    "Awak ingin selalu membuat seng bahagia, setiap hari, .",
    "Cinta awak ke seng lebih besar dari bintang-bintang di langit, .",
    "Seng adalah alasan awak merasa lengkap dalam hidup ini, ."
]

# Fungsi untuk menampilkan pesan romantis secara acak
def show_romantic_message():
    message = random.choice(romantic_messages)
    print("\nPesan untuk, sayang: 💖\n")
    time.sleep(1)  # Pause sejenak untuk efek dramatis
    print(f"'{message}'")
    print("\nSelalu ingat, awak sayang sama seng, ! 💕")

# Menyapa pacar dengan nama Fahira
def greet():
    print(f"allo, seng! Ini pesan spesial : 😊\n")
    time.sleep(1)
    show_romantic_message()

# Jalankan program
if __name__ == "__main__":
    greet()
