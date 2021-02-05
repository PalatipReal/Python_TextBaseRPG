from MainGame import MainGame
print("\n *-*-*-*-*-*-*-*-* Dev TextBase Game build 0.0.1 22/1/2564 *-*-*-*-*-*-*-*-* \n            Make By Palatip ")
print("Character Creator ")
print("\n")
S = MainGame(input("Enter playername:"),input("Enter age:"))
StatePlayer = 0                                                     # เงื่อนไขการทำงาน
while StatePlayer != "4" :
    print("********************************************")
    print("[1] : Start Battle")
    print("[2] : Stat")
    print("[3] : Setting")
    print("[4] : Exit")
    print("Select Action...")
    print("********************************************")
    StatePlayer = input()

    if StatePlayer == "1" :
        S.BattleStart()
        if(S.getPlayerNow_HP() <= 0 ):
            StatePlayer = "4"
            print("Player Dead...")
    elif StatePlayer == "2" :
        S.displaystat()

    elif StatePlayer == "3" :
        print("Setting")

    elif StatePlayer == "4" :
        print("Player Exit....")
    else:
        print("In put Wrong PLS Try Again...\n")
        