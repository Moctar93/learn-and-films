import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

function FilmPlayer() {
    const { film_id } = useParams();
    const [film, setFilm] = useState(null);

    useEffect(() => {
        // Récupérer les détails du film via l'API
        axios.get(`${process.env.REACT_APP_BACKEND_URL}/films/${film_id}/play/`)
            .then(response => {
                setFilm(response.data);
            })
            .catch(error => {
                console.error('Erreur lors de la récupération du film:', error);
            });
    }, [film_id]);

    if (!film) return <div>Chargement...</div>;

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

