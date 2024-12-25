# import random
# from trdg.generators import GeneratorFromStrings
# import os
# from tqdm.auto import tqdm

# NUM_IMAGES_TO_SAVE = 1399

# # Rastgele bir sayı üret
# def random_number():
#     return round(random.uniform(100.0, 1000.0), 2)

# # Kelimeler listesi
# letters = [
#     'Tarih' 
# ]

# # Kelimeleri çoğalt
# expanded_letters = []
# for word in letters:
#     for _ in range(100):  # Her kelimeden 100 adet üret
#         expanded_letters.append(word)

# # Çıktı klasörü oluştur
# output_dir = 'output'
# os.makedirs(output_dir, exist_ok=True)

# # TRDG kullanarak veri üret
# generator = GeneratorFromStrings(
#     strings=expanded_letters,      # Üretilen kelimeler
#     count=len(expanded_letters),   # Görüntü sayısı
#     blur=1,                         # Bulanıklık ekle
#     random_blur=True                # Rastgele bulanıklık
# )

# # Eğer etiket dosyası yoksa oluştur
# if not os.path.exists(f'{output_dir}/labels.txt'):
#     with open(f"{output_dir}/labels.txt", "w") as f:
#         pass

# # Mevcut görüntü sayısını hesapla
# current_index = len([file for file in os.listdir(output_dir) if file.endswith('.png')])

# # Etiket dosyasını aç
# with open(f"{output_dir}/labels.txt", "a") as f:
#     for counter, (img, lbl) in tqdm(enumerate(generator), total=NUM_IMAGES_TO_SAVE):
#         if counter >= NUM_IMAGES_TO_SAVE:
#             break
#         try:
#             img_path = f'{output_dir}/image{current_index}.png'
#             img.save(img_path)
#             f.write(f'image{current_index}.png\t{lbl}\n')
#             current_index += 1
#         except Exception as e:
#             print(f"Görüntü kaydedilirken hata oluştu: {e}")

# print(f"Görüntüler ve etiketler '{output_dir}' klasörüne kaydedildi.")

import random
from trdg.generators import GeneratorFromStrings
import os
import csv
from tqdm.auto import tqdm

NUM_IMAGES_TO_SAVE = 1399

# Rastgele bir sayı üret
def random_number():
    return round(random.uniform(100.0, 1000.0), 2)

# Kelimeler listesi
letters = [
    'Tarih', 
    'Saat', 
    'ISLEM', 
    'TL',
    'TAKSI',
    "taksi",
    'TAKSIMETRE',
    'Tutari',
    'TUTARI',
    'TOPLAM',
    'toplam',
    'Tutar',
    'Toplam',
]

# Kelimeleri çoğalt
expanded_letters = []
for word in letters:
    for _ in range(100):  # Her kelimeden 100 adet üret
        expanded_letters.append(word)

# Çıktı klasörü oluştur
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

# TRDG kullanarak veri üret
generator = GeneratorFromStrings(
    strings=expanded_letters,      # Üretilen kelimeler
    count=len(expanded_letters),   # Görüntü sayısı
    blur=1,                        # Bulanıklık ekle
    random_blur=True               # Rastgele bulanıklık
)

# CSV dosyasını oluştur
csv_file_path = f'{output_dir}/labels.csv'
file_exists = os.path.exists(csv_file_path)

with open(csv_file_path, mode='a', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)

    # İlk satırda başlık ekle (sadece dosya yeni oluşturuluyorsa)
    if not file_exists:
        csv_writer.writerow(['filename', 'words'])

    # Mevcut görüntü sayısını hesapla
    current_index = len([file for file in os.listdir(output_dir) if file.endswith('.png')])

    for counter, (img, lbl) in tqdm(enumerate(generator), total=NUM_IMAGES_TO_SAVE):
        if counter >= NUM_IMAGES_TO_SAVE:
            break
        try:
            img_path = f'{output_dir}/image{current_index}.png'
            img.save(img_path)

            # CSV dosyasına yaz
            csv_writer.writerow([f'image{current_index}.png', lbl])
            current_index += 1
        except Exception as e:
            print(f"Görüntü kaydedilirken hata oluştu: {e}")

print(f"Görüntüler ve etiketler '{output_dir}' klasörüne kaydedildi.")
