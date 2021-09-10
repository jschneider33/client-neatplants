import React from 'react';

import MainLayout from '../../components/layouts/MainLayout';
import BlogHeader from '../../components/blog/BlogHeader';
import BlogBody from '../../components/blog/BlogBody';


const Posts = ({ posts }) => {
    return(
        <div>
            <BlogHeader 
                imageSrc='/assets/blog/1.jpg'
            />
            <BlogBody 
                posts="posts"
            />
        </div>
    )
};

Posts.Layout = MainLayout;

export default Posts;