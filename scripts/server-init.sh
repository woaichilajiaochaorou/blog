#!/bin/bash
set -e

echo "=== Oracle Cloud ARM 博客服务器初始化 ==="

# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装 Docker
if ! command -v docker &> /dev/null; then
    echo ">>> 安装 Docker..."
    curl -fsSL https://get.docker.com | sh
    sudo usermod -aG docker $USER
    echo "Docker 安装完成，请重新登录以应用 docker 组权限"
fi

# 安装 Docker Compose plugin
if ! docker compose version &> /dev/null; then
    echo ">>> 安装 Docker Compose..."
    sudo apt install -y docker-compose-plugin
fi

# 创建博客目录
mkdir -p ~/blog/dist

# 安装 Certbot (用于 HTTPS)
echo ">>> 安装 Certbot..."
sudo apt install -y certbot

echo ""
echo "=== 初始化完成 ==="
echo ""
echo "接下来："
echo "1. 在 GitHub 仓库 Settings > Secrets 中添加："
echo "   - SSH_PRIVATE_KEY: 服务器 SSH 私钥"
echo "   - SERVER_HOST: 服务器公网 IP"
echo "   - SERVER_USER: SSH 用户名 (通常是 ubuntu)"
echo ""
echo "2. 如果有域名，申请 SSL 证书："
echo "   sudo certbot certonly --standalone -d your-domain.com"
echo ""
echo "3. Oracle Cloud 安全列表放行端口："
echo "   - TCP 80  (HTTP)"
echo "   - TCP 443 (HTTPS)"
echo ""
echo "4. 首次部署："
echo "   cd ~/blog && docker compose up -d --build"
