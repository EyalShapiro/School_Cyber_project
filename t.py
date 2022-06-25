# Python program to demonstrate
# langdetect


from langdetect import detect


# Specifying the language for
# detection
print(detect("שלום"))
print(detect("Geeksforgeeks - это компьютерный портал для гиков"))
print(detect("Geeksforgeeks es un portal informático para geeks"))
print(detect("Geeksforgeeks是面向极客的计算机科学门户"))
print(detect("Geeksforgeeks geeks के लिए एक कंप्यूटर विज्ञान पोर्टल है"))
print(detect("Geeksforgeeksは、ギーク向けのコンピューターサイエンスポータルです。"))
