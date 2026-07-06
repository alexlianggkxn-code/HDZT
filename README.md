# 沪东智体官网

沪东智体人工智能科技（上海）有限公司官网首版。项目采用前后端分离：

- `frontend/`：Vue 3 + Vite + TypeScript 官网前端
- `backend/`：Django + Django REST Framework 合作咨询 API 与后台内容管理

公司税号：`91310116MAEKJPKT70`

## 页面内容

首版官网不展示站内搜索，重点呈现：

- 公司首屏与真实研发工位图片
- 业务方向：数据与智能体流程、机器人训练数据、陪伴机器人内容
- 应用场景：训练实验室、数据标注复盘、陪伴内容运营、企业展示试点
- 可交付内容与合作流程
- 合作咨询表单

## 本地开发

### 后端

```powershell
cd backend
..\.venv\Scripts\python.exe manage.py migrate
..\.venv\Scripts\python.exe manage.py seed_search_documents
..\.venv\Scripts\python.exe manage.py runserver
```

如果 `.venv` 不存在，先在仓库根目录创建并安装依赖：

```powershell
C:\Users\liang\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r backend\requirements.txt
```

### 前端

```powershell
cd frontend
.\node_modules\.bin\vite --host 0.0.0.0
```

如果依赖未安装，先运行：

```powershell
cd frontend
C:\Users\liang\.cache\codex-runtimes\codex-primary-runtime\dependencies\bin\pnpm.cmd install
```

## 验证

```powershell
cd backend
..\.venv\Scripts\python.exe manage.py test
```

```powershell
cd frontend
.\node_modules\.bin\vue-tsc -b
.\node_modules\.bin\vite build
```

## API

### 健康检查

`GET /api/health/`

```json
{
  "status": "ok",
  "service": "hudongzhiti-api",
  "company": "沪东智体人工智能科技（上海）有限公司"
}
```

### 合作咨询

`POST /api/contact/`

```json
{
  "name": "李四",
  "organization": "机器人实验室",
  "contact": "lisi@example.com",
  "interest": "companion",
  "message": "希望了解陪伴机器人内容能力合作方案。"
}
```

成功返回：

```json
{
  "id": 1,
  "message": "咨询已提交，我们会尽快联系您。"
}
```

## 后台维护

- `ContactLead`：通过 Django Admin 查看合作咨询线索。
- `SearchDocument`：保留为后台内容资料模型，当前官网前端不展示站内搜索。

