# E-Portfolio MongoDB

![](Logo/Logo_RGB_Forest-Green.png)

## What is MongoDB <a name="what-is-mongodb"></a>

It is a cross-platform open-source document-oriented database program. A record in MongoDB is a document, which is a
data structure composed of field and value pairs. MongoDB documents are similar to JSON objects. The values of fields
may include other documents, arrays, and arrays of documents.

![](Logo/crud-annotated-document.bakedsvg.svg)

To install MongoDB, visit the [MongoDB manual](https://www.mongodb.com/docs/manual/installation/).

## Key features

### High Performance

MongoDB provides high performance data persistence. In particular,

- Support for embedded data models reduces I/O activity on database system. Indexes support faster queries and can
  include keys from embedded documents and arrays.
- Query API The MongoDB Query API supports read and write operations (CRUD) as well as:

- Data Aggregation
- Text Search and Geospatial Queries.

See also:

- [SQL to MongoDB Mapping Chart](https://www.mongodb.com/docs/manual/reference/sql-comparison/)
- [SQL to Aggregation Mapping Chart](https://www.mongodb.com/docs/manual/reference/sql-aggregation-comparison/)

### High Availability

MongoDB's replication facility, called [replica set](https://www.mongodb.com/docs/manual/replication/), provides:

- automatic failover
- data redundancy.

A replica set is a group of MongoDB servers that maintain the same data set, providing redundancy and increasing data
availability.

### Horizontal Scalability

MongoDB provides horizontal scalability as part of its core functionality:

- [Sharding](https://www.mongodb.com/docs/manual/sharding/#std-label-sharding-introduction) distributes data across a
  cluster of machines.

### Support for Multiple Storage Engines

MongoDB supports multiple storage engines:

- [WiredTiger Storage Engine](https://www.mongodb.com/docs/manual/core/wiredtiger/) (including support
  for [Encryption at Rest](https://www.mongodb.com/docs/manual/core/security-encryption-at-rest/))
- [In-Memory](https://www.mongodb.com/docs/manual/core/inmemory/) Storage Engine.

In addition, MongoDB provides pluggable storage engine API that allows third parties to develop storage engines for
MongoDB.

## CRUD <a name="crud"></a>

### Insert Methods

    db.collection.insertOne()

Inserts a single document into the collection.

    db.collection.insertMany()

Inserts multiple documents into the collection.

### Query Methods

The find() method returns a cursor to the documents that match the query. As well as the find() method, the findOne()
method returns a single document that matches the query.

#### Select all documents

    db.collection.find()

It is equivalent to the following SQL query:

    SELECT * FROM collection

#### Equality Condition

The find method takes a query filter parameter.

    db.collection.find({"field": "value"})

It is equivalent to the following SQL query:

    SELECT * FROM collection WHERE field = value

#### AND

    db.collection.find({"field1": "value1", "field2": "value2"})

It is equivalent to the following SQL query:

    SELECT * FROM collection WHERE field1 = value1 AND field2 = value2

#### OR

    db.collection.find({"$or": [{"field1": "value1"}, {"field2": value2}]})

It is equivalent to the following SQL query:

    SELECT * FROM collection WHERE field1 = value1 OR field2 = value2

#### NOT

    db.collection.find({"$not": {"field1": "value1"}})

It is equivalent to the following SQL query:

    SELECT * FROM collection WHERE field1 != value1

#### Range

$gt: greater than $gte: greater than or equal to $lt: less than $lte: less than or equal to

    db.collection.find({"field": {"$gt": value, "$lt": value}})

It is equivalent to the following SQL query:

    SELECT * FROM collection WHERE field > value AND field < value

#### $regex

MongoDB supports regular expressions $regex queries to perform string pattern matches.

    db.collection.find({"field": {"$regex": "value"}})

It is equivalent to the following SQL query:

    SELECT * FROM collection WHERE field REGEXP value

#### $exists

MongoDB supports $exists queries to perform existence checks.

    db.collection.find({"field": {"$exists": true}})

It is equivalent to the following SQL query:

    SELECT * FROM collection WHERE field IS NOT NULL

#### As Example

    db.inventory.find({"status": "A", "$or": [{"qty": {"$lt": 30}}, {"item": {"$regex": "^p"}}]})

It is equivalent to the following SQL query:

    SELECT * FROM inventory WHERE status = "A" AND ( qty < 30 OR item LIKE "p%")

#### Query Arrays

The following example queries for all documents where the field tags value is an array with exactly two elements, "red"
and "blank", in the specified order:

    db.inventory.find({"tags": ["red", "blank"]})

If, instead, you wish to find an array that contains both the elements "red" and "blank", without regard to order or
other elements in the array, use the $all operator:

    db.inventory.find({"tags": {"$all": ["red", "blank"]}})

The following example queries for all documents where tags is an array that contains the string "red" as one of its
elements:

    db.inventory.find({"tags": "red"})

For example, the following operation queries for all documents where the array dim_cm contains at least one element
whose value is greater than 25.

    db.inventory.find({"dim_cm": {"$gt": 25}})

When querying using dot notation, the field and nested field must be inside quotation marks. As Example: this query
finds all documents where the second element of the dim_cm array is greater than 25:

    db.inventory.find({"dim_cm.1": {"$gt": 25}})

### Update Methods

The following example uses the update_one()
method on the inventory collection to update the first document where item equals "paper":

    db.inventory.update_one(
        {"item": "paper"}, 
        {"$set": {"size.uom": "cm", "status": "P"}, "$currentDate": {"lastModified": True}},
    )

update_many() is similar to update_one, except that it updates all documents that match the query.

    db.inventory.update_many(
        {"item": "paper"}, 
        {"$set": {"size.uom": "cm", "status": "P"}, "$currentDate": {"lastModified": True}},
    )

replace_one() replaces a single document with a new document.

    db.inventory.replace_one(
        {"item": "paper"},
        {
            "item": "paper",
            "instock": [{"warehouse": "A", "qty": 60}, {"warehouse": "B", "qty": 40}],
        },
    )

#### Behavior

- Atomicity All write operations in MongoDB are atomic on the level of a single document. For more information on
  MongoDB and atomicity,
  see [Atomicity and Transactions](https://www.mongodb.com/docs/manual/core/write-operations-atomicity/).

- _id Field Once set, you cannot update the value of the _id field nor can you replace an existing document with a
  replacement document that has a different _id field value.

- Field Order For write operations, MongoDB preserves the order of the document fields except for the following cases:

- The _id field is always the first field in the document. Updates that include renaming of field names may result in
  the reordering of fields in the document.

### Delete Methods

#### Delete All Documents

To delete all documents from a collection, pass an empty filter document {} to the delete_many() method. The following
example deletes all documents from the collection:

    db.collection.delete_many({})

#### Delete One Document

The following example deletes the first document where filed is "value":

    db.collection.delete_one({"filed": "value"})

#### Delete Many Documents

The following example deletes all documents where filed is "value":

    db.collection.delete_many({"filed": "value"})

## Validation <a name="validation"></a>

### Data Modeling

Unlike SQL databases, where you must determine and declare a table's schema before inserting data, MongoDB's
collections, by default, do not require their documents to have the same schema. That is:

The documents in a single collection do not need to have the same set of fields and the data type for a field can differ
across documents within a collection. To change the structure of the documents in a collection, such as add new fields,
remove existing fields, or change the field values to a new type, update the documents to the new structure. This
flexibility facilitates the mapping of documents to an entity or an object. Each document can match the data fields of
the represented entity, even if the document has substantial variation from other documents in the collection.

In practice, however, the documents in a collection share a similar structure, and you can enforce document validation
rules for a collection during update and insert operations. See Schema Validation for details.

To read more about MongoDB's Data Modeling,
see [Data Modeling](https://www.mongodb.com/docs/manual/core/data-modeling-introduction/).

### Schema Validation

Validation rules are on a per-collection basis.

To specify validation rules when creating a new collection, use db.createCollection() with the validator option.

To add document validation to an existing collection, use collMod command with the validator option.

MongoDB also provides the following related options:

- `validationLevel` option, which determines how strictly MongoDB applies validation rules to existing documents during
  an update.
- `validationAction` option, which determines whether MongoDB should `error` and reject documents that violate the
  validation rules or `warn` about the violations in the log but allow invalid documents.

To read more about validation options, see
the [Validation Options](https://www.mongodb.com/docs/manual/core/schema-validation/) section of the MongoDB
documentation.

## Sources

- [MongoDB Website](https://www.mongodb.com/)
- [MongoDB manual](https://www.mongodb.com/docs/manual/introduction/)