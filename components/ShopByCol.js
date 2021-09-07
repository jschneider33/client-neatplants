import React from 'react';
import Image from 'next/image';
import { Col } from 'react-bootstrap';
import styles from '../styles/Home.module.sass';

const ShopByCol = ({ imageSrc, text }) => {
    return(
        <div className={styles.shopByCol}>
                <Image 
                    src={imageSrc}
                    alt=""
                    width={100}
                    height={100}
                />
                <h3 className={styles.shopByText}>
                    {text}
                </h3>
        </div>
    )
};

export default ShopByCol;