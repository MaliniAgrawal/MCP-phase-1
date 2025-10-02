from core.nlp_utils import parse_nlp
from config.settings import DEFAULT_REGION

def generate_command(nl_request: str):
    """
    Takes NL request → parse intent/entities → build CLI + explanation.
    """
    intent, entities = parse_nlp(nl_request)

    service = entities.get("service")
    name = entities.get("name")
    region = entities.get("region", DEFAULT_REGION)

    if intent == "create" and service == "s3":
        cli = f"aws s3 mb s3://{name} --region {region}"
        explanation = f"This command creates an S3 bucket named '{name}' in region '{region}'."
        return cli, explanation

    elif intent == "create" and service == "dynamodb":
        cli = f"aws dynamodb create-table --table-name {name} " \
              f"--attribute-definitions AttributeName=Id,AttributeType=S " \
              f"--key-schema AttributeName=Id,KeyType=HASH " \
              f"--provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 " \
              f"--region {region}"
        explanation = f"This command creates a DynamoDB table named '{name}' with a simple primary key 'Id' in region '{region}'."
        return cli, explanation

    else:
        cli = "echo 'Command not recognized yet.'"
        explanation = f"No rule matched for input: '{nl_request}'"
        return cli, explanation
