import React, { useState } from 'react';
<<<<<<< HEAD
const SignUpPage = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');
    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch('http://localhost:8000/api/register/', { // Adresse du backend
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: username,
                email: email,
                password: password,
            }),
        });
        const data = await response.json();
        if (response.ok) {
            setMessage('Inscription réussie !');
        } else {
            setMessage('Erreur lors de l\'inscription : ' + data.message);
        }
    };
    return (
        <div>
            <h1>Inscription</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Nom d'utilisateur:</label>
	            <input
	                type="text"
	                value={username}
	                onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Email:</label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Mot de passe:</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">S'inscrire</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};
export default SignUpPage;
=======
import { useNavigate } from 'react-router-dom';
import './SignUp.css'; // Assurez-vous que le fichier CSS est bien configuré

function SignUpPage() {
  // États pour chaque champ du formulaire
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  // Fonction pour gérer la soumission du formulaire
  const handleSignUp = async (e) => {
    e.preventDefault();

    const userData = {
      username,
      email,
      password,
    };

    try {
      const response = await fetch('http://localhost:8000/api/register/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
      });

      if (response.ok) {
        // Si l'enregistrement est réussi, rediriger vers la page d'accueil
        navigate('/');
      } else {
        const data = await response.json();
        setError(data.message || "Une erreur est survenue lors de l'inscription");
      }
    } catch (error) {
      setError("Erreur serveur. Veuillez réessayer plus tard.");
    }
  };

  return (
    <div className="sign-up-container">
      <h2>Inscription</h2>
      {error && <p className="error-message">{error}</p>}
      <form onSubmit={handleSignUp}>
        <label>Nom d'utilisateur:</label>
        <input
          type="text"
          name="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />

        <label>Email:</label>
        <input
          type="email"
          name="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <label>Mot de passe:</label>
        <input
          type="password"
          name="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button type="submit">S'inscrire</button>
      </form>
    </div>
  );
}

export default SignUpPage;

>>>>>>> 7cd6cd43c71c58a170ec1392ec8018aa83694e86
