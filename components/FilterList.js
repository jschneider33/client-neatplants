import React from "react";
import Link from "next/link";

import FilterItem from "./FilterItem";

const FilterList = ({ categories }) => {
    if(!categories) return null;

    return(
        <ul>
            {categories.map(category => (category.products > 0 && 
                <li key={category.slug}>
                    <Link href={`/categories/${category.slug}`}>
                        <a>
                            <FilterItem {...category} />
                        </a>
                    </Link>
                </li>
            ))}
        </ul>
    )
}

export default FilterList