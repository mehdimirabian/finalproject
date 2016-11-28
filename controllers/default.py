# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

def get_user_name_from_email(email):
    """Returns a string corresponding to the user first and last names,
    given the user email."""
    u = db(db.auth_user.email == email).select().first()
    if u is None:
        return 'None'
    else:
        return ' '.join([u.first_name, u.last_name])

def getEditDisplay(row):
    edit_button =A('Edit', _class='button btn btn-default', _href=URL("default", "edit", args=[row.id]))
    return edit_button

@auth.requires_login()
def index():
    q = db.info
    export_classes = dict(csv=False, json=False, html=False,
                          tsv=False, xml=False, csv_with_hidden_cols=False,
                          tsv_with_hidden_cols=False)
    links = [lambda row: getEditDisplay(row)]
    selectable = lambda ids: delete(ids)
    form = SQLFORM.grid(
        q,
        editable=False,
        links=links,
        create=True,
        selectable=selectable,
        user_signature=False,
        deletable=False,
        fields=[db.info.first_name, db.info.last_name, db.info.user_email, db.info.skills, db.info.available_times,
                ],
        details=True,
        exportclasses=export_classes
    )
    # my_extra_element = TR(LABEL("Don't view"),
    #                       INPUT(_name='Unviewable', value=False, _type='checkbox'))
    # form[1].insert(0, my_extra_element)
    # row = db().select(db.info.ALL)
    # if 'edit' in request.args:
    #     if auth.user.email == row[0].user_email:
    #         response.flash = T("emails are the same")
    return dict(form=form)

@auth.requires_login()
def delete(ids):
    row = db().select(db.info.ALL)
    if row[0].user_email == auth.user.email:
        to_delete = db(db.info.id.belongs(ids))
        to_delete.delete()



@auth.requires_login()
def edit():
    row = db().select(db.info.ALL)
    pizza = 'arsenal'
    print request.vars.skills
    return dict(row = row)

def submit():
    print request.vars.skills
    t_id = db(db.info.user_email == auth.user.email).update(
        skills = request.vars.skills,
        available_times = request.vars.available_times
    )
    t = db.info(request.vars.info_id)
    return response.json(dict(info=t))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    if request.args(0) == 'profile':
        db.auth_user.first_name.writable = db.auth_user.last_name.writable = db.auth_user.email.writable = False
        for field in auth.settings.extra_fields['auth_user']:
            field.readable = True
            field.writable = False
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


