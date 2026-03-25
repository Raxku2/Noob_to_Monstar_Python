from bson import ObjectId


def convert_objectid_in_doc(doc: dict) -> dict:
    """
    Converts all bson.ObjectId values in a MongoDB document to strings.
    Handles nested dicts and lists.
    """
    if not isinstance(doc, dict):
        return doc

    for key, value in doc.items():
        # print(value)
        if isinstance(value, ObjectId):
            doc[key] = str(value)
        elif isinstance(value, dict):
            convert_objectid_in_doc(value)
        elif isinstance(value, list):
            convert_objectid_in_list(value)

    return dict(doc)


def convert_objectid_in_list(docs: list) -> list:
    """
    Converts all bson.ObjectId values in a list of MongoDB documents to strings.
    """
    docs = list(docs)

    for index, item in enumerate(docs):
        if isinstance(item, ObjectId):
            docs[index] = str(item)
        elif isinstance(item, dict):
            convert_objectid_in_doc(item)
        elif isinstance(item, list):
            convert_objectid_in_list(item)
    return docs
