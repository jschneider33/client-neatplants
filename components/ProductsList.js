import React from "react"
import Link from "next/link";
import ProductItem from "./ProductItem"
import {Row, Col} from "react-bootstrap"

import styles from "../styles/ProductList.module.sass"

const ProductsList = ({ products }) => {
    return(
        <div className={styles.main} id="products">
            <Row className={styles.prodRow}>
                {products.map((product) => (
                    <ProductItem key={product.id} product={product} />
                ))}
            </Row>
        </div>
    )
}

export default ProductsList;

{/* <Col sm={4} className={styles.prodCol} key={product.name}> */}
    {/* <Link href={`/shop/${product.permalink}`} key={product.id}> */}
        {/* <a className={styles.prodAnchor}> */}
            {/* <ProductItem
                product={product}
            /> */}
        {/* </a> */}
    {/* </Link> */}
{/* </Col> */}