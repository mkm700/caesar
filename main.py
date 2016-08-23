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
    <title>ROT13</title>
</head>
<body>
"""

#page header
edit_header = "<h1>Enter some text to ROT13:</h1>"

# a form for adding text
form = """
<form method="post">
    <textarea name="decode-text" cols="40" rows="5">%(encrypted)s</textarea>
    <br /><br />
    <input type="submit" value="Decode It"/>
    <div style="color:red;">%(error)s</div>
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
        myText = self.request.get("decode-text")
        encryptedText = cgi.escape(encrypt(myText, 13))

        #if no value was entered, display an error message
        #else write the form with encrypted text
        if myText == "":
            self.write_form("Please enter a value.")
        else:
            self.write_form("",encryptedText)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
