# Program: Kombinasi Koin dengan Algoritma Greedy (versi perbaikan)

# Input jumlah uang
amount = int(input("Masukkan jumlah uang: "))

# Input daftar nilai koin, misal: 1000 500 200 100 50
coins = list(map(int, input("Masukkan daftar nilai koin (pisahkan dengan spasi): ").split()))

# Hapus duplikat dan urutkan koin dari besar ke kecil
coins = sorted(list(set(coins)), reverse=True)

# Variabel untuk hasil
result = {}
remaining = amount

# Algoritma Greedy
for coin in coins:
    if remaining >= coin:
        count = remaining // coin
        remaining = remaining % coin
        result[coin] = count

# Tampilkan hasil
print("\n=== HASIL KOMBINASI KOIN ===")
total_coins = 0
for coin, count in result.items():
    print(f"Koin {coin}: {count} buah")
    total_coins += count

print(f"\nJumlah total koin: {total_coins}")
print(f"Sisa uang yang tidak bisa ditukar: {remaining}")
