# User stories

#### Not Logged in

###### Registering as new user

- Click "Register" from upper right corner
- Enter real name (no validation)
- Enter username (>3, <16 chars) and password (twice, at least 6 characters)
- After successful registration user is directed to log in form
- Unsuccessful redirects back to the form and tells what's wrong
- Relevant SQL: INSERT INTO account (name, username, password, urole) 
VALUES (value1, value2, value3, "USER"); 

###### Logging in
- Click "Login" from upper right corner
- Enter username and password (same validation as before)
- If login is successful user is directed to the front page
- Unsuccessful redirects back to the form and tells what's wrong
- Relevant SQL: SELECT user.id FROM account;

###### Read messages

- No login required
- Click "All messages" from navigation bar
- Choose a message to be read from the list, and click the subject
- Message will be displayed

###### Look categories

- Go to "Categories" in the nav bar
- Category description is displayed by clicking the category in the list
- Relevant SQL: SELECT category.id FROM category;

###### Evince the statistics

- Click "Statistics" in the navigation bar 
- Complex SQL queries given in [here]()

#### Logged in as normal user

###### Add a new message

- Click "Add a new message" from navigation bar (or from "All messages" page)
- Fill in the message form (subject, the message text and categories) in the frame of validations
- Click "Add a new message" button at the bottom of the page
- Success leads to "All messages" page and fail to the form with error message
- Relevant SQL: INSERT INTO message (subject, body, read, account_id, categories) 
VALUES (value1, value2, False, current_user.id, value4); 

###### Edit message

- User can only edit his/her own messages! (Excluding admins)
- Do the "Read messages" operations from above
- Click "Edit" button at the bottom of the page
- Same message form will be displayed as in "Add a new message" but with prefilled fields
- Edit the message to ypour choosing and click "Save changes"
- Success leads to "All messages" page and fail to the form with error message
- Relevant SQL: UPDATE message SET subject = value1, body = value2, categories=
value3 WHERE message.id=message_id;

###### Delete message

- User can only edit his/her own messages! (Excluding admins)
- Do the "Read messages" operations from above
- Click "Delete" button at the bottom of the page
- Message will be deleted right away and completely!
- Relevant SQL: DELETE FROM message WHERE message.id=message_id;

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
- Relevant SQL: INSERT INTO account (name, description) 
VALUES (value1, value2); 

###### Edit a category

- Do the "Look Categories" functionality
- Click "Add a new category" button on the top of the page
- The same form opens as in "Create a new category" with prefilled fields
- Edit the fields to your choosing abiding to the validations
- Click "Submit changes". Success redirects to the "Categories" view and failure 
back to the form with an error message.
- Relevant SQL: UPDATE category SET name = value1, description = value2
WHERE category.id=category_id;

###### Delete category

- Do the "Look categories" operations from above
- Click "Delete" button at the bottom of the page
- Category will be deleted right away and completely!
- Relevant SQL: DELETE FROM category WHERE category.id=category_id;