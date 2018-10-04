import path from 'path';
import VueLoaderPlugin from 'vue-loader/lib/plugin';

const STATIC_URL = process.env.STATIC_URL || 'http://localhost:9001/';

export default {
    entry: [
        '@babel/polyfill',
        './snippr/static/snippr/index.js'
    ],

    output: {
        path: path.resolve(__dirname, 'static-root/snippr'),
        filename: 'index.js',
        chunkFilename: '[name].[hash].js',
        publicPath: `${STATIC_URL}snippr/`
    },

    mode: process.env.NODE_ENV || 'development',

    module: {
        rules: [{
            test: /\.vue$/,
            loader: 'vue-loader'
        }, {
            test: /\.js$/,
            loader: 'babel-loader'
        }, {
            test:/\.(s*)css$/,
            use:['style-loader','css-loader', 'sass-loader']
        }, {
            test: /\.(png|jpe?g|gif|svg)$/,
            loader: 'url-loader',
            options: {
                limit: 1024
            }
        }]
    },

    resolve: {
        alias: {
            source: path.resolve(__dirname, 'snippr/static/snippr')
        }
    },

    plugins: [
        new VueLoaderPlugin()
    ]
};
