import React from 'react'
import Head from 'next/head';
import 'bootstrap/dist/css/bootstrap.css'
import 'react-image-gallery/styles/scss/image-gallery.scss';
import '../styles/globals.sass'

import Navigation from '../components/Navigation';

function MyApp({ Component, pageProps }) {
  const Layout = Component.Layout ? Component.Layout : React.Fragment;

  return (
    <>
      <Layout>
        <Head>
          <meta name="viewport" content="width=device-width, initial-scale=1" />
        </Head>
        <Component {...pageProps} />  
      </Layout>
    </>
  )
}

export default MyApp
