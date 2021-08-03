import React from "react";
import { Row, Col } from "react-bootstrap"

import styles from "../styles/Catalog.module.sass"

import { PRODUCTLIST } from "../info/productInfo.js"

export default function Catalog(){
    const products = PRODUCTLIST;
    console.log(products);

    const makeProductCard = e => {
        return(
            <div>
                "Hello"
            </div>
        )
        // console.log("Hello")
        // for (const p in e){
        //     return(
        //         <h3>
        //             {p["SKU"]}
        //         </h3>
        //     )
        // }
    }


    return(
        <div className={styles.container}>
            <Row>
                {products.forEach(e => makeProductCard(e))}
            </Row>
        </div>
    )

}