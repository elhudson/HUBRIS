import sqlite3
import pandas as pd
 
from logic.processing import generate_abilities, feature, skill_proficiency, power, effect, duration, rng, background, tag_feature, class_feature, pcclass

class Character:
    def __init__(self,player,con):
        sql=f'SELECT * FROM characters WHERE player="{player}"'
        df=pd.read_sql(sql,con)

        self.name=df["name"][0]
        self.str=df["str"][0]
        self.dex=df["dex"][0]
        self.con=df["con"][0]
        self.int=df["int"][0]
        self.wis=df["wis"][0]
        self.cha=df["cha"][0]
        self.xp_earned=df["xp_earned"][0]
        self.xp_spent=df["xp_spent"][0]
        self.alignment=df["alignment"][0]
        self.ability_ids=df["abilities"][0] 
        self.backgrounds=[]
        self.effects=[]
        self.durations=[]
        self.ranges=[]
        self.skills=[]
        self.tag_features=[]
        self.class_features=[]
        self.armor_proficiencies=[]

        self.define_abilities(con)
        self.bin_abilities()
        self.set_tier()
        self.set_hp_max()
        self.skills_str()

          
    def define_abilities(self,con):
        ids_list=self.ability_ids.split(",")
        abs=generate_abilities(ids_list,con)
        self.abilities=abs
        
    def skills_str(self):
        self.skill_names=""
        for skill in self.skills:
            self.skill_names+=skill.name+","

    def set_tier(self):
        spent=self.xp_spent
        self.tier=None
        if 0<spent<=25:
            self.tier=1
        elif 25<spent<=75:
            self.tier=2
        elif 75<spent<=135:
            self.tier=3
        elif 135<spent:
            self.tier=4
        
    def set_hp_max(self):
        self.hp_max=(3*(self.tier))+self.con
        
    def bin_abilities(self):
        for ability in self.abilities:
            if type(ability)==background:
                self.backgrounds.append(ability)
            if type(ability)==pcclass:
                self.char_class=ability
            if type(ability)==effect:
                self.effects.append(ability)
            if type(ability)==rng:
                self.ranges.append(ability)
            if type(ability)==duration:
                self.durations.append(ability)
            if type(ability)==skill_proficiency:
                self.skills.append(ability)
            if type(ability)==tag_feature:
                self.tag_features.append(ability)
            if type(ability)==class_feature:
                self.class_features.append(ability)
            if type(ability)==pcclass:
                self.char_class=ability
                ability.define_hd()
                self.hit_die=ability.hit_die
