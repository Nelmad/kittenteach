'use strict';

const path = require('path');
const webpack = require('webpack');

// let outputPath = path.resolve(__dirname, 'static/core/build');
let fileName = 'app.js';

let plugins = [];

// Get the environment variable defined in the command (see package.json)
let env = process.env.WEBPACK_ENV;

// When compiling for production we want the app to be uglified.
if (env === 'production') {
  let UglifyJSPlugin = require('uglifyjs-webpack-plugin');

  plugins.push(new UglifyJSPlugin());

  // We also add it as a global, the Vue lib needs it to determine if Dev tool should be active or not.
  plugins.push(new webpack.DefinePlugin({
    'process.env': {
      NODE_ENV: '"production"'
    }
  }));
  // Change file name extension to min.js
  fileName = fileName.replace(/js/g, 'min.js');
}

// Main webpack config
module.exports = {
  entry: {
    '/static/core/build/': './static/core/js/vue/main.js'
  },
  output: {
    path: path.resolve(__dirname, './'),
    filename: `[name]${fileName}`
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        enforce: 'pre',
        test: /\.(js|vue)$/,
        loader: 'eslint-loader',
        exclude: /node_modules/,
        options: {
          formatter: require('eslint-friendly-formatter')
        }
      }
    ]
  },
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js'
    }
  },
  plugins // set the previously defined plugins
};
