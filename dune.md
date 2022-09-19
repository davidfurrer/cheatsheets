# dune

[abstractions](https://github.com/duneanalytics/abstractions/tree/master/ethereum/public)

[dune blog article](https://alexkroeger.mirror.xyz/0C3EQBtFqAK4k2TAGPZhg0JMY-upfTAxuTD-o91vBPc)

# Compute topic hash

```sql
keccak256('Pay(uint256,uint256,address,uint256,string,address)')
```

## Cleaning an address

```sql
replace(table.address::text, '\', '0')
```

if topic is an address

```sql
SUBSTRING(topic4 FROM 13 FOR 20)
```

## Get ens name

```sql
bytea2numeric(substring(topic4 from 13 for 20, “ens name”) as ens_name
```

Ref.: https://docs.dune.com/data-tables/abstractions/labels

## Parsing data field

### data is an integer

```sql
select bytea2numeric("data"), data
from polygon."logs"
  where "contract_address" ='\x1421B4337cE370A389cf4E45a6B870487574006E'
  limit 20
```

https://polygonscan.com/address/0x1421b4337ce370a389cf4e45a6b870487574006e#events

logs are created through solidity's emit() function.

Schema polygon.logs:

| name             | meaning                                         |
| ---------------- | ----------------------------------------------- |
| contract_address | e.g. \x1421b4337ce370a389cf4e45a6b870487574006e |
| topic1           |                                                 |
| topic2           |                                                 |
| topic3           |                                                 |
| topic4           |                                                 |
| data             |                                                 |
| tx_hash          |                                                 |
| block_hash       |                                                 |
| block_number     |                                                 |
| block_time       |                                                 |
| index            |                                                 |
| tx_index         |                                                 |
