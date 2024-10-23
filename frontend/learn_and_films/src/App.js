import React, { useState } from 'react';
import './App.css';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => setIsMenuOpen(!isMenuOpen);
  const handleLogin = () => {
    setIsLoggedIn(true);
    setIsMenuOpen(false);
  };
  const handleLogout = () => {
    setIsLoggedIn(false);
    setIsMenuOpen(false);
  };

  return (
    <div className="app">
      {/* Header */}
      <header className="header">
        <img src="https://via.placeholder.com/150x50" alt="Learn and Films Logo" className="logo" />
        <nav>
          <ul className="nav-links">
            <li><a href="#">Accueil</a></li>
            <li><a href="#">Modules</a></li>
            <li><a href="#">Films</a></li>
            <li className="user-menu" onClick={toggleMenu}>
              {isLoggedIn ? 'Gestion Utilisateur' : 'Connexion / Inscription'}
              <ul className={`dropdown ${isMenuOpen ? 'open' : ''}`}>
                {isLoggedIn ? (
                  <>
                    <li><a href="#">Dashboard</a></li>
                    <li><a href="#" onClick={handleLogout}>Déconnexion</a></li>
                  </>
                ) : (
                  <>
                    <li><a href="#" onClick={handleLogin}>Connexion</a></li>
                    <li><a href="#">Inscription</a></li>
                  </>
                )}
              </ul>
            </li>
          </ul>
        </nav>
      </header>

      {/* Hero Section */}
      <section className="hero">
        <div className="hero-content">
          <h1>Apprenez en regardant des films</h1>
          <p>Explorez des parcours d'apprentissage interactifs et divertissants.</p>
          <button className="btn-primary">Commencez maintenant</button>
        </div>
      </section>

      {/* Learning Modules */}
      <section className="modules">
        {/* Module: Histoire de la Révolution Française */}
        <div className="module">
          <h2>Apprendre l'Histoire : La Révolution Française</h2>
          <div className="films-row">
            <div className="film">
              <img src="https://via.placeholder.com/200x300" alt="Film 1" />
              <p>Les Misérables (2019)</p>
            </div>
            <div className="film">
              <img src="https://via.placeholder.com/200x300" alt="Film 2" />
              <p>La Révolution Française (1989)</p>
            </div>
            <div className="film">
              <img src="https://via.placeholder.com/200x300" alt="Film 3" />
              <p>Marie-Antoinette (2006)</p>
            </div>
          </div>
        </div>

        {/* Module: Introduction à l'Astronomie */}
        <div className="module">
          <h2>Introduction à l'Astronomie</h2>
          <div className="films-row">
            <div className="film">
              <img src="https://via.placeholder.com/200x300" alt="Film 1" />
              <p>Interstellar (2014)</p>
            </div>
            <div className="film">
              <img src="https://via.placeholder.com/200x300" alt="Film 2" />
              <p>Cosmos: A Spacetime Odyssey (2014)</p>
            </div>
            <div className="film">
              <img src="https://via.placeholder.com/200x300" alt="Film 3" />
              <p>The Martian (2015)</p>
            </div>
          </div>
        </div>

        {/* Module: Art et Culture */}
        <div className="module">
          <h2>Art et Culture : L'art Moderne</h2>
          <div className="films-row">
            <div className="film">
              <img src="https://via.placeholder.com/200x300" alt="Film 1" />
              <p>Frida (2002)</p>
            </div>
            <div className="film">
              <img src="https://via.placeholder.com/200x300" alt="Film 2" />
              <p>Pollock (2000)</p>
            </div>
            <div className="film">
              <img src="https://via.placeholder.com/200x300" alt="Film 3" />
              <p>The Picasso Legacy (2016)</p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="footer">
	  <p>Nous contacter</p>
	  <p>Contact</p>
	  <p>Support</p>
	  <p>Email</p>
        <h2>&copy; 2024 Learn and Films. Tous droits réservés.</h2>
      </footer>
    </div>
  );
}

export default App;

