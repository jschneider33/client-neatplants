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
                    <Col sm={4} className={styles.prodCol} key={product.name}>
                        <Link href={`/product/${product.permalink}`} key={product.id}>
                            <a>
                                <ProductItem
                                    product={product}
                                />
                        </a>
                        </Link>
                    </Col>
                ))}
            </Row>
            
        </div>
    )
}

export default ProductsList