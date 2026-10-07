---
title: "ClickHouse quota resource counters (execution_time, written_bytes, MergeTree read_bytes) do not accumulate on 26.3"
summary: On ClickHouse 26.3 Altinity build, quota limits for execution_time, written_bytes, and MergeTree read_bytes never count or trip
tags: [clickhouse, quotas, altinity]
date: 2026-10-07
confidence: confirmed
---

**Problem:** Testing `CREATE QUOTA` limits on a ClickHouse 26.3.33.10001.altinitystable
cluster, the resource-family limits never trip and their counters never move:
`execution_time` stays 0 after 6 s of `sleep()`/`sleepEachRow()` and after a
1.3 s CPU-bound query; `written_bytes` stays 0 after two ~8 MB inserts;
`read_bytes` stays 0 after two 16 MB MergeTree reads. No usage row for those
quotas ever appears in `system.quotas_usage`. Meanwhile the query-family
limits on the same cluster work exactly as documented: `queries` (checked
before execution, rejects the next query) and `result_rows` (checked after
execution, the over-limit query runs and the response is rejected) both
count and enforce. A `read_bytes` limit even counted a 48-byte
`system.numbers` read, so the counter exists but MergeTree reads do not
register.

**Cause:** Unknown. Suspected a 26.3 or Altinity-build regression in quota
resource accounting; not checked against upstream vanilla builds. Do not
assume these limits protect anything without testing on your build first.

**Fix / Fact:** On this build, only the query-counting quota limits are
reliable: `queries`, `query_selects`, `query_inserts`, `errors`,
`result_rows`, `result_bytes`. Do not rely on `execution_time`,
`written_bytes`, or `read_bytes`/`read_rows` for load control or usage
tracking there. To capacity-check the resource limits on your own build,
test each one: run a query pair over a single HTTP keep-alive connection
(both requests hit the same node, so per-node counters accumulate), then
read `clusterAllReplicas('<cluster>', 'system.quotas_usage')`.

**Applies to:** ClickHouse 26.3.33.10001.altinitystable. Other builds and
versions untested.
