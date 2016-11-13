# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.

db.define_table('profile',
                Field('id', 'integer'),
                Field('user_email', default=auth.user.email if auth.user_id else None),
                Field('available_times', 'text'),
                Field('photo', 'upload'),
                Field('contact', 'integer')
                )

db.define_table('skill',
                Field('id', 'integer'),
                Field('skill', 'text'))

# I don't want to display the user email by default in all forms.
db.info.user_email.readable = db.info.user_email.writable = False
db.info.skills.requires = IS_NOT_EMPTY()
db.info.available_times.readable = db.info.available_times.writable = False

# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
