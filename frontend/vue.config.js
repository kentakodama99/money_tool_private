module.exports = {
  publicPath:'./',
  devServer: {
    port: 8080,
    disableHostCheck: true,
  },
  configureWebpack: {
    module: {
        rules: [
            {
                test: /.csv$/,
                loader: 'csv-loader'
            }
        ]
    }
  },
  transpileDependencies: [
    'vuetify'
  ]
}
