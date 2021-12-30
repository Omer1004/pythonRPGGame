from classes.game import bcolors, Person
from classes.magic import spell
from classes.inventory import Item
import random



#Creating Black Magic
fire = spell("Fire",8,250,"Black")
metheor = spell("Metheor",10, 297,"Black")
thunder = spell("Thunder",20,715,"Black")
water = spell("Water",10,289,"Black")
ground = spell("Ground",11,340,"Black")
air = spell("Air",5,220,"Black")

#Creating White Magic
cure = spell("Cure",10,500,"White")
cura = spell("Cura",20,1500,"White")

#Creating Items
potion = Item("Potion","hppotion","Heals 500 HP",500)
hipotion = Item("High Potion","hppotion","Heals 1000 HP",1000)
superpotion = Item("Super Potion","hppotion","Heals 1500 HP",1500)
elixer = Item("Elixer","elixer","Fully restores HP/MP of one party member",9999)
hielixer = Item("Mega Elixer","elixer","Fully restores party's HP/MP",9999)
granade = Item("Granade","attack","Deals 500 damage",500)
mppotion = Item("Magic Points Potion","mppotion","restores 40 Magic Points",40)
hmppotion = Item("Magic Points Potion","mppotion","restores 80 Magic Points",80)


player_magic = [fire,metheor,water,thunder,cure,cura]
player_items = [{"Item":potion,"quantity":2},{"Item":hipotion,"quantity":2},
                {"Item":superpotion,"quantity":2},{"Item":elixer,"quantity":2},
                {"Item":hielixer,"quantity":2},{"Item":granade,"quantity":3},
                {"Item":mppotion,"quantity":2},{"Item":hmppotion,"quantity":2}]
enemy_magic = [fire,metheor,cure]
enemy_items = [{"Item":potion,"quantity":2},{"Item":hielixer,"quantity":2},{"Item":granade,"quantity":3}]

#Defining Players
player1 = Person("Doctor ", 3000, 132, 180, 34, player_magic, player_items)
player2 = Person("Omer   ",2500,211,200,34,player_magic,player_items)
player3 = Person("Nick   ",2000,158,214,34,player_magic,player_items)
players = [player1, player2, player3]

#Defining Enemys
enemy1 = Person("Magos", 11000, 65, 400, 100, [fire, air, cure, cura], enemy_items)
enemy2 = Person("Imp  ",1250,130,250,150,enemy_magic,enemy_items)
enemy3 = Person("Imp2 ",1350,135,244,140,enemy_magic,enemy_items)
enemys = [enemy1,enemy2,enemy3]


running = True
i = 0
defited_enemys = 0
defited_players = 0
choice = 1
print(bcolors.OKBLUE+bcolors.BOLD+"lets start")
print("balagan"+bcolors.ENDC)


#Game
while running:
    for player in players:
        if running:
            if defited_enemys == 3:
                continue
            print("================================================================")#get stats
            print("NAME                    HP                                    MP")
            for i in players:
                i.get_stats()
            print()
            for i in enemys:
                i.get_enemy_stats()
            player.choose_action()#choose action
            choice = input("Please enter your choice: ")
            index = int(choice) - 1
            while index<-1|index>2:
                print("Invalid Option please enter your choice again")
                player.choose_action()
                choice = input("Please enter your choice: ")
            if index == -1:
                running = False
                continue


            if index == 0:#if player attack
                dmg = player.generate_damage()
                enemy = player.choose_target(enemys)
                enemys[enemy].take_damage(dmg)
                print("you attacked "+enemys[enemy].name.replace(" ","")+ " for",bcolors.FAIL+ str(dmg)+bcolors.ENDC+" HP")
                if enemys[enemy].get_hp()==0:
                    print(bcolors.BOLD+bcolors.FAIL+enemys[enemy].name+" have died"+bcolors.ENDC)
                    del enemys[enemy]
                    defited_enemys += 1
            elif index == 1:#This is if the player chooses magic
                player.choose_magic()
                magic_choice = int(input("Choose magic: "))-1
                if magic_choice == -1:
                    continue
                spell = player.magic[magic_choice]
                magic_dmg = spell.dmg
                print("you chose the Magic",spell.name)
                cost = spell.cost
                current_mp = player.get_mp()
                if cost>current_mp:
                    print(bcolors.FAIL+"not enough MP"+bcolors.ENDC)
                    continue
                player.reduce_mp(cost)
                if spell.type == "White":
                    player.heal(spell.dmg)
                    print("you have successfuly healed",bcolors.OKBLUE+bcolors.BOLD,spell.dmg,"HP"+bcolors.ENDC)
                elif spell.type == "Black":
                    enemy = player.choose_target(enemys)
                    enemys[enemy].take_damage(magic_dmg)
                    print("you attacked "+enemys[enemy].name.replace(" ","") +
                          " for",bcolors.FAIL+bcolors.BOLD+ str(magic_dmg)+bcolors.ENDC + " points")
                    if enemys[enemy].get_hp() == 0:
                        print(bcolors.BOLD + bcolors.FAIL + enemys[enemy].name + " have died"+bcolors.ENDC)
                        del enemys[enemy]
                        defited_enemys += 1
                        if defited_enemys == 3:
                            continue
                print("spell "+bcolors.HEADER+bcolors.BOLD+spell.name+bcolors.ENDC+" cost "+bcolors.BOLD+bcolors.OKBLUE+str(cost)+"MP"+bcolors.ENDC)

            elif index == 2:#if player choose item
                player.choose_Items()
                itemchoice = int(input("Choose Item: "))-1
                if itemchoice == -1:
                    continue
                player.Items[itemchoice]["quantity"]=int(player.Items[itemchoice]["quantity"])-1
                if player.Items[itemchoice]["quantity"]>=0:
                    item = player.Items[itemchoice]["Item"]
                    if item.type == "hppotion":
                        player.heal(item.prop)
                        print("\n"+bcolors.OKGREEN+bcolors.BOLD+player.name.replace(" ","")+" heals for",str(item.prop),"HP"+bcolors.ENDC)
                    elif item.type == "elixer":
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                        print("\n"+bcolors.OKGREEN+bcolors.BOLD+"fully restores HP/MP"+bcolors.ENDC)
                    elif item.type == "attack":
                        enemy = player.choose_target(enemys)
                        enemys[enemy].take_damage(item.prop)
                        print("deals "+bcolors.FAIL+bcolors.BOLD+str(item.prop),bcolors.ENDC+" points of damage to"
                              +bcolors.FAIL+bcolors.BOLD,enemys[enemy].name.replace(" ","")+bcolors.ENDC)
                        if enemys[enemy].get_hp() == 0:
                            print(bcolors.BOLD + bcolors.FAIL + enemys[enemy].name.replace(" ","") + " have died"+bcolors.ENDC)
                            del enemys[enemy]
                            defited_enemys += 1
                            if defited_enemys ==3:
                                continue
                    elif item.type == "mppotion":
                        player.mp+=item.prop
                        print("\n"+bcolors.OKBLUE+bcolors.BOLD+"MP incresed in"+str(item.prop)+"MP"+bcolors.ENDC)
                else:
                    print("\n"+bcolors.FAIL+bcolors.BOLD+"None Avilable"+bcolors.ENDC)
                    continue

    print()
    # Enemy attack
    for enemy in enemys:
        if defited_enemys == 3:
            continue
        enemy_target = random.randrange(0, len(players))
        enemy_choice = random.randrange(0, 3)
        if enemy.mp<15 and enemy_choice==1:
            enemy_choice=0
        if enemy_choice == 0:
            enemy_dmg = enemy.generate_damage()
            players[enemy_target].take_damage(enemy_dmg)
            print(enemy.name.replace(" ", "") + " attacked " + players[enemy_target].name.replace(" ", "") + " for",
                  bcolors.FAIL + str(enemy_dmg), "HP", bcolors.ENDC)
            if players[enemy_target].get_hp() == 0:
                print(bcolors.BOLD + bcolors.FAIL + players[enemy_target].name.replace(" ","") + " have died" + bcolors.ENDC)
                del players[enemy_target]
                defited_players += 1
        elif enemy_choice == 1:
            spell = enemy.choose_enemy_spell()
            magic_dmg = spell.dmg
            print(enemy.name.replace(" ", "") + " chose the Magic", spell.name)
            cost = spell.cost
            current_mp = enemy.get_mp()
            if cost > current_mp:
                print(bcolors.FAIL + "not enough MP" + bcolors.ENDC)
                continue
            enemy.reduce_mp(cost)
            if spell.type == "White":
                enemy.heal(spell.dmg)
                print(enemy.name.replace(" ", "") + " have successfuly healed", bcolors.OKBLUE + bcolors.BOLD,
                      spell.dmg, "HP" + bcolors.ENDC)
            elif spell.type == "Black":
                players[enemy_target].take_damage(magic_dmg)
                print(enemy.name.replace(" ", "") + " attacked " + players[enemy_target].name.replace(" ", "") +
                      " for", bcolors.FAIL + bcolors.BOLD + str(magic_dmg) + bcolors.ENDC + " points")
                if players[enemy_target].get_hp() == 0:
                    print(bcolors.BOLD + bcolors.FAIL + players[enemy_target].name.replace(" ",
                                                                                           "") + " have died" + bcolors.ENDC)
                    del players[enemy_target]
                    defited_players += 1
        elif enemy_choice == 2:
            itemchoice = random.randrange(0, len(enemy.Items))
            enemy.Items[itemchoice]["quantity"] = int(enemy.Items[itemchoice]["quantity"]) - 1
            if player.Items[itemchoice]["quantity"] >= 0:
                item = enemy.Items[itemchoice]["Item"]
                if item.type == "potion":
                    enemy.heal(item.prop)
                    print("\n" + enemy.name.replace(" ", "") + bcolors.OKGREEN + bcolors.BOLD + "heals for",
                          str(item.prop),
                          "HP" + bcolors.ENDC)
                elif item.type == "elixer":
                    enemy.hp = enemy.maxhp
                    enemy.mp = enemy.maxmp
                    print(enemy.name.replace(" ",
                                             "") + bcolors.OKGREEN + bcolors.BOLD + " fully restores HP/MP" + bcolors.ENDC)
                elif item.type == "attack":
                    players[enemy_target].take_damage(item.prop)
                    print("\n" + "deals " + bcolors.FAIL + bcolors.BOLD + str(item.prop),
                          bcolors.ENDC + " points of damage" + "to"
                          + bcolors.FAIL + bcolors.BOLD, players[enemy_target].name.replace(" ", "") + bcolors.ENDC)
                    if players[enemy_target].get_hp() == 0:
                        print(bcolors.BOLD + bcolors.FAIL + players[enemy_target].name.replace(" ",
                                                                                               "") + " have died" + bcolors.ENDC)
                        defited_players += 1
                        del players[enemy_target]
                elif item.type == "mppotion":
                    enemy.mp += item.prop
                    print("\n" + enemy.name + bcolors.OKBLUE + bcolors.BOLD + " MP incresed in " + str(
                        item.prop) + "MP " + bcolors.ENDC)
            else:
                print("\n" + bcolors.FAIL + bcolors.BOLD + "None Avilable" + bcolors.ENDC)
                continue


    if defited_enemys == 3:
        print(bcolors.OKGREEN + bcolors.BOLD + "You Win" + bcolors.ENDC)
        running = False
    if defited_players == 3:
        print(bcolors.FAIL + bcolors.BOLD + "You Lose" + bcolors.ENDC)
        running = False





