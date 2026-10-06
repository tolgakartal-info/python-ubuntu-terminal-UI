from DBConnection import DBConnection

db = DBConnection(Server="127.0.0.1",Database="terminal",Uid="phpmyadmin", Pwd="880739")

rows = db.Select("info",["name","ip_address","netmask"])
print(rows)

rows = db.Select("terminal_logs",["*"],{})
print(rows)