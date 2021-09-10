import React from 'react';

import styles from '../../styles/Posts.module.sass';

export default function PostContainer({children}){
    return(
        <div className={styles.pageContainer}>
            {children}
        </div>
    )
}