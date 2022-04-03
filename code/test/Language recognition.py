from langdetect import detect
print('________________Laguage________________')
f = detect("Language recognition")  # en
print(f)

f = detect('שלום')  # he
print(f)
f = detect('Frieden')  # de
print(f)
