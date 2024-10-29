import React, { useState } from 'react';
import axios from 'axios';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const Register = () => {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/api/register/', formData);
            toast.success(response.data.message); // Notification de succès
        } catch (error) {
            if (error.response) {
                toast.error(error.response.data.message || 'Erreur lors de l’inscription'); // Notification d'erreur
            } else {
                toast.error('Erreur lors de l’inscription');
            }
        }
    };

    return (
        <>
            <ToastContainer /> {/* Conteneur pour les notifications */}
            <div>
                <h2>Inscription</h2>
                <form onSubmit={handleSubmit}>
                    <input
                        type="text"
                        name="username"
                        placeholder="Nom d'utilisateur"
                        value={formData.username}
                        onChange={handleChange}
                        required
                    />
                    <input
                        type="email"
                        name="email"
                        placeholder="Email"
                        value={formData.email}
                        onChange={handleChange}
                        required
                    />
                    <input
                        type="password"
                        name="password"
                        placeholder="Mot de passe"
                        value={formData.password}
                        onChange={handleChange}
                        required
                    />
                    <button type="submit">S'inscrire</button>
                </form>
            </div>
        </>
    );
};

export default Register;

