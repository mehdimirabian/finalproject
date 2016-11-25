import random

def index():
    pass

# Mocks implementation.
def get_info():
    rows = db().select(db.info.ALL)
    for r in rows:
        if auth.user.email == r['user_email']:
            info=dict(
            user_email=r.user_email,
            skills=r.skills,
            available_times=r.available_times
                )
    print(info)
    return response.json(
        dict(info=info,
             ))




def does_info_exist():
    row = db().select(db.info.user_email)
    for r in row:
        if auth.user.email == r['user_email']:
            return True
        else:
            continue

    return False

@auth.requires_signature()
def add_info():
    t_id = db.info.insert(
        skills = request.vars.skills,
        available_times = request.vars.available_times
    )
    t = db.info(t_id)
    return response.json(dict(info=t))


@auth.requires_signature()
def edit_info():
    t_id = db(db.info.user_email == auth.user.email).update(
        skills = request.vars.skills,
        available_times = request.vars.available_times
    )
    t = db.info(request.vars.info_id)
    return response.json(dict(info=t))


