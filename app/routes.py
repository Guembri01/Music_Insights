from flask import Blueprint, render_template, request, redirect, url_for
from .models import (load_data, analyze_genre_popularity, 
                     analyze_music_features_by_genre, analyze_sales_correlations, 
                     analyze_explicit_content, analyze_duration_by_genre, 
                     analyze_feature_correlation_heatmap, analyze_tempo_by_genre,
                     analyze_energy_vs_danceability, analyze_popularity_over_time,
                     analyze_top_artists_by_popularity, analyze_valence_vs_popularity,
                     analyze_top_popular_tracks, analyze_energy_by_genre,
                     analyze_loudness_vs_energy, analyze_acousticness_distribution)

main = Blueprint('main', __name__)

# Load the dataset once when the application starts
df = load_data()

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
def dashboard():
    # Data analysis functions (using precomputed data where possible)
    genre_pop_json, genre_pop_interpretation = analyze_genre_popularity(df)
    danceability_json, danceability_interpretation = analyze_music_features_by_genre(df, 'danceability')
    correlation_json, correlation_interpretation = analyze_sales_correlations(df)
    explicit_json, explicit_interpretation = analyze_explicit_content(df)
    duration_json, duration_interpretation = analyze_duration_by_genre(df)
    heatmap_json, heatmap_interpretation = analyze_feature_correlation_heatmap(df)
    tempo_json, tempo_interpretation = analyze_tempo_by_genre(df)
    energy_danceability_json, energy_danceability_interpretation = analyze_energy_vs_danceability(df)
    popularity_time_json, popularity_time_interpretation = analyze_popularity_over_time(df)
    top_artists_json, top_artists_interpretation = analyze_top_artists_by_popularity(df)
    valence_popularity_json, valence_popularity_interpretation = analyze_valence_vs_popularity(df)
    top_popular_tracks_json, top_popular_tracks_interpretation = analyze_top_popular_tracks(df)
    energy_by_genre_json, energy_by_genre_interpretation = analyze_energy_by_genre(df)
    loudness_vs_energy_json, loudness_vs_energy_interpretation = analyze_loudness_vs_energy(df)
    acousticness_distribution_json, acousticness_distribution_interpretation = analyze_acousticness_distribution(df)

    return render_template('dashboard.html',
                           genre_popularity=genre_pop_json,
                           genre_pop_interpretation=genre_pop_interpretation,
                           danceability=danceability_json,
                           danceability_interpretation=danceability_interpretation,
                           sales_correlations=correlation_json,
                           sales_correlations_interpretation=correlation_interpretation,
                           explicit=explicit_json,
                           explicit_interpretation=explicit_interpretation,
                           duration=duration_json,
                           duration_interpretation=duration_interpretation,
                           heatmap=heatmap_json,
                           heatmap_interpretation=heatmap_interpretation,
                           tempo=tempo_json,
                           tempo_interpretation=tempo_interpretation,
                           energy_danceability=energy_danceability_json,
                           energy_danceability_interpretation=energy_danceability_interpretation,
                           popularity_time=popularity_time_json,
                           popularity_time_interpretation=popularity_time_interpretation,
                           top_artists=top_artists_json,
                           top_artists_interpretation=top_artists_interpretation,
                           valence_popularity=valence_popularity_json,
                           valence_popularity_interpretation=valence_popularity_interpretation,
                           top_popular_tracks=top_popular_tracks_json,
                           top_popular_tracks_interpretation=top_popular_tracks_interpretation,
                           energy_by_genre=energy_by_genre_json,
                           energy_by_genre_interpretation=energy_by_genre_interpretation,
                           loudness_vs_energy=loudness_vs_energy_json,
                           loudness_vs_energy_interpretation=loudness_vs_energy_interpretation,
                           acousticness_distribution=acousticness_distribution_json,
                           acousticness_distribution_interpretation=acousticness_distribution_interpretation)