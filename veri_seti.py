import os #diske bağlanıp foto urllerini alıcaz
import matplotlib.pyplot as plt #veri görselleştirme grefikler
#fotoğrafları açıp detaylı bir şekilde incelemek için
import cv2 #computer vision bilgisayar görüşü

veri=os.listdir("veriseti")
for image_url in veri:
    img=cv2.imread("veriseti/"+image_url)#bgr
    img =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#rgb - RESMİN RENGİNİ DÖNÜŞTÜRDÜK
    img=cv2.resize(img,(500,500))
    plt.imshow(img)
    plt.show()

    
