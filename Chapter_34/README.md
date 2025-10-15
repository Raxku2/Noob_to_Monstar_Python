# 🚀 Chapter 34: Deploying FastAPI App on Vercel

This chapter shows how to **publish your FastAPI application live** using **Vercel** (serverless Python support). You’ll learn how to connect your GitHub repo, configure Vercel, and deploy your FastAPI project.

---

## 🎯 Why Vercel?

- Offers **serverless functions** for Python / FastAPI. :contentReference[oaicite:0]{index=0}  
- Automatically builds on each commit (CI/CD) when linked to GitHub. :contentReference[oaicite:1]{index=1}  
- Easy to configure via a `vercel.json`. :contentReference[oaicite:2]{index=2}  

---

## 📋 Prerequisites

- A **GitHub account**  
- A **Vercel account** (free plan is sufficient)  
- Your FastAPI application in a GitHub repository  
- `requirements.txt` listing all Python dependencies  
- `vercel.json` configuration file (explained below)  

---

## 1️⃣ Prepare Your FastAPI Project

1. Ensure your project has a **requirements.txt** (run `pip freeze > requirements.txt`)  
2. Create a `vercel.json` file in the root of your project. Example configuration:

```json
{
  "builds": [
    {
      "src": "main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "main.py"
    }
  ]
}
````

* `"src": "main.py"` refers to your FastAPI entry file.
* The `routes` section ensures all requests route to `main.py`.
* You may need to adjust paths if your file structure is different. ([DEV Community][1])

3. (Optional) Specify Python version via `pyproject.toml` or `Pipfile`. ([Vercel][2])

---

## 2️⃣ Push to GitHub

1. Initialize git (if not already):

   ```bash
   git init
   git add .
   git commit -m "Initial FastAPI commit"
   ```
2. Create a GitHub repository and push:

   ```bash
   git remote add origin https://github.com/yourusername/yourrepo.git
   git push -u origin main
   ```
3. Ensure your repository is **public** or that Vercel has access if private. Vercel supports deployment from GitHub directly. ([Stack Overflow][3])

---

## 3️⃣ Connect to Vercel & Deploy

1. Go to [vercel.com](https://vercel.com) → Log in
2. On Vercel dashboard → **New Project** → **Import Git Repository**
3. Authorize Vercel to access your GitHub account
4. Select your FastAPI repo
5. Vercel should detect it's a Python project.
6. In Project Settings → **Environment Variables** → add any secrets (e.g. `MONGO_URI`, tokens).
7. Click **Deploy**
8. Wait for deployment to finish — your FastAPI API is live!

   * Use `https://your-project.vercel.app` as base URL
   * Your API endpoints (e.g. `/docs`) should work

---

## 4️⃣ Using Vercel CLI (Optional)

If you prefer local control:

```bash
npm install -g vercel
vercel login
vercel link  # link your local folder to Vercel project
vercel --prod  # deploy to production
```

This allows you to deploy without pushing to Git every time. ([Vercel][4])

---

## 5️⃣ Troubleshooting Tips

| Issue                                          | Solution                                                                                                   |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `404` on your API endpoints                    | Check your `vercel.json` routing config. ([Vercel Community][5])                                           |
| “Unable to find any supported Python versions” | Ensure your `requirements.txt` exists and the `vercel.json` build config is correct. ([Stack Overflow][6]) |
| Private repo not listed                        | Grant Vercel access in GitHub settings or make the repo public. ([Stack Overflow][3])                      |

---

## ✅ Final Checklist

* [x] requirements.txt present
* [x] vercel.json configured
* [x] GitHub repo pushed
* [x] Vercel project created & linked
* [x] Environment variables set
* [x] Deployed and tested endpoints

Once done, your FastAPI app is live and accessible globally via Vercel’s infrastructure. Congratulations — you’ve deployed your API!

