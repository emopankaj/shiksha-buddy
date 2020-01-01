module.exports = {
    lintOnSave: false,
    runtimeCompiler: true,
    publicPath: '/',
    devServer: {
        proxy: {
            '^/api': {
                target: "http://localhost:8000",
                ws: true,
                changeOrigin: true
            }
        }
    }
};
