import React, { useEffect, useState } from 'react';
import axios from 'axios';

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
                    <img 
                        src={`${process.env.REACT_APP_BACKEND_URL}${film.image}`} 
                        alt={film.title} 
                        className="film-image" 
                    />
                    <h3>{film.title}</h3>
                </div>
            ))}
        </div>
    );
}

export default Films;

