""" Bu benim ilk modul calismam"""


var = "Latif"

def kare(x):
    #Bu fonksiyon girilen degerin karesini alir
    return print(x*x)



def satir(y):
    """Bu fonksiyon girilen degerlerin arasina bosluk yazar"""
    return print(*y)

if __name__=="__min__": #bu modül dogrudan calistirilacaksa (script) alttakiler calisir
    kare(5)
    print("hello")
    satir("Deutschland")

    
    