# 🔐 Face Authentication with Linux PAM

> A Linux-based face authentication project that integrates **face recognition with the Pluggable Authentication Modules (PAM)** framework.

This project explores how biometric face authentication can be connected to the Linux authentication system. It combines Python-based face detection and registration with a custom PAM module written in C.

## ✨ Features

* 👤 Face registration
* 🔍 Face detection
* 🔐 Face-based authentication
* 🐧 Linux PAM integration
* 🐍 Python-based face processing
* ⚙️ Custom PAM module written in C
* 🔗 Integration between Python face authentication and the Linux authentication framework

## 🛠️ Technologies Used

| Technology    | Purpose                                          |
| ------------- | ------------------------------------------------ |
| **Python**    | Face registration, detection, and authentication |
| **C**         | Custom PAM module                                |
| **Linux PAM** | Authentication framework integration             |
| **OpenCV**    | Face detection / image processing                |
| **GCC**       | Compiling the PAM module                         |

## 📂 Project Structure

```text
Face/
│
├── face_detect.py
├── register_face.py
├── authenticate_face_old.py
│
├── pam_3.c
├── pam_3.o
├── a.out
└── README.md
```

### File Description

**`face_detect.py`**
Handles face detection functionality.

**`register_face.py`**
Used for registering a user's face for authentication.

**`authenticate_face_old.py`**
Contains the face authentication logic.

**`pam_3.c`**
C implementation of the custom Linux PAM module.

**`pam_3.o`**
Compiled object file generated from the PAM module source.

**`a.out`**
Compiled executable output.

## 🔄 How It Works

The project follows a basic authentication workflow:

```text
        User
         │
         ▼
   Face Registration
         │
         ▼
    Face Detection
         │
         ▼
   Face Authentication
         │
         ▼
   Linux PAM Module
         │
         ▼
 Authentication Decision
```

The Python components handle the face-related processing, while the C-based PAM component connects the authentication process with the Linux operating system's authentication framework.

## 🎯 Project Objectives

The project was developed to understand how **biometric authentication can be integrated at the operating-system level**.

Key learning areas include:

* Linux authentication mechanisms
* PAM architecture
* C programming
* Python programming
* Face detection and recognition concepts
* Python–C integration
* System-level authentication
* Compiling and working with Linux modules

## 💻 Operating System Concepts

This project demonstrates practical concepts related to:

* **Authentication**
* **Security**
* **System-level programming**
* **Linux PAM**
* **User access control**
* **Biometric authentication**

## ⚠️ Note

This project is primarily an academic/learning implementation. It should be reviewed and secured appropriately before being used as a production authentication mechanism.

## 👨‍💻 Author

**Muhammad Arslan**

Bachelor of Computer Science
Lahore Garrison University, Pakistan

GitHub:
https://github.com/Muhammad-Arslan6621
