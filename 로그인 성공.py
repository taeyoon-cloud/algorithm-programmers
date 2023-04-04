def solution(id_pw, db):
    db_dict = dict(db)
    
    if id_pw[0] in db_dict.keys():
        if db_dict[id_pw[0]] == id_pw[1]:
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail"        