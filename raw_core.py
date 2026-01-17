from random import shuffle, choice, randint
from base64 import b64encode
import time, os
from hashlib import sha3_512
def raw_level1(b: str):
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
    Encoded_decrypt = [hex(x) for x in all_decrypt]

    # Quy trình 6: Xóa tiền tố nhận biết
    Del_tt1 = [x[2:] for x in Encoded_Data]
    Del_tt2 = [x[2:] for x in Encoded_sort]
    Del_tt3 = [x[2:] for x in Encoded_decrypt]

    # Quy trình 7: Xóa space
    Del_space1 = [x.replace(" ", "") for x in Del_tt1]
    Del_space2 = [x.replace(" ", "") for x in Del_tt2]
    Del_space3 = [x.replace(" ", "") for x in Del_tt3]

    # Quy trình 8: Trộn + lọc số
    All_Delete = Del_space1 + Del_space2 + Del_space3
    del_alpha = []
    for delete_alpha in All_Delete:
        if delete_alpha.isdigit():
            del_alpha.append(delete_alpha)

    # Quy trình 9: Sắp xếp và tà đạo
    sorted_last = sorted(del_alpha)

    # Kết quả
    return "".join(sorted_last)

def raw_level2(b: str):
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
    so_decrypt2 = so_decrypt1[:]

    # Quy trình 3: trộn
    all_decrypt1 = hoa + thuong + so + hoa_decrypt1 + thuong_decrypt1
    all_decrypt2 = hoa_decrypt2 + thuong_decrypt2 + so_decrypt2
    all_decrypt = all_decrypt1 + all_decrypt2

    # Quy trình 4: Shuffle
    shuffle(all_decrypt)
    shuffle(all_decrypt1)
    shuffle(all_decrypt2)

    # Quy trình 5: encode
    def to_int(x):
        return ord(x) if isinstance(x, str) else x

    Encoded_Data = [bin(to_int(x)) for x in all_decrypt]
    Encoded_sort = [oct(to_int(x)) for x in all_decrypt1]
    Encoded_decrypt = [hex(x) for x in all_decrypt2]

    # Quy trình 6: Xóa space
    Del_space1 = [x.replace(" ", "") for x in Encoded_Data]
    Del_space2 = [x.replace(" ", "") for x in Encoded_sort]
    Del_space3 = [x.replace(" ", "") for x in Encoded_decrypt]

    # Quy trình 7: Gom + lọc số
    All_Delete = Del_space1 + Del_space2 + Del_space3
    del_alpha = [x for x in All_Delete if x.isdigit()]

    # Quy trình 8: Shuffle lần cuối
    shuffle(del_alpha)

    # Quy trình 9: Cắt đi các số chung
    del_chung = []
    seen = set()
    for chung in del_alpha:
        if chung not in seen:
            seen.add(chung)
            del_chung.append(chung)

    # Quy trình 10: Gây nhiễu số
    fake_number = str(randint(1, 255))
    del_chung.append(fake_number)

    # Quy trình 11: Gây nhiễu ký tự
    fake_alpha = choice([
        "$ox", "A", "b", "c", "D",
        "0x", "0o", "0b", "0d",
        "\\x", "\\u", "\\U",
        "\\ooo", "\\oco",
        "\\b", "\\t", "\\n", "\\r",
        "dec####"
    ])
    del_chung.append(fake_alpha)

    # Kết quả
    return "".join(del_chung)

def raw_level3(b: str):
    hoa = []
    thuong = []
    so = []

    for a in b:
        if a.isupper():
            hoa.append(a)
        elif a.islower():
            thuong.append(a)
        elif a.isdigit():
            so.append(a)

    hoa_decrypt1 = [i.lower() for i in hoa]
    thuong_decrypt1 = [j.upper() for j in thuong]
    so_decrypt1 = [ord(k) for k in so]

    hoa_decrypt2 = [ord(c) for c in hoa_decrypt1]
    thuong_decrypt2 = [ord(c) for c in thuong_decrypt1]
    so_decrypt2 = so_decrypt1[:]

    all_decrypt1 = hoa + thuong + so + hoa_decrypt1 + thuong_decrypt1
    all_decrypt2 = hoa_decrypt2 + thuong_decrypt2 + so_decrypt2
    all_decrypt = all_decrypt1 + all_decrypt2

    shuffle(all_decrypt)
    shuffle(all_decrypt1)
    shuffle(all_decrypt2)

    def to_int(x):
        return ord(x) if isinstance(x, str) else x

    Encoded_Data = [bin(to_int(x)) for x in all_decrypt]
    Encoded_sort = [oct(to_int(x)) for x in all_decrypt1]
    Encoded_decrypt = [hex(x) for x in all_decrypt2]

    Del_space1 = [x.replace(" ", "") for x in Encoded_Data]
    Del_space2 = [x.replace(" ", "") for x in Encoded_sort]
    Del_space3 = [x.replace(" ", "") for x in Encoded_decrypt]

    All_Delete = Del_space1 + Del_space2 + Del_space3
    del_alpha = [x for x in All_Delete if x.isdigit()]

    shuffle(del_alpha)

    del_chung = []
    seen = set()
    for chung in del_alpha:
        if chung not in seen:
            seen.add(chung)
            del_chung.append(chung)
    key = sum(ord(ky) for ky in b) % randint(0,1048576)
    fake_number = (hash(b) ^ key) & 0xff
    del_chung.append(fake_number)

    fake_alpha = choice([
        "$ox", "A", "b", "c", "D",
        "0x", "0o", "0b", "0d",
        "\\x", "\\u", "\\U",
        "\\ooo", "\\oco",
        "\\b", "\\t", "\\n", "\\r",
        "dec####", "encoding=####"
    ])
    del_chung.append(fake_alpha)

    fake_b64 = b64encode(str(del_chung).encode())
    return fake_b64
import random
from base64 import b64encode

def raw_level4(b: str):
    # ====== PHASE 0: SEED ======
    PRIME1 = 1315423911
    PRIME2 = 2654435761
    MOD = 2**32

    state = 0xABCDEF01
    for i, c in enumerate(b):
        state ^= (ord(c) + i * PRIME1) & 0xffffffff
        state = ((state << 7) | (state >> 25)) & 0xffffffff
        state = (state * PRIME2) & 0xffffffff

    # ====== PHASE 1: RAW_LEVEL3 DNA ======
    hoa, thuong, so = [], [], []

    for c in b:
        if c.isupper():
            hoa.append(ord(c.lower()))
        elif c.islower():
            thuong.append(ord(c.upper()))
        elif c.isdigit():
            so.append(ord(c))

    pool = hoa + thuong + so

    random.seed(state)
    random.shuffle(pool)

    # ====== PHASE 2: STATE + AVALANCHE ======
    for x in pool:
        state ^= x
        state = ((state << 11) | (state >> 21)) & 0xffffffff
        state = (state * (x + 97)) & 0xffffffff
        state ^= (state >> 16)

    # ====== PHASE 3: CONTROLLED NOISE ======
    noise_rounds = (state ^ len(b)) % 7 + 3
    for i in range(noise_rounds):
        junk = (state + i * PRIME1) & 0xffffffff
        state ^= ((junk << (i + 3)) | (junk >> (29 - i))) & 0xffffffff
        state = (state * PRIME2) & 0xffffffff

    # ====== PHASE 4: OBFUSCATED OUTPUT ======
    ALPHABET = "QW8x$kZpL@9A!mN7B#E0V2%R6C*D^T&U4F5HJSY"
    out_len = 4

    out = []
    for i in range(out_len):
        idx = (state ^ (state >> (i + 3)) ^ (i * 73)) % len(ALPHABET)
        out.append(ALPHABET[idx])
        state = ((state << 5) | (state >> 27)) & 0xffffffff
        state ^= ord(out[-1]) * PRIME1

    return "".join(out)


def raw_level5(b: str):
    # ===== PHASE 0: CONTEXT TRAP =====
    ctx = (
        len(b),
        sum(ord(c) for c in b),
        id(b) & 0xffff,
        int(time.time()) & 0xff,   # thời điểm
        os.getpid() & 0xff         # tiến trình
    )

    state = 0x9E3779B9
    for i, v in enumerate(ctx):
        state ^= (v + (i << 7)) & 0xffffffff
        state = ((state << 9) | (state >> 23)) & 0xffffffff

    # ===== PHASE 1: INPUT ABSORPTION =====
    for i, c in enumerate(b):
        x = ord(c) ^ ((i + 1) * 131)
        state ^= x
        state = (state * 2654435761) & 0xffffffff
        state ^= (state >> 15)

    # ===== PHASE 2: ENTROPY COLLAPSE =====
    # Cố tình phá tính suy luận
    for _ in range((state ^ len(b)) % 5 + 3):
        noise = (state ^ random.randint(0, 2**16)) & 0xffffffff
        state ^= ((noise << 11) | (noise >> 21)) & 0xffffffff
        state = (state * (noise | 1)) & 0xffffffff

    # ===== PHASE 3: SELF-POISON =====
    poison = state
    state ^= (poison >> 3)
    state ^= (poison << 5) & 0xffffffff
    state ^= hash(str(poison)) & 0xffffffff

    # ===== PHASE 4: SHORT OBFUSCATED OUTPUT =====
    ALPHABET = "QW8x$kZpL@9A!mN7B#E0V2%R6C*D^T&U4F5HJSY"
    out_len = 2

    out = []
    for i in range(out_len):
        idx = (state ^ (state >> (i + 1)) ^ (i * 97)) % len(ALPHABET)
        out.append(ALPHABET[idx])
        state ^= ord(out[-1]) * 31337
        state = ((state << 7) | (state >> 25)) & 0xffffffff

    return "".join(out)

def raw_level6(b: str):
    # ===== CORE: KẾ THỪA LEVEL 5 =====
    core = raw_level5(b)   # mồi nhiễu, đã không tái lập

    # ===== FAKE STRUCTURES (GIẢ CÓ LOGIC) =====
    fake_headers = [
        f"CRC={'PASS' if randint(0,1) else 'FAIL'}",
        f"LEN={randint(0,1024)}",
        f"CHK=0x{randint(0,255):02X}",
        f"TS={int(time.time()) % randint(2,9)}",
        f"KEY[{randint(1,5)}/{randint(1,3)}]"
    ]

    fake_states = [
        "OK",
        "INIT",
        "FINAL",
        "DONE",
        "PENDING",
        "ERROR=0",
        "APPLY"
    ]

    fake_noise = [
        "NULL",
        "REDACTED",
        "...",
        "##"
    ]

    # ===== ASSEMBLY (MÂU THUẪN CỐ Ý) =====
    blocks = [
        f"{choice(fake_headers)}:{core}",
        choice(fake_states),
        f"STEP {randint(5,1)}/{randint(0,0)}"
    ]

    if randint(0,1):
        blocks.append(choice(fake_noise))

    shuffle(blocks)
    return " | ".join(blocks)
