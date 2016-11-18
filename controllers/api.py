import random

def index():
    pass

# Mocks implementation.
def get_info():
    start_idx = int(request.vars.start_idx) if request.vars.start_idx is not None else 0
    end_idx = int(request.vars.end_idx) if request.vars.end_idx is not None else 0
    # We just generate a lot of of data.
    info = []
    has_more = False
    rows = db().select(db.info.ALL, limitby=(start_idx, end_idx + 1))
    for i, r in enumerate(rows):
        if i < end_idx - start_idx:
            t = dict(
                id = r.id,
                skills = r.skills,
                available_times = r.available_times,
            )
            info.append(t)
        else:
            has_more = True
    logged_in = auth.user_id is not None
    return response.json(dict(
        info=info,
        logged_in=logged_in,
        has_more=has_more,
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


