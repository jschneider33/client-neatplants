import React from "react"

import styles from "../styles/Navigation.module.sass"

const SubNav = () => {
    return(
        <nav aria-label="secondary" className={styles.subMain}>
            <div className={styles.subContainer}>
                <ul className={styles.subNavList}>
                    <li className={styles.subNavListItem}>
                        Shop by Category
                        <SubNavCategory />
                    </li>
                    <li className={styles.subNavListItem}>
                        Blog
                    </li>
                </ul>
            </div>
        </nav>
    )
}

const SubNavCategory = () => {
    return(
        <>
            <ul className={styles.subMenuList}>
                <li className={styles.subMenuListItem}>
                    Easy Care
                </li>
                <li className={styles.subMenuListItem}>
                    Pet Friendly
                </li>
            </ul>
        </>
    )
}

export default SubNav;