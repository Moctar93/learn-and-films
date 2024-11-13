import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Dashboard() {
    const [userData, setUserData] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Récupère le token d'authentification depuis le localStorage
        const token = localStorage.getItem("token");

        // Requête GET pour récupérer les informations de l'utilisateur connecté
        axios.get(`${process.env.REACT_APP_BACKEND_URL}/api/user/dashboard/`, {
            headers: token ? { Authorization: `Token ${token}` } : {},
            withCredentials: true, // Si l'authentification repose sur des cookies
        })
        .then(response => {
            setUserData(response.data);
            setError(null); // Réinitialise les erreurs en cas de succès
        })
        .catch(err => {
            console.error('Erreur lors de la récupération des données utilisateur:', err);
            setError("Impossible de récupérer les données de l'utilisateur. Vérifiez votre connexion.");
        });
    }, []);

    // Si les données de l'utilisateur ne sont pas encore chargées, affiche un message de chargement
    if (!userData && !error) return <div>Chargement...</div>;

    return (
        <div className="dashboard">
            {error ? (
                <div className="error-message">{error}</div>
            ) : (
                <>
                    <h1>Bienvenue, {userData.name}</h1>
                    <p>Email: {userData.email}</p>
                    <p>Plan d'abonnement: {userData.subscription_plan}</p>
                    <p>Date de souscription: {userData.subscription_start_date}</p>
                    <p>Fin d'abonnement: {userData.subscription_end_date}</p>
                </>
            )}
        </div>
    );
}

export default Dashboard;

