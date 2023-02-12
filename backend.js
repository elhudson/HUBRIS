const sqlite3 = require('sqlite3').verbose();
let db=new sqlite3.Database("HUBRIS.db")
let player="El"
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

let warehouse=['placeholder'];

let sql="select * from characters where player='El';"
db.all(sql,
    function(err,rows) {
        result=rows[0]
        charname=result.name;
        str=result.str;
        dex=result.dex;
        con=result.con;
        int=result.int;
        wis=result.wis;
        cha=result.cha;
        xp_earned=result.xp_earned;
        xp_spent=result.xp_spent;
        c=new character(charname,str,dex,con,int,wis,cha,xp_earned,xp_spent);
        return c;
}
);

console.log(c)