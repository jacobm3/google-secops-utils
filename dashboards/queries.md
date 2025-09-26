
# 01 Top 10 IOCs Observed

```
$ioc_value = ioc.ioc_value
match:
   $ioc_value
outcome:
   $ioc_count = count(ioc.ioc_value)
```
# 02 Sorting with the Order Section

```
$ioc_value = ioc.ioc_value
match:
   $ioc_value
outcome:
   $ioc_count = count(ioc.ioc_value)
order: $ioc_count desc
limit: 10

```
# 03 Adding additional criteria

```
$ioc_value = ioc.ioc_value
ioc.ioc_type = "IOC_TYPE_DOMAIN"
match:
   $ioc_value
outcome:
   $ioc_count = count(ioc.ioc_value)
order: $ioc_count desc
limit: 10
```

# 04 High severity bar chart

```
$ioc_value = ioc.ioc_value
ioc.ioc_type = "IOC_TYPE_DOMAIN"
ioc.severity = "High"
match:
   $ioc_value
outcome:
   $ioc_count = count(ioc.ioc_value)
order: $ioc_count desc
limit: 10
```

# 05 Event Count Chart

```
metadata.event_type = $event_type
match:
   $event_type
outcome:
   $event_count = count(metadata.event_type)
order:
   $event_count desc

```

# 06 Adding Drilldowns to Charts

```
metadata.event_type = ${event_type}
(
   re.capture(principal.hostname, `(.*)\.stackedpads.local`) in %key_servers or
   re.capture(target.hostname, `(.*)\.stackedpads.local`) in %key_servers or
   re.capture(src.hostname, `(.*)\.stackedpads.local`) in %key_servers
)
```

https://cloud.google.com/chronicle/docs/unified-data-model/udm-usage



# 07 Building a time chart

```
$severity = detection.detection.severity
$date = timestamp.get_timestamp(detection.detection_time.seconds, "%F")
match:
   $date, $severity
outcome:
   $detection_count = count($severity)
order:
   $date asc

```

# 06 Adding Drilldowns to Charts

View events for key servers - 
```
metadata.event_type = ${event_type}
(
   re.capture(principal.hostname, `(.*)\.stackedpads.local`) in %key_servers or
   re.capture(target.hostname, `(.*)\.stackedpads.local`) in %key_servers or
   re.capture(src.hostname, `(.*)\.stackedpads.local`) in %key_servers
)
```

# 06 Adding Drilldowns to Charts

```

```

# 06 Adding Drilldowns to Charts

```

```

