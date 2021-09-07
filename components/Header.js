import React from "react";
import { Row, Col } from "react-bootstrap";
import Image from "next/image";
import Link from "next/link";

import styles from '../styles/Home.module.sass';

export default function Header(){
    return(
        <header className={styles.header}>
            <Row className={styles.headerRow}>
                <Col className={styles.imageCol}>
                    <div className={styles.imageDiv}>
                        {/* <Image 
                            src="/images/11.png"
                            alt=""
                            width={400}
                            height={400}
                        /> */}
                    </div>
                </Col>
                <Col className={styles.titleCol}>
                    <div className={styles.titleDiv}>
                        <h1 className={styles.title}>
                            Create your jungle
                        </h1>
                        <h2 className={styles.subTitle}>
                            Regardless of your space, there's a plant for you
                        </h2>
                        <div className={styles.toShopDiv}>
                            <Link href="/shop">
                                <a className={styles.toShop}>
                                    Shop now
                                </a>
                            </Link>
                        </div>
                    </div>
                </Col>
            </Row>
        </header>
    )
}