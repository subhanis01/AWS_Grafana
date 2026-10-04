# AWS Lambda and Grafana

This repository contains the Lambda handler and a Grafana dashboard definition for monitoring the `student-grafana-demo-io` function.

## Lambda

Deploy `lambda_function.py` as the Lambda handler (`lambda_function.lambda_handler`). The example accepts an `input` string and returns the original value plus its uppercase form.

Example event:

```json
{"input": "grafana"}
```

Example response:

```json
{"input": "grafana", "output": "GRAFANA"}
```

## Grafana dashboard

Import `grafana/student-project-dashboard.json` into Amazon Managed Grafana. The dashboard expects a CloudWatch datasource in `us-east-1` with UID `fg05hcxy7rhfkb`; select or update the datasource UID during import if it differs in your workspace.

The `Lambda Invocations` panel uses CloudWatch Metric Insights:

```sql
SELECT SUM(Invocations) FROM SCHEMA("AWS/Lambda", FunctionName) WHERE FunctionName = 'student-grafana-demo-io'
```

This repository includes the verified Lambda Invocations panel only. The live dashboard also had an `Input Output Demo - Synthetic` panel, which was not included because the expired Grafana API session prevented retrieving its saved definition.