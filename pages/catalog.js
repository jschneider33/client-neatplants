import React from "react"
import { commerce } from "../commerce/commerce"
import ProductsList from "../components/ProductsList"
import FilterList from "../components/FilterList"
import Navigation from "../components/Navigation"
import SubNav from "../components/SubNav"

import styles from "../styles/Catalog.module.sass"

export async function getStaticProps(){
    const merchant = await commerce.merchants.about();
    const { data: products } = await commerce.products.list();
    const { data: categories } = await commerce.categories.list();
    const category  = await commerce.categories.retrieve("cat_VPvL5zraK5AQkX")
    const { data: easyCare } = await commerce.products.list({
        category_slug: ['easy-care'],
    })

    return {
        props: {
            merchant,
            products,
            categories,
            easyCare
        }
    }
}

const Catalog = ({ merchant, products, categories, easyCare}) => {

    return(
        <div>
            <Navigation />
            <SubNav />
            <div className={styles.catalog}>
                <div className={styles.sidebar}>
                    <FilterList categories={categories} />
                </div>
                <div className={styles.content}>
                    <ProductsList products={products} />
                </div>
            </div>
            
        </div>
    )
}

export default Catalog;