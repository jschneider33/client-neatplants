import React from "react"
import Image from "next/image"

import { Row, Col } from "react-bootstrap"
import styles from "../styles/ProductItem.module.sass"

const ProductItem = ({ product }) => {

    // console.log(product.name)

    const splitName = product.name.split(",")
    // console.log(splitName)

    console.log(product.categories)

    return(
        <div className={styles.main}>
            <div className={styles.imageDiv}>
                <Image
                    className={styles.image}
                    src={product.media.source}
                    alt={product.name}
                    width={300}
                    height={300}
                />
            </div>
            <Row className={styles.info}>
                <Col sm={9}>
                    {splitName.length === 1
                        ? <h2 className={styles.name}>{splitName[0]}</h2>
                        : <div>
                            <h2 className={styles.name}>{splitName[1]}</h2>
                            <p className={styles.subName}>{splitName[0]}</p>
                        </div>
                    }
                    {/* <h2 className={styles.name}>{splitName.length === 1 ? <div>{splitName[0]}</div> : <div>{splitName[1]} <br/> {splitName[0]}</div>}</h2> */}
                
                    
                </Col>
                <Col sm={3} className={styles.priceCol}>
                    <p className={styles.price}>${product.price.raw}</p>
                </Col>
            </Row>
        </div>     
    )
}

export default ProductItem;