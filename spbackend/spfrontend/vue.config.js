const BundleTracker = require('webpack-bundle-tracker');
const { defineConfig } = require("@vue/cli-service");

module.exports = {
  publicPath: 'http://0.0.0.0:8080/',
  outputDir: './dist/',

  chainWebpack: config => {
    config
        .plugin('BundleTracker')
        .use(BundleTracker, [{filename: 'webpack-stats.json'}])

    config.output
        .filename('bundle.js')

    config.optimization
      .splitChunks(false)

    config.resolve.alias
        .set('__STATIC__', 'static')

    config.devServer
        .host('0.0.0.0')    
        .port(8080)
        .https(false)
        .headers({'Access-Control-Allow-Origin': ['\*']})
  },

  // uncomment before executing 'npm run build' 
  // css: {
  //     extract: {
  //       filename: 'bundle.css',
  //       chunkFilename: 'bundle.css',
  //     },
  // }
};
