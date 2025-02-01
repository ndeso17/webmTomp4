import os
import ffmpeg

def convert_webm_to_mp4(file_path):
    # Periksa apakah file valid
    if not os.path.isfile(file_path) or not file_path.endswith(".webm"):
        print("File tidak valid! Harap masukkan path lengkap ke file .webm.")
        return

    # Dapatkan direktori dan nama file
    directory = os.path.dirname(file_path)
    filename = os.path.basename(file_path).replace(".webm", ".mp4")
    output_path = os.path.join(directory, filename)

    try:
        print(f"Mengonversi: {file_path} -> {output_path}")

        # Gunakan ffmpeg untuk konversi dengan kualitas terbaik
        ffmpeg.input(file_path).output(output_path, vcodec="libx264", acodec="aac", preset="medium", crf=18, vf="scale=trunc(iw/2)*2:trunc(ih/2)*2").run(overwrite_output=True)

        print(f"✅ Berhasil: {output_path}")
    except ffmpeg.Error as e:
        print(f"❌ Gagal mengonversi {file_path}: {e}")

if __name__ == "__main__":
    file_path = input("Masukkan path lengkap ke file .webm: ").strip()
    convert_webm_to_mp4(file_path)
