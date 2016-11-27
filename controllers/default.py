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

@auth.requires_login()
def index():
    q = db.info  # This queries for all products.
    export_classes = dict(csv=False, json=False, html=False,
                          tsv=False, xml=False, csv_with_hidden_cols=False,
                          tsv_with_hidden_cols=False)

    form = SQLFORM.grid(
        q,
        editable=True,
        create=True,
        user_signature=True,
        deletable=True,
        fields=[db.info.user_email, db.info.skills, db.info.available_times, db.info.image
                ],
        details=True,
        upload=URL('download'),
        exportclasses=export_classes
    )
    row = db().select(db.info.ALL)
    if 'edit' in request.args:
        if auth.user.email == row[0].user_email:
            response.flash = T("emails are the same")

    return dict(form=form)


@auth.requires_login()
def edit():
    """
    This is the page to create / edit / delete a post.
    """



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


