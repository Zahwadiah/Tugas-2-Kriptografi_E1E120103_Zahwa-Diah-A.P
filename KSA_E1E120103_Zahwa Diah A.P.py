kunci = input("Masukkan kunci: ")
s = [x for x in range(256)]
j = 0
kunci = [ord(x) for x in kunci]
for i in range(len(s)):
    j = (j + s[i] + int(kunci[i % len(kunci)])) % 256
    s[i], s[j] = s[j], s[i]
print(s)