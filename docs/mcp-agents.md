# Usage desk: instructions for AI agents

Use the local `firstmate-usage` MCP server to answer questions about the owner's
connected Codex, Claude Code and Antigravity accounts. It reads one shared cache;
calling a tool does not run a model, refresh a provider, spend credit or consume
a quota reset. The public landing page never connects to that private cache.

## Connect

1. Install Usage desk and complete each provider's official sign-in through
   Connections. Keep the local widget/collector running.
2. Reconnect MCP or open a new client session after setup changes. The configured
   server name is `firstmate-usage`; clients may prefix its tool names.
3. Verify without a model prompt:

```powershell
codex mcp get firstmate-usage
claude mcp get firstmate-usage
agy mcp list
```

Bundled-path and current agy registration fixes are included starting with the
local RC18 candidate. The public RC17 download remains an unsigned preview; it
does not include those fixes. For older builds, use the actual physical bundled
interpreter/script paths, not assumed LocalAppData paths. Current agy stores MCP
servers in `.gemini/config/mcp_config.json`. Its official registration command is:

```text
agy mcp add firstmate-usage "ABSOLUTE_BUNDLED_PYTHON_EXE" "ABSOLUTE_USAGE_WIDGET_PY" mcp
```

Replace both placeholders with verified installed paths. Do not overwrite a
different server using the same name. For another MCP client, copy the existing
registration's command and arguments. No API key or network MCP endpoint is
required. Keep normal client tool permissions; do not enable blanket approvals.

## Tools

| Tool | Use |
| --- | --- |
| `usage_get_snapshot` | Current cached accounts, quota pools, reset times, reported credit, source and age. Start here. |
| `usage_get_timeline` | Recorded quota history and upcoming reset information. Use only when history is requested. |
| `usage_get_billing` | Reported credits and legacy cost/subscription records. Unknown renewal dates remain unknown. |

Call `usage_get_snapshot` with `{}` once to read all available connected accounts.
Optional filters are `provider` (`codex`, `claude`, `agy`) and `account` (the opaque
account key returned by the snapshot). Examples:

```json
{}
```

```json
{"provider":"claude"}
```

Discover the tool through the client's normal MCP tool listing. This is an MCP
tool call, not a shell command. Do not invent a tool result or claim the server
is connected simply because its configuration exists.

## Read and report accurately

- Inspect `server_time`, account `observed_at`/`age_seconds`/`stale`, and each
  quota or credit's own age/staleness. Cached observations are not live polling.
- Group quota pools by provider and account. `used_percent` means used;
  `remaining_percent` means remaining. Do not add percentages across pools.
- `resets_at` and `expires_at` are Unix timestamps in seconds. Convert to the
  user's timezone and show date/time plus timezone. Hanoi uses UTC+07. Round only
  for display; keep seconds available when the user needs precise timestamps.
- Check `awaiting_refresh`, `disabled` and missing reset timestamps. A passed
  reset is awaiting confirmation, not proof of a refill. Do not invent a reset.
- Credit `balance` is remaining, `total` is reported total, and `used` is spent
  within that pool. Include `unit`, scope, expiry and source age when supplied.
- Codex provider credits are not USD. Its percentage of the first recorded
  balance is a local baseline, not the plan's total allocation. Do not invent a
  credit expiry when none is reported.
- Claude included cloud credit applies to cloud sessions. Do not describe it as
  a universal allowance for all Claude usage. Report extra usage separately.
- Agy's Gemini and Claude/GPT-OSS pools are shared within their respective model
  families. A model catalog entry does not imply its own independent quota.
- Null, omitted or unreported values mean unknown, never zero. A service error
  means unavailable, not that accounts have no usage. Report disconnected/stale
  sources honestly and suggest reopening the widget or reconnecting the client.
- Do not read provider credential files, request API keys, send model prompts,
  trigger login, buy credit, change billing or dispatch work just to answer a
  usage question. Telemetry does not authorize spending or model execution.
- Do not publish account identifiers, balances or private snapshots to a public
  website. Share only the summary the owner requested in the private conversation.

## Copy into an agent's instructions

```text
For LLM usage questions, use the firstmate-usage MCP server. Call
usage_get_snapshot with {} to read all connected accounts from the local cache.
Report each provider/account and quota separately, including used/remaining,
reset date/time in the user's timezone, credit balance/unit/expiry when reported,
and observation age. Check stale and awaiting_refresh on each pool. Missing is
unknown, not zero; a past reset is not a confirmed refill. Codex credits are not
currency, and Claude cloud credit applies to cloud sessions. Use
usage_get_timeline only for history and usage_get_billing for credit details.
Never start a model, refresh providers, read credentials or change billing to
answer usage questions. If MCP or the cache is unavailable, say so. Keep private
account data out of public pages.
```

References: [agy MCP settings](https://www.antigravity.google/docs/settings?tab=cli),
[MCP tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools).
