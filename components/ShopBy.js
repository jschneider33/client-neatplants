import React from 'react';
import ShopByCol from './ShopByCol';
import { Row, Col } from 'react-bootstrap';

import styles from '../styles/Home.module.sass';

const ShopBy = ({ category, tagline }) => {
    console.log(category.name)
    category[0].children.map(c => console.log(c.slug));
    return(
        <div className={styles.shopByChild}>
            <div className={styles.shopByTitles}>
                <h3 className={styles.shopByTitle}>{tagline}</h3>
                <p className={styles.shopBySub}>{`Shop by ${category[0].name} ->`}</p>
            </div>
            <div className={styles.shopByMain}>
                <div className={styles.shopByRow}>
                    {category[0].children.map(cat_child => (
                        <ShopByCol
                            key={cat_child.id}
                            imageSrc={`/images/${cat_child.slug}-icon.png`}
                            text={cat_child.name}
                        />
                    ))}
                    {/* <ShopByCol 
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
                    /> */}
                </div>
            {/* </div> */}
        </div>
      </div>
    )
};

export default ShopBy;