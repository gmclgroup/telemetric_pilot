# Traccar REST API Examples

Base URL: `http://<YOUR_IP>:8082/api`
Auth: HTTP Basic (`admin` / `<your_password>`)

---

## Devices

```bash
# List all devices
curl -u admin:PASSWORD "http://<YOUR_IP>:8082/api/devices"

# Get a specific device
curl -u admin:PASSWORD "http://<YOUR_IP>:8082/api/devices?id=1"
```

## Positions

```bash
# Latest position for a device
curl -u admin:PASSWORD "http://<YOUR_IP>:8082/api/positions?deviceId=1"

# Positions within a time range (ISO 8601)
curl -u admin:PASSWORD \
  "http://<YOUR_IP>:8082/api/positions?deviceId=1&from=2024-01-01T00:00:00Z&to=2024-01-02T00:00:00Z"
```

## Reports

```bash
# Route report for a device
curl -u admin:PASSWORD \
  "http://<YOUR_IP>:8082/api/reports/route?deviceId=1&from=2024-01-01T00:00:00Z&to=2024-01-02T00:00:00Z"

# Stop report
curl -u admin:PASSWORD \
  "http://<YOUR_IP>:8082/api/reports/stops?deviceId=1&from=2024-01-01T00:00:00Z&to=2024-01-02T00:00:00Z"
```

## Events

```bash
# Get recent events
curl -u admin:PASSWORD "http://<YOUR_IP>:8082/api/events?deviceId=1"
```

---

## Notes
- Replace `<YOUR_IP>` with your DigitalOcean droplet IP
- Replace `PASSWORD` with your admin password
- Full API docs: `http://<YOUR_IP>:8082/api-docs` (Swagger UI)
