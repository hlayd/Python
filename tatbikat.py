e = str("e")
h = str("h")

y = input("Yangın riski var mı? (e/h): ")

if y == h:
    print("Bitir")
else:
    print("Yangın tüpü al")
    y = input("Pim açık mı? (e/h): ")
    
    if y == h:
        print("Pimi çek")
    if y == e or y == h:
        y = input("Kayıt eden biri var mı?  (e/h):")
        y = input("Can riski var mı? (e/h): ")
        if y == h:
            print("Bitir")
        else:
            y = input("Kendini riske değer mi? (e/h): ")
            
            if y == h:
                print("Bitir")
            else:
                y = input("Yangın başladı mı? (e/h): ")
                
                if y == h:
                    y = input("Risk devam ediyor mu? (e/h): ")
                    
                if y == h:
                    print("Bitir")
                else:
                    a = 0
                    sayac = input("Yangının derecesi kaç?: ")
                    sayac = int(sayac)
                        
                    for i in range(sayac, 0, -1):
                        print("Yangın tüpü sık")
                        print("Derece bir azaltıldı")
                        
                    print("Bitir")
