# Code Time Complexity Analyzer

This Streamlit application analyzes the time complexity of code snippets using Google's Generative AI and displays the complexity along with a plot using matplotlib.
> **For Video Demo click [here](https://github.com/shoryasethia/TimeComplexityAnalyzer/blob/main/res/TimeComplexityAnalyzer.mp4)**
![Home Page](https://github.com/shoryasethia/TimeComplexityAnalyzer/blob/main/res/HomePg.png)



## Getting Started

To run this application locally, follow these steps:

### Installation and Set Up

1. Clone the repository:
   ```
   git clone https://github.com/shoryasethia/TimeComplexityAnalyzer.git
   cd TimeComplexityAnalyzer
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Edit `.env` file in the root directory with your Google API key:
   ```
   GOOGLE_API_KEY='your_google_api_key_here'
   ```
4. Running the Application:
   ```
   streamlit run TimeComplexityAnalyzer.py
   ```
## Usage
* Enter your code snippet in the provided text area.
* Click on the Analyze button to analyze the time complexity.
* The application will display the computed time complexity (e.g., O(n), O(n^2), etc.) and a corresponding plot.


### Owner [@shoryasethia](https://github.com/shoryasethia)
> If you liked the repo, do give it a star
