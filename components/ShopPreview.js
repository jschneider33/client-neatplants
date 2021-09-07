import React from 'react';
import Image from 'next/image';
import { Row, Col } from 'react-bootstrap';

import styles from '../styles/Home.module.sass';

const ShopPreview = ({ orientation, imageSrc, content }) => {
    return(
        <div className={styles.shopPreview}>
            <Row className={styles.shopPreviewRow}>
                <Col>
                    <p>{content}</p>
                </Col>
                <Col>
                    <Image 
                        src={imageSrc}
                        alt=""
                        width={200}
                        height={200}
                    />
                </Col>
            </Row>
        </div>
    )
};

export default ShopPreview;