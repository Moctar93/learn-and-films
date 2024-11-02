import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom'; // Ajout de react-router-dom
import './App.css';
import HomePage from './pages/HomePage';
import Register from './Register.js';
import SignUpPage from './pages/SignUpPage';
import Login from './pages/Login';
import UserList from './pages/UserList';
import logo from './images/logo.png';
import image1 from './images/image1.png';
import image2 from './images/image2.png';
import image3 from './images/image3.png';
import image4 from './images/image4.png';
import image5 from './images/image5.png';
import image6 from './images/image6.png';
import image7 from './images/image7.png';
import image8 from './images/image8.png';
import image9 from './images/image9.png';
import videoA from './videos/videoA.mp4';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => setIsMenuOpen(!isMenuOpen);
  const handleLogin = () => {
    setIsLoggedIn(true);
    setIsMenuOpen(false);
  };
  const handleLogout = () => {
	localStorage.removeItem('token'); // Supprimez le token du local storage
	setIsLoggedIn(false); // Mettez à jour l'état pour indiquer que l'utilisateur est déconnecté
  };

  return (
    <Router>
    <div className="app">
	  {/* Header avec le logo */}
      <header className="header">
        <img
          src={logo}
          alt="learn and films"
          className="logo"
        />

	  <div className="search-bar">
            <form action="/search" method="GET">
                <input className="input" type="text" name="query" placeholder="Rechercher..." required/>
                <button className="search" type="submit">Rechercher</button>
            </form>
	  </div>

        <nav>
	  <ul className="nav-links">
	  <li><Link to="/">Accueil</Link></li>
	  <li><Link to="/series">Series</Link></li>
	  <li><Link to="/films">Films</Link></li>
	  <li className="user-menu" onClick={toggleMenu}>
	  {isLoggedIn ? 'Gestion Utilisateur' : 'Connexion / Inscription'}
	  <ul className={`dropdown ${isMenuOpen ? 'open' : ''}`}>
	  {isLoggedIn ? (
          <>
            <li><Link to="/dashboard" onClick={() => setIsMenuOpen(false)}>Dashboard</Link></li>
            <li><button onClick={handleLogout}>Déconnexion</button></li>
          </>
        ) : (
          <>
            <li><Link to="/login" onClick={() => setIsMenuOpen(false)}>Connexion</Link></li>
            <li><Link to="/register" onClick={() => setIsMenuOpen(false)}>Inscription</Link></li>
          </>
        )}
	  </ul>
	  </li>
	  </ul>
	  </nav>
      </header>

	   {/* Routes pour différentes pages */}
        <Routes>
	  <Route path="/" element={<HomePage />} />  {/* Définir la route pour la page d'accueil */}
          <Route path="/register" element={<SignUpPage />} /> {/* Page d'inscription */}
	   <Route path="/login" element={<Login onLoginSuccess={handleLogin} />} /> {/* Page de connexion */}
        </Routes>

      {/* Hero Section */}
	   <section className="hero-section">
        <div className="hero-content">
	  <video autoPlay loop muted playsInline className="hero-video">
             <source src={videoA} type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
      </section>

      {/* Learning Modules */}
      <section className="modules">
        {/* Module: Histoire de la Révolution Française */}
        <div className="module">
          <h2>Apprendre l'Histoire : La Révolution Française</h2>
          <div className="films-row">
            <div className="film">
	  <img
          src={image1}
          alt="film 1"
	  />
              <p>Les Misérables (2019)</p>
            </div>
            <div className="film">
	  <img
          src={image2}
          alt="film 2"
	  />
              <p>La Révolution Française (1989)</p>
            </div>
            <div className="film">
	  <img
          src={image3}
          alt="film 3"
	  />
              <p>Marie-Antoinette (2006)</p>
            </div>
          </div>
        </div>

        {/* Module: Introduction à l'Astronomie */}
        <div className="module">
          <h2>Introduction à l'Astronomie</h2>
          <div className="films-row">
            <div className="film">
	  <img
          src={image4}
          alt="film 4"
	  />
              <p>Cosmos: A Spacetime Odyssey (2014)</p>
              <p>Interstellar (2014)</p>
            </div>
            <div className="film">
	  <img
          src={image5}
          alt="film 5"
          />
              <p>Cosmos: A Spacetime Odyssey (2014)</p>
            </div>
            <div className="film">
	  <img
          src={image6}
          alt="film 6"
          />
              <p>The Martian (2015)</p>
            </div>
          </div>
        </div>

        {/* Module: Art et Culture */}
        <div className="module">
          <h2>Art et Culture : L'art Moderne</h2>
          <div className="films-row">
            <div className="film">
	  <img
          src={image7}
          alt="film 7"
          />
              <p>Frida (2002)</p>
            </div>
            <div className="film">
	  <img
          src={image8}
          alt="film 8"
          />
              <p>Pollock (2000)</p>
            </div>
            <div className="film">
	  <img
          src={image9}
          alt="film 9"
          />
              <p>The Picasso Legacy (2016)</p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="footer">
            <div className="footer-section">
                <h4>Nous contacter</h4>
                <ul>
                    <li><a href="#contact">Contact</a></li>
                    <li><a href="#support">Support</a></li>
                    <li><a href="#email">Email</a></li>
                </ul>
            </div>

            <div className="footer-section">
                <h4>Guide</h4>
                <ul>
                    <li><a href="#faq">FAQ</a></li>
                    <li><a href="#help">Aide</a></li>
                </ul>
            </div>

	   <div className="footer-section">
                <h4>Confidentialités</h4>
                <ul>
                    <li><a href="#privacy">Politique de confidentialité</a></li>
                    <li><a href="#terms">Conditions d'utilisation</a></li>
                </ul>
            </div>

            <div className="footer-section">
                <h4>Informations légales</h4>
                <ul>
                    <li><a href="#legal">Mentions légales</a></li>
                </ul>
            </div>
	  </footer>
	  <div className="right-copy">
          <p className="copyright">&copy; 2024 Learn and Films. Tous droits réservés.</p>
	  </div>
	  <UserList />
	 </div>
	</Router>
  );
}
export default App;
