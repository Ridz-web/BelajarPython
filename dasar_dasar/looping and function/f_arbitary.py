def info(*info):
    return info

print(info("Ridho","smkn9", "laki-laki"))

def user_info(nama_depan,nama_belakang,**info_pribadi):
    return f"Nama: {nama_depan} {nama_belakang}, info lainnya: {info_pribadi}"

print(user_info(
    "Ridho", 
    "Muta'ali",
    no_tlpn = +628577071561,
    umur = 15,
    jurusan = "PPLG"
    ))