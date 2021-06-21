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
        self.combat = Combat(self.u_name, self.password, self.monster)
        if self.combat.options() == True:
            self.second_act()

        else:
            self.combat.options()

    def second_act(self):
        print(
            "NC! Luckily I was able to ran away! Sigh...(Walks away)\n"
            "Looks like I'm now at the end of this damn trees."
            "(Sees temple...) What is that! Looks amazing!(Hears clanking noises)"
            "Oh crap looks like I have to do this all over again."
        )
        self.monster = 'skeletons'
        self.combat = Combat(self.u_name, self.password, self.monster)
        self.skeleton = True
        if self.combat.options() == True:
            self.third_act()

        else:
            self.combat.options()
    def third_act(self):
        print('lmao')
        

