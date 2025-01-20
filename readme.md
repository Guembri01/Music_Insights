# Music Sales Analysis Application

## Description

This application analyzes music data to help a music production company identify the music styles that are most likely to maximize sales. It provides interactive visualizations and insights based on the [Spotify Tracks Dataset](link to hugging face) from Hugging Face (or optionally, data scraped from the web).

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd music_analysis_app
    ```

2. **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    ```

3. **Activate the virtual environment:**
    *   On Windows:
        ```bash
        venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Make sure your virtual environment is activated.
2. Run the following command in your terminal:
    ```bash
    python run.py
    ```
3. Open your web browser and go to `http://127.0.0.1:5000/`

## Technical Choices

*   **Flask:** Web framework for building the application.
*   **Pandas:** Data manipulation and analysis.
*   **Plotly:** Interactive data visualizations.
*   **Hugging Face `datasets` library:** Loading the Spotify Tracks Dataset.
*   **pytest:** Unit testing.

## Deployment

This application can be deployed to Hugging Face Spaces or other cloud platforms like Heroku, PythonAnywhere, etc.

## Screenshots

[Include a screenshot or a link to a video demo of your application here]

## Future Improvements

*   Add user authentication.
*   Implement more sophisticated data analysis techniques.
*   Use machine learning to predict sales based on music features.
*   Allow users to upload their own datasets.