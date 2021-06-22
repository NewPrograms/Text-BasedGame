# This is the part where all scenarios are typed our or played out.
from combat import Combat

class Scenes:


    def __init__(self, u_name, password):
       self.u_name = u_name
       self.password = password
            
    def starting_scene(self):
        print(
            "Huff! Huff! Those zombies are everywhere! I don't know if I can escape\nn",
            "This damned forest! How did this happen!(Flashback)\n",
            "Drafted by that damned king I was forced into the frontlines of the forest of Acacia\n",
            "This dreaded forest consisted of ghastly trees, vicious monsters, and a thick fog",
            "Sensing danger and death our commander ordered for someone to get out of the forest and ",
            "ask for reinforcements. Being close to him I was picked. Unfortunately, zombies noticed me moving",
            " and have been hunting me ever since.", "Damn it! How can I escape this! "
            )
        self.monster = 'zombies'
        if self.conditions(self.monster) == True:
            self.second_act()



    def second_act(self):
        print(
            "NC! Luckily I was able to ran away! Sigh...(Walks away)\n"
            "Looks like I'm now at the end of this damn trees."
            "(Sees temple...) What is that! Looks amazing!(Hears clanking noises)"
            "Oh crap looks like I have to do this all over again."
        )
        self.monster = 'skeletons'
        if self.conditions(self.monster) == True:
            self.third_act()
        
        
        
        else: 
            self.third_act() # This is a temporary fix for a bug

    def third_act(self):
        print('lmao')
        

    def conditions(self, monsters):
        # The cause of the bug is unkown but this is the possbile reason.
        self.combat = Combat(self.u_name, self.password, monsters)
        if self.combat.options() == True:
            return True


        else:
            self.conditions(self.monster)

