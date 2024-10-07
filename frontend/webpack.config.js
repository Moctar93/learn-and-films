const path = require('path');

module.exports = {
  entry: './src/index.js', // Point d'entrée de votre application
  output: {
    path: path.resolve(__dirname, 'dist'), // Dossier de sortie
    filename: 'bundle.js', // Nom du fichier de sortie
  },
  module: {
    rules: [
      {
        test: /\.js$/, // Règle pour les fichiers JavaScript
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader', // Utilisation de Babel pour transpiler le JavaScript
        },
      },
      {
        test: /\.css$/, // Règle pour les fichiers CSS
        use: ['style-loader', 'css-loader'], // Chargeurs pour CSS
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx'], // Extensions que Webpack peut résoudre
  },
  devServer: {
    contentBase: path.join(__dirname, 'public'), // Dossier pour le serveur de développement
    compress: true,
    port: 3000,
  },
};

