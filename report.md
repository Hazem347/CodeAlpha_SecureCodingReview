# Secure Coding Review Report

## Introduction
This project analyzes a vulnerable web application and identifies security issues. The vulnerabilities are then fixed using secure coding practices.

---

## Vulnerabilities Identified

### 1. Plain Text Password Storage
Passwords were stored in plain text, making them vulnerable to exposure.

### 2. Lack of Input Validation
User inputs were not validated, allowing potential injection attacks.

### 3. Debug Mode Enabled
Debug mode exposes sensitive system information.

---

## Fixes Implemented

### 1. Password Hashing
Used werkzeug.security to hash passwords securely.

### 2. Input Validation
Limited input size and checked for invalid inputs.

### 3. Disabled Debug Mode
Turned off debug mode for production safety.

---

## Conclusion
Secure coding practices are essential to protect applications from attacks. This project demonstrates how simple vulnerabilities can be fixed effectively.