import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Films.css';  // Importez le fichier CSS pour le style

function Films() {
    const [films, setFilms] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/films/list/')
            .then(response => setFilms(response.data))
            .catch(error => console.error('Erreur lors de la récupération des films:', error));
    }, []);

    const handleClick = (film) => {
        // Rediriger vers la page de lecture du film avec son ID
        window.location.href = `/films/${film.id}/play`;
    };

    return (
        <div className="films-container">
            {films.map(film => (
                <div key={film.id} className="film-item" onClick={() => handleClick(film)}>
                    <div className="film-video">
                        {/* Utiliser un iframe pour afficher la vidéo */}
                        <iframe
                            width="100%"
                            height="auto"
                            src={film.video_link}  // Assurez-vous que `video_link` est une URL YouTube valide
                            frameBorder="0"
                            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                            allowFullScreen
                        />
                    </div>
                    <h3>{film.title}</h3>
                    <button onClick={() => handleClick(film)}>Play</button>
                </div>
            ))}
        </div>
    );
}

export default Films;

