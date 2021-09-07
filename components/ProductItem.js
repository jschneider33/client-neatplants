import React from "react"
import Image from "next/image"
import Link from "next/link";

import { Row, Col } from "react-bootstrap"
import styles from "../styles/ProductItem.module.sass"

const ProductItem = ({ product }) => {

    const splitName = product.name.split(",")

    return(
        <Col sm={4} className={styles.prodCol}>
            <Link href={`/shop/${product.permalink}`} key={product.id}>
            <a className={styles.prodAnchor}>

            <div className={styles.main}>
                <div className={styles.imageDiv}>
                    <Image
                        className={styles.image}
                        src={product.media.source}
                        alt={product.name}
                        width={280}
                        height={280}
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
                {product.variant_groups && <SizesMarkup sizes={product.variant_groups[0].options} name={product.name} />}
                    
            </div>    
            </a>
            </Link>
        </Col> 
    )
}

const SizesMarkup = ({ sizes, name }) => {
    // console.log(sizes)
    return(
        <Row>
            <Col sm={2} className={styles.sizeCol}>
                Sizes:
            </Col>
            <Col sm={10} className={styles.sizeCol}>
                <ul className={styles.sizeList}>
                    {sizes.map(size => (
                        <li key={`${name}-${size.name}`} className={styles.sizeListItem}>
                            {size.name}
                        </li>
                    ))}
                </ul>
            </Col>
        </Row>
    )

}

export default ProductItem;