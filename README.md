# Telemetric Pilot — 100-Asset GPS Fleet Tracking

> Startup cost: **$4,044** | Monthly overhead: **$35** | Revenue potential: **$24K/mo**

A self-hosted GPS telematics platform for managing 100 tracked assets using OBD2 4G trackers, 1NCE lifetime IoT SIMs, and a Traccar server on DigitalOcean.

---

## Hardware

| Component | Spec | Unit Cost | Total |
|---|---|---|---|
| GPS Trackers (100) | OBD2, 4G LTE, IP67, battery backup | $25 | $2,500 |
| IoT SIMs (100) | 1NCE lifetime — 500MB/10yr, 170+ countries | $14 | $1,400 |

- **Trackers**: Source from Alibaba — search `OBD2 GPS 4G no monthly fee`
- **Protocols**: Ports 5055–5140
- **SIMs**: [1nce.com](https://1nce.com) — pre-paid lifetime, no recurring data fee

---

## Costs

### Startup (One-Time)

| Item | Qty | Unit | Total |
|---|---|---|---|
| Trackers | 100 | $25 | $2,500 |
| SIMs | 100 | $14 | $1,400 |
| VPS (1 month) | 1 | $24 | $24 |
| Domain | 1 | $20 | $20 |
| **TOTAL** | | | **$4,044** |

### Monthly Recurring

| Item | Qty | Unit | Total |
|---|---|---|---|
| VPS | 1 | $24 | $24 |
| SIM data buffer | 100 | $0.10 | $10 |
| Domain renewal | 1 | $1 | $1 |
| **TOTAL** | | | **$35** |

---

## Revenue Model

```
$20/asset/month × 100 assets = $24,000/mo gross
$24,000 − $35 = $23,965/mo net profit
```

---

## SIM Data Optimisation — 7 Levers (Target: 0.3–1.5 MB/mo per SIM)

| # | Lever | Setting | Est. Savings |
|---|---|---|---|
| 1 | Report Interval | Every 5 min | 96% |
| 2 | Packet Size | GPS + basic OBD2 only | 70% |
| 3 | Speed Delta | Transmit only if >5 km/h | 50% |
| 4 | Ignition OFF | Sleep mode | 80% |
| 5 | Angle Change | Transmit only if >30° turn | 30% |
| 6 | Protocol | UDP or MQTT | 20% |
| 7 | Heartbeat | 5–15 min interval | 10% |

---

## Server Setup (≈2 hours)

1. Go to [digitalocean.com](https://digitalocean.com) → Create Droplet → **Traccar** 1-click app (Ubuntu)
2. Open Traccar dashboard: `http://<YOUR_IP>:8082` — default login: `admin` / `admin`
3. Open firewall ports: `8082`, `5055–5140`
4. Validate using [demo.traccar.org](https://demo.traccar.org)

See [`server/setup.md`](server/setup.md) for detailed instructions.

---

## API

```bash
# Fetch latest positions for a device
curl -u admin:admin "http://<YOUR_IP>:8082/api/positions?deviceId=1"
```

See [`api/examples.md`](api/examples.md) for more endpoints.

---

## Project Structure

```
telemetric_pilot/
├── README.md
├── hardware/
│   ├── tracker-specs.md       # OBD2 tracker models, sourcing notes
│   └── sim-config.md          # 1NCE SIM setup & APN settings
├── server/
│   ├── setup.md               # DigitalOcean + Traccar install guide
│   └── traccar.xml            # Traccar server config template
├── api/
│   └── examples.md            # Traccar REST API usage examples
├── scripts/
│   ├── provision.sh           # Server provisioning script
│   └── bulk-device-import.py  # CSV → Traccar device bulk import
└── docs/
    ├── business-model.md      # Revenue, cost, scaling analysis
    └── data-levers.md         # SIM data optimisation detail
```

---

## Quick Start

```bash
git clone https://github.com/gmclgroup/telemetric_pilot.git
cd telemetric_pilot
# Follow server/setup.md to deploy your Traccar instance
```

---

## License

MIT
