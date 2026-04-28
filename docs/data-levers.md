# SIM Data Optimisation — 7 Levers

Target: **0.3–1.5 MB/month per SIM** (1NCE 500MB lifetime)

## Why This Matters
Without optimisation, a GPS tracker can consume 4–8 MB/month.
At that rate, the 500MB lifetime allowance lasts only 5–10 years.
With all 7 levers active, usage drops to ~0.3 MB/mo — effectively infinite.

---

## The 7 Levers

### 1. Report Interval → 5 min | Savings: ~96%
Default trackers report every 10–30 seconds.
Setting to every 5 minutes cuts transmissions from ~8,640/day to ~288/day.
- Traccar config: `<entry key='gt06.period'>300</entry>` (seconds)

### 2. Packet Size → GPS + basic OBD2 only | Savings: ~70%
Disable unused OBD2 PIDs (fuel trim, intake temp, etc.).
Keep: lat, lon, speed, ignition, odometer.
- Configure in tracker firmware via SMS or app

### 3. Speed Delta → transmit only if >5 km/h | Savings: ~50%
Assets parked overnight (majority of the time) generate zero data.
- Tracker firmware setting: `SPEED_THRESHOLD=5`

### 4. Ignition OFF → sleep mode | Savings: ~80%
When ignition is off, tracker enters deep sleep and stops reporting.
Only sends a heartbeat every 5–15 min (see Lever 7).
- Tracker firmware setting: `SLEEP_ON_IGNITION_OFF=1`

### 5. Angle Change → transmit only if >30° | Savings: ~30%
On straight roads, skip redundant position updates.
Only transmit when heading changes by more than 30°.
- Tracker firmware setting: `ANGLE_THRESHOLD=30`

### 6. Protocol → UDP or MQTT | Savings: ~20%
TCP has higher overhead per packet (SYN/ACK handshakes).
UDP or MQTT (with QoS 0) eliminates this overhead.
- Traccar supports both. Confirm your tracker model's protocol.

### 7. Heartbeat → 5–15 min | Savings: ~10%
While in sleep mode, send a minimal keep-alive packet every 5–15 minutes.
This keeps the SIM active and confirms the device is online.
- Tracker firmware setting: `HEARTBEAT_INTERVAL=600` (seconds)

---

## Combined Impact

| Levers Active | Est. Monthly Data |
|---|---|
| None | ~6 MB |
| 1 only | ~0.24 MB |
| 1+2 | ~0.07 MB |
| 1+2+3+4 | ~0.02 MB |
| All 7 | ~0.3–1.5 MB (with heartbeat) |

> The heartbeat (Lever 7) is the floor — it adds ~0.3 MB/mo even when the asset is parked.
