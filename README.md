# Automated ML CI/CD Pipeline with Kubeflow on Kubernetes

## 📌 Project Overview
This project demonstrates the design and implementation of an **automated Machine Learning CI/CD pipeline** using **Kubeflow Pipelines** concepts, containerization, and CI/CD automation.

The pipeline is designed to be Kubernetes-compatible and follows industry practices for automating ML workflows such as preprocessing, training, evaluation, and deployment.

---

## 🛠 Technologies Used
- :contentReference[oaicite:0]{index=0} Pipelines (SDK v2)
- :contentReference[oaicite:1]{index=1} (conceptual execution environment)
- :contentReference[oaicite:2]{index=2}
- :contentReference[oaicite:3]{index=3}
- Python

---

## ⚙️ Pipeline Workflow
The automated ML pipeline consists of the following stages:

1. **Data Preprocessing**
2. **Model Training**
3. **Model Evaluation**
4. **Deployment Readiness**

Each stage is implemented as an independent pipeline component, enabling modular execution and scalability on Kubernetes clusters.

---

## 📂 Project Structure
automated-ml-cicd/
│
├── pipeline/
│ └── pipeline.py # Kubeflow pipeline definition
│
├── src/
│ ├── preprocess.py # Data preprocessing logic
│ ├── train.py # Model training logic
│ └── evaluate.py # Model evaluation logic
│
├── Dockerfile # Container definition
├── requirements.txt # Python dependencies
│
└── .github/
└── workflows/
└── ci-cd.yaml # GitHub Actions CI/CD workflow


---

## 🔁 CI/CD Automation
- The pipeline is automatically compiled whenever code is pushed to the GitHub repository.
- **GitHub Actions** handles:
  - Dependency installation
  - Kubeflow pipeline compilation
  - Validation of pipeline structure

This simulates real-world ML CI/CD automation.

---

## 📦 Deliverables
- Kubeflow pipeline Python definition
- Compiled pipeline YAML (`pipeline.yaml`)
- Dockerfile for containerized execution
- GitHub Actions workflow for CI/CD
- Modular ML scripts
- Documentation

---

## 🚀 Deployment Note
The generated pipeline YAML is compatible with **Kubeflow Pipelines deployed on Kubernetes clusters** such as Minikube or managed cloud services (EKS/GKE/AKS).

---

## ✅ Conclusion
This project demonstrates a complete ML CI/CD workflow aligned with industry practices, enabling automated, scalable, and reproducible machine learning pipelines using Kubeflow and Kubernetes.
