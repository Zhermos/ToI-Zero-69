d,m = int(input()),int(input())
zodiac = ["capricorn", "aquarius", "pisces", "aries", "taurus", "gemini","cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn"]
cutoff = [0, 20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 22, 22]
if(d<cutoff[m]): print(zodiac[m-1])
else: print(zodiac[m])