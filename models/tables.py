# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.


def get_user_name_from_email(email):
    """Returns a string corresponding to the user first and last names,
    given the user email."""
    u = db(db.auth_user.email == email).select().first()
    if u is None:
        return 'None'
    else:
        return ' '.join([u.first_name, u.last_name])


db.define_table('info',
                Field('user_email', default=auth.user.email if auth.user_id else None),
                Field('skills', 'text'),
                Field('available_times', 'text')
                )



# I don't want to display the user email by default in all forms.
db.info.user_email.readable = db.info.user_email.writable = False
db.info.skills.requires = IS_NOT_EMPTY()
db.info.available_times.readable = db.info.available_times.writable = False


# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
