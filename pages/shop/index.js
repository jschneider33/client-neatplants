import React from 'react'
import ProductsList from '../../components/ProductsList';
import FilterList from '../../components/FilterList';
import MainLayout from '../../components/layouts/MainLayout';

import { listProducts, listCategories } from '../../lib/commerce/productAPI';
import styles from '../../styles/Shop.module.sass';

export async function getStaticProps(){
    const products = await listProducts();
    const categories = await listCategories();
    return {
        props: {
            products,
            categories
        }
    }
}

const Shop = ({ products, categories }) => {
    return(
        <div>
            {/* <Navigation /> */}
            <div className={styles.shop}>
                {/* <SubNav /> */}
                <div className={styles.catalog}>
                    <div className={styles.sidebar}>
                        <FilterList categories={categories} />
                    </div>
                    <div className={styles.content}>
                        <ProductsList products={products} />
                    </div>
                </div>
            </div>
        </div>
    )
}

Shop.Layout = MainLayout;

export default Shop;