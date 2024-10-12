// src/components/Header.js
import React from 'react';

function Header() {
    return (
        <header>
            <div className="logo">
                <h1>Learn & Films</h1>
            </div>
            <nav>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">Tutorials</a></li>
                    <li><a href="#">Movies</a></li>
                    <li><a href="#">My List</a></li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;
