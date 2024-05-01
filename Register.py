def splitmanual(a, b = " "):
    list = []
    e = 0
    for i in range(len(a)):
        if ord(a[i]) == ord(b) and i != len(a)-1:
            list.append(a[e:i])
            e = i+1
        elif  i == len(a) - 1:
            if ord(a[i]) != ord(b):
                list.append(a[e:i+1])
            else:
                list.append(a[e:i])
    return list

def cekData(filename, username, delimiter=";"):
    with open(filename, 'r') as file:
        for baris in file:
            listbaris = splitmanual(baris.strip(), b=delimiter)
            if len(listbaris) >= 2:
                existing_username= listbaris[1]
                if existing_username == username:
                    return True
    return False

def nomorUser(filename, delimiter=";"):
    with open(filename, 'r') as file:
        urutan = []
        for baris in file:
            listbaris = splitmanual(baris.strip(), b=delimiter)
            urutan.append(int(listbaris[0]))
        return urutan[-1] + 1

def cekUser(username):
    statususer = False
    syaratuser = [chr(ord('A') + i) for i in range(26)] + [chr(ord('a') + i) for i in range(26)] + [str(i) for i in range(10)] + ["-", "_"]
    for i in username:
        if i not in syaratuser:
            statususer = True
            break
    return statususer

def tambahUser(filename, username, password, role="Agent", coin = "0", delimiter=";"):
    if cekData(filename, username, delimiter):
        print(f"Username {username} sudah terpakai, silahkan gunakan username lain!")
        return
    if cekUser(username):
        print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
        return
    urutan = nomorUser(filename, delimiter)
    with open(filename, 'a') as file:
        monster = int(input("Silahkan pilih salah satu monster sebagai monster awalmu.\n1. Charizard\n2. Bulbasaur\n3. Aspal\nMonster pilihanmu: "))
        monster = "Charizard" if monster == 1 else ("Bulbasaur" if monster == 2 else "Aspal")
        file.write("\n" + str(urutan) + delimiter+ username + delimiter + password + delimiter + role + delimiter + coin)
    print(f"Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster}!")

filename = "c:\\Users\\athar\\Downloads\\Kuliah\\S2\\Dasar Pemrograman\\Tugas Besar\\Register.csv"
username = input("Enter username: ")
password = input("Enter password: ")
statusLogin = False
while not statusLogin:
    tambahUser(filename, username, password)
    statusLogin = True
print(f"Register gagal!\nAnda telah login dengan username {username}, silahkan lakukan “LOGOUT” sebelum melakukan register.")
