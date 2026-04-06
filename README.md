
# 🧩Project WordMix

Game kata sederhana untuk mengisi kebosanan.
Player akan diberikan sebuah kata rahasia, yang memiliki 5 huruf, dan player harus menebak kata tersebut dalam 5 kali percobaan.

## 🚀 Cara Bermain

- Jalankan Program
- Setelah Program Berjalan, sebuah kata yang memilki 5 huruf akan dipilih secara acak dari kamus bahasa inggris
- Ketika player mengetikkan sebuah kata, player akan diberikan sebuah klu atas kata rahasia yang harus di tebak
- Jika player mengetik kata yang mengandung huruf dari kata rahasia tersebut, tetapi dalam posisi yang salah, maka huruf yang telah di tebak akan diberikan tanda 🟨 
- Jika player mengetik kata yang mengandung huruf dari kata rahasia, dan berada dalam posisi yang benar, maka huruf yang telah ditebak akan diberikan tanda 🟩
- Jika kata yang telah di input tidak mengandung huruf yang dimiliki oleh kata rahasia, maka huruf tersebut akan diberikan tanda ⬛
- Player memiliki 5 kali percobaan untuk memenangkan game ini.

## 🛠️Cara Kerja
 Pertama, sebuah array akan digunakan untuk menampung kata kata yang akan digunakan.
```
WORD_LIST = [w for w in spell.word_frequency.keys() if len(w) == 5]
```
dikarenakan    `if len(w) == 5 `, maka kata yang terpilih hanyalah kata yang memiliki panjang sebanyak 5 digit, atau 5 huruf.

lalu 

```

while True:
    TARGET = random.choice(WORD_LIST)
    MAX_TRIES = 5 
```

akan berjalan, yang dimana terjadinya pemilihan kata secara acak. hal ini terjadi karena kata acak tersebut dipilih menggunakan `random`. Disini juga dimana jumlah percobaan disimpan, yaitu di dalam `MAX_TRIES`.

```
while MAX_TRIES > 0:
        guess = input(f"{MAX_TRIES} tries left. Enter guess: ").strip().lower()
        if guess == "quit":
            print("Quit. Bye!")
            exit()  # Exit the entire program
        if len(guess) != 5 or not guess.isalpha():
            print("Please enter exactly 5 alphabetic characters.")
            continue
        if guess not in WORD_LIST:
            print("Word not in allowed 5-letter dictionary.")
            continue
```

disini tempat logic game berlangsung dalam program ini. pertama, jika `MAX_TRIES` lebih banyak daripada 0, maka permainan akan terus berlangsung. ada dua kondisi yang harus dipenuhi untuk membuat sebuah tebakan. 

Yang pertama, 

```
if len(guess) != 5 or not guess.isalpha():
            print("Please enter exactly 5 alphabetic characters.")
```
berdasarkan ini, sebuah tebakan wajib memiliki 5 huruf, tidak kurang, dan tidak lebih.

Selanjutnya,

```
if guess not in WORD_LIST:
            print("Word not in allowed 5-letter dictionary.")
```

sebuah tebakan wajib berupa sebuah kata, yang terdapat di dalam kamus bahasa inggris.

Ketika, dan hanya ketika kedua syarat telah terpenuhi, maka sebuah tebakkan dapat menjadi cobaan, atau tries. Jika tidak, maka jumlah percobaan tidak akan berubah.


Setelah player memberikan sebuah tebakkan, maka program akan melanjutkan ke proses selanjutnya, yaitu letter grading, yang dimana ini akan mengecek huruf apa yang akan diberikan tanda 🟩, 🟨, atau ⬛

```
feedback = []
target_chars = list(TARGET)

for i, ch in enumerate(guess):
    if TARGET[i] == ch:
    feedback.append("🟩")
    target_chars[i] = None
    else:
    feedback.append(None)


 for i, ch in enumerate(guess):
    if feedback[i] is None:
        if ch in target_chars:
            feedback[i] = "🟨"
            target_chars[target_chars.index(ch)] = None
            else:
            feedback[i] = "⬛"
            
```

Jika player berhasil unuk menebak kata rahasia tersebut maka player akan menang.

```
if guess == TARGET:
            print("🎉 Correct! You win!")
            break
```

Untuk setiap percobaan `MAX_TRIES` akan berkurang sebanyak 1.


Jika `MAX_TRIES` mencapai 0, maka permainan akan selesai, dan player akan diberi opsi untuk mengulang permainan (Mendapatkan kata baru) atau selesai bermain.

```
if MAX_TRIES == 0:
        print(f"Game over. The word was: {TARGET}")

           play_again = input("Play again? (y/n): ").strip().lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break

```
## Screenshots


## 👤 Author

- Nama: 2501010120 - Kadek Puja Arya Putra
- GitHub: https://github.com/chokiaispuja

- Nama: 2501010123 - I Gede Fajar Waradana
- GitHub:  https://github.com/dekd3
