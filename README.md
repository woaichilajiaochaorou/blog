# Shannon's Blog

基于 VitePress 的个人技术博客，部署在 Oracle Cloud ARM 实例上。

## 项目结构

```
blog/
├── docs/                          # VitePress 内容目录
│   ├── .vitepress/config.ts       # VitePress 配置
│   ├── index.md                   # 首页
│   ├── about.md                   # 关于页
│   └── posts/                     # 博客文章
├── deploy/                        # 部署配置
│   ├── nginx.conf                 # Nginx 配置 (HTTP)
│   ├── nginx-ssl.conf             # Nginx 配置 (HTTPS 模板)
│   └── docker-compose.prod.yml    # 服务器端 Docker Compose
├── scripts/
│   └── server-init.sh             # 服务器初始化脚本
├── .github/workflows/
│   └── deploy.yml                 # GitHub Actions 自动部署
├── Dockerfile                     # 本地 Docker 构建 (可选)
├── docker-compose.yml             # 本地 Docker 运行 (可选)
└── package.json
```

## 本地开发

```bash
npm install
npm run dev       # 启动开发服务器 http://localhost:5173
npm run build     # 构建静态文件
npm run preview   # 预览构建结果
```

## 部署到 Oracle Cloud ARM

### 1. 开通 Oracle Cloud 实例

- 选择 **Ampere A1** (ARM) 实例
- 配置：4 OCPU / 24GB 内存（永久免费额度内）
- 系统：Ubuntu 22.04
- 开放安全列表端口：TCP 80, 443

### 2. 初始化服务器

SSH 登录服务器后执行：

```bash
# 下载并运行初始化脚本
curl -fsSL https://raw.githubusercontent.com/<你的用户名>/blog/main/scripts/server-init.sh | bash
```

或者手动执行：

```bash
# 安装 Docker
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER

# 创建博客目录
mkdir -p ~/blog/dist ~/blog/deploy
```

### 3. 配置 GitHub Secrets

在 GitHub 仓库 → Settings → Secrets and variables → Actions 中添加：

| Secret 名称       | 值                              |
| ---------------- | ------------------------------- |
| `SSH_PRIVATE_KEY` | 服务器 SSH 私钥（完整内容）         |
| `SERVER_HOST`     | 服务器公网 IP                     |
| `SERVER_USER`     | SSH 用户名（通常是 `ubuntu`）      |

**生成 SSH 密钥对：**

```bash
ssh-keygen -t ed25519 -C "deploy-key" -f ~/.ssh/blog_deploy
# 将公钥添加到服务器
ssh-copy-id -i ~/.ssh/blog_deploy.pub ubuntu@<SERVER_IP>
# 将私钥内容复制到 GitHub Secret SSH_PRIVATE_KEY
cat ~/.ssh/blog_deploy
```

### 4. 首次部署

Push 代码到 `main` 分支，GitHub Actions 会自动构建并部署。

也可以手动在服务器上首次启动：

```bash
cd ~/blog/deploy
docker compose -f docker-compose.prod.yml up -d
```

### 5. 配置 HTTPS（可选）

如果有域名：

```bash
# 停止 Nginx 释放 80 端口
docker compose -f ~/blog/deploy/docker-compose.prod.yml down

# 申请证书
sudo certbot certonly --standalone -d your-domain.com

# 修改 nginx-ssl.conf 中的 YOUR_DOMAIN 为你的域名
# 替换 deploy/nginx.conf 为 nginx-ssl.conf 内容
# 更新 docker-compose.prod.yml 挂载证书目录

# 重新启动
docker compose -f ~/blog/deploy/docker-compose.prod.yml up -d
```

## 写新文章

1. 在 `docs/posts/` 下新建 `.md` 文件
2. 添加 frontmatter：

```markdown
---
title: 文章标题
date: 2026-02-16
---

# 文章标题

正文内容...
```

3. 在 `docs/.vitepress/config.ts` 的 sidebar 中添加文章链接
4. `git push` 到 main，自动部署

## 技术栈

- [VitePress](https://vitepress.dev/) - 静态站点生成
- [Docker](https://www.docker.com/) + [Nginx](https://nginx.org/) - 容器化部署
- [GitHub Actions](https://github.com/features/actions) - CI/CD
- [Oracle Cloud](https://www.oracle.com/cloud/free/) - ARM 服务器（永久免费）
