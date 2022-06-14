# Todo App with TinyDB

Todo Application that performs CRUD operations to TinyDB

## What is TinyDB?
TinyDB is a document-oriented database written in pure Python with no external dependencies. It is designed to be easy and fun to use by providing a simple and clean API.

If you need a simple database with a clean API that just works without lots of configuration, TinyDB might be the right choice for you.

|Group| Code  | Description  |
|---|---|---|
|  **Inserting data** |  `db.insert(...)` |Insert a document|
|  |  `db.insert_multiple(...)` |Insert multiple documents|
|  **Getting data** |  `db.all()` |Get all documents|
| |`iter(db)`|	Iter over all documents|
| |`db.search(query)`|	Get a list of documents matching the query|
|**Updating**|`db.update(fields, query)`|	Update all documents matching the query to contain fields|
|**Removing**|`db.remove(query)`	|Remove all documents matching the query|
| |`db.truncate()`|	Remove all documents|
|**Querying**|`Query()`	|Create a new query object|
| |`Query().field == 2`	|Match any document that has a key field with value == 2 (also possible: !=, >, >=, <, <=)|