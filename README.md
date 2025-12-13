# ⚙️ GitHub Actions Automation Workflows

## 👋 Overview
This repository contains a collection of **GitHub Actions workflows** created to
**automate common DevOps and engineering processes**.

These workflows were initially developed and tested **locally and in a sandbox GitHub account**,
and later **implemented in the actual production GitHub organization** after validation.

The focus is on **automation, reliability, and reducing manual effort**.

---

## 🎯 Purpose
- Automate post-deployment notifications
- Enable safe self-service operations for developers
- Enforce workflow discipline and issue hygiene
- Reuse standardized CI/CD logic across repositories
- Validate workflows safely before production rollout

---

### 🔧 Tech Stack
- **CI/CD:** GitHub Actions
- **Scripting:** Bash, JavaScript
- **Quality:** SonarQube
- **Cloud:** AWS (CloudFront)
- **Integrations:** Redmine, GitHub API

---

### 📌 Workflows Included

#### 🔔 Automated Redmine Notification
- Sends notifications after successful deployments
- Includes:
  - Pull Request name
  - Commit ID
  - Assignee name
  - Deployment status
- Improves visibility between development and project tracking tools

---

#### ☁️ CloudFront Invalidation Workflow
- Allows developers to **trigger CloudFront invalidation** via GitHub Actions
- Removes manual AWS Console access
- Provides controlled and auditable invalidation execution

---

#### 💬 Automated Issue Comment Workflow
- Automatically comments on GitHub issues
- Triggered when an issue is **not updated within a defined time window**
- Helps maintain issue hygiene and prevent stale tasks

---

#### ♻️ Reusable Workflows
- Centralized reusable workflows for:
  - Common CI steps
  - Deployment logic
  - Notifications
- Reduces duplication and enforces consistency across repositories

---

#### 🧪 SonarQube Test Workflow
- Runs static code analysis using SonarQube
- Fails the pipeline on quality gate violations
- Ensures code quality standards before merge

---

### 📁 Repository Structure
