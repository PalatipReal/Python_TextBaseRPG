from Class_Characeter import Player_Characeter
from Class_Characeter import Monter_Characeter
class MainGame(Player_Characeter) :                              
    def __init__(self,name,age):
        super().__init__(name,age)              
    def BattleStart(self):
        # สร้าง Class Monter เพือมาต่อสู้กับผู้เล่น
        Monter = Monter_Characeter()
        # กำหนด ตัวแปร StateBattle เพื่อกำหนดเงื่อนไขการทำงาน    
        StateBattle = 0 
        # วนลูปไปเรื่อยๆ จนกว่าตัวแปร StateBattle จะมีค่าเท่ากับ "3"
        while StateBattle != "3" :
            # แสดงข้อความ สถานะผู้เล่น และ Monter โดยมี Lvl,HP 
            print("Player Lv.  :    "+str(self.getPlayerNow_lvl())+"/"+str(self.getPlayerMax_lvl())
                +"             "
                    +"Monter Lv. : "+str(Monter.getMonterNow_lvl())+"/"+str(Monter.getMonterMax_lvl())
                    )
            print("Player HP   :    "+str(self.getPlayerNow_HP())+"/"+str(self.getPlayerMax_HP())
                +"           "
                    +"Monter HP. : "+str(Monter.getMonterNow_Hp())+"/"+str(Monter.getMonterMax_Hp())
                    )
            # แสดงคำสั่งให้ผู้เล่นสั่งการ มี โจมตี ป้องกัน หลบหนี
            print("********************************************")
            print("[1] : Attack")
            print("[2] : Def")
            print("[3] : Run")
            print("Select Action...")
            print("********************************************")
            # รับค่าจาก Keyborad เพื่อทำเช็คเงื่อนไขการทำงาน 
            StateBattle = input()
            # เลือก 1 โจมตี มอนเตอร์
            if StateBattle == "1" :
                # รับค่าจาก Class Player_Chareacter ผ่าน method GetPlayerRealDamage() มาเก็บตัวแปร PlayerRealDamage
                PlayerRealDamage = self.GetPlayerRealDamage()
                # คำนวณเลือดของ Monter ผ่าน  method setMonterNow_Hp() 
                # โดยนำค่า HP ของ Monter ผ่าน method getMonterNow_Hp() 
                # ปัจจุบันมาลบกับ ตัวแปร PlayerRealDamage
                Monter.setMonterNow_Hp( Monter.getMonterNow_Hp() - PlayerRealDamage )
                # แสดงข้อคุวาม พลังโจมตีที่ผู้เล่นทำได้
                print("Player Attack : "+str(PlayerRealDamage))
                # เงื่อนไข ถ้า Monter มีเลือดต่ำกว่าหรือเท่ากับ 0
                # ทำการลบ Class Monter 
                # แสดงข้อความ Monter Dead 
                # ให้ตัวแปร StateBattle เท่ากับ 3 เพื่อให้หลุดจากลูป Battle
                # จบการทำงานของ เงื่อนไข 
                if (Monter.getMonterNow_Hp()<=0):
                    del Monter
                    print("Monter Dead...") 
                    StateBattle = "3"
                    return
                # รับค่าจาก Class Monter_Chareacter ผ่าน method getMonterRealDamage() มาเก็บตัวแปร MonterRealDamage
                MonterRealDamage = Monter.getMonterRealDamage()
                # คำนวณเลือดของ Monter ผ่าน  method setPlayerNow_HP() 
                # โดยนำค่า HP ของ Monter ผ่าน method getPlayerNow_HP() 
                # ปัจจุบันมาลบกับ ตัวแปร MonterRealDamage
                self.setPlayerNow_HP(self.getPlayerNow_HP() - MonterRealDamage)
                print("Monter Attack : "+str(MonterRealDamage))
                # เงื่อนไข ถ้า Player มีเลือดต่ำกว่าหรือเท่ากับ 0
                # ให้ตัวแปร StateBattle เท่ากับ 3 เพื่อให้หลุดจากลูป Battle
                # จบการทำงานของ เงื่อนไข 
                if (self.getPlayerNow_HP() <= 0):
                    StateBattle = "3"
                    return
            elif StateBattle == "2" :
                print("def")
            elif StateBattle == "3" :
                print("Run")
            else:
                print("In put Wrong PLS Try Again...\n")
                
        
