
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
        this.abilities=
    }
    
    function add_ability(id) {
        

    }
}

import sqlite3 from 'sqlite3'
import { open } from 'sqlite'



const db = await open({
      filename: 'HUBRIS.db',
      driver: sqlite3.Database
    })

async function load_character(player) {
    let sql="select * from characters where player=?"
    const result = await db.get(sql,"El")
    return result
}

