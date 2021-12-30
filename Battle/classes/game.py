import random
from classes.magic import spell

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self,name,hp,mp,atk,df,magic,items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk-10
        self.atkh = atk+10
        self.df = df
        self.magic = magic
        self.Items = items
        self.name = name
        self.actions = ["Attack","Magic","Items"]

    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)

    def take_damage(self,dmg):
        self.hp -= dmg
        if(self.hp<=0):
            self.hp=0
        return self.hp

    def get_hp(self):
        return self.hp
    def get_mp(self):
        return self.mp
    def get_maxhp(self):
        return self.maxhp
    def get_maxmp(self):
        return self.maxmp
    def reduce_mp(self,cost):
        self.mp -=cost
    def heal(self,dmg):
        self.hp+=dmg
        if self.hp>self.maxhp:
            self.hp = self.maxhp
    def choose_action(self):
        i = 1
        print("\n    "+bcolors.BOLD+self.name+bcolors.ENDC)
        print(bcolors.OKBLUE+bcolors.BOLD+"    ACTIONS"+bcolors.ENDC)
        for item in self.actions:
            print("        "+str(i)+":",item)
            i+=1
    def choose_magic(self):
        i = 1
        print(bcolors.BOLD+bcolors.HEADER+"    MAGIC"+bcolors.ENDC)
        for spell in self.magic:
            print("    "+str(i)+":"+spell.type+", "+spell.name+"("+
                  "cost:"+bcolors.BOLD+bcolors.OKBLUE+str(spell.cost)+"MP"+bcolors.ENDC+")")
            i+=1
        print()
    def choose_Items(self):
        i = 1
        print(bcolors.BOLD+bcolors.OKBLUE+"ITEMS"+bcolors.ENDC)
        for item in self.Items:
            print("    "+bcolors.BOLD+bcolors.OKBLUE+str(i)+bcolors.ENDC+":"+item["Item"].name+" - "+item["Item"].description+
                  "(x"+str(item["quantity"])+")")
            i+=1
        print()
    def get_stats(self):
        print("                          _________________________            __________")
        strhp = str(self.hp)+"/"+str(self.maxhp)
        while len(strhp)<9:
            strhp = " "+strhp
        calcHpBar = (self.hp/self.maxhp)*25
        calcMpBar = (self.mp/self.maxmp)*10
        barHp = ""
        barMp = ""
        i = 25
        while i>0:
            if calcHpBar>=0:
                calcHpBar-=1
                barHp = barHp+"█"
            else:
                barHp = barHp+" "
            i-=1
        i=10
        while i>0:
            if calcMpBar>=0:
                calcMpBar-=1
                barMp = barMp+"█"
            else:
                barMp = barMp+" "
            i-=1
        strmp = str(self.mp)+"/"+str(self.maxmp)
        while len(strmp)<7:
            strmp = " "+strmp
        print(self.name+"         "+strhp+"|" + bcolors.OKGREEN + barHp + bcolors.ENDC + "|   "
              +strmp+"|" + bcolors.OKBLUE + barMp + bcolors.ENDC + "|")
    def choose_target(self,enemys):
        i=1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "    TARGET" + bcolors.ENDC)
        for enemy in enemys:
            if enemy.get_hp()!=0:
                print("        "+str(i)+":",enemy.name)
                i+=1
        choice = int(input("    Please enter your target"))-1
        if choice<0|choice>len(enemys)-1:
            return 0
        return choice

    def get_enemy_stats(self):
        print("                          __________________________________________________")
        strhp = str(self.hp) + "/" + str(self.maxhp)
        calcHpBar = (self.hp / self.maxhp) * 50
        barHp = ""
        i = 50
        while len(strhp)<11:
            strhp = " "+strhp
        while i > 0:
            if calcHpBar >= 0:
                calcHpBar -= 1
                barHp = barHp + "█"
            else:
                barHp = barHp + " "
            i -= 1
        print(self.name + "         " + strhp + "|" + bcolors.FAIL + barHp + bcolors.ENDC + "|")
    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.dmg
        if self.mp < spell.cost:
            self.choose_enemy_spell()
        else:
            return spell