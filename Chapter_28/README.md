# 📘 Chapter 28 – Branching, Merging & Pull Requests

When working in teams, it’s best to use **branches** instead of editing `main` directly.

---

## 🔹 Branching
- A **branch** = separate version of the code
- Default branch → `main`

### Create a Branch (GitHub Desktop)
- Branch → New Branch → name it (e.g., `feature-login`)
- Make changes → Commit → Push branch

---

## 🔹 Merging
- After finishing work, **merge branch into main**
- GitHub Desktop → Branch → Merge into main

---

## 🔹 Pull Requests (PRs)
- On **GitHub Website** → Go to repo
- Click **Compare & Pull Request**
- Review changes → Click **Merge Pull Request**
- Deletes the feature branch after merging (optional)

---

## 🔹 Visual Diagram

```
       main branch
           |
           |
      ------------
      |          |
```

feature-1     feature-2
\|          |
\        /
\---merge---
|
main

```

---

## 🧠 Summary
- **Branch** → Isolated workspace  
- **Merge** → Combine changes back into main  
- **Pull Request (PR)** → Ask team to review + merge your changes
