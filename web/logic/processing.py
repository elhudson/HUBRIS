import sqlite3
import pandas as pd

def is_relational(function_name):
    l=function_name.split()
    if len(l)==1:
        return False
    else:
        return True

def get_tables(con):
    s=f'SELECT * FROM sqlite_master WHERE type="table"'
    tables=[]
    cur=con.cursor()
    for row in cur.execute(s):
        tables.append(row[1])
    cur.close()
    pivot_tables=[]
    property_tables=[]
    for table in tables:
        if table!="characters":
            if is_relational(table):
                pivot_tables.append(f'[{table}]')
            else:
                property_tables.append(table)
    return pivot_tables, property_tables


def fetch_by_id(id, con, target=None, is_property=True,):
    properties=get_tables(con)[1]
    relations=get_tables(con)[0]
    if target!=None:
        sql=f'SELECT * FROM [{target}] WHERE id="{id}"'
        d=pd.read_sql_query(sql,con)
    if is_property==True:
        for target in properties:
            sql=f'SELECT * FROM {target} WHERE id="{id}"'
            d=pd.read_sql_query(sql,con)
            if d.empty==False:
                break
    elif is_property==False:
        for target in relations:
            sql=f'SELECT * FROM {target} WHERE primary_key="{id}"'
            d=pd.read_sql_query(sql,con)
            if d.empty==False:
                break
    rec=pd.DataFrame.from_records(d)
    return rec

def find_source(id,con):
    properties=get_tables(con)[1]
    for table in properties:
        sql=f'''SELECT * FROM {table} WHERE id="{id}"'''
        ret=pd.read_sql_query(sql,con)
        if ret.empty==False:
            return table
       
def generate_abilities(ability_ids, con):
    abilities=[]
    for id in ability_ids:
        src=find_source(id,con)
        if src=="effects":
            a=effect(id,con)
            abilities.append(a)
        if src=="durations":
            a=duration(id,con)
            abilities.append(a)
        if src=="ranges":
            a=rng(id,con)
            abilities.append(a)
        if src=="class_features":
            a=class_feature(id,con)
            abilities.append(a)
        if src=="tag_features":
            a=tag_feature(id,con)
            abilities.append(a)
        if src=="backgrounds":
            a=background(id,con)
            abilities.append(a)
        if src=="classes":
            a=pcclass(id,con)
            abilities.append(a)
        if src=="skills":
            a=skill_proficiency(id,con)
            abilities.append(a)
    return abilities

class ability:
    def __init__(self,id,con):
        self.rec=fetch_by_id(id,con)
        self.name=self.rec["title"][0]
        ## self.tier=self.rec["tier"][0]
        self.id=id

class pcclass(ability):
    def __init__(self,id,con):
        super().__init__(id,con)
    def define_hd(self):
        if self.name=="Barbarian":
            self.hit_die="2d4"
        if self.name in ["Sharpshooter","Knight","Fighter"]:
            self.hit_die="d6"
        if self.name in ["Rogue","Priest"]:
            self.hit_die="d4"
        if self.name in ["Elementalist","Beguiler"]:
            self.hit_die="d3"
        if self.name=="Wizard":
            self.hit_die="d2"

    
class feature(ability):
    def __init__(self,id,con):
        super().__init__(id,con)

class skill_proficiency(ability):
    def __init__(self,id,con):
        super().__init__(id,con)

class power(ability):
    def __init__(self,id,con):
        super().__init__(id,con)
        self.pwr=self.rec["pwr"][0]
        self.tree=self.rec["tree"][0]

class effect(power):
    def __init__(self,id,con):
        super().__init__(id,con)

class duration(power):
    def __init__(self,id,con):
        super().__init__(id,con)
        self.ticks=self.rec["ticks"][0]

class rng(power):
    def __init__(self,id,con):
        super().__init__(id,con)

class background(ability):
    def __init__(self,id,con):
        super().__init__(id,con)

class tag_feature(ability):
    def __init__(self,id,con):
        super().__init__(id,con)

class class_feature(ability):
    def __init__(self,id,con):
        super().__init__(id,con)