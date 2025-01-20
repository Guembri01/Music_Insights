Music Insights Modules
======================

This section provides detailed documentation for the modules and functions in the Music Insights project.

.. automodule:: app
   :members:
   :undoc-members:
   :show-inheritance:

   The `app` module is the main entry point for the Flask application. It initializes the Flask app, sets up caching, and registers the blueprints.

.. automodule:: app.models
   :members:
   :undoc-members:
   :show-inheritance:

   The `app.models` module contains functions for loading and analyzing the Spotify Tracks dataset. Below is a detailed description of each function.

   .. autofunction:: load_data
      :noindex:

      Loads the Spotify Tracks dataset from a local file or downloads it from Hugging Face if it doesn't exist locally.

      :param local_path: Path to the local dataset file (default: "data/spotify_tracks_dataset.csv").
      :return: A pandas DataFrame containing the dataset.

   .. autofunction:: analyze_genre_popularity
      :noindex:

      Analyzes the popularity of different music genres.

      :param df: The DataFrame containing the dataset.
      :return: A Plotly figure (as JSON) and an interpretation string.

   .. autofunction:: analyze_music_features_by_genre
      :noindex:

      Analyzes the distribution of a specific music feature across different genres.

      :param df: The DataFrame containing the dataset.
      :param feature: The music feature to analyze (e.g., 'danceability', 'energy', 'tempo').
      :return: A Plotly figure (as JSON) and an interpretation string.

   .. autofunction:: analyze_sales_correlations
      :noindex:

      Analyzes correlations between music features and popularity.

      :param df: The DataFrame containing the dataset.
      :return: A Plotly figure (as JSON) and an interpretation string.

   .. autofunction:: analyze_explicit_content
      :noindex:

      Analyzes the proportion of explicit tracks in each genre.

      :param df: The DataFrame containing the dataset.
      :return: A Plotly figure (as JSON) and an interpretation string.

   .. autofunction:: analyze_duration_by_genre
      :noindex:

      Analyzes the distribution of track durations across different genres.

      :param df: The DataFrame containing the dataset.
      :return: A Plotly figure (as JSON) and an interpretation string.

   .. autofunction:: analyze_feature_correlation_heatmap
      :noindex:

      Generates a heatmap to visualize the correlations between different musical features.

      :param df: The DataFrame containing the dataset.
      :return: A Plotly figure (as JSON) and an interpretation string.

   .. autofunction:: analyze_tempo_by_genre
      :noindex:

      Analyzes the distribution of tempo across different genres.

      :param df: The DataFrame containing the dataset.
      :return: A Plotly figure (as JSON) and an interpretation string.

   .. autofunction:: analyze_energy_vs_danceability
      :noindex:

      Analyzes the relationship between energy and danceability across different genres.

      :param df: The DataFrame containing the dataset.
      :return: A Plotly figure (as JSON) and an interpretation string.

   .. autofunction:: analyze_popularity_over_time
      :noindex:

      Analyzes the trend of track popularity over time.

      :param df: The DataFrame containing the dataset.
      :return: A Plotly figure (as JSON) and an interpretation string.

   .. autofunction:: analyze_top_artists_by_popularity
      :noindex:

      Analyzes the top artists by average track popularity.

      :param df: The DataFrame containing the dataset.
      :return: A Plotly figure (as JSON) and an interpretation string.

   .. autofunction:: analyze_valence_vs_popularity
      :noindex:

      Analyzes the relationship between valence and track popularity.

      :param df: The DataFrame containing the dataset.
      :return: A Plotly figure (as JSON) and an interpretation string.

   .. autofunction:: analyze_top_popular_tracks
      :noindex:

      Analyzes the top 10 most popular tracks.

      :param df: The DataFrame containing the dataset.
      :return: A Plotly figure (as JSON) and an interpretation string.

   .. autofunction:: analyze_energy_by_genre
      :noindex:

      Analyzes the distribution of energy across genres.

      :param df: The DataFrame containing the dataset.
      :return: A Plotly figure (as JSON) and an interpretation string.

   .. autofunction:: analyze_loudness_vs_energy
      :noindex:

      Analyzes the relationship between loudness and energy.

      :param df: The DataFrame containing the dataset.
      :return: A Plotly figure (as JSON) and an interpretation string.

   .. autofunction:: analyze_acousticness_distribution
      :noindex:

      Analyzes the distribution of acousticness.

      :param df: The DataFrame containing the dataset.
      :return: A Plotly figure (as JSON) and an interpretation string.

.. automodule:: app.routes
   :members:
   :undoc-members:
   :show-inheritance:

   The `app.routes` module defines the Flask routes for the application. Below is a detailed description of each route.

   .. autofunction:: index
      :noindex:

      Renders the index page.

      :return: The rendered index.html template.

   .. autofunction:: dashboard
      :noindex:

      Renders the dashboard page with various music insights.

      :return: The rendered dashboard.html template with data visualizations.