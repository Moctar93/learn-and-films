import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Films.css'; // Importez le fichier CSS pour le style

function Films() {
    const [films, setFilms] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Récupère le token d'authentification depuis le localStorage
        const token = localStorage.getItem("token");

        // Requête GET pour récupérer la liste des films
        axios.get(`${process.env.REACT_APP_BACKEND_URL}/films/list/`, {
            headers: token ? { Authorization: `Token ${token}` } : {},
            withCredentials: true, // Si l'authentification repose sur des cookies
        })
        .then(response => {
            setFilms(response.data);
            setError(null); // Réinitialise les erreurs en cas de succès
        })
        .catch(err => {
            console.error('Erreur lors de la récupération des films:', err);
            setError("Impossible de récupérer la liste des films. Vérifiez votre connexion.");
        });
    }, []);

    const handleClick = (film) => {
        // Rediriger vers la page de lecture du film avec son ID
        window.location.href = `/films/${film.id}/play`;
    };

    // Si les données des films ne sont pas encore chargées, affiche un message de chargement
    if (!films.length && !error) return <div>Chargement...</div>;

    return (
        <div className="films-container">
            {error ? (
                <div className="error-message">{error}</div>
            ) : (
                films.map(film => (
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
                ))
            )}
        </div>
    );
}

export default Films;

