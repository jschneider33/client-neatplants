import { commerce } from "../../commerce/commerce"
import Link from "next/link";
import Image from "next/image";
import { Row, Col } from "react-bootstrap";

import styles from "../../styles/Product.module.sass"

export async function getStaticProps({ params }) {
    const { permalink } = params;

    const product = await commerce.products.retrieve(permalink, {
        type: 'permalink'
    });

    return { 
        props: {
            product,
        },

        revalidate: 60,
    }
}


export async function getStaticPaths(){
    const { data: products } = await commerce.products.list();

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
    return(
        <div className={styles.main}>
            <Link href="/catalog">
                <a className="product-detail__back">
                    <p>Back to products</p>
                </a>
            </Link>
            <Row className={styles.productRow}>
                <Col md={5} className={styles.imageCol}>
                    <Image
                        src={product.media.source}
                        alt={product.name}
                        className={styles.prodImage}
                        width={600}
                        height={600}
                    />
                </Col>
                <Col md={4} className={styles.optionsCol}>
                    <h1 className="product-detail__name">{product.name}</h1>
                    <div
                        className="product-detail__description"
                        dangerouslySetInnerHTML={{__html: product.description}}
                    ></div>
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
            
            {/* <img className="product-detail__image" src={product.media.source} alt={product.name} /> */}
            
        </div> 
    )
}

export default ProductDetailPage