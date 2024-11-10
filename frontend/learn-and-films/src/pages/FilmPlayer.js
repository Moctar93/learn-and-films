import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

function FilmPlayer() {
    const { film_id } = useParams();
    const [film, setFilm] = useState(null);

    useEffect(() => {
        axios.get(`${process.env.REACT_APP_BACKEND_URL}/films/${film_id}/play/`)
            .then(response => setFilm(response.data))
            .catch(error => console.error('Erreur lors de la récupération du film:', error));
    }, [film_id]);

    if (!film) return <div>Chargement...</div>;

    return (
        <div className="film-player">
            <h1>{film.title}</h1>
            <video controls src={`${process.env.REACT_APP_BACKEND_URL}${film.video_url}`} />
        </div>
    );
}

export default FilmPlayer;

