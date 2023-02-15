import sqlite3
import pandas as pd

con=sqlite3.connect("HUBRIS.db")



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
                pivot_tables.append(table)
            else:
                property_tables.append(table)
    return pivot_tables, property_tables

relations=get_tables()[0]
properties=get_tables()[1]



def fetch_property(id):
    cur=con.cursor()
    for table in properties:
        sql=f'SELECT * FROM {table} WHERE id="{id}"'
        d=pd.read_sql_query(sql,con)
        if d.empty==False:
            break
    rec=pd.DataFrame.from_records(d)
    return rec
       
def fetch_relations(id)