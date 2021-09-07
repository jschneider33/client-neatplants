import React from 'react';
import { Row } from 'react-bootstrap';

import ShopByCol from './ShopByCol';
import styles from '../styles/Home.module.sass';

const ShopBySize = ({ subText }) => {
    return(
        <div className={styles.shopByMain}>
            <p className={styles.shopBySub}>{subText}</p>
                <div className={styles.shopByRow}>
                    <ShopByCol 
                        imageSrc="/images/monsteras-home.jpg"
                        text="small"
                    />
                    <ShopByCol 
                        imageSrc="/images/monsteras-home.jpg"
                        text="medium"
                    />
                    <ShopByCol 
                        imageSrc="/images/monsteras-home.jpg"
                        text="large"
                    />
                </div>
            {/* </div> */}
        </div>
    )
};

export default ShopBySize;