import React, { useState } from "react";
import Link from "next/link";
import Image from "next/image";
import Breadcrumbs from "../../components/Breadcrumbs";
import { useRouter } from 'next/router';
import ProductPhotos from "../../components/ProductPhotos";
import RelatedProducts from "../../components/RelatedProducts";
// import FSLightbox from "fslightbox-react";
import { Row, Col } from "react-bootstrap";
import { getProductByPermalink } from '../../lib/commerce/productAPI';

import styles from "../../styles/Product.module.sass";

export async function getStaticProps({ params }) {
    const { permalink } = params;

    const product = getProductByPermalink(permalink);

    return { 
        props: {
            product,
        },

        revalidate: 60,
    }
}


export async function getStaticPaths(){
    const products = await listProducts()

    return {
        paths: products.map((product) => ({
            params: {
                permalink: product.permalink,
            },
        })),
        fallback: false
    }
}

const ProductDetailPage = ({ product }) => {
    const [cartInfo, setCartInfo] = useState({
        permalink: product.permalink,
        size: 4,
        imageIndex: 0,
    })

    let productPhotos = [];
    product.assets.map(asset => productPhotos.push(asset.url));

    let sizeIndexes = {};
    product.variant_groups[0].options.map((variant, i) => {
        sizeIndexes[variant["name"]] = {
                // id: variant.assets[0],
                idx: i,
            }
    });
    
    console.log(sizeIndexes)
    console.log(sizeIndexes[cartInfo.size])

    const sizeChange = e => {
        e.preventDefault()
        // console.log(e.target.name)
        // const newSizeIndex = sizeIndexes.
        setCartInfo({...cartInfo, size: e.target.name})
    }

    return(
        <div className={styles.main}>
            <Breadcrumbs 
                permalink={product.permalink}
            />
            <Row className={styles.productRow}>
                <Col md={5} className={styles.imageCol}>
                {/* <button onClick={ () => setToggler(!toggler) }>
                    Toggle Lightbox
                </button> */}
                {/* <FSLightbox
                    type="image"
                    toggler={toggler}
                    sources={productPhotos}
                /> */}
                    {/* <Image
                        src={product.media.source}
                        alt={product.name}
                        className={styles.prodImage}
                        width={500}
                        height={500}
                    /> */}
                    <ProductPhotos 
                        photos={productPhotos}
                        startIndex={sizeIndexes[cartInfo.size].idx}
                    />
                </Col>
                <Col md={4} className={styles.optionsCol}>
                    <h1 className={styles.title}>{product.name}</h1>
                    
                    <div className={styles.sizes}>
                        <p className={styles.sizeTitle}>Sizes:</p>
                        <ul className={styles.sizeList}>
                            {product.variant_groups[0].options.map(size => (
                                <li key={`product--${product.permalink}-${size.name}`} className={styles.sizeItem}>
                                    <button name={size.name} onClick={e => sizeChange(e)} className={`${styles.sizeButton} ${cartInfo.size === size.name ? styles.sizeButtonActive : styles.sizeButtonInactive}`}>
                                        {`${size.name} in`}
                                    </button>
                                </li>
                            ))}
                        </ul>
                    </div>
                    <div className={styles.description}>
                        {/* <h3 className={styles.descriptionTitle}>Description</h3> */}
                        <div
                            className={styles.descriptionContent}
                            dangerouslySetInnerHTML={{__html: product.description}}
                        ></div>
                    </div>
                    
                </Col>
                <Col md={3} className={styles.cartCol}>
                    <div className="product-detail__price">
                        {product.price.formatted_with_symbol}
                    </div>
                        <button
                            name="View item"
                            className="product-detail__btn"
                        >
                        <span>Add to cart</span>
                        </button>
                </Col>
            </Row>

            <RelatedProducts 
                products={product.related_products}
            />
            
            {/* <img className="product-detail__image" src={product.media.source} alt={product.name} /> */}
            <pre>
            {JSON.stringify(product, null, 2)}
            </pre>
        </div> 
    )
}

export default ProductDetailPage