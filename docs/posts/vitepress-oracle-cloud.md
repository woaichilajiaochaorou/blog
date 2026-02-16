---
title: VitePress + Oracle Cloud ARM 博客搭建指南
date: 2026-02-16
---

# VitePress + Oracle Cloud ARM 博客搭建指南

本文记录了从零搭建 VitePress 博客并部署到 Oracle Cloud ARM 实例的完整流程。

## 架构概览

```text
GitHub Repo → GitHub Actions → SSH → Oracle Cloud ARM
                                       ├── Docker
                                       ├── Nginx (反向代理 + SSL)
                                       └── VitePress (静态文件)
```

## 1. 本地开发

```bash
npm install
npm run dev      # 启动开发服务器
npm run build    # 构建静态文件
```

## 2. 服务器准备

Oracle Cloud 永久免费 ARM 实例配置：

- **CPU**：4 OCPU (Ampere A1)
- **内存**：24 GB
- **存储**：200 GB
- **系统**：Ubuntu 22.04

## 3. Docker 部署

使用 Docker Compose 一键启动：

```bash
docker compose up -d
```

## 4. 自动部署

每次 push 到 `main` 分支，GitHub Actions 自动：

1. 构建 VitePress 静态文件
2. 通过 SSH + rsync 将文件同步到服务器
3. 重载 Nginx

整个过程约 1-2 分钟完成。
