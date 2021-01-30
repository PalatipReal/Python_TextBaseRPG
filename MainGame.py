from Class_Characeter import Player_Characeter
from Class_Characeter import Monter_Characeter
class MainGame(Player_Characeter) :                              
    def __init__(self,name,age):
        super().__init__(name,age)              
    def BattleStart(self):
        Monter = Monter_Characeter()
        StateBattle = 0 
        while StateBattle != "3" :
            print("Player Lv.  :    "+str(self.getPlayerNow_lvl())+"/"+str(self.getPlayerMax_lvl())
                +"             "
                    +"Monter Lv. : "+str(Monter.getMonterNow_lvl())+"/"+str(Monter.getMonterMax_lvl())
                    )
            print("Player HP   :    "+str(self.getPlayerNow_HP())+"/"+str(self.getPlayerMax_HP())
                +"           "
                    +"Monter HP. : "+str(Monter.getMonterNow_Hp())+"/"+str(Monter.getMonterMax_Hp())
                    )
            print("********************************************")
            print("[1] : Attack")
            print("[2] : Def")
            print("[3] : Run")
            print("Select Action...")
            print("********************************************")
            StateBattle = input()
            if StateBattle == "1" :
                PlayerRealDamage = self.GetRealDamage()
                Monter.setMonterNow_Hp( Monter.getMonterNow_Hp() - PlayerRealDamage )
                print("Player Attack : "+str(PlayerRealDamage))
                if (Monter.getMonterNow_Hp()<=0):
                    del Monter
                    print("Monter Dead...") 
                    StateBattle = "3"
                    return
                MonterRealDamage = Monter.getMonterRealDamage()
                self.setPlayerNow_HP(self.getPlayerNow_HP() - MonterRealDamage)
                print("Monter Attack : "+str(MonterRealDamage))
                if (self.getPlayerNow_HP() <= 0):
                    StateBattle = "3"
                    return
            elif StateBattle == "2" :
                print("def")
            elif StateBattle == "3" :
                print("Run")
            else:
                print("In put Wrong PLS Try Again...\n")
        