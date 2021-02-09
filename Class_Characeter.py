import random 
class Player_Characeter    :                                            # สร้าง Class สำหรับ ตัวละคร นำหน้าที่ควบคุม เก็บข้อมูลของตัวละคร
    def __init__(characeter,name,age)   :                               # ฟังชั่น ประกาศตัวแปรเริ่มต้นของ Class 
        characeter.Name                     =   name                    # รับค่า ชื่อ ตัวละคร เข้ามาจากตอนสร้าง Class 
        characeter.Age                      =   age                     # รับค่า อายุ ตัวละคร เข้ามาจากตอนสร้าง Class 
        characeter.Max_lvl                  =   100                     # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า lvl สูงสุด ของตัวละคร
        characeter.Now_lvl                  =   1                       # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า lvl ปัจจุบัน ของตัวละคร
        characeter.Max_Exp                  =   10                     # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า Exp สูงสุด ของตัวละคร
        characeter.Now_Exp                  =   1                       # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า Exp ปัจจุบัน ของตัวละคร
        characeter.Max_HP                   =   100                     # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า HP สูงสุด ของตัวละคร
        characeter.Now_HP                   =   100                     # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า HP ปัจจุบัน ของตัวละคร
        characeter.Max_Mana                 =   100                     # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า Mana สูงสุด ของตัวละคร
        characeter.Now_Mana                 =   100                     # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า Mana ปัจจุบัน ของตัวละคร
        characeter.Base_Damage              =   10                      # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า Base_Damage  ของตัวละคร
        characeter.Base_Defense             =   10                      # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า Base_Defense  ของตัวละคร             
        characeter.Base_Accuracy            =   10
        characeter.Base_Agility             =   10
        characeter.Base_Critical_Rate       =   0.1                     # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า Base_Critical_Rate  ของตัวละคร
        characeter.Vit                      =   0
        characeter.Str                      =   0
        characeter.Dex                      =   0
        characeter.Res                      =   0
        characeter.Luck                     =   0
        random.seed(characeter.Age)
    def getPlayerName(self):                                            # ประกาศ ฟังชั่น สำหรับ รับค่าชื่อตัวละคร 
        return self.Name
    def getPlayerAge(self):                                             # ประกาศ ฟังชั่น สำหรับ รับค่าอายุตัวละคร
        return self.Age
    def getPlayerBase_Damage(self):                                     # ประกาศ ฟังชั่น สำหรับ รับ Base_Damage ตัวละคร
        return self.Base_Damage
    def getPlayerBase_Defense(self):                                     # ประกาศ ฟังชั่น สำหรับ รับ Base_Damage ตัวละคร
        return self.Base_Defense
    def getPlayerMax_HP(self):                                          # ประกาศ ฟังชั่น สำหรับ รับ HP ปัจจุบัน ตัวละคร
        return self.Max_HP
    def getPlayerNow_HP(self):                                          # ประกาศ ฟังชั่น สำหรับ รับ HP ปัจจุบัน ตัวละคร
        return self.Now_HP
    def getPlayerCritical_Rate(self):
        return self.Base_Critical_Rate
    def getPlayerMax_lvl(self):
        return self.Max_lvl
    def getPlayerNow_lvl(self):
        return self.Now_lvl   
    def getDataPlayer(self):
        Data = [self.Name,self.Now_HP]
        return Data
    def GetPlayerRealDamage(self) :                                           # ประกาศ ฟังชั่น สำหรับ โจมตี 
        RealDamage = self.Base_Damage + random.randint(-5,5)
        return RealDamage
    def defense(self,damage) :                                          # ประกาศ ฟังชั่น สำหรับ โดนโจมตี
        print(Player.Name +" Was hit by someting")
        Player.Now_Hp = Player.Now_Hp+Player.Base_Defense - damage
        print("Hp = "+ str(Player.Now_Hp))
    def displaystat(self):

        print("\n *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("Player Name :    "+str(self.Name))
        print("Player Age  :    "+str(self.Age))
        print("Player Lv.  :    "+str(self.Now_lvl)+"/"+str(self.Max_lvl))
        print("Player HP   :    "+str(self.Now_HP)+"/"+str(self.Max_HP))
        print("Player Mana :    "+str(self.Now_Mana)+"/"+str(self.Max_Mana))
        print("Player EXP  :    "+str(self.Now_Exp)+"/"+str(self.Max_Exp))
        print("Player Damage   :    "+str(self.Base_Damage))
        print("Player Defense  :    "+str(self.Base_Defense))
        print("Player Critical_Rate  :  "+str(self.Base_Critical_Rate))
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n ")
    def setPlayerNow_HP(self,PlayerNowHP):
        self.Now_HP = PlayerNowHP
    def setPlayerFullHP(self):
        self.Now_HP = self.Max_HP
    def checkLvlUpPlayer(self,newPlayerExp):
        self.Now_Exp = self.Now_Exp + newPlayerExp
        if(self.Now_Exp >= self.Max_Exp):
            self.Now_lvl = self.Now_lvl + 1
            self.Now_Exp = self.Now_Exp  - self.Max_Exp 
            self.Max_Exp = 10*(self.Now_lvl*self.Now_lvl)/1
            self.SelectStatusPlayer()
            print("Player Lv.  :    "+str(self.Now_lvl)+"/"+str(self.Max_lvl)) 
            print("Player EXP  :    "+str(self.Now_Exp)+"/"+str(self.Max_Exp))   
    def setLvlUpPlayer(self):
        self.Now_lvl = self.Now_lvl + 1
        self.Now_Exp = 0
        self.Max_Exp = 10*(self.Now_lvl*self.Now_lvl)/1
        self.SelectStatusPlayer()
    def SelectStatusPlayer(self):
        print("********************************************")
        print("[1] : Vit")
        print("[2] : Str")
        print("[3] : Dex")
        print("[4] : Res")
        print("[5] : Luck")
        print("Select Status...")
        SelectStatusPlayer = ""
        while SelectStatusPlayer != "EndSelectStatusPlayer" :
            SelectStatusPlayer = input()
            if SelectStatusPlayer == "1" :
                print("Select Vit")
                self.Vit            = self.Vit + 1
                self.Max_HP         = self.Max_HP + 10
                self.Base_Damage    = self.Base_Damage + 1
                self.Base_Defense   = self.Base_Defense +2
                return
            elif SelectStatusPlayer == "2" :
                print("Select Str")
                self.Str            = self.Str + 1
                self.Max_HP         = self.Max_HP + 2
                self.Base_Damage    = self.Base_Damage + 2
                self.Base_Defense   = self.Base_Defense +10
                return
            elif SelectStatusPlayer == "3" :
                print("Select Dex")
                self.Dex            = self.Dex + 1
                self.Base_Accuracy  = self.Base_Accuracy + 5
                self.Base_Agility   = self.Base_Agility + 5
                self.Base_Damage    = self.Base_Damage + 2
                return
            elif SelectStatusPlayer == "4" :
                print("Select Res")
                self.Res            = self.Res +1
                self.Base_Defense   = self.Base_Defense + 10
                self.Max_HP         = self.Max_HP + 2
                return
            elif SelectStatusPlayer == "5" :
                print("Select Luck")
                self.Luck               = self.Luck +1
                self.Base_Critical_Rate = self.Base_Critical_Rate + 0.1
                self.Max_HP             = self.Max_HP + 1
                self.Base_Damage        = self.Base_Damage + 1
                self.Base_Defense       = self.Base_Defense +1
                self.Base_Accuracy      = self.Base_Accuracy + 1
                self.Base_Agility       = self.Base_Agility + 1
                return
            else:
                print("In put Wrong PLS Try Again...\n")
                print("********************************************")
class Monter_Characeter    :                                            # สร้าง Class สำหรับ Monter นำหน้าที่ควบคุม เก็บข้อมูลของตัวละคร
    def __init__(Monter)   :                                            # ฟังชั่น ประกาศตัวแปรเริ่มต้นของ Class 
        Monter.Max_lvl                  =   100                     # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า lvl สูงสุด ของตัวละคร
        Monter.Now_lvl                  =   1                       # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า lvl ปัจจุบัน ของตัวละคร
        Monter.Max_HP                   =   10                     # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า HP สูงสุด ของตัวละคร
        Monter.Now_HP                   =   10                     # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า HP ปัจจุบัน ของตัวละคร
        Monter.Max_Mana                 =   100                     # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า Mana สูงสุด ของตัวละคร
        Monter.Now_Mana                 =   100                     # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า Mana ปัจจุบัน ของตัวละคร
        Monter.Base_Damage              =   5                       # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า Base_Damage  ของตัวละคร
        Monter.Base_Defense             =   10                      # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า Base_Defense  ของตัวละคร             
        Monter.Base_Critical_Rate       =   0.1                     # ประกาศ สร้างตัวแปร สำหรับ เก็บค่า Base_Critical_Rate  ของตัวละคร
    def getMonterMax_lvl(self):
        return self.Max_lvl
    def getMonterNow_lvl(self):
        return self.Now_lvl
    def getMonterBase_Damage(self):                                     # ประกาศ ฟังชั่น สำหรับ รับ Base_Damage ตัวละคร
        return self.Base_Damage
    def getMonterNow_Hp(self):                                          # ประกาศ ฟังชั่น สำหรับ รับ HP ปัจจุบัน ตัวละคร
        return self.Now_HP
    def getMonterMax_Hp(self):
        return self.Max_HP
    def setMonterNow_Hp(self,NowHP):
        self.Now_HP = NowHP
    def getMonterRealDamage(self):
        return self.Base_Damage + random.randint(-5,5)
    def getExpFromMonter(self):
        return ( (150 * self.Now_lvl )/10 )