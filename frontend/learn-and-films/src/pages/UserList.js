import React, { useEffect, useState } from 'react';
import axios from 'axios';

const UserList = () => {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchUsers = async () => {
      const token = localStorage.getItem('token'); // Récupérer le jeton d'authentification

      try {
        const response = await axios.get('http://localhost:8000/api/users/', {
          headers: {
            Authorization: `Bearer ${token}`, // Utiliser le jeton récupéré
          },
        });
        setUsers(response.data); // Mettre à jour l'état avec les utilisateurs récupérés
      } catch (err) {
        // Gérer les erreurs de manière plus détaillée
        if (err.response) {
          setError(err.response.data || "Erreur lors de la récupération des utilisateurs");
        } else {
          setError("Erreur de connexion au serveur");
        }
      }
    };

    fetchUsers(); // Appeler la fonction pour récupérer les utilisateurs
  }, []);

  return (
    <div>
      <h2>Liste des utilisateurs</h2>
      {error && <p>{error}</p>} {/* Afficher un message d'erreur s'il y en a */}
      <ul>
        {users.length > 0 ? (
          users.map(user => (
            <li key={user.id}>
              Nom d'utilisateur : {user.username} - Email : {user.email}
            </li>
          ))
        ) : (
          <p>Aucun utilisateur trouvé.</p>
        )}
      </ul>
    </div>
  );
};

export default UserList;

