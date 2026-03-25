# Security Policy

## Architecture

TraderLab 101 is a single HTML file that runs entirely in your browser. There is no server, no database, no authentication, and no external data transmission. All data is stored in `localStorage` on your machine.

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0     | ✅ Current |

## Reporting a Vulnerability

If you find a security issue (e.g. XSS in user-entered data, data leakage, or malicious behavior in the code), please:

1. **Do not** open a public issue
2. Open a private security advisory via GitHub's "Report a vulnerability" button on the Security tab
3. Or reach out directly via the Traders Lab Discord

I'll review and respond as quickly as possible.

## Data Safety

- All data stays in your browser's `localStorage`
- No data is sent to any server
- The only outbound network requests are:
  - **BMBridge** (localhost only) — for real-time price data from Sierra Chart
  - **Yahoo Finance** — for delayed price quotes (fallback feed)
- Export your data regularly via Settings → Export Backup
