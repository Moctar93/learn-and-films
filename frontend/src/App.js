import React from 'react';
import './index.css'; // Import du fichier CSS
import Header from './components/Header';
import Home from './components/Home';
import About from './components/About';
import Footer from './components/Footer';

function App() {
    return (
        <>
            <Header />
            <Home />
            <About />
            <Footer />
        </>
    );
}

export default App;

