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
    setError(''); // Réinitialisez l'erreur avant de faire la demande
    setSuccessMessage(''); // Réinitialisez le message de succès avant de faire la demande

    console.log('Tentative de connexion avec:', { username, password }); // Log pour débogage

    try {
      const response = await axios.post('http://localhost:8000/api/login/', {
        username,
        password,
      });

      console.log('Réponse du serveur:', response); // Affiche la réponse complète dans la console

      if (response.data && response.data.token) {
        localStorage.setItem('token', response.data.token);
        setIsLoggedIn(true);
	// onLoginSuccess();  Appeler la fonction de gestion de la connexion
        setSuccessMessage("Connexion réussie ! Bienvenue " + response.data.username); // Afficher le message de succès
        setTimeout(() => {
          navigate('/'); // Redirigez vers la page d'accueil après 3 secondes
        }, 3000);
      } else {
        setError("Erreur lors de la connexion. Aucune donnée d'authentification reçue.");
      }
    } catch (err) {
      console.error("Erreur capturée:", err); // Log de l'erreur pour débogage

      // Vérifiez si l'erreur contient une réponse et gérez-la
      if (err.response && err.response.data) {
        setError(err.response.data.detail || "Erreur lors de la connexion. Vérifiez vos identifiants."); // Affiche un message d'erreur plus précis
      } else {
        setError("Erreur lors de la connexion. Vérifiez vos identifiants.");
      }
    }
  };

  return (
    <div className="sign-up-container">
      <h2>Connexion</h2>
      {error && <p className="error-message" style={{ color: 'black' }}>{error}</p>} {/* Affiche le message d'erreur */}
      {successMessage && <p className="success-message" style={{ color: 'black' }}>{successMessage}</p>} {/* Affiche le message de succès */}
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


