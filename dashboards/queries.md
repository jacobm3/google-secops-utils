
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

# 

```

```

