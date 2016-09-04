var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker')

module.exports= {
  context: __dirname,
  entry:{
      main:[
         './react_jsx/src/index.js',
         'webpack/hot/only-dev-server'
      ]
  },
  output:{
    path : __dirname + '/react_jsx/dst',
    filename:'[name]-[hash].js'
  },
  module : {
    loaders : [
      {
        test:/\.jsx?$/,
        exclude:/node_modules/,
        loader: 'babel-loader',
        query:{
          presets: ['es2015','react','stage-0']
        }
      }
    ]
  },
  resolve: {
    modulesDirectories: ['node_modules', 'bower_components'],
    extensions: ['', '.js', '.jsx']
  },
   plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ]
}
