# These are the controllers for your ajax api.
def get_user_name_from_email(email):
    """Returns a string corresponding to the user first and last names,
    given the user email."""
    u = db(db.auth_user.email == email).select().first()
    if u is None:
        return 'None'
    else:
        return ' '.join([u.first_name, u.last_name])


def index():
	pass


# def get_posts():
# 	"""This controller is used to get the posts.  Follow what we did in lecture 10, to ensure
#     that the first time, we get 4 posts max, and each time the "load more" button is pressed,
#     we load at most 4 more posts."""
# 	# Implement me!
# 	start_idx = int(request.vars.start_idx) if request.vars.start_idx is not None else 0
# 	end_idx = int(request.vars.end_idx) if request.vars.end_idx is not None else 0
# 	posts = []
# 	has_more = False
# 	rows = db().select(db.post.ALL, orderby=~db.post.id, limitby=(start_idx, end_idx + 1))
# 	for i, r in enumerate(rows):
# 		if i < end_idx - start_idx:
# 			p = dict(
# 				id=r.id,
# 				post=r.post_content,
# 				username=get_user_name_from_email(r.user_email),
# 				created_on=r.created_on,
# 				updated_on=r.updated_on,
# 			)
# 			posts.append(p)
# 		else:
# 			has_more = True
# 	logged_in = auth.user_id is not None
# 	return response.json(dict(
# 		posts=posts,
# 		has_more=has_more,
# 		logged_in=logged_in,
# 	))
#

# Note that we need the URL to be signed, as this changes the db.
@auth.requires_signature()
def add_skill():
	"""Here you get a new post and add it.  Return what you want."""
	# Implement me!
	s_id = db.skill.insert(
		id=request.vars.id,
		skill=request.vars.skill
	)
	s = db.skill(s_id)
	return response.json(dict(skill=s))

@auth.requires_signature()
def add_profile():
	"""Here you get a new post and add it.  Return what you want."""
	# Implement me!
	p_id = db.profile.insert(
		id=request.vars.id,
		available_time=request.vars.available_time,
		profile_image=request.vars.profile_image,
		contact=request.vars.contact
	)
	p = db.profile(p_id)
	return response.json(dict(profile=p))

# @auth.requires_signature()
# def del_post():
# 	db(db.post.id == request.vars.post_id).delete()
# 	response.flash = T("Post Deleted")
# 	return "ok"
#
#
# @auth.requires_signature()
# def edit_post():
# 	print(request.vars.post_content)
# 	print(request.vars.post_id_edit)
# 	db(db.post.id == request.vars.post_id_edit).update(post_content=request.vars.post_content)

# return response.json(dict(post=p))
