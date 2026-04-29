import sys

# ใช้ Dictionary เก็บสินค้า และ List เก็บผลลัพธ์เพื่อพิมพ์ทีเดียวตอนจบ
inventory = {}
results = []

# อ่าน Input ทั้งหมดเก็บไว้ก่อนตามเงื่อนไข "ต้องถูกเก็บไว้ในลำดับก่อน"
all_input = sys.stdin.read().splitlines()

for line in all_input:
    parts = line.split()
    if not parts:
        continue
    
    cmd = parts[0]
    
    if cmd == "ADD":
        name, qty = parts[1], int(parts[2])
        inventory[name] = inventory.get(name, 0) + qty
        
    elif cmd == "REMOVE":
        name, qty = parts[1], int(parts[2])
        current = inventory.get(name, 0)
        
        if qty > current:
            # กรณีสต็อกไม่พอ: แจ้งเตือน -> ลบจนหมด -> เอาออกจากคลัง
            results.append(f"Not enough stock for {name}")
            if name in inventory:
                del inventory[name]
        else:
            # กรณีสต็อกพอ: ลบปกติ -> ถ้าเหลือ 0 ให้เอาออกจากคลัง
            inventory[name] = current - qty
            if inventory[name] <= 0:
                if name in inventory:
                    del inventory[name]
                
    elif cmd == "CHECK":
        # ตรวจสอบสินค้า < 5 และเรียงตามชื่อ A-Z
        low_stock_list = []
        # ดึงชื่อสินค้ามาเรียง A-Z ก่อนตรวจสอบ
        for name in sorted(inventory.keys()):
            if inventory[name] < 5:
                low_stock_list.append(f"{name}: {inventory[name]}")
        
        if not low_stock_list:
            results.append("All stocks are sufficient")
        else:
            # เพิ่มรายการที่เจอเข้าในผลลัพธ์ทีละบรรทัด
            results.extend(low_stock_list)
            
    elif cmd == "REPORT":
        # แสดงสินค้าทั้งหมดในคลัง (ซึ่งต้อง > 0) เรียงตามชื่อ A-Z
        for name in sorted(inventory.keys()):
            # ตรวจสอบซ้ำเพื่อความชัวร์ว่าไม่พิมพ์ตัวที่เหลือ 0
            if inventory[name] > 0:
                results.append(f"{name}: {inventory[name]}")
                
    elif cmd == "END":
        break

# แสดงผลลัพธ์ทั้งหมดหลังจากประมวลผลคำสั่ง END แล้วเท่านั้น
for res in results:
    print(res)