# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.


db.define_table('info',
                Field('user_email', default=auth.user.email if auth.user_id else None),
                Field('first_name', default=auth.user.first_name if auth.user_id else None, requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]),
                Field('last_name', default=auth.user.last_name if auth.user_id else None, requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]),
                Field('skills', 'text'),
                Field('available_times', 'text'),
                Field('image', default=auth.user.image if auth.user_id else None)
                )

# I don't want to display the user email by default in all forms.

db.info.user_email.readable = False
db.info.id.readable = False
db.info.user_email.writable = False
db.info.first_name.writable = False
db.info.last_name.writable = False
db.info.image.writable = False
db.info.image.readable = False
db.info.skills.requires = IS_NOT_EMPTY()


# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
