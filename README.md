# finalproject 
 
 1.delete the file /finalproject/routes.example.py
 2.go to web2py/example/routes.parametric.py and move that to your web2py folder
 3.rename routes.parametric.py to routes.py
 4. modify the routes.py as following:


 routers = dict(

    # base router
    BASE=dict(
        default_application='init',   #change this from welcome to init and add ALL for applications
              applications='ALL'
              

    ),
)


PS: I will modify this more to replace http://127.0.0.1:8000 with just our website name later thats easy, and also add either the cutome username or id number or however you guys want too later but for now once you goto the web page instead of showing 
http://127.0.0.1:8000/finalproject/default/index  if you are not logged in it will just show:
http://127.0.0.1:8000/finalproject and prompt you with a static home page 
just to welcome you which i just thought it looks nice and once you are logged in you direct to your profile with a route of:
http://127.0.0.1:8000/finalproject/profile_info + showing your first name and last name if you try to go to /profile_info while you are not logged in
you will redirect to log in page 

 
