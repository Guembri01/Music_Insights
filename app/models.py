import pandas as pd
from datasets import load_dataset
import plotly.express as px
import plotly.graph_objects as go
import os
from . import cache

def load_data(local_path="data/spotify_tracks_dataset.csv"):
    """
    Loads the Spotify Tracks dataset.
    Downloads the dataset from Hugging Face if it doesn't exist locally.
    """
    if not os.path.exists(local_path):
        print("Dataset not found locally. Downloading from Hugging Face...")
        try:
            dataset = load_dataset("maharshipandya/spotify-tracks-dataset")
            df = pd.DataFrame(dataset['train'])

            # Create the 'data' directory if it doesn't exist
            os.makedirs(os.path.dirname(local_path), exist_ok=True)

            df.to_csv(local_path, index=False)
            print(f"Dataset downloaded and saved to {local_path}")
        except Exception as e:
            print(f"Error downloading or saving dataset: {e}")
            return None
    else:
        print("Loading dataset from local file...")
        df = pd.read_csv(local_path)

    return df

# Data Analysis Functions
@cache.cached(timeout=3600, key_prefix='analyze_genre_popularity')
def analyze_genre_popularity(df):
    """
    Analyzes the popularity of different music genres.
    Returns a Plotly figure (as JSON) and an interpretation string.
    """
    genre_popularity = df.groupby('track_genre')['popularity'].mean().sort_values(ascending=False)

    fig = px.bar(genre_popularity,
                 x=genre_popularity.index,
                 y=genre_popularity.values,
                 title="Popularité moyenne par genre",
                 labels={'x': 'Genre', 'y': 'Popularité moyenne'})

    fig.update_layout(
        height=300,
        title_x=0.5,
        title_font=dict(size=14),
        xaxis_title="",
        yaxis_title="Popularité moyenne",
        yaxis_title_font=dict(size=12),
        xaxis_tickfont=dict(size=10),
        yaxis_tickfont=dict(size=10)
    )

    graphJSON = fig.to_json()

    interpretation = """
    Ce graphique montre le score de popularité moyen pour chaque genre. 
    En supposant que la popularité est corrélée aux ventes, cela suggère les genres 
    sur lesquels il pourrait être plus rentable de se concentrer.
    """
    return graphJSON, interpretation

@cache.cached(timeout=3600, key_prefix='analyze_music_features_by_genre')
def analyze_music_features_by_genre(df, feature='danceability'):
    """
    Analyzes the distribution of a specific music feature across different genres.

    Args:
        df: The DataFrame.
        feature: The music feature to analyze (e.g., 'danceability', 'energy', 'tempo').

    Returns:
        A Plotly figure (as JSON) and an interpretation string.
    """
    feature_by_genre = df.groupby('track_genre')[feature].mean().sort_values(ascending=False)
    
    fig = px.bar(
        data_frame=df,
        x='track_genre',
        y=feature,
        color='track_genre',
        title=f"Moyenne de {feature.capitalize()} par genre",
        category_orders={"track_genre": feature_by_genre.index.tolist()}
    )

    fig.update_layout(
        height=300,
        title_x=0.5,
        title_font=dict(size=14),
        xaxis_title="",
        yaxis_title=f"Moyenne de {feature.capitalize()}",
        yaxis_title_font=dict(size=12),
        xaxis_tickfont=dict(size=10),
        yaxis_tickfont=dict(size=10),
        showlegend=False
    )

    graphJSON = fig.to_json()

    interpretation = f"""
    Ce graphique compare la moyenne de {feature} entre différents genres musicaux. 
    Il aide à comprendre comment les caractéristiques musicales varient selon le genre et quels genres 
    sont associés à des valeurs plus ou moins élevées de cette caractéristique. Ces informations peuvent être 
    utiles pour adapter la production musicale à des publics cibles spécifiques.
    """
    return graphJSON, interpretation

@cache.cached(timeout=3600, key_prefix='analyze_sales_correlations')
def analyze_sales_correlations(df):
    """
    Analyzes correlations between music features and popularity.

    Returns:
        A Plotly figure (as JSON) and an interpretation string.
    """
    numerical_df = df.select_dtypes(include=['number'])
    correlation_matrix = numerical_df.corr()
    popularity_correlations = correlation_matrix['popularity'].sort_values(ascending=False)

    fig = px.bar(
        x=popularity_correlations.index,
        y=popularity_correlations.values,
        title='Corrélation entre les caractéristiques musicales et la popularité',
        labels={'x': 'Caractéristique musicale', 'y': 'Corrélation avec la popularité'},
        color=popularity_correlations.index,
        color_discrete_sequence=px.colors.sequential.Viridis
    )

    fig.update_layout(
        height=300,
        title_x=0.5,
        title_font=dict(size=14),
        xaxis_title="",
        yaxis_title="Corrélation",
        yaxis_title_font=dict(size=12),
        xaxis_tickfont=dict(size=10),
        yaxis_tickfont=dict(size=10),
        showlegend=False
    )

    graphJSON = fig.to_json()

    interpretation = """
    Ce graphique affiche la corrélation entre diverses caractéristiques musicales et la popularité des pistes. 
    Des corrélations positives suggèrent que des valeurs plus élevées d'une caractéristique sont associées à une popularité plus élevée, 
    tandis que des corrélations négatives suggèrent l'inverse. Ces informations peuvent être précieuses pour 
    comprendre quelles caractéristiques musicales pourraient contribuer au succès d'une piste.
    """
    return graphJSON, interpretation

@cache.cached(timeout=3600, key_prefix='analyze_explicit_content')
def analyze_explicit_content(df):
    """
    Analyzes the proportion of explicit tracks in each genre.
    """
    explicit_counts = df.groupby(['track_genre', 'explicit']).size().unstack(fill_value=0)
    explicit_proportion = explicit_counts.div(explicit_counts.sum(axis=1), axis=0)

    fig = px.bar(explicit_proportion,
                 x=explicit_proportion.index,
                 y=True,
                 title="Proportion de pistes explicites par genre",
                 labels={'x': 'Genre', 'y': 'Proportion de pistes explicites', 'value': 'Proportion', 'variable': 'Explicite'},
                 color_discrete_sequence=["#FF6347"])

    fig.update_layout(
        height=300,
        title_x=0.5,
        title_font=dict(size=14),
        xaxis_title="",
        yaxis_title="Proportion",
        yaxis_title_font=dict(size=12),
        xaxis_tickfont=dict(size=10),
        yaxis_tickfont=dict(size=10),
        yaxis_tickformat=".2%"
    )

    graphJSON = fig.to_json()

    interpretation = """
    Ce graphique montre la proportion de pistes avec du contenu explicite dans chaque genre. 
    Il peut être utile pour comprendre le public cible et les normes de contenu associées à différents genres. 
    Par exemple, les genres avec une forte proportion de pistes explicites pourraient être moins adaptés aux 
    campagnes marketing axées sur la famille.
    """
    return graphJSON, interpretation

@cache.cached(timeout=3600, key_prefix='analyze_duration_by_genre')
def analyze_duration_by_genre(df):
    """
    Analyzes the distribution of track durations across different genres.
    """
    fig = px.box(df,
                 x='track_genre',
                 y='duration_ms',
                 title="Distribution des durées de pistes par genre",
                 labels={'track_genre': 'Genre', 'duration_ms': 'Durée (ms)'},
                 color='track_genre',
                 category_orders={"track_genre": df.groupby('track_genre')['duration_ms'].median().sort_values(ascending=False).index.tolist()})

    fig.update_layout(
        height=300,
        title_x=0.5,
        title_font=dict(size=14),
        xaxis_title="",
        yaxis_title="Durée (ms)",
        yaxis_title_font=dict(size=12),
        xaxis_tickfont=dict(size=10),
        yaxis_tickfont=dict(size=10),
        showlegend=False
    )

    graphJSON = fig.to_json()

    interpretation = """
    Ce diagramme en boîte montre la distribution des durées de pistes pour chaque genre. 
    Il aide à identifier les genres qui ont tendance à avoir des pistes plus longues ou plus courtes. 
    Ces informations peuvent être pertinentes pour la création de listes de lecture, la programmation radio et 
    la compréhension des préférences des auditeurs pour différents genres.
    """
    return graphJSON, interpretation

@cache.cached(timeout=3600, key_prefix='analyze_feature_correlation_heatmap')
def analyze_feature_correlation_heatmap(df):
    """
    Generates a heatmap to visualize the correlations between different musical features.
    """
    numerical_features = df.select_dtypes(include=['number'])
    corr_matrix = numerical_features.corr()

    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='Viridis',
        zmin=-1,
        zmax=1
    ))

    fig.update_layout(
        height=350,
        title_x=0.5,
        title_font=dict(size=14),
        xaxis_title="",
        yaxis_title="",
        xaxis_tickfont=dict(size=10),
        yaxis_tickfont=dict(size=10),
        xaxis_showticklabels=True,
        yaxis_showticklabels=True,
        yaxis_autorange='reversed'
    )

    graphJSON = fig.to_json()

    interpretation = """
    Cette carte de chaleur visualise les corrélations entre différentes caractéristiques musicales. 
    Les corrélations positives sont indiquées dans des couleurs plus chaudes (plus proches de 1), indiquant que deux caractéristiques 
    ont tendance à augmenter ensemble. Les corrélations négatives sont indiquées dans des couleurs plus froides (plus proches de -1), 
    indiquant que lorsqu'une caractéristique augmente, l'autre a tendance à diminuer. Comprendre ces relations peut aider à 
    sélectionner des caractéristiques pour la modélisation prédictive ou pour créer de la musique avec des caractéristiques spécifiques.
    """
    return graphJSON, interpretation

@cache.cached(timeout=3600, key_prefix='analyze_tempo_by_genre')
def analyze_tempo_by_genre(df):
    """
    Analyzes the distribution of tempo across different genres.
    """
    fig = px.box(df,
                 x='track_genre',
                 y='tempo',
                 title="Distribution du Tempo par Genre",
                 labels={'track_genre': 'Genre', 'tempo': 'Tempo (BPM)'},
                 color='track_genre',
                 category_orders={"track_genre": df.groupby('track_genre')['tempo'].median().sort_values(ascending=False).index.tolist()})

    fig.update_layout(
        height=300,
        title_x=0.5,
        title_font=dict(size=14),
        xaxis_title="",
        yaxis_title="Tempo (BPM)",
        yaxis_title_font=dict(size=12),
        xaxis_tickfont=dict(size=10),
        yaxis_tickfont=dict(size=10),
        showlegend=False
    )

    graphJSON = fig.to_json()

    interpretation = """
    Ce diagramme en boîte montre la distribution du tempo (BPM) pour chaque genre. 
    Il aide à identifier les genres qui ont tendance à avoir des tempos plus rapides ou plus lents. 
    Ces informations peuvent être utiles pour la création de playlists ou pour comprendre les préférences des auditeurs.
    """
    return graphJSON, interpretation

@cache.cached(timeout=3600, key_prefix='analyze_energy_vs_danceability')
def analyze_energy_vs_danceability(df):
    """
    Analyzes the relationship between energy and danceability across different genres.
    """
    fig = px.scatter(df,
                     x='energy',
                     y='danceability',
                     color='track_genre',
                     title="Relation entre l'Énergie et la Danseabilité par Genre",
                     labels={'energy': 'Énergie', 'danceability': 'Danseabilité'},
                     opacity=0.6)

    fig.update_layout(
        height=400,
        title_x=0.5,
        title_font=dict(size=14),
        xaxis_title="Énergie",
        yaxis_title="Danseabilité",
        xaxis_title_font=dict(size=12),
        yaxis_title_font=dict(size=12),
        xaxis_tickfont=dict(size=10),
        yaxis_tickfont=dict(size=10),
        legend_title_text='Genre'
    )

    graphJSON = fig.to_json()

    interpretation = """
    Ce graphique en nuage de points montre la relation entre l'énergie et la danseabilité des pistes, 
    colorées par genre. Il aide à identifier les genres qui ont tendance à avoir des pistes plus énergiques 
    et dansables, ce qui peut être utile pour la création de playlists ou pour cibler des publics spécifiques.
    """
    return graphJSON, interpretation

@cache.cached(timeout=3600, key_prefix='analyze_popularity_over_time')
def analyze_popularity_over_time(df):
    """
    Analyzes the trend of track popularity over time.
    """
    if 'release_date' not in df.columns:
        interpretation = """
        La colonne 'release_date' n'est pas disponible dans le jeu de données. 
        Impossible d'analyser la popularité au fil du temps.
        """
        fig = go.Figure()
        fig.update_layout(
            title="Popularité au fil du temps (Données indisponibles)",
            height=300,
            title_x=0.5,
            title_font=dict(size=14),
            xaxis_title="",
            yaxis_title="Popularité moyenne",
            xaxis_title_font=dict(size=12),
            yaxis_title_font=dict(size=12),
            xaxis_tickfont=dict(size=10),
            yaxis_tickfont=dict(size=10)
        )
        graphJSON = fig.to_json()
        return graphJSON, interpretation

    df['release_year'] = pd.to_datetime(df['release_date']).dt.year
    popularity_over_time = df.groupby('release_year')['popularity'].mean().reset_index()

    fig = px.line(popularity_over_time,
                  x='release_year',
                  y='popularity',
                  title="Popularité des pistes au fil des années",
                  labels={'release_year': 'Année de sortie', 'popularity': 'Popularité moyenne'})

    fig.update_layout(
        height=300,
        title_x=0.5,
        title_font=dict(size=14),
        xaxis_title="Année de sortie",
        yaxis_title="Popularité moyenne",
        xaxis_title_font=dict(size=12),
        yaxis_title_font=dict(size=12),
        xaxis_tickfont=dict(size=10),
        yaxis_tickfont=dict(size=10)
    )

    graphJSON = fig.to_json()

    interpretation = """
    Ce graphique en ligne montre l'évolution de la popularité moyenne des pistes au fil des années. 
    Il peut révéler des tendances dans les préférences des auditeurs et aider à comprendre comment la popularité 
    des pistes a changé au fil du temps.
    """
    return graphJSON, interpretation

@cache.cached(timeout=3600, key_prefix='analyze_top_artists_by_popularity')
def analyze_top_artists_by_popularity(df):
    """
    Analyzes the top artists by average track popularity.
    """
    top_artists = df.groupby('artists')['popularity'].mean().sort_values(ascending=False).head(20)

    fig = px.bar(top_artists,
                 x=top_artists.values,
                 y=top_artists.index,
                 orientation='h',
                 title="Top 20 des artistes par popularité moyenne",
                 labels={'x': 'Popularité moyenne', 'y': 'Artistes'})

    fig.update_layout(
        height=400,
        title_x=0.5,
        title_font=dict(size=14),
        xaxis_title="Popularité moyenne",
        yaxis_title="Artistes",
        xaxis_title_font=dict(size=12),
        yaxis_title_font=dict(size=12),
        xaxis_tickfont=dict(size=10),
        yaxis_tickfont=dict(size=10)
    )

    graphJSON = fig.to_json()

    interpretation = """
    Ce graphique en barres horizontales montre les 20 artistes les plus populaires en fonction de la popularité 
    moyenne de leurs pistes. Cela peut aider à identifier les artistes les plus influents ou les plus appréciés 
    par le public.
    """
    return graphJSON, interpretation

@cache.cached(timeout=3600, key_prefix='analyze_valence_vs_popularity')
def analyze_valence_vs_popularity(df):
    """
    Analyzes the relationship between valence and track popularity.
    """
    fig = px.scatter(df,
                     x='valence',
                     y='popularity',
                     title="Relation entre la Valence et la Popularité",
                     labels={'valence': 'Valence', 'popularity': 'Popularité'})

    fig.update_layout(
        height=400,
        title_x=0.5,
        title_font=dict(size=14),
        xaxis_title="Valence",
        yaxis_title="Popularité",
        xaxis_title_font=dict(size=12),
        yaxis_title_font=dict(size=12),
        xaxis_tickfont=dict(size=10),
        yaxis_tickfont=dict(size=10)
    )

    graphJSON = fig.to_json()

    interpretation = """
    Ce graphique en nuage de points montre la relation entre la valence (positivité) des pistes et leur popularité. 
    Une tendance positive pourrait indiquer que les pistes plus positives sont plus populaires, tandis qu'une tendance 
    négative pourrait suggérer le contraire.
    """
    return graphJSON, interpretation

@cache.cached(timeout=3600, key_prefix='analyze_top_popular_tracks')
def analyze_top_popular_tracks(df):
    """
    Analyzes the top 10 most popular tracks.
    """
    top_tracks = df.nlargest(10, 'popularity')

    fig = px.bar(top_tracks,
                 x='track_name',
                 y='popularity',
                 title="Top 10 des pistes les plus populaires",
                 labels={'track_name': 'Nom de la piste', 'popularity': 'Popularité'})

    fig.update_layout(
        height=400,
        title_x=0.5,
        title_font=dict(size=14),
        xaxis_title="",
        yaxis_title="Popularité",
        yaxis_title_font=dict(size=12),
        xaxis_tickfont=dict(size=10),
        yaxis_tickfont=dict(size=10),
        showlegend=False
    )

    graphJSON = fig.to_json()

    interpretation = """
    Ce graphique montre les 10 pistes les plus populaires du jeu de données. 
    Il aide à identifier les pistes qui ont le plus de succès auprès des auditeurs.
    """
    return graphJSON, interpretation

@cache.cached(timeout=3600, key_prefix='analyze_energy_by_genre')
def analyze_energy_by_genre(df):
    """
    Analyzes the distribution of energy across genres.
    """
    fig = px.box(df,
                 x='track_genre',
                 y='energy',
                 title="Distribution de l'énergie par genre",
                 labels={'track_genre': 'Genre', 'energy': 'Énergie'})

    fig.update_layout(
        height=400,
        title_x=0.5,
        title_font=dict(size=14),
        xaxis_title="",
        yaxis_title="Énergie",
        yaxis_title_font=dict(size=12),
        xaxis_tickfont=dict(size=10),
        yaxis_tickfont=dict(size=10),
        showlegend=False
    )

    graphJSON = fig.to_json()

    interpretation = """
    Ce diagramme en boîte montre la distribution de l'énergie des pistes par genre. 
    Il aide à comprendre quels genres ont tendance à avoir des pistes plus énergiques.
    """
    return graphJSON, interpretation

@cache.cached(timeout=3600, key_prefix='analyze_loudness_vs_energy')
def analyze_loudness_vs_energy(df):
    """
    Analyzes the relationship between loudness and energy.
    """
    fig = px.scatter(df,
                     x='loudness',
                     y='energy',
                     title="Relation entre la Loudness et l'Énergie",
                     labels={'loudness': 'Loudness', 'energy': 'Énergie'})

    fig.update_layout(
        height=400,
        title_x=0.5,
        title_font=dict(size=14),
        xaxis_title="Loudness",
        yaxis_title="Énergie",
        xaxis_title_font=dict(size=12),
        yaxis_title_font=dict(size=12),
        xaxis_tickfont=dict(size=10),
        yaxis_tickfont=dict(size=10)
    )

    graphJSON = fig.to_json()

    interpretation = """
    Ce graphique en nuage de points montre la relation entre la loudness et l'énergie des pistes. 
    Une corrélation positive pourrait indiquer que les pistes plus fortes en loudness ont tendance à être plus énergiques.
    """
    return graphJSON, interpretation

@cache.cached(timeout=3600, key_prefix='analyze_acousticness_distribution')
def analyze_acousticness_distribution(df):
    """
    Analyzes the distribution of acousticness.
    """
    fig = px.histogram(df,
                       x='acousticness',
                       title="Distribution de l'acousticness",
                       labels={'acousticness': 'Acousticness'})

    fig.update_layout(
        height=400,
        title_x=0.5,
        title_font=dict(size=14),
        xaxis_title="Acousticness",
        yaxis_title="Nombre de pistes",
        xaxis_title_font=dict(size=12),
        yaxis_title_font=dict(size=12),
        xaxis_tickfont=dict(size=10),
        yaxis_tickfont=dict(size=10)
    )

    graphJSON = fig.to_json()

    interpretation = """
    Ce graphique montre la distribution de l'acousticness des pistes. 
    Il aide à comprendre combien de pistes ont un niveau d'acousticness donné.
    """
    return graphJSON, interpretation