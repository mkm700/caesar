#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
from caesar import encrypt


# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <style>
    body {
        font-family: arial, sans-serif;
    }
    h1 {
        font-size: 1.5em;
        text-align: center;
    }
    form {
        background-color:#eee;
        padding: 30px;
        border: 1px #333 solid;
        margin: 30px auto;
        width:400px;
    }
    .error {
        color: red;
    }
    </style>
    <title>ROT13</title>
</head>
<body>
"""

#page header
edit_header = "<h1>LaunchCode: Formation Assignment</h1>"

# a form for adding text
form = """
<form method="post">
    Rotate by: <input type="text" name="rotate">
    <br /><br />
    <textarea name="decode-text" cols="60" rows="5">%(encrypted)s</textarea>
    <br /><br />
    <input type="submit" value="Decode It"/>
    <div class="error">%(error)s</div>
</form>
"""


# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""


class MainHandler(webapp2.RequestHandler):
    def write_form(self, error="",encrypted=""):
        # combine all the pieces to build the content of our response
        main_content = edit_header + form
        response = page_header + main_content + page_footer
        self.response.write(response % {"error": error, "encrypted": encrypted})

    def get(self):
        self.write_form()

    def post(self):
        rotate = int(self.request.get("rotate"))
        myText = self.request.get("decode-text")
        encryptedText = cgi.escape(encrypt(myText, rotate))

        #if no value was entered, display an error message
        #else write the form with encrypted text
        if myText == "":
            self.write_form("Please enter a value.")
        else:
            self.write_form("",encryptedText)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
