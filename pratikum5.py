from datetime import date


def hitung_biaya_pemesanan(jenis_kamar, lama_menginap):
    """
    Menghitung total biaya pemesanan hotel berdasarkan jenis kamar dan lama menginap.

    Parameter:
    jenis_kamar (str): "Standard" atau "Deluxe"
    lama_menginap (int): Jumlah malam menginap

    Returns:
    int: Total biaya pemesanan
    """

    if jenis_kamar == "Standard":
        biaya_per_malam = 200000
    elif jenis_kamar == "Deluxe":
        biaya_per_malam = 350000
    else:
        print("Jenis kamar tidak valid.")
        return 0

    total_biaya = biaya_per_malam * lama_menginap
    return total_biaya


jenis_kamar = input("Masukkan jenis kamar (Standard/Deluxe): ")

tanggal_checkin_str = input("Masukkan tanggal check-in (YYYY-MM-DD): ")
tanggal_checkout_str = input("Masukkan tanggal check-out (YYYY-MM-DD): ")



checkin = date.fromisoformat(tanggal_checkin_str)
checkout = date.fromisoformat(tanggal_checkout_str)

lama_menginap = (checkout - checkin).days

total_biaya = hitung_biaya_pemesanan(jenis_kamar, lama_menginap)

print("\n===== DETAIL PEMESANAN HOTEL =====")
print(f"Jenis Kamar       : {jenis_kamar}")
print(f"Tanggal Check-in  : {checkin}")
print(f"Tanggal Check-out : {checkout}")
print(f"Lama Menginap     : {lama_menginap} malam")
print(f"Total Biaya       : Rp {total_biaya:,}".replace(",", "."))