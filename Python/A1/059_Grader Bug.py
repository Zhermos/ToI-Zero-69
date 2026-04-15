p = {
    "BKK-CNX":10,
    "CNX-UBP":15,
    "UBP-BKK":20,
    "BKK-PKT":25,
    "PKT-CNX":30,
    "UBP-PKT":40
}
w = {
    "BKK-CNX":30,
    "CNX-UBP":40,
    "UBP-BKK":40,
    "BKK-PKT":50,
    "PKT-CNX":60,
    "UBP-PKT":70
}
result = ""
a,b = map(str,input().split())
result += a+"-"+b
c = float(input())
if(result in p):
    print(f"{(p[result]+(c*w[result])):.2f}")
else:print("Error")