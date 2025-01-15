# python-statlearning-lab

This repository is part of the topic: **"Investigación Avanzada II"**.  
Class times are from **7:00 PM to 8:30 PM** on specified dates.

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
8. [Steps to Create or Update Your Repository](#steps-to-create-or-update-your-repository)

---

## Course Description

This set of classes introduces participants to a range of topics in data science and analytics using Python, including:

- Basic Python programming  
- Web scraping (administrative, news, and social media sites)  
- Machine learning concepts (supervised and unsupervised)  
- Deep learning basics  
- Natural language processing (including topic modeling, labeling with BERT, and sentiment analysis)

Classes take place **from 7:00 PM to 8:30 PM** on scheduled dates, indicated below.

---

## Schedule

**Week 1 (January 17th, 2025)**  
- **Introduction to Python**  
  *7:00 PM – 8:30 PM*

**Week 2 (January 22nd, 2025)**  
- **Scraping Administrative and News Websites in Python**  
  *7:00 PM – 8:30 PM*

**Week 2 (January 24th, 2025)**  
- **Scraping Social Media Data in Python**  
  *7:00 PM – 8:30 PM*

**Week 4 (February 5th, 2025)**  
- **Machine Learning Lecture**  
  *7:00 PM – 8:30 PM*

**Week 4 (February 7th, 2025)**  
- **Deep Learning Lecture**  
  *7:00 PM – 8:30 PM*

**Week 8 (March 5th, 2025)**  
- **Natural Language Processing (NLP)**  
  *7:00 PM – 8:30 PM*  
  *Covers supervised/unsupervised ML, topic modeling, labeling with BERT, and sentiment analysis.*

**Week 8 (March 7th, 2025)**  
- **Continuation of the NLP Lecture**  
  *7:00 PM – 8:30 PM*

---

## Topics Covered

1. **Python Basics**  
   - Installation and environment setup  
   - Data types, control structures, functions  

2. **Web Scraping**  
   - Libraries and tools for requests and parsing (e.g., `requests`, `BeautifulSoup`, `Selenium`)  
   - Techniques for scraping administrative, news, and social media websites  

3. **Machine Learning**  
   - Overview of supervised learning (classification, regression)  
   - Overview of unsupervised learning (clustering, dimensionality reduction)  

4. **Deep Learning**  
   - Introduction to neural networks and frameworks (e.g., TensorFlow, PyTorch)  
   - Basic building blocks of deep models  

5. **Natural Language Processing (NLP)**  
   - Topic modeling, labeling with BERT, sentiment analysis  
   - Supervised vs. unsupervised approaches  

---

## Repository Structure

python-statlearning-lab/ ├── README.md # This file ├── week1/ │ ├── introduction_to_python.ipynb │ └── ... ├── week2/ │ ├── scraping_administrative_news.ipynb │ ├── scraping_social_media.ipynb │ └── ... ├── week4/ │ ├── machine_learning_lecture.ipynb │ ├── deep_learning_lecture.ipynb │ └── ... └── week8/ ├── nlp_lecture_part1.ipynb ├── nlp_lecture_part2.ipynb └── ...


- Each **`weekX/`** folder contains Jupyter notebooks and resources for the respective sessions (e.g., Week 1, Week 2, Week 4, Week 8).  
- Organize your lecture materials, data, or additional scripts accordingly.

---

## Getting Started

1. **Clone or Download this Repository**  
   - Click the green “Code” button on this GitHub page.  
   - Copy the HTTPS or SSH link and run `git clone <URL>` in your terminal, or choose **“Download ZIP”** to get a compressed version.

2. **Install Python & Libraries**  
   - Refer to the [Appendix: Installation Guide](#appendix-installation-guide) below for a detailed overview.  
   - Using **Anaconda** or **Miniconda** is recommended for an easy setup.

3. **Open the Notebooks**  
   - In a terminal or Anaconda Prompt, navigate to the repository folder and run:  
     ```bash
     jupyter lab
     ```  
     or  
     ```bash
     jupyter notebook
     ```
   - Alternatively, open the `.ipynb` files in **Visual Studio Code** with the Python and Jupyter extensions installed.

4. **Follow Along in Class**  
   - Each folder (e.g., `week1`, `week2`, `week4`, `week8`) corresponds to a specific series of lectures.  
   - Run the cells in each notebook, read the explanations, and work on the provided exercises.

---

## Contact

- **Instructor**: José Luis  
- **Email**: [Your Instructor’s Email Here]  

If you have any questions or issues, feel free to **open a GitHub issue** or email the instructor.

---

## Appendix: Installation Guide

Below is a concise overview of how to set up your environment for these classes.

### 1. Installing Python 3

- **Anaconda (Recommended)**  
  - Visit [https://www.anaconda.com/](https://www.anaconda.com/) and download the **Anaconda** distribution for your operating system (Windows, macOS, or Linux).  
  - This includes Python 3, Jupyter, and many data science libraries by default.  
  - On Windows, consider checking “Add Anaconda to my PATH” during installation if prompted.

- **Miniconda (Lightweight Alternative)**  
  - If you prefer a minimal environment, get **Miniconda** from [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html).  
  - You can then install only the packages you need for this course.

### 2. Verifying Your Installation

After installing Anaconda or Miniconda, open a terminal (macOS/Linux) or Anaconda Prompt (Windows) and run:

```bash
conda --version
python --version
