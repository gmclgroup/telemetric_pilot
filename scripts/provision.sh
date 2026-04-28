#!/bin/bash
# provision.sh — Post-deploy hardening & port setup for Traccar on Ubuntu
# Run as root on your DigitalOcean droplet

set -e

echo "==> Updating system..."
apt-get update -y && apt-get upgrade -y

echo "==> Configuring UFW firewall..."
ufw default deny incoming
ufw default allow outgoing
ufw allow ssh
ufw allow 8082/tcp   # Traccar web UI
ufw allow 5055:5140/tcp
ufw allow 5055:5140/udp
ufw --force enable

echo "==> Enabling Traccar service..."
systemctl enable traccar
systemctl start traccar

echo "==> Traccar status:"
systemctl status traccar --no-pager

echo ""
echo "✓ Done. Access Traccar at http://$(curl -s ifconfig.me):8082"
echo "  Default login: admin / admin — CHANGE THIS NOW"
