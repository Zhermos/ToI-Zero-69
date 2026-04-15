import sys

# ใช้ sys.stdin.read().split() คือท่าไม้ตายที่ปลอดภัยที่สุด
# ต่อให้ Grader ส่งมาบรรทัดเดียว หรือหลายบรรทัด ท่านี้จะหยิบข้อมูลออกมาเป็นก้อนๆ เสมอ
data = sys.stdin.read().split()

# ป้องกัน Runtime Error: เช็คว่าข้อมูลมาครบ 3 ตัวไหม
if len(data) >= 3:
    level = data[0]
    year = int(data[1])
    salary = int(data[2])

    # 1. จัดการโบนัสพื้นฐาน
    bonus_base = {"M": 1500, "B": 1000, "G": 500}
    
    # 2. หาตำแหน่ง Index แถว (i) ตามประเภทพนักงาน
    if level == "M": i = 0
    elif level == "B": i = 1
    else: i = 2

    # 3. หาตำแหน่ง Index คอลัมน์ (j) ตามอายุงาน (ต้องลอก Logic C++ มาเป๊ะๆ)
    # C++: if(B < 5) j=0, else if(B < 10) j=1, else j=2
    if year < 5:
        j = 0
    elif year < 10:
        j = 1
    else:
        j = 2

    # 4. ตารางเปอร์เซ็นต์ (Dividend Rates)
    rates = [
        [6, 8, 10], # M
        [5, 6, 7],  # B
        [4, 5, 6]   # G
    ]

    # 5. คำนวณเงินปันผล (ใช้ // 100 เพื่อให้เป็น Integer เหมือน C++)
    dividend = (salary * rates[i][j]) // 100
    
    # แสดงผลรวม
    print(bonus_base[level] + dividend)