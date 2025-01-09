def rangking(nilai) :
    if nilai >= 90 and nilai < 101 :
        return 'kamu rangking 3 besar'
    elif nilai >= 50 and nilai < 90 :
        return 'kamu rangking 10 besar'
    elif nilai < 50 :
        return 'kamu tolol'
    else :
        return 'bukan termasuk nilai'
        