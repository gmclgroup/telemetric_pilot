# Business Model — Telemetric Pilot

## Unit Economics

| Metric | Value |
|---|---|
| Assets tracked | 100 |
| Price per asset/mo | $20 |
| Gross revenue/mo | $24,000 |
| Monthly costs | $35 |
| **Net profit/mo** | **$23,965** |
| Startup cost | $4,044 |
| **Break-even** | **< 1 month** |

## Scaling

| Assets | Revenue/mo | Costs/mo | Profit/mo |
|---|---|---|---|
| 100 | $24,000 | $35 | ~$23,965 |
| 250 | $60,000 | ~$60 | ~$59,940 |
| 500 | $120,000 | ~$100 | ~$119,900 |
| 1,000 | $240,000 | ~$175 | ~$239,825 |

> Costs scale slowly — main VPS upgrade needed at ~500 devices (move to $48/mo plan).

## Cost Breakdown

### One-Time
- 100× GPS trackers @ $25 = **$2,500**
- 100× 1NCE lifetime SIMs @ $14 = **$1,400**
- Domain registration = **$20**
- First month VPS = **$24**
- **Total: $4,044**

### Monthly Recurring
- VPS hosting = **$24**
- SIM data buffer (overage reserve) = **$10**
- Domain renewal (amortised) = **$1**
- **Total: $35/mo**

## Key Advantages
- SIM cost is one-time (lifetime plan) — not monthly
- Traccar is open-source — no licence fees
- DigitalOcean 1-click deploy — no DevOps expertise required
- OBD2 trackers need no installation — plug-and-play
