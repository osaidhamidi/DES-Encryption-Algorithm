
INITIAL_PERMUTATION = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

FINAL_PERMUTATION = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]


S_BOXES = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]


CHOICE1 = [
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
]

CHOICE2 = [
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20,
    13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46,
    42, 50, 36, 29, 32
]

EXPAND_PERM = [
    32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30,
    31, 32, 1
]

P_PERM= [
    16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27,
    3, 9, 19, 13, 30, 6, 22, 11, 4, 25
]

# 1. Key Generation
def generate_keys(key):

    binary_key = format(key, '064b')
    key56 = [binary_key[i - 1] for i in CHOICE1]

    C = key56[:28]
    D = key56[28:]

    keys_list = []
    for round in range(1, 17):
        if round in [1,2,9,16]:
            C = C[1:] + [C[0]]
            D = D[1:] + [D[0]]
        else:
            C = C[2:] + C[:2]
            D = D[2:] + D[:2]
        cd = C + D

        key48 = [cd[i - 1] for i in CHOICE2]
        keys_list.append("".join(key48))
    
    return keys_list


# 2. Initial Permutation
def initial_permutation(block):

    binary_block = format(block, '064b')
    perm_block = [binary_block[i - 1] for i in INITIAL_PERMUTATION]
    joined_block = "".join(perm_block)

    return joined_block

# 3. Feistel Round
def feistel_round(left, right, key):
    
    right_arr = list(right)
    left_arr = list(left)

    expand_right = [right_arr[i - 1] for i in EXPAND_PERM]

    key_arr = list(key)

    kr_arr = [int(k) ^ int(e) for k, e in zip(key_arr, expand_right)]

    kr_subarrs_int = [kr_arr[i:i + 6] for i in range(0, len(kr_arr), 6)]
    kr_subarrs = [[str(i) for i in subarray] for subarray in kr_subarrs_int]

    sboxed = []

    for idx, subarray in enumerate(kr_subarrs):
        row = int("".join([subarray[0], subarray[-1]]), 2)
        entry = int("".join(subarray[1:-1]),2)
        sboxed.append(format(S_BOXES[idx][row][entry], '04b'))
    

    flattened_sboxed = [item for sub in sboxed for item in sub]
    final_perm = [flattened_sboxed[i - 1] for i in P_PERM]
    

    fp_xor_left_int = [int(k) ^ int(e) for k, e in zip(final_perm, left_arr)]


    fp_xor_left = [str(i) for i in fp_xor_left_int]
    

    new_left = right
    new_right= "".join(fp_xor_left)

    return new_left, new_right

# 4. Final Permutation
def final_permutation(block):

    final_block = "".join([block[i - 1] for i in FINAL_PERMUTATION])

    return final_block

# 5. Encryption
def encrypt(plaintext, key):

    perm_block = initial_permutation(plaintext)
    keys_list = generate_keys(key)
    left = perm_block[:32]
    right = perm_block[32:]

    for round in range(16):
       left,right = feistel_round(left,right, keys_list[round])
    

    return int(final_permutation(right+left),2)
    


    

# 6. Decryption
def decrypt(ciphertext, key):

    perm_block = initial_permutation(ciphertext)
    keys_list = generate_keys(key)
    left = perm_block[:32]
    right = perm_block[32:]

    for round in range(16):
       left,right = feistel_round(left,right, keys_list[15 - round])

    return int(final_permutation(right+left),2)

# 7. Testing
if __name__ == "__main__":

    plaintext = 0x4E45565251554954 # Example 64-bit block
    
    key = 0x4b41534849534142 # Example 64-bit key

    ciphertext = encrypt(plaintext, key)
    decrypted = decrypt(ciphertext, key)

    # # # Print results
    print(f"Plaintext: {hex(plaintext)}")
    print(f"Ciphertext: {hex(ciphertext)}")
    print(f"Decrypted: {hex(decrypted)}")
