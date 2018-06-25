# User stories

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

###### Add a new message

- Log in 
- Click "Add a new message" from navigation bar (or from "All messages" page)
- Fill in the message form (subject, the message text and categories) in the frame of validations
- Click "Add a new message" button at the bottom of the page
- Success leads to "All messages" page and fail to the form with error message

###### Read messages

- No login required
- Click "All messages" from navigation bar
- Choose a message to be read from the list, and click the subject
- Message will be displayed

###### Edit message

- User can only edit his/her own messages! (Excluding admins)
- Log in
- Do the "Read messages" operations from above
- Click "Edit" button at the bottom of the page
- Same message form will be displayed as in "Add a new message" but with prefilled fields
- Edit the message to ypour choosing and click "Save changes"
- Success leads to "All messages" page and fail to the form with error message

###### Look categories

- No login required
- Go to "Categories" in the nav bar
- Category description is displayed by clicking the category in the list

###### Create a category

- Log in as admin (same as normal Log in, must have admin rights)
- Go to "Categories" in the nav bar
- Click "Add a new category"
- Fill in category name and description (abiding to validations) and click "Add"
- Success leads to "Categories" page and fail to the form with error message

