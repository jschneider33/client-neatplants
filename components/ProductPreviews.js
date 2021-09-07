import React from "react";
import ProductItem from "./ProductItem";
import { Row } from 'react-bootstrap';
import styles from '../styles/Home.module.sass';


const ProductPreviews = ({ featuredProducts }) => {
    const thisClick = e => {
        console.log(e.target)
    }

    console.log(featuredProducts)

    if(!featuredProducts){
        console.log("undef")
        return <div>Loading...</div>;
    }

    return(
        <div>
            Home Shop Previews!
            <div>
                <Row className={styles.featRow}>

                {featuredProducts.map((product) => (
                    <ProductItem key={product.id} product={product} />
                ))}
                </Row>
            </div>
        </div>
    )
};

export default ProductPreviews;