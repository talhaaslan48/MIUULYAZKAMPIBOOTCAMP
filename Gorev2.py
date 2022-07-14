# GÖREV  2: Verilen string ifadenin tüm harflerini büyük harfe
# çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime
# ayırınız.

# İpucu: String methodlarını kullanınız.

text = "The goal is to turn data into information, and information into sight"
text = text.replace("."," ")
text = text.replace(","," ")
text = text.upper().split(" ")