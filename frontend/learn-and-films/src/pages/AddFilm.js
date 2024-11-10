import React, { useState } from 'react';

function AddFilm() {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [link, setLink] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const filmData = { title, description, link };

        try {
            const response = await fetch('/films/add-film-api/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(filmData),
            });

            if (response.ok) {
                alert('Film ajouté avec succès !');
                setTitle('');
                setDescription('');
                setLink('');
            } else {
                alert("Erreur lors de l'ajout du film.");
            }
        } catch (error) {
            console.error('Erreur:', error);
        }
    };

    return (
	<div className="sign-up-container">
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Titre"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                required
            />
            <input
                type="text"
                placeholder="Description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                required
            />
            <input
                type="text"
                placeholder="Lien du film"
                value={link}
                onChange={(e) => setLink(e.target.value)}
                required
            />
            <button type="submit">Ajouter le film</button>
        </form>
	</div>
    );
}

export default AddFilm;

