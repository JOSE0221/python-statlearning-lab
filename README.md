# Python Data Collection, Machine Learning, and NLP

**Applied Research II (ECO-40212) — Spring 2026**

This repository contains materials for the Python and data science sessions of the Applied Research II course at ITAM. The sessions cover practical skills for empirical research, including web scraping, machine learning, and natural language processing.

---

## Course Information

| | |
|---|---|
| **Instructor** | Horacio Larreguy ([horacio.larreguy@itam.mx](mailto:horacio.larreguy@itam.mx)) |
| **Teaching Assistant** | José Luis Pérez Castellanos ([jose.perez.castellanos@itam.mx](mailto:jose.perez.castellanos@itam.mx)) |
| **Schedule** | Wednesdays, 7:00–10:00 AM |
| **Room** | RH 111 |
| **Canvas** | [itam.instructure.com/courses/17289](https://itam.instructure.com/courses/17289) |

---

## TA Session Schedule

All TA-led sessions run during the first half of class (7:00–8:30 AM) unless otherwise noted.

| Week | Date | Topic | Materials |
|:----:|:----:|:------|:---------:|
| 2 | Jan 21, 2026 | Introduction to Python | [`week02/`](week02/) |
| 3 | Jan 28, 2026 | Web Scraping: Administrative, News & Social Media | [`week03/`](week03/) |
| 8 | Mar 4, 2026 | Machine Learning & Deep Learning | [`week08/`](week08/) |
| 11 | Mar 25, 2026 | Natural Language Processing | [`week11/`](week11/) |
| 13 | Apr 8, 2026 | Office Hours: Coding Issues | — |

---

## Topics Covered

### Week 2: Introduction to Python
- Python installation and environment setup (Miniconda, VS Code, Google Colab)
- Data types, control structures, and functions
- Working with Jupyter notebooks
- Essential libraries: `numpy`, `pandas`

### Week 3: Web Scraping
- HTTP requests and HTML parsing with `requests` and `BeautifulSoup`
- Dynamic content with `Selenium`
- Scraping administrative and government data sources
- Extracting data from news websites
- Social media data collection (ethical considerations and API usage)

### Week 8: Machine Learning & Deep Learning
- Supervised learning: classification and regression
- Unsupervised learning: clustering and dimensionality reduction
- Model evaluation and cross-validation
- Introduction to neural networks and deep learning fundamentals
- Libraries: `scikit-learn`, `tensorflow`/`pytorch`

### Week 11: Natural Language Processing
- Text preprocessing and tokenization
- Topic modeling (LDA, structural topic models)
- Text classification with BERT and transformer models
- Sentiment analysis
- Applications to political science research

---

## Repository Structure

```
python-statlearning-lab/
├── week02/          # Python fundamentals
├── week03/          # Web scraping
├── week08/          # Machine learning & deep learning
├── week11/          # Natural language processing
├── data/            # Sample datasets
├── requirements.txt # Python dependencies
└── README.md
```

Each week folder contains:
- Jupyter notebooks (`.ipynb`) with code and explanations
- Practice exercises
- Supplementary resources

---

## Getting Started

### Option A: Google Colab (Recommended for beginners)

Google Colab requires no local installation and provides free GPU access.

1. Go to [colab.research.google.com](https://colab.research.google.com/)
2. Upload notebooks from this repository via **File → Upload notebook**
3. Install dependencies in a cell:
   ```python
   !pip install -r requirements.txt
   ```

### Option B: Local Setup with VS Code

1. **Install Python** via [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
2. **Create environment:**
   ```bash
   conda create --name statlearn python=3.11
   conda activate statlearn
   ```
3. **Install VS Code** from [code.visualstudio.com](https://code.visualstudio.com/)
4. **Install the Python extension** in VS Code (search "Python" in Extensions)
5. **Clone and open this repository:**
   ```bash
   git clone https://github.com/[your-username]/python-statlearning-lab.git
   cd python-statlearning-lab
   pip install -r requirements.txt
   ```
6. Open any `.ipynb` file — VS Code will enable Jupyter support automatically

### Option C: JupyterLab

1. Follow steps 1–2 from Option B
2. Install and launch JupyterLab:
   ```bash
   conda install -c conda-forge jupyterlab
   pip install -r requirements.txt
   jupyter lab
   ```

---

## Assignments

After each TA session, optional homework assignments are available for bonus points. Assignments help solidify the material and are submitted via Canvas.

| Session | Assignment | Due Date |
|---------|------------|----------|
| Week 2 | Python basics exercises | Jan 27, 2026 |
| Week 3 | Web scraping project | Feb 3, 2026 |
| Week 8 | ML classification task | Mar 10, 2026 |
| Week 11 | NLP analysis | Mar 31, 2026 |

---

## Resources

### Documentation
- [Python Documentation](https://docs.python.org/3/)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/user_guide.html)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)

### Books
- McKinney, W. *Python for Data Analysis* (3rd ed.)
- James et al. *An Introduction to Statistical Learning* (Python edition)

### Course Materials
- [Overleaf Thesis Template](https://www.overleaf.com/latex/templates/itam-thesis-template-2-dot-0/dmcdzfyqqfpg)
- [Prof. Larreguy's Supervised Theses](https://sites.google.com/site/hlarreguy/supervised-theses)

---

## Contact

For questions about TA sessions or technical issues:
- **Email:** [jose.perez.castellanos@itam.mx](mailto:jose.perez.castellanos@itam.mx)
- **GitHub Issues:** Open an issue in this repository

For questions about the course, research design, or thesis:
- **Email:** [horacio.larreguy@itam.mx](mailto:horacio.larreguy@itam.mx)

---

## License

Materials in this repository are for educational use within the Applied Research II course at ITAM.
