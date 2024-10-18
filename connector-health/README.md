# SOAR Connector Health Checks

These scripts can check the health of your SOAR connectors. They use the SecOps/SOAR API to retrieve connector stats.

For more info on the SOAR API, see the Swagger API docs interface at:

https://{your_instance_url}/swagger/index.html

# Usage

Export the following environment variables:

```
export SOAR_HOSTNAME=your-instance.siemplify-soar.com
export SOAR_API_KEY=xxxxxxx-yyyy-zzzz-xxxx-yyyyyyyyy
```

Run `list-connectors.py` to obtain the identifier of the connector in question:

```
./list-connectors.py
```

Pipe that through jq for friendlier output:

```
./list-connectors.py | jq
```

You should see output similar to this:

```
$ ./list-connectors.py 
[
  {
    "integration": "Microsoft365",
    "cards": [
      {
        "identifier": "Microsoft 365 Connector_55dab596-8d87-11ef-b630-00163ec19d19",
        "isEnabled": true,
        "isRemote": false,
        "displayName": "Microsoft 365 Events Connector",
        "status": 1
      },
```

Copy the full identifier string of the connector you want to monitor and pass it to `get-connector-stats.py` with double quotes:

```
./get-connector-stats.py "Rapid7 InsightIDR - Investigations Connector_4589a7ec-8d87-11ef-86bf-00163ec19d19"
```

```
$ ./get-connector-stats.py "Rapid7 InsightIDR - Investigations Connector_4589a7ec-8d87-11ef-86bf-00163ec19d19"
{
  "connectorIdentifier": null,
  "connectivityStatus": 1,
  "amountAlertsInLastDay": 4,
  "avgAlertsPerDay": 9
}
```

A failing connector should have a connectivityStatus value other than 1 and amountAlertsInLastDay will go to zero within 24 hours.


