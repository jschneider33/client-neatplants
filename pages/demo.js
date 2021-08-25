import React from "react"
import { commerce } from "../commerce/commerce"
import ProductsList from "../components/ProductsList"

export async function getStaticProps(){
    const merchant = await commerce.merchants.about();
    const { data: products } = await commerce.products.list();

    return {
        props: {
            merchant,
            products,
        }
    }
}

const Demo = ({ merchant, products }) => {
    return(
        <div>
            <ProductsList products={products} />
        </div>
    )
}

export default Demo;