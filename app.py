
from PIL import Image
img = Image.open("python.png")
islem = input("Yapmak istediğiniz işlemi seçiniz:\n1-Görseli aç\n2-Görseli döndür\n3-Görseli yeniden boyutlandır\n4-Çıkış")


def image_resize():
    width = int(input("Genişliği giriniz: "))
    height = int(input("Yüksekliği giriniz: "))
    new_img = img.resize(width,height)
    new_img.show()


def imagerotator():
    angle = int(input("Açıyı giriniz: "))
    out = img.rotate(angle, expand=True)
    out.save('rotate-output.png')
    out.show()


def open_image():
    img.show()


if islem == "1":
    open_image()
elif islem == "2":
    imagerotator()
elif islem == "3":
    image_resize()
elif islem == "4":
    pass
