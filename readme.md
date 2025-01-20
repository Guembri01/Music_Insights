
# Music Insights: A Data-Driven Music Analysis Application

## Description

**Music Insights** is a Flask-based web application designed to help music production companies and enthusiasts analyze music data to identify trends, popular genres, and features that maximize sales. The application leverages the [Spotify Tracks Dataset](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset) from Hugging Face to provide interactive visualizations and actionable insights.

### Key Features
- **Genre Popularity Analysis**: Identify the most popular music genres based on track popularity.
- **Feature Correlation**: Explore correlations between music features (e.g., danceability, energy) and popularity.
- **Interactive Dashboards**: Visualize data with dynamic and interactive Plotly charts.
- **Caching**: Improve performance with Flask-Caching for faster data retrieval.
- **Comprehensive Insights**: Gain insights into explicit content, track duration, tempo, and more.

---

## Installation

### Prerequisites
- Python 3.12 or higher
- Poetry (for dependency management)

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Guembri01/Music_Insights.git
   cd Music_Insights
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies using Poetry**:
   ```bash
   poetry install
   ```

5. **Run the application**:
   ```bash
   poetry run flask run
   ```

6. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000/`.

---

## Usage

### Home Page
- The home page provides an overview of the application and links to the dashboard.

### Dashboard
- The dashboard displays interactive visualizations, including:
  - Genre popularity.
  - Feature correlations (e.g., danceability vs. energy).
  - Track duration distribution by genre.
  - Explicit content analysis.
  - Popularity trends over time.

### Interacting with Visualizations
- Hover over charts to view detailed information.
- Use dropdowns or filters (if implemented) to customize the data displayed.

---

## Technical Choices

- **Flask**: A lightweight and flexible web framework for building the application.
- **Pandas**: For efficient data manipulation and analysis.
- **Plotly**: For creating interactive and dynamic visualizations.
- **Hugging Face `datasets`**: For easy access to the Spotify Tracks Dataset.
- **Flask-Caching**: To cache analysis results and improve performance.
- **pytest**: For writing and running unit tests.

---

## Deployment

### GitHub Pages
The documentation for this project is hosted on GitHub Pages:
```
https://guembri01.github.io/Music_Insights/
```

### Heroku
To deploy the Flask application to Heroku:
1. Install the Heroku CLI.
2. Create a Heroku app:
   ```bash
   heroku create
   ```
3. Push your code to Heroku:
   ```bash
   git push heroku main
   ```
4. Open your app:
   ```bash
   heroku open
   ```

### Hugging Face Spaces
You can also deploy the application to Hugging Face Spaces for sharing interactive demos.

---

## Screenshots

![Dashboard Screenshot](https://via.placeholder.com/800x400.png?text=Dashboard+Screenshot)  
*Example of the interactive dashboard.*

---

## Future Improvements

- **User Authentication**: Add login functionality for personalized dashboards.
- **Machine Learning**: Predict sales based on music features using machine learning models.
- **Custom Datasets**: Allow users to upload and analyze their own datasets.
- **Advanced Visualizations**: Add more interactive and customizable charts.
- **API Integration**: Integrate with Spotify's API for real-time data analysis.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing the Spotify Tracks Dataset.
- [Plotly](https://plotly.com/) for enabling interactive visualizations.
- [Flask](https://flask.palletsprojects.com/) for making web development simple and efficient.
```

---

### **Key Improvements**
1. **Clear Structure**: The README is divided into sections for easy navigation.
2. **Detailed Installation Instructions**: Step-by-step guide for setting up the project.
3. **Usage Examples**: Explains how to interact with the application.
4. **Technical Choices**: Highlights the tools and libraries used.
5. **Deployment Options**: Provides instructions for deploying to GitHub Pages, Heroku, and Hugging Face Spaces.
6. **Future Improvements**: Outlines potential enhancements for the project.
7. **Contributing Guide**: Encourages contributions with clear steps.
8. **License and Acknowledgments**: Adds professionalism and credits to third-party resources.

---

### **Next Steps**
1. Replace the placeholder screenshot with an actual screenshot of your dashboard.
2. Update the Hugging Face dataset link if necessary.
3. Add a link to your deployed application (if applicable).

Let me know if you need further assistance! 🚀
