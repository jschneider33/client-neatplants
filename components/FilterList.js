import React from "react";
import Link from "next/link";

import FilterItem from "./FilterItem";
import styles from "../styles/FilterList.module.sass"

const FilterList = ({ categories }) => {
    if(!categories) return null;

    return(
        <ul className={styles.list}>
            {categories.map(category => (category.products > 0 && 
                <li key={category.slug} className={styles.listItem}>
                    <Link href={`/category/${category.slug}`}>
                        <a className={styles.listItemLink}>
                            <FilterItem {...category} />
                        </a>
                    </Link>
                </li>
            ))}
        </ul>
    )
}

export default FilterList