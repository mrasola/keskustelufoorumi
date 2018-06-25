# Creating tables

#### Account:

````
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	urole VARCHAR(80), 
	PRIMARY KEY (id)
);
````

#### Category:
````
CREATE TABLE category (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	description VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
````

#### Message:
````
CREATE TABLE message (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	subject VARCHAR(144) NOT NULL, 
	body VARCHAR(144) NOT NULL, 
	read BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (read IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
````

#### Relation between message and category:
````
CREATE TABLE relation (
	id INTEGER NOT NULL, 
	category_id INTEGER, 
	message_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(category_id) REFERENCES category (id) ON DELETE cascade, 
	FOREIGN KEY(message_id) REFERENCES message (id) ON DELETE cascade
);
````