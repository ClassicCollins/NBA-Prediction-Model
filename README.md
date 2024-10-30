# NBA-Prediction-Model
Predicting the teams that will qualify and win the 2022-2023 NBA
<!-- Improved compatibility of back to top link: See: https://github.com/ClassicCollins/NBA-Prediction-Model/back2top -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out NBA-Prediction-Model project. 
*** Thanks for checking out my project!
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for stars-url, forks-url, etc.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links 
-->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]
[![Python][Python-logo]][Python-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Twitter][twitter-shield]][twitter-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ClassicCollins/NBA-Prediction-Model/blob/classic/image/screenshot.png">
    <img src="image/screenshot.png" alt="Logo" width="60" height="40">
  </a>

<h3 align="center">NBA Prediction Model</h3>

  <p align="center">
    A project designed to spark your interest NBA Games Prediction using Python.!
    <br />
    <a href="https://github.com/ClassicCollins/NBA-Prediction-Model"><strong>Explore the Docs(Trained Model, Notebook etc) »</strong></a>
    <br />
    <br />
    <a href="https://nba-game-predictor.streamlit.app/">Predict with App</a>
    ·
    <a href="https://github.com/ClassicCollins/NBA-Prediction-Model/blob/classic/.github/ISSUE_TEMPLATE/bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/ClassicCollins/NBA-Prediction-Model/blob/classic/.github/ISSUE_TEMPLATE/feature-request-form---.md">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>View Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#project-Goal">Project Goal</a></li>
        <li><a href="#tools-and-libraries">Tools and Libraries</a></li>
        <li><a href="#steps-and-method">Steps and Method</a></li>
        <li><a href="#results">Results</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#Required-Packages">Required Packages</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://zindi.africa/)

* `Welcome` This repository contains the code and resources for predicting the teams that will qualify for the 2022-2023 NBA Playoffs from both East and West conferences, as well as the eventual winners of each conference and the NBA finals.
* `Introduction:` This project utilizes machine learning models to predict NBA game outcomes and playoff qualifications. The models are trained using historical NBA data, including ELO and RAPTOR ratings, and predict game outcomes based on these features. The predictions are then used to determine the teams that will qualify for the playoffs and the eventual winners of the conference finals and NBA finals.

### Project Goal
`The goal` is to predict if a team will win or lose. Sounds interesting right? :smile:
**[Predict with APP](https://nba-game-predictor.streamlit.app/)**
<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Tools and Libraries

* [![Python][Python-logo]][Python-url]
* [![Pandas][Pandas-logo]][Pandas-url]
* [![NumPy][NumPy-logo]][NumPy-url]
* [![Matplotlib][Matplotlib-logo]][Matplotlib-url]
* [![Seaborn][Seaborn-logo]][Seaborn-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- STEPS and METHODOLOGY -->
## Steps and Method
* `The dataset` The data used in this project includes:

- nba_elo.csv: Historical ELO ratings of NBA teams.

- nba_elo_latest.csv: Latest ELO ratings data.

- modern_raptors_team.csv: RAPTOR ratings data for NBA teams.
  
* `Data cleaning, preprocessing, and validation` were performed to ensure there were no duplicates or missing values, and that the data was in the correct format.
* `Exploratory Data Analysis` was conducted on the dataset to visualize it and identify patterns, trends, correlations, and outliers
* `The model` was built using several machine learning algorithms, including Logistic Regression, Gradient Boosting Classifier, and Random Forest Classifier
* `The tarining` The models are trained on historical data from the 2019-2022 seasons and are used to predict outcomes for the 2023 season.
* `Feature engineering and hyperparameter tuning` were performed to optimize the model’s performance.
* `Evaluation` The model was evaluated using accuracy metric, however, other metrics like precision, recall, and F1-score were used to evaluate the model. 
* `Cross-validation` was also used to ensure the model’s robustness and generalizability.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- RESULTS -->
## Results
* Logistic Regression demonstrated superior accuracy compared to other models.
* Results were generated and stored in the [results folder](https://github.com/ClassicCollins/NBA-Prediction-Model/tree/classic/results)
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Install Required Packages

Ensure you have Python installed and then run:
* requirement
  ```sh
  pip install -r requirements.txt
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ClassicCollins/NBA-Prediction-Model.git
   ```
   ```sh
   cd NBA-Prediction-Model
   ```
2. Install required packages
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Notebook: Open the notebook in Jupyter and run the cells to reproduce the analysis:
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENCE -->
## License
* This project is licensed under the MIT License. See the [LICENSE](https://github.com/ClassicCollins/NBA-Prediction-Model/blob/master/LICENSE) file for details
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Collins Emezie Ugwuozor - [@ClassicCollins2](https://x.com/ClassicCollins2) - ugwuozorcollinsemezie@gmail.com

Project Link: [NBA-Prediction-Model](https://nba-game-predictor.streamlit.app/)

Don't forget to give the project a star! Thanks again!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Python](https://www.python.org)
* [Img Shields](https://shields.io)
* [Streamlit](https://nba-game-predictor.streamlit.app/)
* [MIT License](https://opensource.org/license/mit)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ClassicCollins/NBA-Prediction-Model.svg?style=for-the-badge
[contributors-url]: https://github.com/ClassicCollins/NBA-Prediction-Model/contributors
[twitter-shield]: https://img.shields.io/badge/-Twitter-black.svg?style=for-the-badge&logo=x&colorB=555
[twitter-url]: https://x.com/ClassicCollins2
[traffic-shield]: https://img.shields.io/github/traffic/ClassicCollins/NBA-Prediction-Model.svg?style=for-the-badge
[traffic-url]: https://github.com/ClassicCollins/NBA-Prediction-Model/traffic
[forks-shield]: https://img.shields.io/github/forks/ClassicCollins/NBA-Prediction-Model.svg?style=for-the-badge
[forks-url]: https://github.com/ClassicCollins/NBA-Prediction-Model/forks
[stars-shield]: https://img.shields.io/github/stars/ClassicCollins/NBA-Prediction-Model.svg?style=for-the-badge
[stars-url]: https://github.com/ClassicCollins/NBA-Prediction-Model/stargazers
[issues-shield]: https://img.shields.io/github/issues/ClassicCollins/NBA-Prediction-Model.svg?style=for-the-badge
[issues-url]: https://github.com/ClassicCollins/NBA-Prediction-Model/issues
[license-shield]: https://img.shields.io/github/license/ClassicCollins/NBA-Prediction-Model.svg?style=for-the-badge
[license-url]: https://github.com/ClassicCollins/NBA-Prediction-Model/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-white.svg?style=for-the-badge&logo=linkedin&colorB=blue
[linkedin-url]: https://linkedin.com/in/collins-ugwuozor
[product-screenshot]: image/screenshot1.png
[Python-logo]: https://img.shields.io/badge/Python-20232A?style=for-the-badge&logo=python&logoColor=61DAFB
[Python-url]: https://www.python.org/
[Pandas-logo]: https://img.shields.io/badge/Pandas-20232A?style=for-the-badge&logo=pandas&logoColor=blue
[Pandas-url]: https://pandas.pydata.org/
[NumPy-logo]: https://img.shields.io/badge/Numppy-20232A?style=for-the-badge&logo=numpy&logoColor=61DAFB
[NumPy-url]: https://numpy.org/
[Matplotlib-logo]: https://img.shields.io/badge/Matplotlib-red?style=for-the-badge&logo=matplotlib&logoColor=0769AD
[Matplotlib-url]: https://matplotlib.org/ 
[Seaborn-logo]: https://img.shields.io/badge/Seaborn-20232A?style=for-the-badge&logo=seaborn&logoColor=61DAFB
[Seaborn-url]: https://seaborn.pydata.org/
