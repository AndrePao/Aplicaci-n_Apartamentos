import mechanize

def Login_Facebook(email,Password):
    url="https://www.facebook.com/login"
    op=mechanize.Browser()
    op.set_handle_robots(False)
    op.addheaders=[('User-Agent','Mozilla/5.0 (Windows; U; Wimdows Nt 6.0; en-US; rv:1.9.0.6)')]
    op.open(url)
    op.select_form(nr=0)
    op.form["email"]=email
    op.form["pass"]=Password
    op.submit()
    if op.geturl()!="https://www.facebook.com/login.php?login_attempt=1":
        return True
        
    else:
        return False
