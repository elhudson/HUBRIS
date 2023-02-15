from nopy import NotionClient
import pandas as pd
import sqlite3 as sql
from key_generator.key_generator import generate

## read notion databases into python 

client=NotionClient("secret_TrlevNz6r9aY0bTxYzu2ytLwSbkIkibkbTDUfpTCiHI")

def read_effects():
    effect_db=client.retrieve_db("3b66c0a5ff9a42aca5f47a262c62b27a")
    pages=list(effect_db.get_pages())
    effects={}

    for page in pages:
        id=page.id
        title=page.title
        tier=page.properties["Tier"].option.name
        if len(page.properties["Description"].rich_text)==0:
            description=None;
        else:
            description=page.properties["Description"].rich_text[0].plain_text
        tree=page.properties["Tree"].option.name
        xp=page.properties["XP"].number
        pwr=page.properties["Power"].number
        tags=page.properties["Tags"].relations
        d={}
        d["title"]=title
        d["tier"]=tier
        d["description"]=description
        d["tree"]=tree
        d["xp"]=xp
        d["pwr"]=pwr
        d["tags"]=tags
        effects[id]=d
    return effects
            
def read_durations():
    duration_db = client.retrieve_db("1da81c78e7934c4ca2144477e5efcf8b")
    pages = list(duration_db.get_pages())
    durations = {}

    for page in pages:
        id = page.id
        title = page.title
        tier = page.properties["Tier"].option.name
        if len(page.properties["Description"].rich_text) == 0:
            description = None
        else:
            description = page.properties["Description"].rich_text[0].plain_text
        xp = page.properties["XP"].number
        pwr = page.properties["Power"].number
        ticks=page.properties["Ticks"].number
        d={}
        d["title"]=title
        d["tier"]=tier
        d["description"]=description
        d["xp"]=xp
        d["pwr"]=pwr
        d["ticks"]=ticks
        durations[id] = d
    return durations

def read_ranges():
    range_db = client.retrieve_db("1da81c78e7934c4ca2144477e5efcf8b")
    pages = list(range_db.get_pages())
    ranges = {}

    for page in pages:
        id = page.id
        title = page.title
        tier = page.properties["Tier"].option.name
        if len(page.properties["Description"].rich_text) == 0:
            description = None
        else:
            description = page.properties["Description"].rich_text[0].plain_text
        xp = page.properties["XP"].number
        pwr = page.properties["Power"].number
        d={}
        d["title"]=title
        d["tier"]=tier
        d["description"]=description
        d["xp"]=xp
        d["pwr"]=pwr
        ranges[id] =d
    return ranges

def read_class_features():
    class_feature_db=client.retrieve_db("4eaa6b73c3c84189943de75ed709d7eb")
    pages=list(class_feature_db.get_pages())
    class_features={}

    for page in pages:
        id=page.id
        title=page.title
        if page.properties["Tier"].option==None:
            tier=None
        else:
            tier=page.properties["Tier"].option.name
        if len(page.properties["Description"].rich_text)==0:
            description=None;
        else:
            description=page.properties["Description"].rich_text[0].plain_text
        xp=page.properties["XP"].number
        feature_class=page.properties["Class"].relations
        d={}
        d["title"]=title
        d["tier"]=tier
        d["description"]=description
        d["xp"]=xp
        d["class"]=feature_class
        class_features[id]=d
    return class_features
    
def read_tag_features():
    tag_feature_db=client.retrieve_db("04a91868699f4afc8c0280ff4ac1e3ad")
    pages=list(tag_feature_db.get_pages())
    tag_features={}

    for page in pages:
        id=page.id
        title=page.title
        if page.properties["Tier"].option==None:
            tier=None
        else:
            tier=page.properties["Tier"].option.name
        if len(page.properties["Description"].rich_text)==0:
            description=None;
        else:
            description=page.properties["Description"].rich_text[0].plain_text
        xp=page.properties["XP"].number
        tag=page.properties["Tag"].relations
        d={}
        d["title"]=title
        d["tier"]=tier
        d["description"]=description
        d["xp"]=xp
        d["tag"]=tag
        tag_features[id]=d
    return tag_features

def read_classes():
    class_db=client.retrieve_db("3df41ba0adef41da89da5873f4b7f7b0")
    pages=list(class_db.get_pages())
    classes={}

    for page in pages:
        id=page.id
        title=page.title
        xp=4
        if len(page.properties["Description"].rich_text)==0:
            description=None;
        else:
            description=page.properties["Description"].rich_text[0].plain_text
        tags=page.properties["Class Tags"].relations
        skills=page.properties["Class Skills"].relations
        d={}
        d["title"]=title
        d["description"]=description
        d["xp"]=xp
        d["tags"]=tags
        d["skills"]=skills
        classes[id]=d
    return classes

def read_backgrounds():
    background_db=client.retrieve_db("367c52ae497f430b98ccc7716c8cae3f")
    pages=list(background_db.get_pages())
    backgrounds={}

    for page in pages:
        id=page.id
        title=page.title
        feature=page.properties["Feature"].rich_text[0].plain_text+" "+page.properties["Feature"].rich_text[1].plain_text
        skill=page.properties["Proficiency"].relations
        attribute=page.properties["Attribute"].relations
        d={}
        d["title"]=title
        d["feature"]=feature
        d["attribute"]=attribute
        d["skill"]=skill
        backgrounds[id]=d
    return backgrounds

def read_skills():
    skill_db=client.retrieve_db("194cfc4a2a7e49c7a3bda3f7d65fd870")
    pages=list(skill_db.get_pages())
    skills={}

    for page in pages:
        id=page.id
        title=page.title
        attribute=page.properties["Attribute"].relations
        classes=page.properties["Classes"].relations
        backgrounds=page.properties["Backgrounds"].relations
        d={}
        d["title"]=title
        d["classes"]=classes
        d["attribute"]=attribute
        d["backgrounds"]=backgrounds
        skills[id]=d
    return skills

def read_tags():
    tag_db=client.retrieve_db("c932f3aa6db54aa2a4efad6fd38a2c63")
    pages=list(tag_db.get_pages())
    tags={}
    for page in pages:
        id=page.id
        title=page.title
        classes=page.properties["Classes"].relations
        effects=page.properties["Effects"].relations
        d={}
        d["title"]=title
        d["classes"]=classes
        d["effects"]=effects
        tags[id]=d
    return tags

def read_attributes():
    attribute_db=client.retrieve_db("0c18e1f7462e45a0ba2a025e9d25184a")    
    pages=list(attribute_db.get_pages())
    attributes={}
    for page in pages:
        id=page.id
        title=page.title
        backgrounds=page.properties["Backgrounds"].relations
        skills=page.properties["Skills"].relations
        d={}
        d["title"]=title
        d["skills"]=skills
        d["backgrounds"]=backgrounds
        attributes[id]=d
    return attributes

def read_databases(): 
    databases={}
    databases["effects"]=read_effects()
    databases["durations"]=read_durations()
    databases["ranges"]=read_ranges()
    databases["class_features"]=read_class_features()
    databases["tag_features"]=read_tag_features()
    databases["classes"]=read_classes()
    databases["backgrounds"]=read_backgrounds()
    databases["skills"]=read_skills()
    databases["tags"]=read_tags()
    databases["attributes"]=read_attributes()
    return databases

## generate pivot tables from notion database

def find_relations(database):
    properties=[]
    instance=database[list(database.keys())[0]]
    for property in instance.keys():
        if type(instance[property])==list:
            properties.append(property)
    return properties

def pivot_table(p1, p2, database,nth_relation):
    p1_ids=[]
    p2_ids=[]
    primary_keys=[]
    property_n=find_relations(database)[nth_relation]
    for property_1_id in database.keys():
        property_n_ids_list=database[property_1_id][property_n]
        for id in property_n_ids_list:
            p1_ids.append(id)
            p2_ids.append(property_1_id)
    for i in range(len(p1_ids)):
        key=generate()
        primary_keys.append(key.get_key())
    d={}
    d["primary_key"]=primary_keys
    d[p1+"_key"]=p1_ids
    d[p2+"_key"]=p2_ids
    pivot_table=pd.DataFrame(data=d)
    return pivot_table

def generate_relations(databases):
    relations={}
    for db_name in databases.keys():
        rels=find_relations(databases[db_name])
        if len(rels)!=0:
            relations[db_name]=rels
    return relations

def generate_pivot_tables(dbs):
    tables={}
    relations=generate_relations(dbs)
    for db_name in relations.keys():
        db=dbs[db_name]
        rels=relations[db_name]
        for i in range(len(rels)):
            relation=rels[i]
            table=pivot_table(db_name,relation,db,i)
            table_name=str(db_name +" to "+relation)
            tables[table_name]=table
    return tables

## convert each dict to a dataframe & drop properties handled by the pivot tables

def convert(dbs):
    processed={}
    for db_name in dbs.keys():
        db=dbs[db_name]
        p=drop_process(db)
        processed[db_name]=p
    del dbs
    return processed

def drop_process(db):
    frame=to_df(db)
    rels=find_relations(db)
    cols=list(frame.columns)[:]
    for col in cols:
        if col in rels:
            frame=frame.drop(col,axis=1)
    return frame


def to_df(dict):
    c=[]
    for entry_id in dict.keys():
        entry=dict[entry_id]
        entry["id"]=entry_id
        c.append(entry)
    t=pd.DataFrame.from_records(c)
    return t
    
## write all tables to SQL database HUBRIS.db

def to_db(content_tables):
    link=sql.connect("HUBRIS.db")
    for table_name in content_tables.keys():
        t=content_tables[table_name]
        t.to_sql(table_name, link, if_exists='replace')
    link.close()

