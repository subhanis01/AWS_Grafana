def lambda_handler(event, context):
    value = event.get("input", "")
    return {"input": value, "output": value.upper()}