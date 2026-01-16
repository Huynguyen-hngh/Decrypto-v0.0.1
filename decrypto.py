print("=" * 30)
print("Chào mừng bạn đã đến với phần mềm Raw dữ liệu bản v0.0.1, vui lòng hãy nhập dữ liệu bạn muốn raw vào đây:\n")
b = input().strip()

hoa = []
thuong = []
so = []

# Phân loại
for a in b:
    if a.isupper():
        hoa.append(a)
    elif a.islower():
        thuong.append(a)
    elif a.isdigit():
        so.append(a)

# Quy trình 1: đảo hoa ↔ thường, số → ASCII
hoa_decrypt1 = [i.lower() for i in hoa]
thuong_decrypt1 = [j.upper() for j in thuong]
so_decrypt1 = [ord(k) for k in so]

# Quy trình 2: tất cả → ASCII
hoa_decrypt2 = [ord(c) for c in hoa_decrypt1]
thuong_decrypt2 = [ord(c) for c in thuong_decrypt1]
so_decrypt2 = so_decrypt1[:]   # đã là ASCII rồi

# Quy trình 3: trộn
all_decrypt1 = hoa + thuong + so + hoa_decrypt1 + thuong_decrypt1
all_decrypt2 = hoa_decrypt2 + thuong_decrypt2 + so_decrypt2
all_decrypt = all_decrypt1 + all_decrypt2

# Quy trình 4: sắp xếp
sort_decrypt = sorted(all_decrypt2)
sort_2 = sorted(all_decrypt2, reverse=True)

# Quy trình 5: encode từng số
Encoded_Data = [bin(x) for x in sort_decrypt]
Encoded_sort = [oct(x) for x in sort_2]
Encoded_decrypt = [hex(x) for x in all_decrypt2]

#Quy trình 6: Xóa tiền tố nhận biết
Del_tt1 = [x[2:] for x in Encoded_Data]
Del_tt2 = [x[2:] for x in Encoded_sort]
Del_tt3 = [x[2:] for x in Encoded_decrypt]

# Quy trình 7: Xóa space
Del_space1 = [x.replace(" ", "") for x in Del_tt1]
Del_space2 = [x.replace(" ", "") for x in Del_tt2]
Del_space3 = [x.replace(" ", "") for x in Del_tt3]

# Quy trình 8: Trộn cả 3 cái vào với nhau và xóa đi các chữ cái trong danh sách
All_Delete = Del_space1 + Del_space2 + Del_space3
del_alpha = []
for delete_alpha in All_Delete:
    if delete_alpha.isdigit():
        del_alpha.append(delete_alpha)

# Quy trình 9: Sắp xếp và tà đạo
sorted_last = sorted(del_alpha)

# Quy trình 10: In ra
Answer = sorted_last
print("Dữ liệu của bạn sau khi raw:\n")
print("".join(Answer))

