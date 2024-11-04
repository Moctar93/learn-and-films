import React, { useState } from 'react';
import axios from 'axios';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const Register = () => {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        subscription: 'basic', // Par défaut, l'abonnement est "basic"
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
            // Envoi de la demande d'inscription avec abonnement au backend
            const response = await axios.post('http://localhost:8000/api/register/', formData);

            if (response.data.paymentUrl) {
                // Redirige l'utilisateur vers PayPal pour le paiement
                window.location.href = response.data.paymentUrl;
            } else {
                // Affiche une notification de succès si aucun paiement PayPal n'est requis
                toast.success(response.data.message);
            }
        } catch (error) {
            if (error.response) {
                toast.error(error.response.data.message || 'Erreur lors de l’inscription');
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
                    <select
                        name="subscription"
                        value={formData.subscription}
                        onChange={handleChange}
                        required
                    >
                        <option value="basic">Basic - 5.00€</option>
                        <option value="standard">Standard - 10.00€</option>
                        <option value="premium">Premium - 15.00€</option>
                    </select>
                    <button type="submit">S'inscrire et payer</button>
                </form>
            </div>
        </>
    );
};

export default Register;

