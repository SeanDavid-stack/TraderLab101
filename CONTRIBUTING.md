# Contributing to TraderLab 101

Thanks for your interest in contributing. Here's how you can help.

## Reporting Bugs

Open an issue with:
- What you did (steps to reproduce)
- What you expected to happen
- What actually happened
- Browser and OS (e.g. Chrome 120, Windows 11)
- Screenshot if relevant

## Feature Requests

Open an issue with:
- What you want and why it would be useful
- How you'd expect it to work
- Whether it fits the Auction Market Theory / Traders Lab methodology

## Code Contributions

TraderLab 101 is a single HTML file by design. If you want to submit a fix or feature:

1. Fork the repo
2. Make your changes to `TraderLab101.html`
3. Test thoroughly — open the file in Chrome, log some trades, check analytics
4. Submit a pull request with a clear description of what changed and why

### Guidelines

- Keep everything in the single file — no external dependencies, no build tools
- All data stays in localStorage — no external API calls except BMBridge (localhost) and Yahoo Finance (price feed)
- Match the existing code style (vanilla JS, no frameworks)
- Test with the demo data file to make sure nothing breaks

## Questions

Open an issue or reach out via the Traders Lab Discord.
