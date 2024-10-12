// src/components/Home.js
import React from 'react';

function Home() {
    return (
        <main>
            <section className="hero">
                <h1>Welcome to Learn and Films</h1>
                <p>Learn new skills and enjoy great movies.</p>
                <button>Start Learning</button>
            </section>

            <section className="content-row">
                <h2>Popular Tutorials</h2>
                <div className="content-grid">
                    <div className="content-item"><img src="https://via.placeholder.com/150" alt="Tutorial 1" /><p>JavaScript Basics</p></div>
                    <div className="content-item"><img src="https://via.placeholder.com/150" alt="Tutorial 2" /><p>Introduction to Python</p></div>
                    <div className="content-item"><img src="https://via.placeholder.com/150" alt="Tutorial 3" /><p>Web Development</p></div>
                    <div className="content-item"><img src="https://via.placeholder.com/150" alt="Tutorial 4" /><p>Data Science</p></div>
                </div>
            </section>

            <section className="content-row">
                <h2>Popular Movies</h2>
                <div className="content-grid">
                    <div className="content-item"><img src="https://via.placeholder.com/150" alt="Movie 1" /><p>Movie Title 1</p></div>
                    <div className="content-item"><img src="https://via.placeholder.com/150" alt="Movie 2" /><p>Movie Title 2</p></div>
                    <div className="content-item"><img src="https://via.placeholder.com/150" alt="Movie 3" /><p>Movie Title 3</p></div>
                    <div className="content-item"><img src="https://via.placeholder.com/150" alt="Movie 4" /><p>Movie Title 4</p></div>
                </div>
            </section>
        </main>
    );
}

export default Home;

