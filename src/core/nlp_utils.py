import re

def parse_nlp(nl_request: str):
    """
    Very simple rule-based parser:
    Extracts intent (create/delete) + service (s3/dynamodb) + name + region.
    """
    nl_request = nl_request.lower()
    intent = None
    service = None
    entities = {}

    # Intent
    if "create" in nl_request:
        intent = "create"
    elif "delete" in nl_request:
        intent = "delete"

    # Service
    if "s3" in nl_request or "bucket" in nl_request:
        service = "s3"
    elif "dynamodb" in nl_request or "table" in nl_request:
        service = "dynamodb"

    entities["service"] = service

    # Name
    match_name = re.search(r"named?\s+(\w+)", nl_request)
    if match_name:
        entities["name"] = match_name.group(1)

    # Region
    match_region = re.search(r"(us-\w+-\d+)", nl_request)
    if match_region:
        entities["region"] = match_region.group(1)

    return intent, entities
