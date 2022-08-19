
from curses.ascii import isalnum, isalpha, ispunct
import os
import uuid
import secrets
import string
import fileinput


class user:
    def __init__(self,login,parol,id,age,tel,male):
        self.login = login
        self.password = parol
        self.id = id
        self.age = age
        self.tel = tel
        self.male = male

    def register(self,login,parol,id,age,tel,male):
        f = open("database.txt","a")
        f.write(f"""login: {login}
parol: {parol}
id: {id}
age: {age}
tel: {tel}
male: {male}\n\n""")
        f.close()
        print("Tabriklaymiz.Siz muvaffaqiyatli ro'yhatdan o'tdingiz!")
    def loginIn(self,login,parol):
        bool = False
        f = open("database.txt","r").read()
        lst = f.split("\n\n")
        for i in lst:
            for qator in i.split("\n"):
                soz = qator.split()
                if bool == True:
                    if len(soz)>1 and soz[0] == "parol:" and soz[1] == parol:
                        print("\nTabriklaymiz siz tizimga muvaffaqiyatli kirdingiz!\n")
                        print(i)
                        return True
                if len(soz)>1 and soz[0] == "login:" and soz[1] == login:
                    bool = True
                else:
                    bool = False
        if bool == False:
            return False
    def changePassword(self,parol,yangi):
        bool1 = False
        n = open("database.txt","r+")
        for line in fileinput.input("database.txt"):
            if parol in line:
                bool1 == True
            n.write(line.replace(parol,yangi))
        n.close()
    def show_users(self):
        r = open("database.txt","r")
        print(r.read())
        r.close()
    def checkParolAndCheckLogin(self,login,parol):
        count = 0
        for i in range(len(login)):
            if isalpha(login[i]) or isalnum(login[i]) or login[i] == "_":
                count+=1
        if count == len(login):
            count1 = 0
            count2 = 0
            count3 = 0
            for i in range(len(parol)):
                if isalpha(parol[i]):
                    count1+=1
                elif isalnum(parol[i]):
                    count2+=1
                elif parol[i] == "_":
                    count3+=1
            if count1>0 and count1+count2+count3 == len(parol) and count2>0:
                return True
            else:
                return False
        else:
            return False

    def generatePassword():
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(10))  
        return password
    def getUserById(self,id):
        d = open("database.txt","r").read()
        lst = d.split("\n\n")
        for i in lst:
            for qator in i.split("\n"):
                soz = qator.split()
                if len(soz)>1 and soz[0] == "id:" and soz[1] == id:
                    return i
    def checknumber(self,number):
        count = 0
        for i in range(len(number)):
            if i == 0 and number[i] == "+":
                count+=1
            elif isalnum(number[i]):
                count+=1
        return count == len(number)

print("Assalomu alaykum hurmatli foydalanuvchi! ")
print("[1] Ro'yhatdan o'tish.\n[2] Profilga kirish.")
print("[3] Barcha foydalanuvchilarni ko'rish.")
print("[4] id bo'yicha izlash")

tanlov = input("son kiriting: ")
if tanlov == "1":
    login = str()
    parol = str()
    id = str()
    age = str()
    tel = str()
    male = str()
    odam = user(login,parol,id,age,tel,male)
    while 1:
        login = input("Login kiriting: ")
        print("random parol uchun [ha/yo'q]")
        rozi = input()
        if rozi == "ha":
            parol =  user.generatePassword()
            print("bu sizning parolingiz",parol)
        else:
            parol = input("parol kiriting: ")
        if len(login)>=8 and len(parol)>=8:
            if odam.checkParolAndCheckLogin(login,parol):
                print("login va parol qabul qilindi.")
                break
            else:
                print("login yoki parolingiz hato.\nEslatma: login 8 ta harf va sonlar yigindisidan")
                print("(sonlar majburiy emas) iborat bo'lishi kerak")
                print("parol kiritishda esa sonlar va harflar (ikkisidan ham qatnashishi shart) yigindisi 8 dan oshishi kerak ")
                print("Qaytadan urinib ko'ring! ")
    id = uuid.uuid4()
    age = input("Yoshingizni kiriting: ")
    while 1:
        print("raqam uchun namuna ==> +998949174127 ")
        tel = input("Raqamingizni kiriting: ")
        if len(tel) == 13:
            if odam.checknumber(tel):
                print("raqam qabul qilindi")
                break
            else:
                print("bunday raqam mavjud emas.")
        else:
            print("Raqamni qaytadan kiriting.")
    male = input("jinsingiz: ")
    user.register(odam,login,parol,id,age,tel,male)
elif tanlov == "2":
    print("Ro'yhatdan o'tgan bo'lsangiz")
    booling = False
    while 1:
        if booling == True:
            break
        login = input("login kiriting: ")
        parol = input("parol kiriting: ")
        if user.checkParolAndCheckLogin(None,login,parol):
            if user.loginIn(None,login,parol):
                print("parolni o'zgartirishni hohlaysizmi? [ha/yo'q]")
                tanlov = input()
                if tanlov == "ha":
                    while 1:
                        yangi = input("yangi parol kiriting: ")
                        if user.checkParolAndCheckLogin(None,login,yangi):
                            user.changePassword(None,parol,yangi)
                            print(f"parolingiz {yangi} ga o'zgardi")
                            booling = True
                            break
                        else:
                            print(" yang parol to'g'ri kelmaydi. Qaytadan kiriting. ")
                else:
                    print("OK. o'zingiz bilasiz ")
            else:
                print("bunday profil yo'q qaytadan kiriting: ")
        else:
            print("hatolik bor qaytadan kiriting:")
elif tanlov == "3":
    print()
    user.show_users(None)
elif tanlov == "4":
    id = input("id kiriting: ")
    print(user.getUserById(None,id))
else:
    print("o'zi 4 ta son berilgan ko'z bormi ibiiii")
