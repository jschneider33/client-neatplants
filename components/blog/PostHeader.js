import React from 'react';

const PostHeader = ({ title, datetime, coverImg }) => {
    return(
        <>
            <h2>{title}</h2>
            <p>{datetime}</p>
        </>
    )
};

export default PostHeader;