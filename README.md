# Git Integration Project

This project demonstrates complete Git workflow integration as requested:
- Git configuration and local repository initialization
- Branching strategy with `main`, `developer1`, and `developer2`
- File creation and tracking
- Commits, logs, and status checks
- Branch merges and merge conflict resolution
- GitHub remote setup and pushing all branches

Repository URL: [Github-repo](https://github.com/Barath2903/Github-repo.git)

## Project Files
- `app.py`: Python module with **5 functions**:
  - `add(a, b)`
  - `subtract(a, b)`
  - `multiply(a, b)`
  - `divide(a, b)`
  - `power(base, exponent)`

## Branching Strategy
- `main`: Source/integration branch
- `developer1`: Feature/update branch created from `main`
- `developer2`: Feature/update branch created from `main`

Both developer branches were intentionally changed on the same code line to force a merge conflict during integration.

## Step-by-Step Execution

### 1) Create a Brand-New Project
```bash
mkdir -p git-integration-project
cd git-integration-project
```

### 2) Configure & Initialize Local Git Repository
```bash
git init -b main
git config user.name "Barath Dev"
git config user.email "barath.dev@example.com"
```

### 3) Create Initial Project File (5 Functions)
```bash
touch app.py
```
Then added Python code with 5 required functions.

### 4) First Commit on `main`
```bash
git add app.py
git commit -m "Initial commit on main: add 5-function utility module"
```
Commit: `c4f9f42`

### 5) Create and Update `developer1` (Second Commit)
```bash
git checkout -b developer1
# update power() logic
git add app.py
git commit -m "Second commit on developer1: tweak power calculation"
```
Commit: `075ecf6`

### 6) Create `developer2` from `main` and Update (Third Commit)
```bash
git checkout main
git checkout -b developer2
# update same power() line differently
git add app.py
git commit -m "Third commit on developer2: alternate power logic"
```
Commit: `e6ba704`

### 7) Merge in Required Order and Produce Conflict
Merge order required:
1. Merge `developer1` into `main`
2. Merge `developer2` into `main`

Commands:
```bash
git checkout main
git merge developer1
git merge developer2
```
Conflict occurred in `app.py` as expected (same line modified in both branches).

### 8) Resolve Merge Conflict with Latest Change Only
Conflict was resolved by accepting the latest change from `developer2` for the conflicted file.

```bash
git checkout --theirs app.py
git add app.py
git commit -m "Merge developer2 into main: resolve conflict using latest developer2 change"
```
Merge commit: `dc5632f`

### 9) Create/Connect GitHub Remote and Push Project
Remote:
```bash
git remote add origin https://github.com/Barath2903/Github-repo.git
```
Push commands:
```bash
git push -u origin main
git push -u origin developer1
git push -u origin developer2
```

All three branches are available on GitHub.

## Verification Commands
Use these to verify repository state:

```bash
git status
git branch -a
git log --oneline --decorate --graph --all
```

## Final Outcome (Requirements Checklist)
- [x] New project created
- [x] Local Git configured and initialized
- [x] Remote GitHub repository connected
- [x] First commit on `main`
- [x] Project pushed to remote
- [x] `developer1` branch created, updated, committed
- [x] `developer2` branch created from `main`, updated, committed
- [x] Merged `developer1` then `developer2` into `main`
- [x] Merge conflict occurred
- [x] Conflict resolved with latest change only
- [x] `developer1` and `developer2` pushed to remote
