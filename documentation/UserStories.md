# User stories

#### Not Logged in

###### Registering as new user

- Click "Register" from upper right corner
- Enter real name (no validation)
- Enter username (>3, <16 chars) and password (twice, at least 6 characters)
- After successful registration user is directed to log in form
- Unsuccessful redirects back to the form and tells what's wrong

###### Logging in
- Click "Login" from upper right corner
- Enter username and password (same validation as before)
- If login is successful user is directed to the front page
- Unsuccessful redirects back to the form and tells what's wrong

###### Read messages

- No login required
- Click "All messages" from navigation bar
- Choose a message to be read from the list, and click the subject
- Message will be displayed

###### Look categories

- Go to "Categories" in the nav bar
- Category description is displayed by clicking the category in the list

#### Logged in as normal user

###### Add a new message

- Click "Add a new message" from navigation bar (or from "All messages" page)
- Fill in the message form (subject, the message text and categories) in the frame of validations
- Click "Add a new message" button at the bottom of the page
- Success leads to "All messages" page and fail to the form with error message

###### Edit message

- User can only edit his/her own messages! (Excluding admins)
- Do the "Read messages" operations from above
- Click "Edit" button at the bottom of the page
- Same message form will be displayed as in "Add a new message" but with prefilled fields
- Edit the message to ypour choosing and click "Save changes"
- Success leads to "All messages" page and fail to the form with error message

###### Delete message

- User can only edit his/her own messages! (Excluding admins)
- Do the "Read messages" operations from above
- Click "Delete" button at the bottom of the page
- Message will be delted right away and completely!

#### Logged in as admin

NOTE: Admin privileges are manually given. There is no way 
to get them "inside" the app.

###### Logging in

- Same as any user. Admins just have more privileges.

###### Create a category

- Go to "Categories" in the nav bar
- Click "Add a new category"
- Fill in category name and description (abiding to validations) and click "Add"
- Success leads to "Categories" page and fail to the form with error message

###### Edit a category

- Do the "Look Categories" functionality
- Click "Add a new category" button on the top of the page
- The same form opens as in "Create a new category" with prefilled fields
- Edit the fields to your choosing abiding to the validations
- Click "Submit changes". Success redirects to the "Categories" view and failure 
back to the form with an error message.
