# 部署说明

本项目推荐使用免费或低成本组合上线：

- 前端：Render Static Site
- 后端：Render Web Service
- 数据库：Supabase PostgreSQL

## 1. 准备数据库

1. 登录 Supabase，创建一个新项目。
2. 在 Project Settings / Database 中复制 PostgreSQL 连接字符串。
3. 连接字符串作为后端环境变量 `DATABASE_URL` 使用。

## 2. 部署后端

Render 创建 Web Service：

- Root Directory: `backend`
- Runtime: Python
- Build Command:

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

- Start Command:

```bash
python manage.py migrate && python manage.py seed_search_documents && gunicorn config.wsgi:application
```

- Health Check Path: `/api/health/`

后端环境变量：

```text
DJANGO_SECRET_KEY=换成一段足够长的随机密钥
DJANGO_DEBUG=false
PYTHON_VERSION=3.13.5
ALLOWED_HOSTS=你的后端域名.onrender.com
CORS_ALLOWED_ORIGINS=https://你的前端域名.onrender.com
CSRF_TRUSTED_ORIGINS=https://你的后端域名.onrender.com
DATABASE_URL=Supabase PostgreSQL 连接字符串
DJANGO_SUPERUSER_USERNAME=线上后台用户名
DJANGO_SUPERUSER_PASSWORD=线上后台密码
DJANGO_SUPERUSER_EMAIL=可选邮箱
```

后端上线后先访问：

```text
https://你的后端域名.onrender.com/api/health/
```

返回 `{"status":"ok"}` 即后端可用。

## 3. 部署前端

Render 创建 Static Site：

- Root Directory: `frontend`
- Build Command:

```bash
pnpm install && pnpm run build
```

- Publish Directory:

```text
dist
```

前端环境变量：

```text
VITE_API_BASE_URL=https://你的后端域名.onrender.com
```

前端上线后，打开官网并提交一次合作咨询，确认后端后台能看到记录。

## 4. 创建线上管理员

首次上线后，需要进入 Render 后端服务的 Shell，执行：

```bash
python manage.py createsuperuser
```

然后访问：

```text
https://你的后端域名.onrender.com/admin/
```

可以维护：

- 合作咨询：官网表单提交后的线索记录。
- 搜索内容：保留为内部内容资料模型。

## 5. 使用 Blueprint

仓库根目录提供了 `render.yaml`。也可以在 Render 中使用 Blueprint 创建服务，然后在控制台补齐上述环境变量。

注意：前端域名和后端域名创建完成后，需要相互补齐：

- 后端 `CORS_ALLOWED_ORIGINS` 填前端域名。
- 后端 `CSRF_TRUSTED_ORIGINS` 填后端域名。
- 前端 `VITE_API_BASE_URL` 填后端域名。
