
class character {
    constructor(name, str, dex, con, int, wis, cha, xp_earned, xp_spent) {
        this.name = name;
        this.str = str;
        this.dex = dex;
        this.con = con;
        this.int = int;
        this.wis = wis;
        this.cha = cha;
        this.xp_earned = xp_earned;
        this.xp_spent = xp_spent;
    }
}

import sqlite3 from 'sqlite3'
import { open } from 'sqlite'
const db = await open({
      filename: 'HUBRIS.db',
      driver: sqlite3.Database
    })

let sql="select * from characters where player='El';"

const result = await db.get(sql)
const char=new character(result.name,result.str,result.dex,result.con,result.int,result.wis,result.cha,result.xp_earned,result.xp_spent)
console.log(char)