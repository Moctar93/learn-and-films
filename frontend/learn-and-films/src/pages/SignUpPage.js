import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './SignUp.css';

function SignUpPage() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [subscription, setSubscription] = useState('basic');
  const [error, setError] = useState('');
  const [isPaid, setIsPaid] = useState(false); // Suivi du paiement
  const navigate = useNavigate();

  const handleSignUp = async (e) => {
    e.preventDefault();
    if (!isPaid) {
      setError("Veuillez effectuer le paiement pour compléter l'inscription.");
      return;
    }

    const userData = {
      username,
      email,
      password,
      subscription,
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
        navigate('/');
      } else {
        const data = await response.json();
        setError(data.message || "Erreur d'inscription");
      }
    } catch (error) {
      setError("Erreur serveur. Veuillez réessayer.");
    }
  };

  const loadPayPalButton = () => {
  if (window.paypal) {
    window.paypal.Buttons({
      createOrder: (data, actions) => {
        return actions.order.create({
          purchase_units: [{
            amount: {
              value: subscription === 'basic' ? '5.00' : subscription === 'standard' ? '10.00' : '15.00'
            }
          }]
        });
      },
      onApprove: (data, actions) => {
        return actions.order.capture().then(details => {
          setIsPaid(true);
          setError("");
          alert("Paiement réussi pour " + details.payer.name.given_name);
        });
      },
      onError: (err) => {
        setError("Erreur lors du paiement. Veuillez réessayer.");
      }
    }).render('#paypal-button');
  } else {
    console.error("Le SDK PayPal n'est pas chargé.");
  }
};


  React.useEffect(() => {
  if (!window.paypal) {
    const script = document.createElement("script");
    script.onload = loadPayPalButton;
    document.body.appendChild(script);
  } else {
    loadPayPalButton();
  }
}, [subscription]);

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
        <label>Choisissez un abonnement :</label>
        <select
          name="subscription"
          value={subscription}
          onChange={(e) => setSubscription(e.target.value)}
          required
        >
          <option value="basic">Basic - 5.00 USD</option>
          <option value="standard">Standard - 10.00 USD</option>
          <option value="premium">Premium - 15.00 USD</option>
        </select>

        <div id="paypal-button" style={{ margin: '20px 0' }}></div>

        <button type="submit">S'inscrire</button>
      </form>
    </div>
  );
}

export default SignUpPage;

