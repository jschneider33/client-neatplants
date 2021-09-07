import React from 'react';
import ShopByCol from './ShopByCol';

import styles from '../styles/Home.module.sass';

const ShopBy = ({ category, tagline }) => {
    category[0].children.map(c => console.log(c));
    return(
        <div className={styles.shopByChild}>
          <h3 className={styles.shopByTitle}>{tagline}</h3>
          <div className={styles.shopByMain}>
            <p className={styles.shopBySub}>{category.slug}</p>
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
      </div>
    )
};

export default ShopBy;