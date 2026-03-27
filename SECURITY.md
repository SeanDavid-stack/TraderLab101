# Security Policy

## Data Privacy

TraderLab 101 is a client-side application. All data is stored in your browser's `localStorage` and never leaves your computer.

**No data is transmitted to any server**, with these optional exceptions:
- **Google Fonts** — loaded on page open (font files only, no user data)
- **Yahoo Finance** — price data fetched when BMBridge is not configured (no user data sent)
- **BMBridge** — connects to YOUR local server (localhost) for price data
- **Anthropic API** — only if YOU configure an API key and initiate an AI Coach call

## Reporting a Vulnerability

1. **Do NOT open a public issue**
2. Use GitHub's private security advisory feature
3. Include: description, steps to reproduce, potential impact
4. Allow 48 hours for response

## Known Considerations

- localStorage is not encrypted — physical access = data access
- JSON exports are plaintext
- API keys stored in plaintext in localStorage
- No authentication — no user accounts or passwords

## Recommendations

- Don't use on shared/public computers
- Store JSON backups securely
- Treat API keys like passwords
