def magic_string(cnt=[0]):
    cnt[0]+= 1
    return str("BestSchool, " * (cnt[0]-1) + "BestSchool")

for i in range(10):
    print(magic_string())
