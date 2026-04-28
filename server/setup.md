# Server Setup — DigitalOcean + Traccar

## Estimated Time: ~2 hours

## Step 1 — Deploy VPS
1. Go to [digitalocean.com](https://digitalocean.com) and log in
2. **Create** → **Droplet** → **Marketplace** tab
3. Search for **Traccar** → Select the 1-click app (Ubuntu base)
4. Choose plan: **Basic — $24/mo** (2 vCPU / 2GB RAM recommended for 100 devices)
5. Select datacenter region closest to your assets
6. Add SSH key or set root password
7. Click **Create Droplet** — note your `<YOUR_IP>`

## Step 2 — Access Traccar Dashboard
1. Open browser: `http://<YOUR_IP>:8082`
2. Default credentials: `admin` / `admin`
3. **Change the password immediately** after first login

## Step 3 — Open Firewall Ports
Run on the droplet (or via DigitalOcean Firewall rules):
```bash
ufw allow 8082/tcp    # Traccar web UI
ufw allow 5055:5140/tcp
ufw allow 5055:5140/udp
ufw enable
```

## Step 4 — Validate
1. Open [demo.traccar.org](https://demo.traccar.org) in a browser
2. Register a test device and confirm data comes through
3. Point a real tracker at your server IP on the correct protocol port

## Step 5 — Domain (Optional)
1. Register domain via Namecheap/Cloudflare (~$20 first year, ~$12/yr after)
2. Add an A record pointing to `<YOUR_IP>`
3. Install SSL: `sudo certbot --nginx -d yourdomain.com`

## Traccar Config File
Located at: `/opt/traccar/conf/traccar.xml`
See [`traccar.xml`](traccar.xml) in this folder for a template.
