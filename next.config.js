const path = require('path')


module.exports = {
  reactStrictMode: true,
  sassOptions: {
    includePaths: [path.join(__dirname, 'styles')],
  },
  images: {
    domains: ['cdn.chec.io', 'picsum.photos'],
  },
  env: {
    SANDBOX_PUBLIC_KEY: 'pk_test_318253e3cfa17aff2480dfa616723878764f8544d402a',
  },
}
