import mpmath as mp

mp.mp.dps = 80

H = [mp.mpf("0")]
s = mp.mpf("0")
for k in range(1, 56):
    s += mp.mpf(1) / mp.mpf(k)
    H.append(s)

def B(n):
    return (H[n] + mp.e**(H[n]) * mp.log(H[n])) / mp.mpf(n)

ok = True
for n in range(1, 55):
    if not (B(n + 1) > B(n)):
        ok = False
        break

print("verified" if ok else "not verified")
