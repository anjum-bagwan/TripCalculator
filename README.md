# Project Development Journey & Problem Solving Report

## Project Overview

The **Trip Calculator** project was developed as a web-based application to help users calculate estimated travel expenses based on multiple trip-related inputs such as number of travelers, travel distance, vehicle type, stay duration, food preferences, and additional activities. The project was built using **Python Flask**, **HTML**, and **CSS**.

The main objective of this project was not only to create a functional travel expense calculator but also to gain practical experience in:

* Backend development using Flask
* Frontend form handling
* Dynamic result rendering
* Git and GitHub workflow
* Error debugging and project deployment practices

---

# Technologies Used

## Frontend

* HTML5
* CSS3

## Backend

* Python
* Flask Framework

## Tools & Platforms

* VS Code
* Git
* GitHub
* Command Prompt / PowerShell

---

# Features of the Project

* User-friendly trip planning form
* Dynamic cost calculation
* Trip summary result page
* Cost breakdown display
* Responsive structure
* GitHub project hosting

---

# Problems Faced During Development

## 1. Result Page Not Appearing

### Problem

One of the major issues faced during development was that after submitting the form, the **result page was not appearing**. The server was running, but the application was not rendering the `result.html` page correctly.

### Cause

The issue was mainly caused due to:

* Flask server configuration mistakes
* Incorrect route handling
* Missing Flask package installation
* Template rendering issues

### Solution

The problem was solved by:

* Correcting the Flask route structure
* Verifying the `render_template()` function
* Ensuring the `templates` folder structure was correct
* Installing Flask properly using:

```bash
pip install flask
```

After installing Flask and correcting the server-side code, the result page started rendering successfully.

---

## 2. ModuleNotFoundError: No module named 'flask'

### Problem

While running the server, the following error occurred:

```bash
ModuleNotFoundError: No module named 'flask'
```

### Cause

Flask was not installed in the system environment.

### Solution

The issue was resolved using:

```bash
pip install flask
```

This installed the Flask framework successfully and allowed the application server to run properly.

---

## 3. Git Merge Conflict Issue

### Problem

While pushing the project to GitHub, Git displayed merge conflict errors such as:

```bash
Your branch and 'origin/main' have diverged
You have unmerged paths
```

### Cause

The local repository and remote repository had different commits, causing conflicts during push operations.

### Solution

The issue was solved by:

* Identifying conflicting files
* Removing unnecessary conflict-generated folders/files
* Adding resolved files again
* Completing the merge manually

Commands used:

```bash
git add .
git commit -m "resolved merge conflict"
git push origin main
```

After resolving the conflicts, the project was successfully uploaded to GitHub.

---

# Git Commands Used in This Project

## Initialize Git Repository

```bash
git init
```

## Check Status

```bash
git status
```

## Add Files

```bash
git add .
```

## Commit Changes

```bash
git commit -m "message"
```

## Connect GitHub Repository

```bash
git remote add origin <repository-link>
```

## Push Code to GitHub

```bash
git push origin main
```

## Pull Changes

```bash
git pull origin main
```

---

# Learning Outcomes

Through this project, the following practical skills were improved:

* Flask backend integration
* HTML form handling
* Debugging server-side errors
* Understanding Git workflow
* Solving merge conflicts
* Using GitHub for version control
* Managing project structure professionally

This project also improved problem-solving ability and provided hands-on experience with real development challenges.

---

# Conclusion

The Trip Calculator project was a valuable learning experience that combined frontend development, backend logic, debugging, and GitHub workflow management. Several real-world issues were encountered during development, including Flask installation problems, server rendering issues, and Git merge conflicts. Each issue was resolved through debugging, command-line operations, and proper project management techniques.

This project helped strengthen both technical development skills and practical software engineering workflow understanding.
