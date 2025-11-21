# Version Control Guide for Crafts by Cates

This guide will help you safely work with Git and GitHub on this project. Follow these steps carefully to avoid conflicts and maintain a clean codebase.

## Table of Contents
1. [Before You Start Working](#before-you-start-working)
2. [Creating a Feature Branch](#creating-a-feature-branch)
3. [Making Changes](#making-changes)
4. [Committing Your Changes](#committing-your-changes)
5. [Pushing Your Changes](#pushing-your-changes)
6. [Creating a Pull Request](#creating-a-pull-request)
7. [Merging Your Changes](#merging-your-changes)
8. [Common Issues and Solutions](#common-issues-and-solutions)

---

## Before You Start Working

**ALWAYS start by pulling the latest changes from the remote repository.** This ensures you're working with the most up-to-date code.

### Step 1: Check Your Current Branch

```bash
git branch
```

**What this does:** Shows you which branch you're currently on. The active branch will have an asterisk (*) next to it.

**Expected output:**
```
* main
  feature-branch-name
```

### Step 2: Switch to Main Branch

```bash
git checkout main
```

**What this does:** Switches you to the `main` branch (the primary branch of the project).

**Why:** You want to make sure `main` is up-to-date before creating a new feature branch.

### Step 3: Pull Latest Changes

```bash
git pull origin main
```

**What this does:** Downloads the latest changes from the remote repository (GitHub) and merges them into your local `main` branch.

**Why:** This ensures you have all the latest updates from your collaborators before starting new work.

**Expected output:**
```
Already up to date.
```
or
```
Updating abc1234..def5678
Fast-forward
 app/routes.py | 10 +++++-----
 1 file changed, 5 insertions(+), 5 deletions(-)
```

---

## Creating a Feature Branch

**NEVER commit directly to `main`.** Always create a feature branch for your changes.

### Step 4: Create a New Feature Branch

```bash
git checkout -b feature/your-feature-name
```

**What this does:** Creates a new branch AND switches to it in one command.

**Naming convention:** Use descriptive names like:
- `feature/add-contact-form`
- `feature/update-homepage-styling`
- `bugfix/fix-image-carousel`
- `enhancement/improve-navigation`

**Example:**
```bash
git checkout -b feature/add-gallery-page
```

**Expected output:**
```
Switched to a new branch 'feature/add-gallery-page'
```

---

## Making Changes

Now you can safely make changes to the code! Edit files in VSCode as needed.

### Step 5: Check What You've Changed

```bash
git status
```

**What this does:** Shows you which files have been modified, added, or deleted.

**Expected output:**
```
On branch feature/add-gallery-page
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   app/routes.py
        modified:   app/templates/gallery.html

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        app/static/images/new-image.jpg
```

---

## Committing Your Changes

### Step 6: Stage Your Changes

**Option A: Add specific files**
```bash
git add app/routes.py
git add app/templates/gallery.html
```

**Option B: Add all changed files**
```bash
git add .
```

**What this does:** Stages files for commit. Think of this as selecting which changes you want to save.

**Why:** Git requires you to explicitly choose which changes to include in a commit.

### Step 7: Verify Staged Changes

```bash
git status
```

**Expected output:**
```
On branch feature/add-gallery-page
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   app/routes.py
        modified:   app/templates/gallery.html
        new file:   app/static/images/new-image.jpg
```

### Step 8: Commit Your Changes

```bash
git commit -m "Add gallery page with image display functionality"
```

**What this does:** Saves your staged changes with a descriptive message.

**Commit message best practices:**
- Use present tense ("Add feature" not "Added feature")
- Be descriptive but concise
- Start with a verb (Add, Fix, Update, Remove, etc.)

**Good examples:**
- `git commit -m "Add contact form validation"`
- `git commit -m "Fix carousel navigation bug"`
- `git commit -m "Update homepage hero image"`

**Bad examples:**
- `git commit -m "stuff"` ❌
- `git commit -m "changes"` ❌
- `git commit -m "idk"` ❌

---

## Pushing Your Changes

### Step 9: Push Your Feature Branch to GitHub

```bash
git push origin feature/your-feature-name
```

**What this does:** Uploads your local branch and commits to GitHub.

**Example:**
```bash
git push origin feature/add-gallery-page
```

**First time pushing a new branch?** You might see:
```
fatal: The current branch feature/add-gallery-page has no upstream branch.
```

**Solution:** Git will suggest the correct command:
```bash
git push --set-upstream origin feature/add-gallery-page
```

**What this does:** Creates the branch on GitHub and links your local branch to it.

---

## Creating a Pull Request

### Step 10: Open a Pull Request on GitHub

1. Go to the repository on GitHub
2. You'll see a yellow banner saying "Your recently pushed branches"
3. Click **"Compare & pull request"**
4. Add a title and description explaining your changes
5. Click **"Create pull request"**

**What this does:** Requests that your changes be reviewed and merged into the `main` branch.

**Why:** This allows for code review and prevents accidental breaking changes.

---

## Merging Your Changes

### Step 11: Wait for Review (if applicable)

If working with collaborators, wait for someone to review your pull request.

### Step 12: Merge the Pull Request

Once approved (or if you're working solo):

1. Click **"Merge pull request"** on GitHub
2. Click **"Confirm merge"**
3. Optionally, click **"Delete branch"** to clean up

**What this does:** Incorporates your feature branch changes into the `main` branch.

### Step 13: Update Your Local Main Branch

```bash
git checkout main
git pull origin main
```

**What this does:** Switches back to `main` and downloads the newly merged changes.

### Step 14: Delete Your Local Feature Branch (Optional)

```bash
git branch -d feature/your-feature-name
```

**What this does:** Removes the feature branch from your local machine since it's been merged.

**Example:**
```bash
git branch -d feature/add-gallery-page
```

---

## Common Issues and Solutions

### Issue 1: "Your branch is behind 'origin/main'"

**Solution:**
```bash
git pull origin main
```

**What happened:** Someone else pushed changes while you were working.

---

### Issue 2: Merge Conflicts

**What happened:** You and someone else changed the same lines of code.

**Solution:**
1. Git will mark the conflicts in your files like this:
```
<<<<<<< HEAD
Your changes
=======
Their changes
>>>>>>> main
```

2. Open the file in VSCode
3. Decide which changes to keep (or combine them)
4. Remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
5. Stage and commit the resolved files:
```bash
git add .
git commit -m "Resolve merge conflict"
```

---

### Issue 3: Accidentally Committed to Main

**If you haven't pushed yet:**
```bash
git reset --soft HEAD~1
```

**What this does:** Undoes the last commit but keeps your changes.

**Then:**
1. Create a feature branch: `git checkout -b feature/your-feature-name`
2. Commit again: `git commit -m "Your message"`
3. Push: `git push origin feature/your-feature-name`

---

### Issue 4: Want to Discard All Local Changes

**⚠️ WARNING: This will permanently delete your uncommitted changes!**

```bash
git restore .
```

**What this does:** Reverts all modified files to their last committed state.

---

## Quick Reference Cheat Sheet

```bash
# Start working
git checkout main
git pull origin main
git checkout -b feature/your-feature-name

# Make changes, then...
git status                                    # Check what changed
git add .                                     # Stage all changes
git commit -m "Descriptive message"           # Commit changes
git push origin feature/your-feature-name     # Push to GitHub

# After merging PR on GitHub
git checkout main
git pull origin main
git branch -d feature/your-feature-name       # Clean up local branch
```

---

## Best Practices Summary

✅ **DO:**
- Always `git pull` before starting work
- Create feature branches for all changes
- Write clear, descriptive commit messages
- Commit often (small, logical chunks)
- Push your branches to GitHub regularly

❌ **DON'T:**
- Commit directly to `main`
- Use vague commit messages
- Wait too long between commits
- Force push (`git push -f`) unless you know what you're doing
- Commit sensitive information (passwords, API keys, etc.)

---

## Getting Help

- **Check status:** `git status`
- **View commit history:** `git log --oneline`
- **See what changed:** `git diff`
- **Undo last commit (keep changes):** `git reset --soft HEAD~1`

If you're ever unsure, ask before running a command! It's better to ask than to accidentally lose work.

---

**Happy coding! 🚀**
