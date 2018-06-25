#### More complex SQL aggregate queries:

````
"SELECT Account.id, Account.username, COUNT(Message.id) FROM Account"
" LEFT JOIN Message ON Message.account_id = Account.id"
" GROUP BY Account.id ORDER BY COUNT(Message.id) DESC"
````

````
"SELECT Category.id, Category.name, COUNT(message_id) FROM Relation"
" INNER JOIN Category ON Category.id = Relation.category_id"
" GROUP BY Category.id ORDER BY COUNT(message_id) DESC"
````