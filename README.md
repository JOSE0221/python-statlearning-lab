# python-statlearning-lab

This repository is part of the topic: **"Investigación Avanzada II"**.  
Class times are from **7:00 AM to 8:30 AM** on specified dates.

---

# Python Data Collection, Machine Learning, and NLP (2025)

Welcome to the **Python Data Collection, Machine Learning, and NLP** repository! This collection of materials is designed to help you follow along with a series of hands-on classes.

## Table of Contents

1. [Course Description](#course-description)  
2. [Schedule](#schedule)  
3. [Topics Covered](#topics-covered)  
4. [Repository Structure](#repository-structure)  
5. [Getting Started](#getting-started)  
6. [Contact](#contact)  
7. [Appendix: Installation Guide](#appendix-installation-guide)  

---

## Course Description

This set of classes introduces participants to a range of topics in data science and analytics using Python, including:

- Basic Python programming  
- Web scraping (administrative, news, and social media sites)  
- Machine learning concepts (supervised and unsupervised)  
- Deep learning basics  
- Natural language processing (including topic modeling, labeling with BERT, and sentiment analysis)

Classes take place **from 7:00 AM to 8:30 AM** on scheduled dates, indicated below.

---

## Schedule

**Week 1 (January 17th, 2025)**  
- **Introduction to Python**  
  *7:00 AM – 8:30 AM*

**Week 2 (January 22nd, 2025)**  
- **Scraping Administrative and News Websites in Python**  
  *7:00 AM – 8:30 AM*

**Week 2 (January 24th, 2025)**  
- **Scraping Social Media Data in Python**  
  *7:00 AM – 8:30 AM*

**Week 4 (February 5th, 2025)**  
- **Machine Learning Lecture**  
  *7:00 AM – 8:30 AM*

**Week 4 (February 7th, 2025)**  
- **Deep Learning Lecture**  
  *7:00 AM – 8:30 AM*

**Week 8 (March 5th, 2025)**  
- **Natural Language Processing (NLP)**  
  *7:00 AM – 8:30 AM*  
  *Covers supervised/unsupervised ML, topic modeling, labeling with BERT, and sentiment analysis.*

**Week 8 (March 7th, 2025)**  
- **Continuation of the NLP Lecture**  
  *7:00 AM – 8:30 AM*

---

## Topics Covered

1. **Python Basics**  
   - Installation and environment setup  
   - Data types, control structures, functions  

2. **Web Scraping**  
   - Libraries and tools for requests and parsing (e.g., `requests`, `BeautifulSoup`, `Selenium`)  
   - Techniques for scraping administrative, news, and social media websites  

3. **Machine Learning**  
   - Overview of supervised learning (classification & regression)  
   - Overview of unsupervised learning (clustering, dimensionality reduction)  

4. **Deep Learning**  
   - Introduction to deep learning
   - Basic building blocks of deep models  

5. **Natural Language Processing (NLP)**  
   - Topic modeling, labeling with BERT, sentiment analysis  
   - Supervised vs. unsupervised approaches  

---

## Repository Structure

- Each **`weekX/`** folder contains Jupyter notebooks and resources for the respective sessions (e.g., Week 1, Week 2, Week 4, Week 8).  

---

## Getting Started

1. **Install Python & Libraries**  
   - Refer to the [Appendix: Installation Guide](#appendix-installation-guide) below for a detailed overview.  
   - Using **Jupyter**, **Miniconda**, **Google Colab**, or **Visual Studio Code** is recommended for an easy setup.

---

## Contact

- **Instructor**: José Luis  
- **Email**: jose.perez.castellanos@itam.mx

If you have any questions or issues, feel free to **open a GitHub issue** or email the instructor.

---

## Appendix: Installation Guide

### 1. Installing Python

To run the materials in this repository, you need Python 3.#. You can set up Python using one of the following methods:

- **Miniconda**: Miniconda provides an isolated Python environment and an easy way to manage packages. Download it from [Miniconda's official website](https://docs.conda.io/en/latest/miniconda.html).  
- **Python.org**: Download and install the latest version of Python from [python.org](https://www.python.org/downloads/). Ensure that you check the option to add Python to your PATH during installation.

---

### 2. Setting up interface that runs code through a file called a notebook.

You can choose one of the following environments to work with the Notebooks files:

#### **Option A: Google Colab (Recommended)**

Google Colab is a cloud-based tool that requires no local installation. It's particularly useful if you want to avoid setting up Python on your system.

1. **Visit Google Colab**  
   - Go to [Google Colab](https://colab.research.google.com/).  

2. **Upload Notebook Files**  
   - Upload `.ipynb` files from this repository by clicking on the "File" menu and selecting "Upload notebook."

3. **Install Required Libraries**  
   - Use the following code snippet in a Colab cell to install any dependencies:  
     ```python
     !pip install -r requirements.txt
     ```

4. **Run Notebooks**  
   - Colab provides a ready-to-use Jupyter interface in your browser.

---

#### **Option B: Visual Studio Code (Recommended)**

Visual Studio Code (VS Code) is a versatile code editor that supports Jupyter Notebooks through extensions.

1. **Install VS Code**  
   - Download and install Visual Studio Code from [code.visualstudio.com](https://code.visualstudio.com/).

2. **Install the Python Extension**  
   - Open VS Code and go to the Extensions view (`Ctrl+Shift+X` or `Cmd+Shift+X` on macOS).  
   - Search for "Python" and install the extension provided by Microsoft.

3. **Set Up Your Python Environment**  
   - Use the terminal in VS Code to activate your Miniconda environment:  
     ```bash
     conda activate statlearn
     ```

4. **Open a Notebook**  
   - Open the repository folder in VS Code.  
   - Open a `.ipynb` file; the Python extension will automatically enable Jupyter support.

5. **Install Required Libraries**  
   - Ensure all dependencies are installed using:  
     ```bash
     pip install -r requirements.txt
     ```

#### **Option C: Miniconda**

1. **Install Miniconda**  
   - Download Miniconda for your operating system from [Miniconda's official website](https://docs.conda.io/en/latest/miniconda.html).  
   - Follow the installation steps, ensuring that Miniconda is added to your system's PATH during setup.

2. **Create a New Environment**  
   - Open your terminal (Command Prompt, PowerShell, or Terminal).  
   - Create a new environment:  
     ```bash
     conda create --name statlearn python=3.9
     ```
   - Activate the environment:  
     ```bash
     conda activate statlearn
     ```

3. **Install JupyterLab and Dependencies**  
   - Install JupyterLab:  
     ```bash
     conda install -c conda-forge jupyterlab
     ```
   - Install additional libraries:  
     ```bash
     pip install -r requirements.txt
     ```

4. **Launch JupyterLab**  
   - Run the following command to start JupyterLab:  
     ```bash
     jupyter lab
     ```
   - Open the URL displayed in your terminal to access the Jupyter interface in your browser.

---
---

With these options, you can choose the setup that best suits your workflow and preferences. For troubleshooting or additional support, refer to the [Jupyter Documentation](https://jupyter.org/documentation).
