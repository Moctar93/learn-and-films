import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './SignUp.css';

const Login = ({ setIsLoggedIn }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [successMessage, setSuccessMessage] = useState(''); // État pour le message de succès

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Réinitialisez les messages d'erreur et de succès
    setError('');
    setSuccessMessage('');
    
    console.log('Tentative de connexion avec:', { username, password });

    try {
      const response = await axios.post('http://localhost:8000/api/login/', { username, password });
      console.log('Réponse du serveur:', response);

      // Vérification de la présence du token dans la réponse
      if (response.data && response.data.token) {
        localStorage.setItem('token', response.data.token); // Stocker le token dans localStorage
        setIsLoggedIn(true); // Met à jour l'état de connexion dans le parent
        setSuccessMessage(`Connexion réussie ! Bienvenue, ${response.data.username || 'utilisateur'}.`); // Affiche le message de succès

        // Redirection vers la page d'accueil après un délai de 3 secondes
        setTimeout(() => {
          navigate('/');
        }, 3000);
      } else {
        console.warn("Aucun token reçu dans la réponse.");
        setError("Erreur lors de la connexion. Aucune donnée d'authentification reçue.");
      }
    } catch (err) {
      console.error("Erreur capturée lors de la connexion:", err);

      // Gestion des erreurs provenant de l'API
      if (err.response && err.response.data) {
        setError(err.response.data.detail || "Erreur de connexion au serveur. Veuillez réessayer plus tard.");
      } else {
        setError("Connexion réussie ! Bienvenue");
      }
    }
  };

  return (
    <div className="sign-up-container">
      <h2>Connexion</h2>
      
      {/* Messages d'erreur et de succès */}
      {error && <p className="error-message" style={{ color: 'black' }}>{error}</p>}
      {successMessage && <p className="success-message" style={{ color: 'black' }}>{successMessage}</p>}
      
      <form onSubmit={handleSubmit}>
        <div>
          <label>Nom d'utilisateur</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Mot de passe</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Se connecter</button>
      </form>
    </div>
  );
};

export default Login;

