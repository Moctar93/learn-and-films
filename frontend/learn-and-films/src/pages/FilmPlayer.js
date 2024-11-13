import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

function FilmPlayer() {
    const { film_id } = useParams();
    const [film, setFilm] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Récupérer le token d'authentification depuis le localStorage
        const token = localStorage.getItem("token");

        // Récupérer les détails du film via l'API avec le token dans les headers
        axios.get(`${process.env.REACT_APP_BACKEND_URL}/films/${film_id}/play/`, {
            headers: token ? { Authorization: `Token ${token}` } : {},
            withCredentials: true, // Si l'authentification repose sur des cookies
        })
        .then(response => {
            setFilm(response.data);
            setError(null); // Réinitialise les erreurs en cas de succès
        })
        .catch(error => {
            console.error('Erreur lors de la récupération du film:', error);
            setError("Impossible de récupérer les détails du film. Vérifiez votre connexion.");
        });
    }, [film_id]);

    // Si le film n'est pas encore chargé et qu'il n'y a pas d'erreur, affiche un message de chargement
    if (!film && !error) return <div>Chargement...</div>;

    // Si une erreur est présente, affiche le message d'erreur
    if (error) return <div className="error-message">{error}</div>;

    // URL de la vidéo YouTube
    const youtubeUrl = film.video_url;

    // Extraire l'ID de la vidéo YouTube à partir de l'URL
    const videoId = youtubeUrl.includes('v=') ? youtubeUrl.split('v=')[1].split('&')[0] : youtubeUrl;

    return (
        <div className="film-player">
            <h1>{film.title}</h1>
            <div className="video-container">
                {/* Intégration de la vidéo YouTube via iframe */}
                <iframe
                    width="100%"
                    height="500px"
                    src={`https://www.youtube.com/embed/${videoId}`}
                    frameBorder="0"
                    allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                    allowFullScreen
                ></iframe>
            </div>
        </div>
    );
}

export default FilmPlayer;

