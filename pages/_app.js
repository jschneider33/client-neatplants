import Head from "next/head";

import 'bootstrap/dist/css/bootstrap.css'
import "react-image-gallery/styles/scss/image-gallery.scss";
import '../styles/globals.sass'

import Navigation from "../components/Navigation";

function MyApp({ Component, pageProps }) {
  return (
    <>
        <Head>
          <meta name="viewport" content="width=device-width, initial-scale=1" />
        </Head>
        <Navigation />
        <Component {...pageProps} />      
    </>
  )
}

export default MyApp
