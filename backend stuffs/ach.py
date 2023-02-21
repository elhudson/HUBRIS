import sqlite3
import pandas as pd

path="C:\\Users\\elhud\\Projects\\HUBRIS\\HUBRIS.db"
con=sqlite3.connect(path)

class character:
    def __init__(self,player):
        sql=f'SELECT * FROM characters WHERE player="{player}"'
        df=pd.read_sql(sql,con)
        self.str=df["str"][0]
        self.dex=df["dex"][0]
        self.con=df["con"][0]
        self.int=df["int"][0]
        self.wis=df["wis"][0]
        self.cha=df["cha"][0]
        self.ability_ids=df["abilities"][0]


def is_relational(function_name):
    l=function_name.split()
    if len(l)==1:
        return False
    else:
        return True

def get_tables():
    s=f'SELECT * FROM sqlite_schema WHERE type="table"'
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

relations=get_tables()[0]
properties=get_tables()[1]


def fetch_by_id(id, target=None, is_property=True):
    if target!=None:
        sql=f'SELECT * FROM [{target}] WHERE id="{id}"'
        d=pd.read_sql_query(sql,con)
    if is_property==True:
        for table in properties:
            sql=f'SELECT * FROM {table} WHERE id="{id}"'
            d=pd.read_sql_query(sql,con)
            if d.empty==False:
                break
    elif is_property==False:
        for table in relations:
            sql=f'SELECT * FROM {table} WHERE primary_key="{id}"'
            d=pd.read_sql_query(sql,con)
            if d.empty==False:
                break
    rec=pd.DataFrame.from_records(d)
    return rec
       
class ability:
    def __init__(self,id):
        self.rec=fetch_by_id(id)
        self.name=self.rec["title"][0]
        self.xp=self.rec["xp"][0]
        self.desc=self.rec["description"][0]
        ## self.tier=self.rec["tier"][0]
        self.id=id

class feature(ability):
    def __init__(self,id):
        super().__init__(id)
        
class power(ability):
    def __init__(self,id):
        super().__init__(id)
        self.pwr=self.rec["pwr"][0]
        self.tree=self.rec["tree"][0]

class effect(power):
    def __init__(self,id):
        super().__init__(id)

class duration(power):
    def __init__(self,id):
        super().__init__(id)
        self.ticks=self.rec["ticks"][0]

class rng(power):
    def __init__(self,id):
        super().__init__(id)

class background(ability):
    def __init__(self,id):
        super().__init__(id)
        self.ability=fetch_by_id(self.id)["title"][0]

class tag_feature(ability):
    def __init__(self,id):
        super().__init__(id)

class class_feature(ability):
    def __init__(self,id):
        super().__init__(id)