import React from 'react';

import styles from '../../styles/Blog.module.sass';

const BlogHeader = ({ imageSrc }) => {
    return(
        <header className={styles.header}>
            <div className={styles.headerSub}>
                Body Header
            </div>
        </header>
    )
};

export default BlogHeader;