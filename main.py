import webapp2
import re




class Signup(webapp2.RequestHandler):

    def get(self):
        error = self.request.get("error")
        username = self.request.get("username")

        form = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Sign Up</title>
            </head>
            <body>
                <form method="post">
                    <h2>Signup</h2>
                    <label>Username:<input type="text" name="username" value="{}"></label>
                    <br>
                    <label>Password:<input type="password" name="password"></label>
                    <br>
                    <label>Verify:<input type="password" name="verify"></label>
                    <br>
                    <label>Email:<input type="text" name="email"></label>
                    <br>
                    <br>
                    <input type="submit" value="Sign Up">
                </form><br><br>
                <div style="color:red;">{}</div>
            </body>
        </html>
        """.format(username,error)

        self.response.write(form)

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")


        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        if USER_RE.match(username) == None:
            error = "Invalid Username"
            self.redirect("/?error={}&username={}".format(error,username))

        PASS_RE = re.compile(r"^.{3,20}$")
        if PASS_RE.match(password) == None:
            self.redirect("/?error=" + "Invalid Password")
        elif not password == verify:
            self.redirect("/?error=" + "Invalid Password")

        EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
        if email:
            if EMAIL_RE.match(email) == None:
                self.redirect("/?error=" + "Invalid Email")
            else:
                self.response.write("Welcome, " + username + "!")
        else:
            self.response.write("Welcome, " + username + "!")



app = webapp2.WSGIApplication([
    ('/', Signup)
], debug=True)
