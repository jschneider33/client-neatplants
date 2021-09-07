import React from "react"

import ProductItem from "./ProductItem";

import { Row, Col } from "react-bootstrap";
import styles from "../styles/Product.module.sass";

const RelatedProducts = ({ products }) => {
    products.map(product => {
        console.log(product)
    })
    return(
        <>
            <Row className={styles.relatedRow}>
                {products.map(product => (
                    <ProductItem
                        product={product}
                    />
                ))}
                {/* {JSON.stringify(product, null, 2)} */}
            </Row>
        </>
    )
};

export default RelatedProducts;